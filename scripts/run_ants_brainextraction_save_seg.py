# import os.path as op
# from nipype import Node, Workflow, DataGrabber, DataSink, MapNode
# from nipype.interfaces import ants, fsl
#
# # Node to grab data.
# grab = Node(DataGrabber(outfields=['t1']), name='grabber')
# grab.inputs.base_directory = '/om/user/jakubk/meningioma/data'
# grab.inputs.template = '*.nii.gz'
# # Change filenames later to specify T1.
# grab.inputs.field_template = {'t1': '*.nii.gz'}
# grab.inputs.sort_filelist = True
#
# # Node to run ants.BrainExtraction.
# # Segments the anatomical image and should extract brain.
# bet = MapNode(fsl.BET(), iterfield=['in_file'], name='bet')
#
# # Node to save output files.
# sinker = Node(DataSink(), name='sinker')
# sinker.inputs.base_directory = '/om/user/jakubk/meningioma/output_test/'
#
# # Workflow.
# wf = Workflow(name='bet_test', base_dir='/om/scratch/Wed/jakubk/')
# wf.connect(grab, 't1', bet, 'in_file')
# wf.connect(bet, 'out_file', sinker, 'bet')
# wf.connect(bet, 'inskull_mask_file', sinker, 'bet.@mask')
# # wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=50GB'})






import os.path as op
from nipype import Node, Workflow, DataGrabber, DataSink, MapNode
from nipype.interfaces import ants

# Node to grab data.
grab = Node(DataGrabber(outfields=['t1']), name='grabber')
grab.inputs.base_directory = op.abspath('data')
grab.inputs.template = '*.nii.gz'
# Change filenames later to specify T1.
grab.inputs.field_template = {'t1': '*.nii.gz'}
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

# Node to save output files.
sinker = Node(DataSink(), name='sinker')
sinker.inputs.base_directory = op.abspath('output_test')

# Workflow.
wf = Workflow(name='ants', base_dir='/om/scratch/Wed/jakubk/secondtry')
wf.connect(grab, 't1', seg, 'anatomical_image')
wf.connect(seg, 'BrainExtractionBrain', sinker, 'extracted.brain')
wf.connect(seg, 'BrainExtractionMask', sinker, 'extracted.brain_masks')
wf.connect(seg, 'BrainExtractionSegmentation', sinker, 'extracted.seg_full')
wf.connect(seg, 'BrainExtractionCSF', sinker, 'extracted.csf')
wf.connect(seg, 'BrainExtractionGM', sinker, 'extracted.gm')
wf.connect(seg, 'BrainExtractionWM', sinker, 'extracted.wm')
wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=50GB'})
