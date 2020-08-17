# coding:utf-8
import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    # 相加
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)


def subtract_demo(m1, m2):
    # 相减
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)


def divide_demo(m1, m2):
    # 相除
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)


def multiply_demo(m1, m2):
    # 相乘
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


def others(m1, m2):
    # 判断提取图片是否有效果，方法之一是计算均值，
    # 方差，若无效就会出现[[0.]]
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]
    print(M1)
    print(M2)
    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


def logic_demo(m1, m2):
    # 像素逻辑与或非
    dst = cv.bitwise_and(m1, m2)
    cv.imshow("logic_demo_and", dst)
    dst = cv.bitwise_or(m1, m2)
    cv.imshow("logic_demo_or", dst)
    dst = cv.bitwise_not(m2)
    cv.imshow("logic_demo_not", dst)


def contrast_braghtness_demo(image, c, b):
    h, w, ch = image.shape
    black = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, black, 1-c, b)
    cv.imshow("con-bri-demo", dst)

src1 = cv.imread("opencv-4.4.0/data/LinuxLogo.jpg")
src2 = cv.imread("opencv-4.4.0/data/WindowsLogo.jpg")
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)
contrast_braghtness_demo(src2, 1.2, 100)
# add_demo(src1, src2)
# subtract_demo(src1, src2)
# divide_demo(src1, src2)
# multiply_demo(src1, src2)
# others(src1, src2)
# logic_demo(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()

# 测试功能
# 像素运算
# 代码编写时间 2020.8.14
