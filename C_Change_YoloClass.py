# 脚本：批量修改文件后缀 
# 作者：黄敏瑜 uuyymilkyl
# 脚本直接覆盖原路径,记得备份o

import os
import cv2
from PIL import Image
import re

filename = "D:/darknet-master/build/darknet/x64/DataSet/Armor/obj/"
list_path = os.listdir(filename)

for index in list_path:
    name = index.split('.')[0]
    #name = re.split('[.png,.jpeg,')
    #print(name)
    #name1 = '5_11'
    suffix = 'jpg'
    #print(suffix)
    path = filename + '/' +index
    new_path = filename +  '/' + name  +'.'+ suffix
    print(new_path)
    
    os.rename(path, new_path)
        
    