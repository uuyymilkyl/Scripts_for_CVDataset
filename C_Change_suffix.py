# -*- coding: utf-8 -*-
# �ű��������޸��ļ���׺ 
# ���ߣ������ uuyymilkyl
# �ű�ֱ�Ӹ���ԭ·��,�ǵñ���o

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
        
    