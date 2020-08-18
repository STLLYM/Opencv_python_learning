# coding:utf-8
import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess


def recognize_text():
    gray= cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 3))
    bin2 = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow("binary", bin2)

    cv.bitwise_not(bin2, bin2)
    textimage = Image.fromarray(bin2)
    text = tess.image_to_string(textimage)
    print("识别结果：" % text)


src = cv.imread("opencv-4.4.0/data/yanzhengma4.png")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
recognize_text()

cv.waitKey(0)
cv.destroyAllWindows()

# 测试功能
# 由于谷歌OCR引擎没有安装故没有调试成功
# 验证码识别
# 代码编写时间 2020.8.18
