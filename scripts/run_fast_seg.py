from os import path as op

from nipype import DataGrabber, DataSink, Node, MapNode, Workflow
from nipype.interfaces import fsl

# Node to grab data.
grab = Node(DataGrabber(outfields=['t1', 'brain']), name='grabber')
grab.inputs.base_directory = '/om/user/jakubk/meningioma/'
grab.inputs.template = '*.nii.gz'
# Change filenames later to specify T1.
grab.inputs.field_template = {'t1': 'data/*.nii.gz',
                              'brain': 'ants_seg_output/brain/*.nii.gz'}
grab.inputs.sort_filelist = True

fast = MapNode(fsl.FAST(), iterfield=['in_files'], name='fast')
fast.inputs.img_type = 1
fast.inputs.probability_maps = True
fast.iterables = ('number_classes', [3, 4, 5])

sinker = Node(DataSink(), name='sinker')
sinker.inputs.base_directory = op.abspath('fast_output')

# How can we iterate over original NIFTI files and extracted brains together?
# Run original NIFTI files.
wf = Workflow(name='fast_brain', base_dir='/om/scratch/Wed/jakubk/')
wf.connect(grab, 'brain', fast, 'in_files')
wf.connect(fast, 'probability_maps', sinker, 'prob')
wf.connect(fast, 'restored_image', sinker, 'restored')
wf.connect(fast, 'tissue_class_files', sinker, 'tissue_files')
wf.connect(fast, 'tissue_class_map', sinker, 'tissue_map')
wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=50GB'})
