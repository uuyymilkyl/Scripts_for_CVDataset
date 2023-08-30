import os
import cv2
from PIL import Image


filename = "D:/Treat_for_data/Data/Data_forGAN"
list_path = os.listdir(filename)

save_path = "D:/Treat_for_data/GANed_Data" + '/'
for index in list_path:
    print(index)
    img = cv2.imread(filename +'/' + index,0)

    #print(type(img))
    change_img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    path = filename + '/' + index
    cv2.imwrite(path, change_img)
    #if w < 40 or h < 40:
    #    new_path = save_path + '/' + index
    #    print(new_path)
    #    os.rename(path,new_path)
        
    #else:
    #    new_path1 = save_path + '/' + index
    #    print(new_path1)
    #    os.rename(path, new_path1)
        