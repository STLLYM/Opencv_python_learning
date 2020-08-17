# coding:utf-8

import cv2 as cv
import numpy as np


def template_demo():
    #  图像匹配
    sample = cv.imread("opencv-4.4.0/data/mes.jpg")
    target = cv.imread("opencv-4.4.0/data/messi5.jpg")

    cv.imshow("sample", sample)
    cv.imshow("target", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = sample.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, sample, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md==cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        # cv.imshow("match"+np.str(md), target)
        cv.imshow("match" + np.str(md), result)


template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
