"""
画像を表示
"""
import os
import cv2

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# 画像の読み取り
IMG_FILE_NAME = "kinkaku.JPG"
FULL_PATH = os.path.join(BASE_PATH, IMG_FILE_NAME)
IMG = cv2.imread(FULL_PATH)

# 画像サイズの取得
HEIGHT = IMG.shape[0]
WIDTH = IMG.shape[1]

# サイズ変更
IMG2 = cv2.resize(IMG, (int(WIDTH*0.2), int(HEIGHT*0.2)))

# 画像の表示
cv2.imshow("test", IMG2)
cv2.waitKey(0)

# ファイル書き出しの確認
cv2.imwrite(os.path.join(BASE_PATH, 'kinkaku2.JPG'), IMG2)
