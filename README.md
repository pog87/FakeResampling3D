# FakeResampling3D
Fake Nodes scheme for Gibbs-free 3D medical image resampling

This software provides a Fake Nodes resampling scheme for multimodal medical imaging proposed in the paper 

> "Reducing the Gibbs effect in multimodal medical imaging by the Fake Nodes Approach".

For a sample of its usage, see the `main.sh` files where the Shepp Logan phantom `SL_lq.nii.gz` get resampled to the same size of `SL_hq.nii.gz` both with trilinear interpolation (as provided by ANTs) and with the Fake Nodes approach plus trilinear interpolation.
