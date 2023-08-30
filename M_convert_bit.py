# -*- coding: utf-8 -*-

from PIL import Image
import os

def convert_to_bmp(image_path):
    # 打开图像
    img = Image.open(image_path)

    # 将图像转换为bmp格式
    if img.mode != 'RGB':
        img = img.convert('RGB')

    new_image_path = os.path.splitext(image_path)[0] + ".bmp"
    img.save(new_image_path, format='BMP')

    #print(f"已将 {image_path} 转换为 {new_image_path}")

# 图像文件夹路径
image_folder = "E:/database/"

# 获取文件夹中的所有图像文件
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# 遍历图像文件列表
for image_file in image_files:
    # 仅处理jpg、png和bmp格式的图像
    if image_file.lower().endswith(('.jpg', '.png', '.bmp')):
        image_path = os.path.join(image_folder, image_file)
        convert_to_bmp(image_path)
