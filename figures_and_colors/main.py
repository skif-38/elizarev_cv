import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.io import imread 
from skimage.color import rgb2hsv as hsv
from pathlib import Path






current_path = Path(__file__).parent
image = imread(current_path / "balls_and_rects.png")



hsv = hsv(image)
h = hsv[:, :, 0]

colors_rectangle = []
colors_circle = []

for color in np.unique(h):
    if color == 0.0:
        continue
    binary = h == color
    labeled = label(binary)
    props = regionprops(labeled)
    for region in props:
        extent = region.extent
        if extent > 0.9:
            colors_rectangle.append(color)
        else:
            colors_circle.append(color)






groups_rectangle = [[colors_rectangle[0]]]
group_circle = [[colors_circle[0]]]

delta = 0.051




for i in range(1, len(colors_circle)):
    if abs(colors_circle[i - 1] - colors_circle[i]) < delta:
        group_circle[-1].append(colors_circle[i])
    else:
        group_circle.append([colors_circle[i]])



for i in range(1, len(colors_rectangle)):
    if abs(colors_rectangle[i - 1] - colors_rectangle[i]) < delta:
        groups_rectangle[-1].append(colors_rectangle[i])
    else:
        groups_rectangle.append([colors_rectangle[i]])




print(f"Rectangles. Count elements {sum(len(row) for row in groups_rectangle)}: ")
for grp in groups_rectangle:
    print(f"Mean value - {np.mean(grp)}, count - {len(grp)} ")

print(f"Circles. Count elements {sum(len(row) for row in group_circle)}: ")
for grp in group_circle:
    print(f"Mean value - {np.mean(grp)}, count - {len(grp)} ")

print(f"All elements: {sum(len(row) for row in groups_rectangle) + sum(len(row) for row in group_circle)}")