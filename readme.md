# Meningioma

How accurately can we detect meningiomas?

Data on [Open Neuroimaging Laboratory](http://openneu.ro/metasearch/)

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


Similarity matrix: gives you an array of values that indicates the similarities
of your inputs. Similar to a covariance matrix.

Cosine similarity uses some distance metric (e.g., euclidian, manhattan, etc.)

Manifold will give you clusters (hopefully).

t-SNE: http://distill.pub/2016/misread-tsne/

silhouette coefficient (score) gives you sense of whether or not there is a
good amount of clustering in your outputs.

Look at Greg's post on Slack.

Good slice: case_005_2


Clemens: consider a searchlight approach. The meningioma should have less variability than other parts of the brain, so the searchlight could locate part of the tumor, and then region-growing could discover the rest.
