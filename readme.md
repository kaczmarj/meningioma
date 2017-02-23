# Meningioma

Goals
-----
1. To automatically segment meningiomas pre- and post-surgery.
1. To assess brain's spatial recovery post-surgery.

- Data is available on [Brainbox](http://brainbox.pasteur.fr/project/meningioma)
- [Ongoing literature search](/lit_review.md)


Table of contents
-----------------
1. [Ground truth segmentation](#ground-truth-segmentation)
1. [Segmentation with slicer](#segmentation-with-slicer)
1. [ANTs brain extraction](#ants-brain-extraction)
1. [t-SNE on synthetic brain](#t-sne-on-synthetic-brain)


Ground truth segmentation
-------------------------

| case | segmented | reviewed |
|:----:|:---------:|:--------:|
| [001](http://brainbox.pasteur.fr/mri/?url=https://dl.dropbox.com/sh/71jbelduefu41xs/AADysls57HwmJT0pdbbSVI4Na/case_001_2.nii.gz) | &#10004; | |
| [002](http://brainbox.pasteur.fr/mri/?url=https://dl.dropbox.com/sh/71jbelduefu41xs/AAAx8y8Mp_jh0yad1CjD2Z4Ra/case_002_2.nii.gz) | &#10004; | |
| [003](http://brainbox.pasteur.fr/mri/?url=https://dl.dropbox.com/sh/71jbelduefu41xs/AABhDQJ-GQKMzHdFDGN6MrFBa/case_003_2.nii.gz) | &#10004; | |


Segmentation with Slicer
------------------------

An example of semi-automatic segmentation with Slicer's Segmentation Editor module.

<img src='/images/project_week/case_052_2_slicer_seg.png?raw=true', height=400>



ANTs brain extraction
---------------------

We attempted to remove the skull with ANTs `antsBrainExtraction.sh`. Results were mixed. In some cases, the script performed well. In other cases, parts of the brain were removed, or parts of the skull (usually close to the meningioma) remained.

<img src='/images/project_week/case_052_ants_brain.png?raw=true', height=300>

Above: successful brain extraction.

<img src='/images/project_week/case_001_ants_brain_failure.png?raw=true', height=300>

Above: unsuccessful brain extraction.



t-SNE on synthetic brain
------------------------

[[source](/notebooks/dim_reduction.ipynb)]

- blue == background
- green == skull
- red == brain
- cyan == tumor

<table>
  <tr>
    <td><img src='/images/tsne/synthetic_brain_0.png?raw=true', width=200></td>
    <td><img src='/images/tsne/tsne_synthetic_brain_0.png?raw=true'></td>
  </tr>
  <tr>
    <td><img src='/images/tsne/synthetic_brain_1.png?raw=true', width=200></td>
    <td><img src='/images/tsne/tsne_synthetic_brain_1.png?raw=true'></td>
  </tr>
  <tr>
    <td><img src='/images/tsne/synthetic_brain_2.png?raw=true', width=200></td>
    <td><img src='/images/tsne/tsne_synthetic_brain_2.png?raw=true'></td>
  </tr>
</table>
