# Author: Jakub Kaczmarzyk <jakubk@mit.edu>
"""Python implementation of algorithm described by Menze and colleagues (2010).

Menze, B. H., Van Leemput, K., Lashkari, D., Weber, M. A., Ayache, N., &
    Golland, P. (2010, September). A generative model for brain tumor
    segmentation in multi-modal images. In International Conference on Medical
    Image Computing and Computer-Assisted Intervention (pp. 151-159). Springer
    Berlin Heidelberg.

Notes
-----
c is number of channels (observations for each voxel). Each imaging modality?
k sub i is tissue class of voxel i. This is known.
a is probabilistic atlas (prob of being tumor).
a sub i is voxel i's probability of being a tumor. This is unknown.
t sub i is a binary vector of length c indicating whether voxel i is classified
    as tumor in each channel c.
"""
from __future__ import print_function

import numpy as np

C = 2  # Number of image modalities.
K = 3  # Number of tissue classes.
orig_slice = np.ones((256, 256))
img_x, img_y = orig_slice.shape  # Image dimensions.

# 1. Generative tumor model
#
# 1a. Normal state -- p(k sub i = k)
#   This is known from priors. Is this each voxel's probability of being a
#   tissue type in k? So for K=3, each voxel would have three probabilities.
#
#   p(k sub i = k) = pi sub ki.
def normal_state():
    """"""
    pass

# 1b. Tumor state -- p(t sub i; a sub i)
#   The probability that tumor is present in voxel i.
#   Array `t` could have shape (1, C) or shape (n_voxels, C) (or somethine else)
#   Better: `t` could have shape (X, Y, C). For example, (256, 256, 4).


a = np.zeros((img_x, img_y))  # Tumor presence probabilities. (How is this different from t?)
t_c = np.zeros((img_x, img_y, C))  # Binary array of tumor presence in each channel.
t = np.zeros((img_x, img_y))  # Initialize empty array for tumor prob values.

def tumor_state(a, t_c, C):
    """Return array of voxel-wise probability of tumor presence. A greater value
    indicates greater chance that tumor is present in that voxel.

    Parameters
    ----------
    a: array of tumor presence probabilities.
    t_c: array of latent tumor state in each channel. Atlas `a` in the paper.
    C: int, number of imaging modalities.

    Returns
    -------
    t: array of voxel-wise probability of tumor presence.
    """
    img_x, img_y = a.shape
    t = np.zeros((img_x, img_y))
    # Look at np.nditer docs to iterate over two arrays at once.
    for x in range(img_x):
        for y in range(img_y):
            t[x, y] = np.prod([np.power(a[x, y], t_c[x, y, c])
                               * np.power((1 - a[x, y]), (1 - t_c[x, y, c]))
                               for c in range(C)])
    return t


# 1c. Data likelihood -- p(y sub i | t sub i, k sub i; theta.)
#
#
# # Make gaussian distribution.
# np.random.normal(mean, stdev), where stdev == np.sqrt(variance)
#
# theta is the set of all mean and variance parameters for the gaussian distributions.
# Should have shape (n_tissue_classes + 1, n_channels, 2).
# First axis is n_tissue_classes + 1 to account for the tumor.
#
# y sub i is vector of intensity observations at voxel i for each channel. Does
# this mean y sub i has the original intensity values for each channel?

theta = np.zeros((K + 1, C, 2))  # Last axis contains (mean, stdev).

def data_likelihood():
    y = np.zeros((img_x, img_y))
    for x in range(img_x):
        for y in range(img_y):
            this_k = 0  # Predicted tissue class of this voxel. From normal_state().
            y[x, y] = np.prod([np.power(dist_1(theta[this_K, c, 0], theta[this_K, c, 1]), (1 - t_c[x, y, c]))
             * np.power(dist_2(theta[K+1, c, 0], theta[K+1, c, 1]), t_c[x, y, c])
             for c in range(C)])



# 2. Maximum likelihood parameter estimation









#
