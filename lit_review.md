# Literature review

1. Multimodal Brain Tumor Segmentation Challenge (BraTS)
  - Analysis of many segmentation methods (many are automatic)
  - [BraTS website](http://braintumorsegmentation.org/)
  - Training and testing data available [here](https://www.smir.ch/BRATS/Start2015) (registration required).
    - ~300 glioma cases. All have T1, T1-contrast, T2, and T2 FLAIR. All have associated target values.


1. A brain tumor segmentation framework based on outlier detection (Prastawa et al., 2004)
  - Automatic
  - Method
    - Three stages: 1) detect abnormal regions with the help of a healthy brain atlas; 2) determine whether region has tumor and edema; 3) apply spatial and geometric constraints.
      - Stage 1: Use probabilistic brain atlas (Evans et al., 1993). Register subject scan to the atlas. Get random samples of each tissue class (white matter, gray matter, CSF). Intensities of the different tissue types cluster well and are normally distributed. Remove outliers from normal tissue types. For the voxels with intensities differing from normal tissue or voxels that are not in an expected location, add the voxels to "abnormal" class.
      - Stage 2: Cluster "abnormal" into edema and tumor classes.
      - Stage 3: Remove false positives with geometric and spatial constraints.
  - Results
    - Used VALMET segmentation validation tool (Gerig et al., 2001).
    - One rater segmented several scans at two different times. Automatic segmentation was different from the first rating to a similar degree that the first rating was different from the second rating.
      - A lot of the variability came from the edema segmentation. Would that be relevant to our project?
    - Segmenting each case took about 1 h 30 min.


1. A generative model for brain tumor segmentation in multi-modal images (Menze et al., 2010)
    - Automatic
    - Method
      - Use priors to determine each voxel's probability of being a certain tissue class (white matter, gray matter, and CSF) in each imaging modality; then estimate each voxel's probability of being tumor or not, using some unknown parameters. A separate algorithm estimates the unknown parameters using the Maximum Likelihood method.
    - Results
      - Outperforms several other EM (expectation-maximization) segmentation methods.
      - Not in the paper, but this method was one of the best in the BraTS competition.
    - Notes
      - Could not find code implementation online. Trying to implement in Python.


1. Level-set evolution with region competition: automatic 3-d segmentation of brain tumors (Ho et al., 2002)
  - Automatic
  - Method
    - Used level-set snakes balanced by a probability map of T1 images of meningiomas and glioblastomas. Probability map gives probability that each voxel is tumor or not. Found by registering T1 pre- and post-contrast images and finding difference in intensities.
  - Results
    - Segmentation was about 85 to 90% in agreement with that of an expert.
  - Notes
    - Common method for segmentation: intensity thresholding, erosion, connectivity, and finally dilation. (Not generalizable)
    - Look at Warfield et al.


1. Segmentation of brain structures in presence of a space-occupying lesion (Pollo et al., 2004)
  - Method
  - Notes
     - Segmented ventricles and basal ganglia in presence of meningioma. This could be useful for assessing improvement post-surgery.


1. Segmentation of meningiomas and low grade gliomas in MRI (Kaus et al., 1999)
  - Automatic
  - Method
    - Iterating over segmentation by (1) statistical classification and (2) registration.
    - Used k-Nearest Neighbors.


1. Multi-modal glioblastoma segmentation: man versus machine (Porz et al., 2014)
  - Automatic
  - Test of Brain Tumor Image Analysis software (aka BraTumIA).
  - Related papers: Meier et al., 2017; Bauer et al., 2012; Bauer et al., 2011.


1. Brain tumor segmentation with deep neural networks (Havaei et al., 2016)
  - .
