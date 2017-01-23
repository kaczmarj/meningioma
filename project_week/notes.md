# Meningioma project notes


Skull strip
-----------
- Use ANTs BrainExtraction with different templates. See which template works best.


Segmentation
------------
- Try ANTs and FAST. FreeSurfer?


Notes from Satra
----------------
Import segmentation NIFTI into nibabel, convert to numpy array, and compute a similarity matrix.

Embedding is a method of dimensionality reduction. Techniques:

  - Diffusion map (satra has a script)
  - TSNE
  - kernel PCA


After embedding, brain becomes cloud of points in reduced dimensional space. A subset of the cloud will be the tumor. Clouds from different brains should share some subset, which is the tumor. Register the brains together.

- Look for template with > 3 classes (lesion template).
- Look at histogram of intensities. Histogram registration (anything in ANTs?).
- Make sure physical connection plays a role in classification.
