import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import opening, dilation, closing, erosion

def area(labeled, label=1):
    return (labeled == label).sum() 

def centroid(labeled, label=1):
    ys, xs = np.where(labeled == label)
    if len(ys) == 0:
        return None, None
    cy = np.mean(ys)
    cx = np.mean(xs)
    return cy, cx

def neighbours4(y, x):
    return [(y, x+1), (y+1, x), (y, x-1), (y-1, x)]

def neighboursX(y, x):
    return [(y-1, x+1), (y+1, x+1), (y+1, x-1), (y-1, x-1)]

def neighbours8(y, x):
    return neighbours4(y, x) + neighboursX(y, x)

def get_bounds(labeled, label=1, connectivity=neighbours4):
    pos = np.where(labeled == label)
    bounds = []
    
    for y, x in zip(*pos):
        for yn, xn in connectivity(y, x):
            if yn < 0 or yn >= labeled.shape[0]:
                bounds.append((y, x))
                break
            elif xn < 0 or xn >= labeled.shape[1]:
                bounds.append((y, x))
                break
            elif labeled[yn, xn] != label:
                bounds.append((y, x))
                break
    return bounds

if __name__ == "__main__":

    labeled = np.zeros((16, 16), dtype="int")
    labeled[4:, :4] = 2
    labeled[12:-1, 6:9] = 3

    labeled[3:10, 8:] = 1
    labeled[[3, 4, 3], [8, 8, 9]] = 0
    labeled[[8, 9, 9], [8, 8, 9]] = 0
    labeled[[3, 4, 3], [-2, -1, -1]] = 0
    labeled[[9, 8, 9], [-2, -1, -1]] = 0

    for i in range(1, np.max(labeled) + 1):
        print(f"Area = {area(labeled, label=i)}") 

    plt.imshow(labeled, cmap='gray')
    
    for i in range(1, np.max(labeled) + 1):
        cy, cx = centroid(labeled, i)
        if cy is not None:
            plt.scatter(cx, cy, color='red', s=50)
        
        bounds = get_bounds(labeled, label=i, connectivity=neighbours4)
        for y, x in bounds:
            plt.scatter(x, y, color='blue', s=10)
    
    plt.show()