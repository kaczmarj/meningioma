import os.path as op
from nipype import Node, Workflow, DataGrabber, DataSink, MapNode
from nipype.interfaces import ants

base_dir = '/om/user/jakubk/meningioma/'

# Node to grab data.
grab = Node(DataGrabber(outfields=['t1']), name='grabber')
grab.inputs.base_directory = '/om/user/jakubk/meningioma/data'
grab.inputs.template = '*.nii.gz'
# Change filenames later to specify T1.
grab.inputs.field_template = {'t1': '*.nii.gz'}
grab.inputs.sort_filelist = True

# Node to run antsCorticalThickness.
# Segments the anatomical image and should extract brain.
template_dir = op.join(base_dir, 'ants_templates', 'OASIS-30_Atropos_template')
seg = MapNode(ants.CorticalThickness(), iterfield=['anatomical_image'], name='seg')
seg.inputs.dimension = 3
seg.inputs.brain_template = op.join(template_dir, 'T_template0.nii.gz')
seg.inputs.t1_registration_template = op.join(template_dir, 'T_template0_BrainCerebellum.nii.gz')
seg.inputs.brain_probability_mask = op.join(template_dir,
                                            'T_template0_BrainCerebellumProbabilityMask.nii.gz')
seg.inputs.segmentation_priors = [op.join(template_dir, 'Priors2', 'priors{}.nii.gz'.format(i)) for i in range(1, 7)]
seg.inputs.extraction_registration_mask = op.join(template_dir, 'T_template0_BrainCerebellumExtractionMask.nii.gz')
seg.inputs.quick_registration = True
seg.inputs.segmentation_iterations = 1

# Node to save output files.
sinker = Node(DataSink(), name='sinker')
sinker.inputs.base_directory = op.join(base_dir, 'ants_seg_output')

# Workflow.
wf = Workflow(name='ants_seg', base_dir='/om/scratch/Wed/jakubk/secondtry')
wf.connect(grab, 't1', seg, 'anatomical_image')
wf.connect(seg, 'BrainSegmentation', sinker, 'segs/.')
wf.connect(seg, 'BrainExtractionMask', sinker, 'extract/.')
wf.connect(seg, 'CorticalThickness', sinker, 'thickness/.')
wf.connect(seg, 'BrainVolumes', sinker, 'vols/.')
wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=50GB'})
