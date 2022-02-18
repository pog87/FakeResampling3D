import sys
import numpy as np
import scipy.ndimage as ndim
import nibabel as nib

if len(sys.argv) < 3:
    print(f"usage: python {sys.argv[0]} functional_fake_upscaled.nii.gz anatomical_segment.nii.gz")
    sys.exit(0)

s = ndim.generate_binary_structure(3,1)

func = sys.argv[1]
anat = sys.argv[2]

f = nib.load(func)
F = np.array(f.dataobj)

a = nib.load(anat)
A = np.array(a.dataobj, dtype = int)

Idx = np.unique(A)

F = F.reshape((len(Idx), A.shape[0],A.shape[1],A.shape[2]))

C = np.zeros(A.shape)

for i in Idx:
    Fx = F[i, :, :, :]
    C[A==i] = Fx[A==i]

nib.save(nib.Nifti1Image(C, f.affine), func.replace(".nii.gz", "_unfake.nii.gz"))
