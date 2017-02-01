"""Modified script to run antsBrainExtraction on meningioma T1-contrast data.
"""
from glob import glob
import os.path as op
from nipype import DataGrabber, DataSink, IdentityInterface, Node, Workflow
from nipype.interfaces import ants

data_dir = '/om/user/jakubk/meningioma/data'
template_dir = '/om/user/jakubk/meningioma/ants_templates/OASIS-30_Atropos_template'

subjects = [op.split(path)[-1][:10] for path in glob('../data/*.nii.gz')]

datasource = Node(DataGrabber(infields=['subject_id'],
                              outfields=['subject_id', 't1c']),
                 name='datasource')
datasource.inputs.base_directory = data_dir
datasource.inputs.template = '*'
datasource.inputs.field_template = {'t1c': '%s*.nii.gz'}
datasource.inputs.template_args = {'t1c': [['subject_id']]}
datasource.inputs.sort_filelist = True
datasource.inputs.subject_id = subjects

seg = Node(ants.BrainExtraction(), name='seg',
           iterables=['anatomical_image', 'out_prefix'], itersource=datasource,
           synchronize=True)
seg.inputs.dimension = 3
seg.inputs.keep_temporary_files = 1
seg.inputs.brain_template = op.join(template_dir, 'T_template0.nii.gz')
seg.inputs.brain_probability_mask = op.join(template_dir,
                                            'T_template0_BrainCerebellumProbabilityMask.nii.gz')

# Node to save output files. This does not work. Why?
sinker = Node(DataSink(), name='sinker')
# Add container.
sinker.inputs.base_directory = op.abspath('antsBrainExtraction_output')

# Workflow.
wf = Workflow(name='antsBrainExtraction', base_dir='/om/scratch/Wed/jakubk')
wf.connect(datasource, 't1c', seg, 'anatomical_image')
wf.connect(datasource, 'subject_id', seg, 'out_prefix')
wf.connect(seg, 'BrainExtractionBrain', sinker, 'brain')
wf.connect(seg, 'BrainExtractionMask', sinker, 'brain_masks')
wf.connect(seg, 'BrainExtractionSegmentation', sinker, 'seg_full')
wf.connect(seg, 'BrainExtractionCSF', sinker, 'csf')
wf.connect(seg, 'BrainExtractionGM', sinker, 'gm')
wf.connect(seg, 'BrainExtractionWM', sinker, 'wm')
wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=50GB'})
