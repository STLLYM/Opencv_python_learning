# coding:utf-8

import cv2 as cv
import numpy as np


def lapalian_demo(image):
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])  # 定义卷积核
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lpls", lpls)


def sobel_demo(image):
    # soble算子效果较弱， scharr会强一些
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient_x", gradx)
    cv.imshow("gradient_y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)


src = cv.imread("C:\\Users\\15098\\Desktop\\t1.jpg")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
