"""Save 2-D t-SNE scatter plot and array."""
import os.path as op
from nipype import Node, Function, IdentityInterface, Workflow

def make_X_y():
    """Return arrays X and y to be used in t-SNE. Also return the subj ID."""
    from os import path as op
    import nibabel as nib
    import numpy as np
    from sklearn.metrics import pairwise

    subj = 'case_005_2'

    PATH = op.join('/', 'om', 'user', 'jakubk', 'meningioma')
    SAVE_PATH = op.join(PATH, 'tsne_output')

    # Load original scan and FAST segmentation
    brain = nib.load(op.join(PATH, 'data', '{}.nii.gz'.format(subj)))
    seg = nib.load(op.join(PATH, 'segmentation/fast/brain/classes_4/{}_brain_seg.nii.gz'.format(subj)))
    brain = brain.get_data()
    seg = seg.get_data()

    slice_ = 127
    b_slice = brain[:, :, slice_]
    s_slice = seg[:, :, slice_]

    b_slice_masked = np.ma.masked_array(b_slice, mask=~s_slice.astype(bool))
    b_slice_masked = np.ma.filled(b_slice_masked, fill_value=0.)

    X = b_slice_masked.flatten().reshape(-1, 1)
    y = s_slice.flatten().astype(np.int32)

    # Similarity matrix. But does Laplacian Kernel return similarity matrix?
    return pairwise.laplacian_kernel(X), y, subj


def run_tsne(X, y, perp, l_rate, subj):
    """Run t-SNE on X and save 2D scatter plot and t-SNE output."""
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.manifold import TSNE
    fname = op.join(SAVE_PATH, "{}_{}_{}".format(subj, perp, l_rate))
    # Run t-SNE. This takes the longest (about 2 hours?)
    X_tsne = TSNE(perplexity=perp, learning_rate=l_rate, n_iter=5000).fit_transform(X)

    # Make scatter plot.
    palette = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=palette[y.astype(np.int)])
    plt.title("Subj: {}; Perplexity: {}; L rate: {}".format(subj, perp, l_rate))

    # Save scatter plot.
    plt.savefig(fname + '.png')
    # Save t-SNE output array.
    np.save(fname + '.npy', X_tsne)


# Iternode to specify perplexity and learning rate arguments.
infosource = Node(IdentityInterface(fields=['perp_iter', 'l_rate_iter']),
                  name='iter_vals')
infosource.iterables = [('perp_iter', [20, 30, 50]),
                        ('l_rate_iter', [500, 750, 1000, 1500])]

# Function node to create X and y arrays.
X_y = Node(Function(input_names=[],
                    output_names=['X', 'y', 'subj'],
                    function=make_X_y),
           name='X_y')

# Function node to run t-SNE and save scatter plot and t-SNE output.
tsne = Node(Function(input_names=['X', 'y', 'perp', 'l_rate', 'subj'],
                     output_names=[],
                     function=run_tsne),
            name='tsne')

# Create the workflow.
base_dir = op.join('/', 'om', 'scratch', 'Tue', 'jakub')
wf = Workflow(name='wf', base_dir=base_dir)
wf.connect([(infosource, tsne, [('perp_iter', 'perp'), ('l_rate_iter', 'l_rate')]),
            (X_y, tsne, [('X', 'X'), ('y', 'y'), ('subj', 'subj')])])
wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=80GB'})
