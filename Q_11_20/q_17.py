"""
Laplacian Filter
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


def laplacian_filter(img):
    """
    input BGR image
    return BGR image filtered by Laplacian filter
    """
    kernel = np.array([[0, 1, 0],[1, -4, 1], [0, 1, 0]])

    result_img = cv2.filter2D(grayscale(img.copy()), -1, kernel)

    result_img = result_img.astype(np.uint8)
    return result_img


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_FILE_NAME = "kinkaku2.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
img = cv2.imread(FULL_PATH)

img2 = laplacian_filter(img)

cv2.imshow("sobel", img2)
cv2.waitKey(0)
