# coding:utf-8
import cv2 as cv
import numpy as np


def fill_color_demo(image):
    # 彩色图像的填充
    copyimg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    # 填充，从（30， 30）出发，到下值30-100， 和上值30+50
    cv.floodFill(copyimg, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyimg)


def fill_binary():
    # 二值图象的填充
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("fill_binary", image)

    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (50, 2, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary", image)


src = cv.imread("C:\\Users\\15098\\Desktop\\t1.jpg")
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
print(src.shape)

# fill_color_demo(src)

# ROI操作指的是Region of Interest
# car_card = src[350:450, 250:500]
# gray = cv.cvtColor(car_card, cv.COLOR_BGR2GRAY)
# backcard = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
# src[350:450, 250:500] = backcard
# cv.imshow("car_card", src)

fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()

# 测试功能
# ROI与泛洪填充
# 代码编写时间 2020.8.14
