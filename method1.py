import cv2
import matplotlib.pyplot as plt
import numpy as np

i1 = cv2.imread(f"photos/s1/p{19}.jpg")
i2 = cv2.imread(f"photos/s1/p{8}.jpg")

img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2RGB)


def diff(bg, phase):
    newImg = np.zeros([len(bg), len(bg[0])])
    for i in range(0, len(bg)):
        for k in range(0, len(bg[0])):
            deltaR = pow(bg[i, k, 0], 2) - pow(phase[i, k, 0], 2)
            deltaG = pow(bg[i, k, 1], 2) - pow(phase[i, k, 1], 2)
            deltaB = pow(bg[i, k, 2], 2) - pow(phase[i, k, 2], 2)
            Delta = deltaR + deltaG + deltaB
            # print(abs(Delta))
            if abs(Delta) > 45000:
                newImg[i, k] = False
            else:
                newImg[i, k] = True
    return newImg


def clear_photo(img):
    out = np.copy(img)
    kernel = np.ones((20, 20), np.uint8)
    opening = cv2.morphologyEx(out, cv2.MORPH_OPEN, kernel)
    for i in range(0,  len(opening)):
        for k in range(0, len(opening[0])):
            if opening[i, k]:
                opening[i, k] = False
            else:
                opening[i, k] = True
    kernel = np.ones((125, 125), np.uint8)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel)

    return opening


fiq1, ax = plt.subplots()
ax.imshow(img1)
ax.set_title("bg")

fiq2, ax = plt.subplots()
ax.imshow(img2)
ax.set_title("phase")

img3 = diff(img1, img2)
opening = clear_photo(img3)


fiq3, ax = plt.subplots()
ax.imshow(img3)
ax.set_title("phase diff")

fiq4, ax = plt.subplots()
ax.imshow(opening)
ax.set_title("phase diff2")

plt.show()
