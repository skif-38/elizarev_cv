import numpy as np
from skimage.measure import label
from skimage.morphology import opening

data = np.load('stars.npy')

kernel_vertical = np.array([
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0]])

kernel_diag = np.array([
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1]])

after_plus = opening(data, footprint=kernel_vertical)
after_cross = opening(data, footprint=kernel_diag)
labeled_plus = label(after_plus)
labeled_cross = label(after_cross)
result = labeled_cross.max() + labeled_plus.max()
print(result)