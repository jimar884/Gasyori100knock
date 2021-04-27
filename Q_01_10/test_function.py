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

a = np.arange(12)
print(a[3:6])
print(np.mean(a[3:6]))
