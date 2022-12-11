import cv2
from skimage.filters import threshold_otsu


class dataImage:
    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(self.path)
        self.img = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.imgbin = self.calcotsu()

    def calcotsu(self):
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        thresh = threshold_otsu(img_gray)
        img_otsu = img_gray < thresh
        return img_otsu
