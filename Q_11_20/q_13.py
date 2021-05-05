"""
Min Max Filter
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def grayscale(img):
    H, W, _ = img.shape
    result_img = np.zeros((H, W))
    blue = img[:, :, 0].copy()
    green = img[:, :, 1].copy()
    red = img[:, :, 2].copy()
    result_img = 0.299*red + 0.587*green + 0.114*blue
    result_img = result_img.astype(np.uint8)

    return result_img


def min_max_filter(img, k_size=3):
    """
    input BGR image, standard deviation and kernel size(k_seze x k_size)
    return BGR image filtered by Men-Max filter
    """
    heignt, width, _ = img.shape

    pad = k_size // 2
    result_img = np.zeros((heignt+pad*2, width+pad*2), dtype=np.float)
    result_img[pad:pad+heignt, pad:pad+width] = grayscale(img).astype(np.float)

    tmp = result_img.copy()

    for y in range(heignt):
        for x in range(width):
            result_img[y+pad, x+pad] = np.max(tmp[y:y+k_size, x:x+k_size]) - np.min(tmp[y:y+k_size, x:x+k_size])
    result_img = result_img.astype(np.uint8)
    return result_img


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_FILE_NAME = "kinkaku2.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
img = cv2.imread(FULL_PATH)

img2 = min_max_filter(img)

cv2.imshow("min-max", img2)
cv2.waitKey(0)




