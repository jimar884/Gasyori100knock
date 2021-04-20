"""
画像の2値化
"""

import os
import cv2
import numpy as np

def binary_image(img, thread=128):
    """
    2値化した画像を返す
    """
    blue = img[:, :, 0].copy()
    green = img[:, :, 1].copy()
    red = img[:, :, 2].copy()
    result = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    result = result.astype(np.uint8)
    result[result < thread] = 0
    result[result >= thread] = 255

    return result

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_FILE_NAME = "kinkaku2.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
IMG = cv2.imread(FULL_PATH)

IMG2 = binary_image(IMG.copy().astype(np.float))

# cvtColorを使わないと並べて表示できない
IMG3 = cv2.hconcat([IMG, cv2.cvtColor(IMG2, cv2.COLOR_GRAY2BGR)])
cv2.imshow('compare 2 images', IMG3)
cv2.waitKey(0)
