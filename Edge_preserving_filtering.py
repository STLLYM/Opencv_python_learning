# coding:utf-8

import cv2 as cv
import numpy as np


def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)


def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)


src = cv.imread("opencv-4.4.0/data/lena.jpg")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
bi_demo(src)
# shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

# 测试功能
# 边缘保留滤波（EPF）
# 代码编写时间 2020.8.15

