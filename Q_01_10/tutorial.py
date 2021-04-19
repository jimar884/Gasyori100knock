import cv2
import os

bace_path = os.path.dirname(os.path.abspath(__file__))
img_file_name = "kinkaku.JPG"
full_path = os.path.join(bace_path, img_file_name)
# print(full_path)
img = cv2.imread(full_path)
cv2.imshow("test", img)
cv2.waitKey(0)