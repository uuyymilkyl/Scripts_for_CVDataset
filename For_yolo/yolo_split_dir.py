# 脚本：将Yolo txt 数据集按划分文件直接复制进darknet工程下
# 作者：到处搜刮而来

import os
import shutil
from tqdm import tqdm
 
SPLIT_PATH = r"D:/Treat_for_data/Data/Yolov7_main"      # main set路径
IMGS_PATH = r"D:/Treat_for_data/Data/Image3"            # 图像路径
TXTS_PATH = r"D:/Treat_for_data/Data/labels"            # txt标签文件路径
 
TO_IMGS_PATH = r'D:/yolov7-main/data/barcode_dataset/images'    #yolo darknert 工程下的数据集 图像路径
TO_TXTS_PATH =r'D:/yolov7-main/data/barcode_dataset/labels'     #yolo darknert 工程下的数据集 标签路径
 
data_split = ['trainval.txt', 'val.txt','test.txt']
to_split = ['trainval', 'val','test']
 
for index, split in enumerate(data_split):
    split_path = os.path.join(SPLIT_PATH, split)
 
    to_imgs_path = os.path.join(TO_IMGS_PATH, to_split[index])
    if not os.path.exists(to_imgs_path):
        os.makedirs(to_imgs_path)
 
    to_txts_path = os.path.join(TO_TXTS_PATH, to_split[index])
    if not os.path.exists(to_txts_path):
        os.makedirs(to_txts_path)
 
    f = open(split_path, 'r')
    count = 1
 
    for line in tqdm(f.readlines(), desc="{} is copying".format(to_split[index])):
        #
        src_img_path = os.path.join(IMGS_PATH, line.strip() + '.jpg')
        dst_img_path = os.path.join(to_imgs_path, line.strip() + '.jpg')
        if os.path.exists(src_img_path):
            shutil.copyfile(src_img_path, dst_img_path)
        else:
            print("error file: {}".format(src_img_path))
 
        # 
        src_txt_path = os.path.join(TXTS_PATH, line.strip() + '.txt')
        dst_txt_path = os.path.join(to_txts_path, line.strip() + '.txt')
        if os.path.exists(src_txt_path):
            shutil.copyfile(src_txt_path, dst_txt_path)
        else:
            print("error file: {}".format(src_txt_path))

