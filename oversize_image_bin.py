# coding:utf-8

import cv2 as cv
import numpy as np


def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gary = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gary[row:row+ch, col:cw+col]
            dev = np.std(roi)
            if dev < 15:
                gary[row:row + ch, col:cw + col] = 255
            else:
                ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                gary[row:row + ch, col:cw + col] = dst

            print(np.std(dst), np.mean(dst))
    cv.imwrite("result_binary.png", gary)
 

src = cv.imread("opencv-4.4.0/data/test123.png")
# cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
# cv.imshow("the first image", src)
big_image_binary(src)
cv.waitKey(0)
cv.destroyAllWindows()


# 测试功能
# 超大图像二值化
# 代码编写时间 2020.8.15
