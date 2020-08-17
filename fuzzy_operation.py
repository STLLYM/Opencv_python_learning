# coding:utf-8

import cv2 as cv
import numpy as np


def blur_demo(image):
    # 均值模糊，常用功能，去噪
    dst = cv.blur(image, (5, 5))
    cv.imshow("blur_demo", dst)


def median_blur_demo(image):
    # 中值模糊，常用功能，去椒盐噪声
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo", dst)


def custom_blur_demo(image):
    # 自定义模式
    # kernel = np.ones([5, 5], np.float32)/25  # 自定义版本均值模糊
    # dst = cv.filter2D(image, -1, kernel=kernel)

    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 自定义版本的锐化
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("custom_blur_demo", dst)


src = cv.imread("C:\\Users\\15098\\Desktop\\t1.jpg")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
# blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
