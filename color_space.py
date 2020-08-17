# coding:utf-8
import cv2 as cv
import numpy as np


def extrace_object_demo():
    # 提取视频中的带有颜色的部分（颜色由三通道的范围值决定）
    capture = cv.VideoCapture("C:\\Users\\15098\\Desktop\\video0.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([78, 43, 46])
        upper_hsv = np.array([99, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        # dst = cv.bitwise_and(frame, frame, mask = mask)
        # cv.imshow("mask", dst)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    # 变幻色彩计算方式
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gary", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb", ycrcb)


src = cv.imread("C:\\Users\\15098\\Desktop\\t1.jpg")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
extrace_object_demo()

# 分离三通道
b, g, r = cv.split(src)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

# 融合三通道
src = cv.merge([b, g, r])
# 红色通道置零
src[:, :, 2] = 0
cv.imshow("changed image", src)

cv.waitKey(0)
cv.destroyAllWindows()

# 测试功能
# 色彩空间
# 代码编写时间 2020.8.14

