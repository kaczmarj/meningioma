# Notes for segmentation project


Look into
---------

- Literature search
  1. What have people done in tumor segementation?

- Segmentation algorithms
  1. Ants segmentation tool
  1. FAST (FSL tool)
  1. Slicer segmentation tool
  1. SPM segmentation tool
  1. ITK-SNAP
  1. SIFT

- Clustering
  1. scikit-learn


Read
----
[MIT EM tutorial](http://www.cs.huji.ac.il/~yweiss/emTutorial.pdf)
[EM coin toss](http://ai.stanford.edu/~chuongdo/papers/em_tutorial.pdf)
[EM slideshow](http://nmr.mgh.harvard.edu/~koen/Miccai2003Tutorial_VanLeemput.pdf)
[EM Python implementation](https://people.duke.edu/~ccc14/sta-663/EMAlgorithm.html)
[Python stats implementations](http://python-for-signal-processing.blogspot.com/2012/11/expectation-maximization-expectation.html)




Notes
-----

Similarity matrix: gives you an array of values that indicates the similarities
of your inputs. Similar to a covariance matrix.

Cosine similarity uses some distance metric (e.g., euclidian, manhattan, etc.)

Embedding will give you clusters (hopefully).

t-SNE: http://distill.pub/2016/misread-tsne/

silhouette coefficient (score) gives you sense of whether or not there is a
good amount of clustering in your outputs.

Clemens: consider a searchlight approach. The meningioma should have less variability than other parts of the brain, so the searchlight could locate part of the tumor, and then region-growing could discover the rest.

number after back-tic is patient ID.
1-5 pre-op. 6-10 post-op
T1, T1- contrast, T2, T2-flair, ADC (static image from diffusion-like scan.).
