# Author: Jakub Kaczmarzyk <jakubk@mit.edu>
"""Python implementation of algorithm described by Menze and colleagues (2010).

Menze, B. H., Van Leemput, K., Lashkari, D., Weber, M. A., Ayache, N., &
    Golland, P. (2010, September). A generative model for brain tumor
    segmentation in multi-modal images. In International Conference on Medical
    Image Computing and Computer-Assisted Intervention (pp. 151-159). Springer
    Berlin Heidelberg.

Notes
-----
C is number of channels (observations for each voxel). Imaging modalities?
k sub i is tissue class of voxel i. This is known.
a is probabilistic atlas (prob of being tumor).
a sub i is voxel i's probability of being a tumor. This is unknown.
t sub i is a binary vector of length c indicating whether voxel i is classified
    as tumor in each channel c. Value of 1 indicates tumor is present.
beta affects smoothness of segmentations. This is the only adjustable arg.
"""
from __future__ import division, print_function
import numpy as np

# 1. Generative tumor model
#
# 1a. Normal state -- p(k sub i = k)
#   This is known from priors. Is this each voxel's probability of being a
#   tissue type in k? So for K=3, each voxel would have three probabilities.
#
#   p(k sub i = k) = pi sub ki.
def normal_state():
    """Multinomial distribution for a voxel's tissue label."""
    pass


# 1b. Tumor state -- p(t sub i; a sub i)
#   The probability that tumor is present in voxel i.
def tumor_state(a_voxel, t_voxel):
    """Return probability that voxel is a tumor, given "latent" probabilistic
    atlas. In the paper, this is p(t sub i; a sub i), where i is a voxel.

    Parameters
    ----------
    a_voxel: scalar
        Probability that this voxel is a tumor. Defined by "latent"
        probabilistic atlas.
    t_voxel: ndarray
        Array of {0, 1} that indicates presence of tumor in channel c. Value of
        1 indicates tumor is present. Array has shape (C, ), where C is the
        number of channels.
    """
    return np.prod([np.power(a_voxel, t_voxel_c)
                    * np.power((1 - a_voxel), (1 - t_voxel_c))
                    for t_voxel_c in t_voxel])


# 1c. Data likelihood -- p(y sub i | t sub i, k sub i; theta.)
#
#
# # Make gaussian distribution.
# np.random.normal(mean, stdev), where stdev == np.sqrt(variance)
#
# theta is the set of all mean and variance parameters for the gaussian
# distributions.
# Should have shape (n_tissue_classes + 1, n_channels, 2).
# First axis is n_tissue_classes + 1 to account for the tumor.
#
# y sub i is vector of intensity observations at voxel i for each channel. Does
# this mean y sub i has the original intensity values for each channel?

theta = np.zeros((K + 1, C, 2))
# This is not correct yet. But this is the basic idea.
gaussians = np.array([np.random.normal(mean, np.sqrt(var))
                      for mean, var in theta])

def data_likelihood(y_voxel, k_voxel, t_voxel, gaussians, K):
    """Return image observation for a voxel. In the paper, this is
    p(y sub i | t sub i, k sub i; theta)

    Create Gaussians outside of the function, so distributions are not created
    for each voxel.

    y_voxel: ndarray
        Array of intensity observations at one voxel in each channel.
    k_voxel: int
        The tissue class of the voxel.
    t_voxel: ndarray
        Array of {0, 1} that indicates presence of tumor in channel c. Value of
        1 indicates tumor is present. 1-D array with length C, where C is the
        number of channels.
    gaussians: ndarray
        1-D array of normal distributions with length (K + 1).
    K: int
        Number of healthy tissue classes.
    """
    return np.prod([np.power(gaussians[k_voxel, c], (1 - t_voxel[c]))
                    * np.power(gaussians[K + 1, c], t_voxel[c])
                    for c in range(t_voxel)])


# 2. Maximum likelihood parameter estimation
