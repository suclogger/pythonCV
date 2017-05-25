# -*- coding: utf-8 -*-

import cv2

#两个回调函数
def thresholdType(threshold_type):
    global THRESHOLD_TYPE
    THRESHOLD_TYPE = threshold_type
    print THRESHOLD_TYPE, THRESHOLD_VALUE
    ret, dst = cv2.threshold(scr, THRESHOLD_VALUE, max_value, THRESHOLD_TYPE)
    cv2.imshow(window_name,dst)

def thresholdValue(threshold_value):
    global THRESHOLD_VALUE
    THRESHOLD_VALUE = threshold_value
    print THRESHOLD_TYPE, THRESHOLD_VALUE
    ret, dst = cv2.threshold(scr, THRESHOLD_VALUE, max_value, THRESHOLD_TYPE)
    cv2.imshow(window_name,dst)

#全局变量
"""
"Type: 
0: Binary 
1: Binary Inverted 
2: Truncate 
3: To Zero 
4: To Zero Inverted"
"""
THRESHOLD_VALUE = 0
THRESHOLD_TYPE = 3
max_value = 255
max_type = 4
max_BINARY_value = 255
window_name = "Threshold Demo"
trackbar_type = "Type"
trackbar_value = "Value"

#读入图片，模式为灰度图，创建窗口
scr = cv2.imread("nameplate.jpg",0)
cv2.namedWindow(window_name)

#创建滑动条
cv2.createTrackbar( trackbar_type, window_name, \
                    THRESHOLD_TYPE, max_type, thresholdType)
cv2.createTrackbar( trackbar_value, window_name, \
                    THRESHOLD_VALUE, max_value, thresholdValue )
#初始化
thresholdType(0)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()