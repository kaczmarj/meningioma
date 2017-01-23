from glob import glob
import os
import os.path as op

from nipype.interfaces import ants
import nipype.interfaces.utility as niu
import nipype.pipeline.engine as pe

PATH = op.abspath('.')

# ANTs BrainExtraction

def get_files():
    return sorted(glob(op.join(PATH, 'data/*.nii.gz')))

anat_files = pe.Node(niu.IdentityInterface(fields=['anatomical']),
                     name='anat_files')
anat_files.iterables = [('anatomical', get_files())]

strip = pe.Node(ants.BrainExtraction(), name='strip')
strip.inputs.dimension = 3
strip.inputs.brain_template = op.join(PATH, 'ants_templates/NKI/T_template.nii.gz')
prob_fname = op.join(PATH, 'ants_templates/NKI/T_templateProbabilityMask.nii.gz')
strip.inputs.brain_probability_mask = prob_fname

wf = pe.Workflow(name='ants_brainstripper_NKI', base_dir='ants_skullstrip')
wf.connect(anat_files, 'anatomical', strip, 'anatomical_image')
wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=16GB'})
