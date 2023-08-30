# -*- coding: utf-8 -*-

from PIL import Image
import os

def convert_to_bmp(image_path):
    # ��ͼ��
    img = Image.open(image_path)

    # ��ͼ��ת��Ϊbmp��ʽ
    if img.mode != 'RGB':
        img = img.convert('RGB')

    new_image_path = os.path.splitext(image_path)[0] + ".bmp"
    img.save(new_image_path, format='BMP')

    #print(f"�ѽ� {image_path} ת��Ϊ {new_image_path}")

# ͼ���ļ���·��
image_folder = "E:/database/"

# ��ȡ�ļ����е�����ͼ���ļ�
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# ����ͼ���ļ��б�
for image_file in image_files:
    # ������jpg��png��bmp��ʽ��ͼ��
    if image_file.lower().endswith(('.jpg', '.png', '.bmp')):
        image_path = os.path.join(image_folder, image_file)
        convert_to_bmp(image_path)
