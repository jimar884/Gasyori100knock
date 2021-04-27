import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def BGR2HSV(_img):
	img = _img.copy() / 255.

	hsv = np.zeros_like(img, dtype=np.float32)

	# get max and min
	max_v = np.max(img, axis=2).copy()
	min_v = np.min(img, axis=2).copy()
	min_arg = np.argmin(img, axis=2)

	# H
	hsv[..., 0][np.where(max_v == min_v)]= 0
	## if min == B
	ind = np.where(min_arg == 0)
	hsv[..., 0][ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60
	## if min == R
	ind = np.where(min_arg == 2)
	hsv[..., 0][ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
	## if min == G
	ind = np.where(min_arg == 1)
	hsv[..., 0][ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300
		
	# S
	hsv[..., 1] = max_v.copy() - min_v.copy()

	# V
	hsv[..., 2] = max_v.copy()
	
	return hsv


def HSV2BGR(hsv):
	# img = _img.copy() / 255.

	# # get max and min
	# max_v = np.max(img, axis=2).copy()
	# min_v = np.min(img, axis=2).copy()

	out = np.zeros_like(hsv)
	H = hsv[..., 0].copy()
	S = hsv[..., 1].copy()
	V = hsv[..., 2].copy()

	C = S
	H_ = H / 60
	X = C * (1 - np.abs( H_ % 2 - 1))
	Z = np.zeros_like(H)

	vals = [[C,X,Z], [X,C,Z], [Z,C,X], [Z,X,C], [X,Z,C], [C,Z,X]]
    

	for i in range(6):
		ind = np.where((i <= H_) & (H_ < (i+1)))
		out[..., 2][ind] = (V - C)[ind] + vals[i][0][ind]
		out[..., 1][ind] = (V - C)[ind] + vals[i][1][ind]
		out[..., 0][ind] = (V - C)[ind] + vals[i][2][ind]

	# out[np.where(max_v == min_v)] = 0
	# out = np.clip(out, 0, 1)
	# print(out*255)
	out = (out * 255).astype(np.uint8)

	return out

    
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_FILE_NAME = "kinkaku2.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
img = cv2.imread(FULL_PATH)

# hsv image
img2 = BGR2HSV(img)
# rgb imgae (not original)
img3 = HSV2BGR(img2)

# print(img)
# print(img2)
# print(img3)
# show image
cv2.imshow('hsv', img3)
# cv2.imshow('hsv', cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
cv2.waitKey(0)