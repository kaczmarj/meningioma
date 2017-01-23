from glob import glob
import os
import os.path as op

from nipype.interfaces import afni, ants, fsl, slicer, spm, io
import nipype.interfaces.utility as niu
import nipype.pipeline.engine as pe

PATH = op.abspath('.')
PATH

files = sorted(glob(op.join(PATH, 'data/*.nii.gz')))
print("{} NIFTI files".format(len(files)))

# ANTs BrainExtraction

def get_files():
    return sorted(glob(op.join(PATH, 'data/*.nii.gz')))

anat_files = pe.Node(niu.IdentityInterface(fields=['anatomical']),
                     name='anat_files')
anat_files.iterables = [('anatomical', get_files())]

templates = [op.join(PATH,
                     'ants_templates/IXI/T_template{}.nii.gz'.format(i)) for i in range(4)]
strip = pe.Node(ants.BrainExtraction(), name='strip')
strip.inputs.dimension = 3
strip.iterables = ('brain_template', templates)
strip.inputs.brain_probability_mask = op.join(PATH, 'ants_templates/IXI/T_templateProbabilityMask.nii.gz')

wf = pe.Workflow(name='ants_brainstripper', base_dir='ants_skullstrip')
wf.connect(anat_files, 'anatomical', strip, 'anatomical_image')
wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=16GB'})
