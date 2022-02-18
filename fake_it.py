import sys
import numpy as np
import scipy.ndimage as ndim
import nibabel as nib

if len(sys.argv) < 3:
    print(f"usage: python {sys.argv[0]} functional.nii.gz anatomical_segment.nii.gz")
    sys.exit(0)

s = ndim.generate_binary_structure(3,1)

func = sys.argv[1]
anat = sys.argv[2]

f = nib.load(func)
F = np.array(f.dataobj)

a = nib.load(anat)
A = np.array(a.dataobj, dtype = int)

Idx = np.unique(A)

if not F.shape == A.shape:

    zoom = np.array(F.shape) / np.array(A.shape)
    A = ndim.zoom(A, zoom, order=0, mode='nearest')
    A = np.array(A, dtype = 'int')

C = []
for i in Idx:
    Fa = np.zeros_like(F)
    Fa[A==i] = F[A==i]
    for _ in range(5):
        Fa = ndim.grey_dilation(Fa, footprint = s)
        Fa = ndim.gaussian_filter(Fa, .5)
        Fa[A==i] = F[A==i]
    C.append(Fa)

D = np.concatenate(C, axis = 0)
nib.save(nib.Nifti1Image(D, f.affine), func.replace(".nii.gz", "_fake.nii.gz"))
