# coding:utf-8

import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)  # flip是方向调换   参数为1是左右调换   参数是-1是上下调换
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


src = cv.imread("C:\\Users\\15098\\Desktop\\t1.jpg")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
get_image_info(src)
video_demo()
cv.waitKey(0)
cv.destroyAllWindows()


# 测试功能
# 图片和视频的加载与保存
# 代码编写时间 2020.8.13
