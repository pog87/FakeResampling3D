import numpy as np
import sys

import nibabel as nib
from skimage.metrics import structural_similarity as ssim
# computes some error measures between two images
# Inputs: image1.nii.gz image2.nii.gz

def matrix(fname):
    a = nib.load(fname)
    return np.asanyarray(a.dataobj)


def RMSE(X,Y):
    return np.sqrt(np.mean((X - Y) ** 2))


def PSNR(X,Y):
    rmse = RMSE(X,Y)
    if(rmse == 0):
        return 100
    else:
     return  20. * np.log10( max(X.max(), Y.max()) / rmse)

def SSIM(X,Y):
     return ssim(X, Y,data_range=X.max() - Y.min())

a = sys.argv[1]
b = sys.argv[2]

A = matrix(a)
B = matrix(b)

print(f"RMSE: {RMSE(A,B)}")
print(f"PSNR: {PSNR(A,B)}")
print(f"SSIM: {SSIM(A,B)}")
