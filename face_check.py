# coding:utf-8
import cv2 as cv
import numpy as np


def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_dector = cv.CascadeClassifier("opencv-4.4.0/opencv-4.4.0/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces = face_dector.detectMultiScale(gray, 1.02, 5)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("face", image)



# src = cv.imread("opencv-4.4.0/data/topstar.png")
# cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
# cv.namedWindow("face", cv.WINDOW_AUTOSIZE)
# cv.imshow("the first image", src)
# face_detect_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

# 摄像头检测人脸
capture = cv.VideoCapture(0)
while(True):
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    face_detect_demo(frame)
    c = cv.waitKey(10)
    if c == 27:
        break


cv.waitKey(0)

# 测试功能
# 人脸识别
# 代码编写时间 2020.8.18
