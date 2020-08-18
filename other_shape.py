# coding:utf-8
import cv2 as cv
import numpy as np


def top_hat_gray_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # 顶帽为当前，黑帽为TOPHAT改为BLACKHAT
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    cimage = np.array(gray.shape, np.uint8)
    cimage = 100
    dst = cv.add(dst, cimage)
    cv.imshow("tophat", dst)


def hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY |cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("binary_hat", dst)


def gradient_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY |cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("gradient_binary_hat", dst)


def gradient_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dm = cv.dilate(image, kernel)
    em = cv.erode(image, kernel)
    dst1 = cv.subtract(image, em)  # 内部梯度
    dst2 = cv.subtract(dm, image)  # 外部梯度
    cv.imshow("internal_gradient", dst1)
    cv.imshow("external_gradient", dst2)


src = cv.imread("opencv-4.4.0/data/black.png")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
gradient_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

# 测试功能
# 其他形态学操作
# 如：顶帽，黑帽，形态学梯度
# 代码编写时间 2020.8.15
