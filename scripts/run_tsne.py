"""Save 2-D t-SNE scatter plot and array."""
import os.path as op
from nipype import Node, Function, IdentityInterface, Workflow

imports = ['import os.path as op',
           'import matplotlib.pyplot as plt',
           'import nibabel as nib',
           'import numpy as np',
           'import seaborn as sns',
           'from sklearn.metrics import pairwise',
           'from sklearn.manifold import TSNE',
           ]

def run_tsne(perp, l_rate):
    """Return arrays X and y to be used in t-SNE. Also return the subj ID."""
    subj = 'case_005_2'

    PATH = "/om/user/jakubk/meningioma"
    SAVE_PATH = op.join(PATH, 'tsne_output')
    fname = op.join(SAVE_PATH, "{}_{}_{}".format(subj, perp, l_rate))

    # Load original scan and FAST segmentation
    print("Loading data ...")
    brain = nib.load(op.join(PATH, 'data/{}.nii.gz'.format(subj)))
    seg = nib.load(op.join(PATH, 'segmentation/fast/brain/classes_4/{}_brain_seg.nii.gz'.format(subj)))
    brain = brain.get_data()
    seg = seg.get_data()

    slice_ = 127
    b_slice = brain[:, :, slice_]
    s_slice = seg[:, :, slice_]

    b_slice_masked = np.ma.masked_array(b_slice, mask=~s_slice.astype(bool))
    b_slice_masked = np.ma.filled(b_slice_masked, fill_value=0.)

    print("Creating arrays X and y ...")
    X = b_slice_masked.flatten().reshape(-1, 1)
    y = s_slice.flatten().astype(np.int32)

    print("Computing similarity matrix ...")
    X_sim = pairwise.laplacian_kernel(X)

    # Run t-SNE. This takes the longest (about 2 hours?)
    print("Running t-SNE ...")
    X_tsne = TSNE(perplexity=perp, learning_rate=l_rate, n_iter=1000).fit_transform(X_sim)

    # Make scatter plot.
    print("Creating scatter plot ...")
    palette = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=palette[y.astype(np.int)])
    plt.title("Subj: {}; Perplexity: {}; L rate: {}".format(subj, perp, l_rate))

    # Save scatter plot.
    print("Saving scatter plot and t-SNE output array ...")
    plt.savefig(fname + '.png')
    # Save t-SNE output array.
    np.save(fname + '.npy', X_tsne)

    print("Finished.")


# Iternode to specify perplexity and learning rate arguments.
infosource = Node(IdentityInterface(fields=['perp_iter', 'l_rate_iter']),
                  name='iter_vals')
infosource.iterables = [('perp_iter', [20, 35, 50]),
                        ('l_rate_iter', [500, 1000, 1500, 2000])]

# Function node to run t-SNE and save scatter plot and t-SNE output.
tsne = Node(Function(input_names=['perp', 'l_rate'],
                     output_names=[],
                     function=run_tsne,
                     imports=imports),
            name='tsne')

# Create the workflow.
base_dir = '/om/scratch/Wed/jakub'
wf = Workflow(name='iter_tsne', base_dir=base_dir)
wf.connect([(infosource, tsne, [('perp_iter', 'perp'), ('l_rate_iter', 'l_rate')])])
wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=80GB'})



# # BROKEN CODE : raises EOFError after ~20 min, related to pickling # #
#
#
# """Save 2-D t-SNE scatter plot and array."""
# import os.path as op
# from nipype import Node, Function, IdentityInterface, Workflow
#
# imports = ['from os import path as op',
#            'import matplotlib.pyplot as plt',
#            # 'import nibabel as nib',
#            'import numpy as np',
#            'import seaborn as sns',
#            'from sklearn.metrics import pairwise',
#            'from sklearn.manifold import TSNE',
#            ]
#
# def make_X_y():
#     """Return arrays X and y to be used in t-SNE. Also return the subj ID."""
#     subj = 'case_005_2'
#
#     PATH = "/om/user/jakubk/meningioma"
#
#     # Load original scan and FAST segmentation
#     print("Loading data ...")
#     brain = nib.load(op.join(PATH, 'data', '{}.nii.gz'.format(subj)))
#     seg = nib.load(op.join(PATH, 'segmentation/fast/brain/classes_4/{}_brain_seg.nii.gz'.format(subj)))
#     brain = brain.get_data()
#     seg = seg.get_data()
#
#     slice_ = 127
#     b_slice = brain[:, :, slice_]
#     s_slice = seg[:, :, slice_]
#
#     b_slice_masked = np.ma.masked_array(b_slice, mask=~s_slice.astype(bool))
#     b_slice_masked = np.ma.filled(b_slice_masked, fill_value=0.)
#
#     print("Creating arrays X and y ...")
#     X = b_slice_masked.flatten().reshape(-1, 1)
#     y = s_slice.flatten().astype(np.int32)
#
#     print("Computing similarity matrix ...")
#     return pairwise.laplacian_kernel(X), y, subj
#
#
# def run_tsne(X, y, perp, l_rate, subj):
#     """Run t-SNE on X and save 2D scatter plot and t-SNE output."""
#     PATH = "/om/user/jakubk/meningioma"
#     SAVE_PATH = op.join(PATH, 'tsne_output')
#     fname = op.join(SAVE_PATH, "{}_{}_{}".format(subj, perp, l_rate))
#     # Run t-SNE. This takes the longest (about 2 hours?)
#     print("Running t-SNE ...")
#     X_tsne = TSNE(perplexity=perp, learning_rate=l_rate, n_iter=5000).fit_transform(X)
#
#     # Make scatter plot.
#     print("Creating scatter plot ...")
#     palette = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
#     plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=palette[y.astype(np.int)])
#     plt.title("Subj: {}; Perplexity: {}; L rate: {}".format(subj, perp, l_rate))
#
#     # Save scatter plot.
#     print("Saving scatter plot and t-SNE output array ...")
#     plt.savefig(fname + '.png')
#     # Save t-SNE output array.
#     np.save(fname + '.npy', X_tsne)
#
#     print("Finished.")
#
#
# # Iternode to specify perplexity and learning rate arguments.
# infosource = Node(IdentityInterface(fields=['perp_iter', 'l_rate_iter']),
#                   name='iter_vals')
# infosource.iterables = [('perp_iter', [20, 30, 50]),
#                         ('l_rate_iter', [500, 750, 1000, 1500])]
#
# # Function node to create X and y arrays.
# X_y = Node(Function(input_names=[],
#                     output_names=['X', 'y', 'subj'],
#                     function=make_X_y,
#                     imports=imports),
#            name='X_y')
#
# # Function node to run t-SNE and save scatter plot and t-SNE output.
# tsne = Node(Function(input_names=['X', 'y', 'perp', 'l_rate', 'subj'],
#                      output_names=[],
#                      function=run_tsne,
#                      imports=imports),
#             name='tsne')
#
# # Create the workflow.
# base_dir = op.join('/', 'om', 'scratch', 'Tue', 'jakub')
# wf = Workflow(name='wf', base_dir=base_dir)
# wf.connect([(infosource, tsne, [('perp_iter', 'perp'), ('l_rate_iter', 'l_rate')]),
#             (X_y, tsne, [('X', 'X'), ('y', 'y'), ('subj', 'subj')])])
# wf.run(plugin='SLURM', plugin_args={'sbatch_args': '--mem=80GB'})
