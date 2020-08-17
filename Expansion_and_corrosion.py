# coding:utf-8

import cv2 as cv
import numpy as np


def erode_demo(image):
    #  腐蚀
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.erode(binary, kernel)
    cv.imshow("erode_demo", dst)


def dilate_demo(image):
    #  膨胀
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.dilate(binary, kernel)
    cv.imshow("erode_demo", dst)



# src = cv.imread("opencv-4.4.0/data/num2.jpg")
# cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
# cv.imshow("the first image", src)
# erode_demo(src)
# cv.waitKey(0)
# cv.destroyAllWindows()


src = cv.imread("opencv-4.4.0/data/lena.jpg")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
dst = cv.erode(src, kernel)
cv.imshow("result", dst)
cv.waitKey(0)
cv.destroyAllWindows()

# 测试功能
# 膨胀和腐蚀
# 代码编写时间 2020.8.17
