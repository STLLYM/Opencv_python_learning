# coding:utf-8

import cv2 as cv
import numpy as np


def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value: %s" % ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    contours, hireachy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        rate = min(w, h)/max(w, h)
        print("ractangle rate is %s" % rate)
        mm = cv.moments(contour)
        # print(type(mm))
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        # cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("contour area is %s" % area)
        approxcurve = cv.approxPolyDP(contour, 4, True)
        print(approxcurve.shape)
        if approxcurve.shape[0] > 6:
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)
        if approxcurve.shape[0] == 4:
            cv.drawContours(dst, contours, i, (0, 255, 255), 2)
        if approxcurve.shape[0] == 3:
            cv.drawContours(dst, contours, i, (255, 0, 255), 2)

    cv.imshow("weasure-contours", dst)


src = cv.imread("opencv-4.4.0/data/detect_blob.png")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
measure_object(src)
cv.waitKey(0)
cv.destroyAllWindows()

# 测试功能
# 对象测量
# 代码编写时间 2020.8.17
