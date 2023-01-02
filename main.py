from Image import dataImage
from Participation import Participation1
import matplotlib.pyplot as plt
import numpy as np

arr = []

# for i in range(1, 10):
#    arr.append(dataImage(f"photos/s1/p{i}.jpg"))
#
# p1 = Participation1(arr)
# print(p1.perc)

import cv2
from skimage.filters import threshold_otsu

i1 = cv2.imread(f"photos/s1/p{19}.jpg")
i2 = cv2.imread(f"photos/s1/p{12}.jpg")

img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)

bg = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
phase = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

thresh = threshold_otsu(bg)
bg = bg < thresh

thresh = threshold_otsu(phase)
phase = phase < thresh

print(phase)

def count(bg, phase):
    pixels = 0
    shape = False
    show = pixels
    show[:, :] = False
    for i in range(0, len(bg)):
        for k in range(0, len(bg[0])):
            if phase[i, k]:
                pass





# diff1 = np.subtract(bg, phase)
# diff2 = np.subtract(phase, bg)
# sum1 = np.add(bg, phase)

fiq1, ax = plt.subplots()
ax.imshow(bg)
ax.set_title("bg")

fiq2, ax = plt.subplots()
ax.imshow(phase)
ax.set_title("phase")

plt.show()
