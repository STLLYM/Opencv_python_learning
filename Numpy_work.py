# coding:utf-8
import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width: %s, height: %s, channels: %s" %(width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255-pv
    cv.imshow("pixels_demo", image)


def create_image():
    # 注释一，创建一个单一的0阵，然后赋值生成一个图片
    # img = np.zeros([400, 400, 3], np.uint8)
    # img[:, :, 0] = np.ones([400, 400])*255
    # cv.imshow("new image", img)
    # 注释二，直接生成一个1阵，生成一个图片，并保存
    # img = np.ones([400, 400, 1], np.uint8)
    # img = img * 255
    # cv.imshow("new image", img)
    # cv.imwrite("C:\\Users\\15098\\Desktop\\123.png", img)
    m1 = np.ones([3, 3], np.float)
    m1.fill(122.388)
    print(m1)

    m2 = m1.reshape([1, 9])
    print(m2)


def inverse(image):
    # 像素色反转
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo", dst)





src = cv.imread("C:\\Users\\15098\\Desktop\\t1.jpg")   # blue, green, red
cv.namedWindow("the first image", cv.WINDOW_AUTOSIZE)
cv.imshow("the first image", src)
t1 = cv.getTickCount()
# create_image()
inverse(src)
# access_pixels(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency();
print("time : %s ms" % (time*1000))
cv.waitKey(0)


cv.destroyAllWindows()

