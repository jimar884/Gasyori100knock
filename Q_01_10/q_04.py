"""
大津の2値化
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def grayscale(img):
    """
    グレースケール化した画像を返す
    """
    blue = img[:, :, 0].copy()
    green = img[:, :, 1].copy()
    red = img[:, :, 2].copy()
    result = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    result = result.astype(np.uint8)

    return result

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_FILE_NAME = "kinkaku2.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
img = cv2.imread(FULL_PATH)

img2 = grayscale(img)
# ravel:1次元化
# bins:分割数
# rwidth:棒の幅
# range:横軸の目盛り
plt.hist(img2.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.xlabel('value')
plt.ylabel('appearance')
plt.show()

# cv2.imshow('grayscale', img2)
# cv2.waitKey(0)
