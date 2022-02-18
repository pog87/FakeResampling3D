import numpy as np
import sys

import nibabel as nib


def matrix(fname):
    a = nib.load(fname)
    return np.asanyarray(a.dataobj)

def evaluate(a,seg):
    A   = matrix(a)
    Seg = matrix(seg)
    val = np.unique(Seg)
    S=[]
    for v in val:
        S.append(np.mean(A[Seg==v]))
    return S

funct = sys.argv[1]
mask = sys.argv[2]

res = evaluate(funct, mask)
print("Mean value per segment:")
print(res)
