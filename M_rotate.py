# 脚本：数据集扩增操作：旋转
# 作者：黄敏瑜

import cv2 as cv
import os
import numpy as np

filename = "D:/Data"
save_path = "D:/Treat_for_data/rotated_Data2" + '/'
# 计算旋转变换矩阵
def handle_rotate_val(x,y,rotate):
  cos_val = np.cos(np.deg2rad(rotate))
  sin_val = np.sin(np.deg2rad(rotate))
  return np.float32([
      [cos_val, sin_val, x * (1 - cos_val) - y * sin_val],
      [-sin_val, cos_val, x * sin_val + y * (1 - cos_val)]
    ])


def image_rotate(src, rotate=0):
  h,w,c = src.shape
  print(h,w,c)
  M = handle_rotate_val(w//2,h//2,rotate)
  img = cv.warpAffine(src, M, (w,h))
  return img

if __name__ == "__main__":

    list_path = os.listdir(filename)

for index in list_path:
    print(index)
    img = cv.imread(filename +'/' + index)
    for i in range(0,80):                       #旋转80度 每一度生成一张新的数据
        rotate_img = image_rotate(img,i)
        index_new =  str(i) + index 
        path = filename + '/' + index_new
        cv.imwrite(path, rotate_img)
    #if w < 40 or h < 40:

