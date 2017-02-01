"""Script to run antsBrainExtraction on meningioma T1-contrast data.
"""
import os.path as op
from nipype import Node, Workflow, DataGrabber, DataSink, MapNode
from nipype.interfaces import ants

# Node to grab data.
grab = Node(DataGrabber(outfields=['t1c']), name='grabber')
grab.inputs.base_directory = op.abspath('data')
grab.inputs.template = '*.nii.gz'
grab.inputs.field_template = {'t1c': '*.nii.gz'}
grab.inputs.sort_filelist = True

# Node to run ants.BrainExtraction.
# Segments the anatomical image and should extract brain.
template_dir = op.abspath('ants_templates/OASIS-30_Atropos_template')
seg = MapNode(ants.BrainExtraction(), iterfield=['anatomical_image'], name='seg')
seg.inputs.dimension = 3
seg.inputs.keep_temporary_files = 1
seg.inputs.brain_template = op.join(template_dir, 'T_template0.nii.gz')
seg.inputs.brain_probability_mask = op.join(template_dir,
                                            'T_template0_BrainCerebellumProbabilityMask.nii.gz')

# Node to save output files. This does not work. Why?
sinker = Node(DataSink(), name='sinker')
sinker.inputs.base_directory = op.abspath('antsBrainExtraction_output')

# Workflow.
wf = Workflow(name='antsBrainExtraction', base_dir='/om/scratch/Wed/jakubk')
wf.connect(grab, 't1c', seg, 'anatomical_image')
wf.connect(seg, 'BrainExtractionBrain', sinker, 'extracted.brain')
wf.connect(seg, 'BrainExtractionMask', sinker, 'extracted.brain_masks')
wf.connect(seg, 'BrainExtractionSegmentation', sinker, 'extracted.seg_full')
wf.connect(seg, 'BrainExtractionCSF', sinker, 'extracted.csf')
wf.connect(seg, 'BrainExtractionGM', sinker, 'extracted.gm')
wf.connect(seg, 'BrainExtractionWM', sinker, 'extracted.wm')
wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=50GB'})
