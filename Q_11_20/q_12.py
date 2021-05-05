"""
Motion Filter
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def motion_filter(img, k_size=3):
    """
    input BGR image, standard deviation and kernel size(k_seze x k_size)
    return BGR image filtered by Motion filter
    """
    heignt, width, channel = img.shape

    pad = k_size // 2
    result_img = np.zeros((heignt+pad*2, width+pad*2, channel), dtype=np.float)
    result_img[pad:pad+heignt, pad:pad+width] = img.copy().astype(np.float)

    tmp = result_img.copy()

    kernel = np.zeros((k_size, k_size))
    for i in range(k_size):
        kernel[i, i] = 1

    for y in range(heignt):
        for x in range(width):
            for c in range(channel):
                result_img[y+pad, x+pad, c] = np.mean(np.dot(tmp[y:y+k_size, x:x+k_size, c], kernel))
    result_img = result_img.astype(np.uint8)
    return result_img


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_FILE_NAME = "kinkaku2.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
img = cv2.imread(FULL_PATH)

img2 = motion_filter(img)

cv2.imshow("motion", img2)
cv2.waitKey(0)




