"""
Prewitt Filter
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


def prewitt_filter(img, k_size=5, mode='x'):
    """
    input BGR image, standard deviation and kernel size(k_seze x k_size)
    return BGR image filtered by Prewitt filter
    """
    kernels = np.zeros((2, k_size, k_size))
    kernels[0, :, 0], kernels[0, :, k_size-1] = 1, -1
    kernels[1, 0, :], kernels[1, k_size-1, :] = 1, -1
    
    kernel = kernels[0] if mode=='x' else kernels[1]

    result_img = cv2.filter2D(grayscale(img.copy()), -1, kernel)

    result_img = result_img.astype(np.uint8)
    return result_img


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_FILE_NAME = "kinkaku2.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
img = cv2.imread(FULL_PATH)

img2 = prewitt_filter(img, mode='x')
img3 = prewitt_filter(img, mode='y')

cv2.imshow("prewitt", cv2.hconcat([img2, img3]))
cv2.waitKey(0)
