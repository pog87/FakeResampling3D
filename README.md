# FakeResampling3D
Fake Nodes scheme for Gibbs-free 3D medical image resampling

This software provides a Fake Nodes resampling scheme for multimodal medical imaging proposed in the preprint

> "Reducing the Gibbs effect in multimodal medical imaging by the Fake Nodes Approach". https://arxiv.org/abs/2202.10325

For a sample of its usage, see the `main.sh` files where the Shepp Logan phantom `SL_lq.nii.gz` get resampled to the same size of `SL_hq.nii.gz` both with trilinear interpolation (as provided by ANTs) and with the Fake Nodes approach plus trilinear interpolation.

To verify that Fake Nodes resampling leads to a higher accuracy in assessing the mean value per segment, execute the script `main_execution.sh`.


## Requirements:

 * python >= 3.9
 * numpy
 * scipy
 * nibabel >= 3.1
 * ANTs https://github.com/ANTsX/ANTs
