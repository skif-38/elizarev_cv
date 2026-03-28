import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import opening, dilation, closing, erosion

image = np.load("coins.npy")

labeled = label(image)



def area(image, label=1):
    return (image == label).sum()


# for i in range(1, np.max(labeled) + 1):
#         print(f"Area = {area(labeled, label=i)}")
slov = {}   
for n in range(1, labeled.max()+1):
    s_coin = area(labeled, n)
    if s_coin not in slov:
        slov[s_coin] = 1
    else:
        slov[s_coin] += 1

sort_slov = dict(sorted(slov.items()))

nominals = [1, 2, 5, 10]
sum = 0
i = 0
for val in sort_slov:
    count = sort_slov[val]
    if i < len(nominals):
        nominal = nominals[i]
        sum += count * nominal
        print(f"Номинал: {nominal}, количество: {count}")
    i += 1

print(f"Cумма: {sum}")

plt.imshow(labeled)
plt.show()