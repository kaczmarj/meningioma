# Literature review


## Existing software

1. [ITK-SNAP]()
1. [3D Slicer]()
1. [MICCAI Example 1](https://github.com/naldeborgh7575/brain_segmentation)
1. [dcemriS4](https://github.com/bjw34032/dcemriS4) (R package)
1. [BraTumIA](http://www.istb.unibe.ch/research/medical_image_analysis/software/index_eng.html)
1. [CAD workstation](http://ieeexplore.ieee.org/xpls/icp.jsp?arnumber=7208489)
1. [Matlab example 2D](https://github.com/Deepak1194/Brain-tumor-Segmentation)
1. [CRKIT](http://crl.med.harvard.edu/software/CRKIT/index.php)
1. [AutoSeg](https://www.nitrc.org/projects/autoseg/)



## Meningioma segmentation problem

1. A 3D Interactive Multi-object Segmentation Tool using Local Robust Statistics Driven Active Contours (Gao et al., 2012)
  - Semi-automatic
  - Method
    - Compare 3D Slicer, ITK-SNAP, and manual segmentation.

1. Segmentation of meningiomas and low grade gliomas in MRI (Kaus et al., 1999)
  - Automatic (but user selects sample points for each tissue class).
  - Method
    - Based on 'Adaptive Template moderated Classification'.
    - Segments tissue into skin, brain, ventricles, and tumor (i.e., meningioma or low-grade glioma).
    - Iterating over segmentation by (1) statistical classification and (2) registration.
    - Used k-Nearest Neighbors.
  - Results
    - Comparable to manual segmentation.


1. Automatic Brain Tumor Segmentation by Subject Specific Modification of Atlas Priors (Prastawa et al., 2003)
  - Automatic
  - Method
    - Used healthy priors and tumor priors.
      - Co-registered T1, T1-contrast, and T2 to common space, then registered those to ICBM brain atlas.
      - Subtracted T1 from T1 contrast. (Model histograms?)
      - Created prior probability map for tumor using the histogram model?
      - .
  - Results
    - .


1. Automated segmentation of MR images of brain tumors (Kaus et al., 2001)
  - Automatic
  - Method
    - .
  - Results
    - .


1. Automatic segmentation of meningioma from non-contrasted brain MRI integrating fuzzy clustering and region growing (Hsieh et al., 2011)
  - Automatic
  - Method
    - Used fuzzy-c clustering, then region growing, and some knowledge-based information.
  - Results
    - Performance was comparable to previous automatic segmentation techniques.



## General tumor segmentation problem

1. Multimodal Brain Tumor Segmentation Challenge (BraTS)
  - Attempt to segment gliomas (more difficult than meningiomas).
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


1. Multi-modal glioblastoma segmentation: man versus machine (Porz et al., 2014)
  - Automatic
  - Test of Brain Tumor Image Analysis software (aka BraTumIA).
  - Related papers: Meier et al., 2017; Bauer et al., 2012; Bauer et al., 2011.


1. Brain tumor segmentation with deep neural networks (Havaei et al., 2016)
  - .


## Related reading

1. [Expectation maximization slideshow](http://nmr.mgh.harvard.edu/~koen/Miccai2003Tutorial_VanLeemput.pdf)
  - [Tutorial paper](http://www.cs.huji.ac.il/~yweiss/emTutorial.pdf)
  - [EM in Python](https://people.duke.edu/~ccc14/sta-663/EMAlgorithm.html)
  - Intensity distributions of different tissue classes are modeled as normal distributions.
  - Gaussian mixture model: if the mean and variance of each tissue type is known, voxels can be classified based on their intensity.
  - Expectation maximization algorithm:
    - "If the tissue labels were known, parameter estimation would straightforward. EM algorithm iteratively fills in [tissue labels] and updates the parameters accordingly."
    - Expectation step:
      - Classify the voxels based on current parameter estimation.
    - Maximization step:
      - Re-estimate the parameters based on current classification.
    - Iterate over E and M steps.
  - The E step of the EM algorithm can take into account prior probability maps. Introduces geometrical constraints. Atlas is used to initialize the EM algorithm.
  - MR field inhomogeneity is also known as bias field. EM algorithm can take this into account.
