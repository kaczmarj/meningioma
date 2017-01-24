from __future__ import division, print_function
from os import path as op

import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
from sklearn.metrics import pairwise
from sklearn.manifold import TSNE
import seaborn as sns

PATH = '/om/user/jakubk/meningioma'
SAVE_PATH = '/om/user/jakubk/meningioma/tsne_output'

# Load original scan and FAST segmentation
subj = 'case_005_2'
brain = nib.load(op.join(PATH, 'data/{}.nii.gz'.format(subj)))
seg = nib.load(op.join(PATH, 'segmentation/fast/brain/classes_4/{}_brain_seg.nii.gz'.format(subj)))
brain = brain.get_data()
# Segmentation done by FSL's FAST with 4 classes on an extracted brain (with ANTs).
seg = seg.get_data()

slice_ = 127
b_slice = brain[:, :, slice_]
s_slice = seg[:, :, slice_]

# Apply mask to remove skull.
b_slice_masked = np.ma.masked_array(b_slice, mask=~s_slice.astype(bool))

X = b_slice_masked.flatten().reshape(-1, 1)
y = b_slice.flatten()

# Color pallete.
palette = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])

X_sim = pairwise.laplacian_kernel(X)

for l_rate in [500, 750, 1000, 2000]:
    for perp in [20, 30, 50]:
        fname = '{}_{}_{}'.format(subj, perp, l_rate)
        fname = op.join(SAVE_PATH, fname)
        
        X_tsne = TSNE(perplexity=perp, learning_rate=l_rate).fit_transform(X_sim)
        
        np.save(fname + '.npy', X_tsne)
        plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=palette[y.astype(np.int)])
        plt.title("Subj: {}; Perplexity: {}; L rate: {}".format(subj, perp, l_rate))
        plt.savefig(fname + '.png')
