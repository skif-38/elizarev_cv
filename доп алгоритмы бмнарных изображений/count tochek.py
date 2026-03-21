import numpy as np
import matplotlib.pyplot as plt
from skimage import measure

M1 = np.array([[0, 0], [0, 1]])
M2 = np.array([[0, 1], [1, 1]])

def euler(labled, lebel):
    obj = labled == label
    m1_count = 0
    m2_count = 0
    for y in range(obj.shape[0]-1):
        for x in range(obj.shape[1]-1):
            sub = obj[y:y+2, x:x+2]
            if np.all(M1 == sub):
                m1_count
            elif np.all(M2 == sub):
                m2_count += 1
        return abs(m1)

data = np.load(r"\\wsl.localhost\Ubuntu\home\skif\elizarev_cv\доп алгоритмы бинарных изображений\holes.npy")
labeled = measure.label(data)

for lebel in np.unique(labeled)[1:]:
    print(euler(labeled, lebel))


plt.imshow(labeled)
plt.show()