import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import opening, dilation, closing, erosion

image = np.load("wires6.npy")
struct = np.ones((3, 1))
processed = opening(image, footprint=struct)
labeled = label(image)
count = labeled.max()

for n in range(1, labeled.max()+1):
    wire = labeled == n
    parts = label(opening(wire, footprint=struct))
    
    print(f"Провод = {n}, parts = {parts.max()}")


plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(processed)
plt.show()