# Meningioma

Goals
-----
1. To automatically segment meningiomas pre- and post-surgery.
1. To assess brain's spatial recovery post-surgery.


- Data is available on [Open Neuroimaging Laboratory](http://openneu.ro/metasearch/)
- [Ongoing literature search](/lit_review.md)



Table of contents
-----------------
1. [Segmentation with slicer](#segmentation-with-slicer)
1. [ANTs brain extraction](#ants-brain-extraction)
1. [t-SNE on synthetic brain](#t-sne-on-synthetic-brain)



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
