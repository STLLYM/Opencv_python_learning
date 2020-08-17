# coding:utf-8

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def equalHist_demo(image):
    # 全局的直方图均衡化
    gary = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gary)
    cv.imshow("equalHist_demo", dst)


def clahe_demo(image):
    # 局部的直方图均衡化
    gary = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    dst = clahe.apply(gary)
    cv.imshow("equalHist_demo", dst)


def create_rgb_hist(image):
    # 自定义计算
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = (b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist


def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    # 巴式距离
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    # 相关性
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    # 卡方
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴式距离：%s， 相关性：%s， 卡方：%s" % (match1, match2, match3))


src = cv.imread("opencv-4.4.0/data/mask.png")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
equalHist_demo(src)

image1 = cv.imread("opencv-4.4.0/data/graf1.png")
image2 = cv.imread("opencv-4.4.0/data/graf3.png")
hist_compare(image1, image2)

cv.waitKey(0)
cv.destroyAllWindows()
