# Literature review

Template
N. Title  
  - Amount of user intervention
  - Method
  - Results
  - Notes

  1. A generative model for brain tumor segmentation in multi-modal images (Menze et al., 2010)
    - Automatic
    - Method
      - Model healthy brain, then model tumor state. Apply probabilities that each voxel is tumor.
      - .

1. Level-set evolution with region competition: automatic 3-d segmentation of brain tumors (Ho et al., 2002)
  - Automatic
  - Method
    - Used level-set snakes balanced by a probability map of T1 images of meningiomas and glioblastomas. Probability map gives probability that each voxel is tumor or not. Found by registering T1 pre- and post-contrast images and finding difference in intensities.
  - Results
    - Segmentation was about 85 to 90% in agreement with that of an expert.
  - Notes
    - Common method for segmentation: intensity thresholding, erosion, connectivity, and finally dilation. (Not generalizable)
    - Look at Warfield et al.

1. A brain tumor segmentation framework based on outlier detection (Prastawa et al., 2004)
  - Method
    - Used T2 MR images (non-contrasted). Detected abnormal regions with the help of a healthy brain atlas. Determine the intensity properties of the different tissue types. Finally, apply geometric and spatial constraints to the tumor region.
  - Results

1. Segmentation of brain structures in presence of a space-occupying lesion (Pollo et al., 2004)
  - Method
  - Notes
     - Segmented ventricles and basal ganglia in presence of meningioma. This could be useful for assessing improvement post-surgery.

1. Segmentation of meningiomas and low grade gliomas in MRI (Kaus et al., 1999)
  - Automatic
  - Method
    - Iterating over segmentation by (1) statistical classification and (2) registration.
    - Used k-Nearest Neighbors.

1. The multimodal brain tumor image segmentation benchmark (BRATS) (Menze et al., 2014)
  - Analysis of many segmentation methods (most are automatic)
  - Method
    - .
