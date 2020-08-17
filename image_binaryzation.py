# coding:utf-8

import cv2 as cv
import numpy as np


def threshold_demo(image):
    # 全局阈值
    gary = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # OTSU和TRIANGLE是计算阈值（加|的参数）
    # BINARY是阈值法二值化图象, +_INV是黑白反转,
    # TRUNC是大于127的全部处理, TOZERO是小于127的全部处理
    ret, binary = cv.threshold(gary, 127, 255, cv.THRESH_BINARY )
    print("threshold value %s" % ret)
    cv.imshow("binary", binary)


def local_threshold_demo(image):
    # 局部阈值
    gary = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gary, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("binary", binary)


def custom_threshold(image):
    # 均值阈值  未调成功
    gary = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gary.shape[:2]
    m = np.reshape(gary, [1, w+h])
    mean = m.sum()/(m*h)
    print("mean : ", mean)
    ret, binary = cv.threshold(gary, mean, 255, cv.THRESH_BINARY)
    cv.imshow("binary", binary)


src = cv.imread("data/sudoku.png")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
custom_threshold(src)
cv.waitKey(0)

cv.destroyAllWindows()
