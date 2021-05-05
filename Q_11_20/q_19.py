"""
LoG Filter
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


def log_filter(img, k_size=5, sigma=3):
    """
    input BGR image, kernel size, standard deviation
    return BGR image filtered by LoG filter
    """
    kernel = np.zeros((k_size, k_size))
    x_pad = y_pad = k_size // 2
    for x in range(-x_pad, k_size-x_pad):
        for y in range(-y_pad, k_size-y_pad):
            kernel[x+x_pad, y+y_pad] = (x**2 + y**2 - 2*(sigma**2)) * np.exp(-(x**2 + y**2) / (2*(sigma**2)))
    kernel /= 2 * np.pi * (sigma**6)
    kernel /= kernel.sum()

    result_img = cv2.filter2D(img.copy(), -1, kernel)

    result_img = result_img.astype(np.uint8)
    return result_img


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_FILE_NAME = "kinkaku2.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
img = cv2.imread(FULL_PATH)

img2 = log_filter(img)

cv2.imshow("log", img2)
cv2.waitKey(0)
