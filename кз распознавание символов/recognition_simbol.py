import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops
from skimage.io import imread
from pathlib import Path

save_path = Path(__file__).parent

def extractor(region):
    cy, cx = region.centroid_local
    cy /= region.image.shape[0]
    cx /= region.image.shape[1]

    return np.array([region.area/region.image.size, cy, cx])

def classificator(region, templates):
    features = extractor(region)
    result = ""
    min_d = 10 ** 16
    for symbol, t in templates.items():
        d = ((t - features) ** 2).sum() ** 0.5
        if d < min_d:
            result = symbol
            min_d = d

    return result

template = imread("alphabet-small.png")[:, :, :-1]
print(template.shape)
template = template.sum(2)

binary = template != 765

labeled = label(binary)
props = regionprops(labeled)

templates = {}

for region, symbol in zip(props, ["8", "0", "A", "B", "1", "W", "X", "*", "/", "-"]):
    templates[symbol] = extractor(region)

print(classificator(props[0], templates))

image = imread("alphabet.png")[:, :, :-1]
binary_big = image.mean(2) > 0

labeled_big = label(binary_big)
print(np.max(labeled_big))
aprops = regionprops(labeled_big)
result = {}

image_path = save_path / "out"
image_path.mkdir(exist_ok=True)


for region in aprops:
    symbol = classificator(region, templates)
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1
    plt.cla()
    plt.title(f"Class - '{symbol}'")
    plt.imshow(region.image)
    plt.savefig(image_path / f" image_{region.label}.png")
print(result)

plt.imshow(binary_big)
plt.show()