"""
Discretion of Color
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_FILE_NAME = "kinkaku2.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
img = cv2.imread(FULL_PATH)

kernel = np.zeros((3, 3))
kernel[1, 0] = -1
kernel[1, 1] = 1
img2 = cv2.filter2D(img, -1, kernel)
cv2.imshow('fliter2D', img2)
cv2.waitKey(0)

print(np.dot(kernel, A[1:1+3, 1:1+3]))