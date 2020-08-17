# coding:utf-8

import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv.Canny(gray, 30, 150)
    cv.imshow("Canny Edge", edge_output)
    return edge_output


def contous_demo(image):
    # dst = cv.GaussianBlur(image, (9, 9), 0)   # 用于消除噪点
    # gary = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gary, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("binary image", binary)

    binary = edge_demo(image)

    contours, heriachy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, contours, -1, (0, 0, 255), 3)
    cv.imshow("detect contours", image)


src = cv.imread("opencv-4.4.0/data/coins.jpg")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
contous_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
