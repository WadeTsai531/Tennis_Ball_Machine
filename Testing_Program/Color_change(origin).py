from tkinter.tix import IMAGE
import cv2
import numpy as np
from PIL import Image
import re

#设定顏色的阈值最小值和最大值
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

img = cv2.imread('D:/train_20220914/001o.jpg')       #輸入圖片
img1 = cv2.imread('D:/train_20220914/red.jpg')
img1 = cv2.resize(img1, (190, 305), interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)  #通过幕布的形式将图片变为二进制模式，蓝色区域为白色，不是蓝色的区域为黑色，这样获取到了图片中的蓝色区域

r = cv2.bitwise_and(img1, img,mask=blue_mask)       #将白色部分用紅色填充
cv2.imwrite('D:/train_20220914/001_black.jpg',r)

img2 = cv2.imread('D:/train_20220914/001_black.jpg')
color_dist = {
    'black': {
    'Lower': np.array([0, 0, 0]), 'Upper': np.array([254, 150, 150])}}
hsv = cv2.cvtColor(img2, cv2.COLOR_RGB2HSV)
background_mask = cv2.inRange(hsv, color_dist['black']['Lower'], color_dist['black']['Upper'])

person_mask = ~background_mask
scenic_img = cv2.bitwise_and(img, img, mask = background_mask)
person_img = cv2.bitwise_and(img, img2, mask = person_mask)
alpha_img = cv2.addWeighted(scenic_img, 1, person_img,1,0)

cv2.imshow('2',alpha_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#https://www.cxyzjd.com/article/qq_45779334/108095410
#https://steam.oxxostudio.tw/category/python/ai/opencv-mask.html
#https://codeantenna.com/a/4Co1rfxzWi