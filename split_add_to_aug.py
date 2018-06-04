import os
import shutil
import PIL.Image as I
from random import Random
import re

if __name__ == '__main__':
    data_path = 'D:\\iMaterial_kaggle\\furniture\\unzip\\baidu_images'
    split_path = 'D:\\iMaterial_kaggle\\furniture\\unzip\\baidu_images_add'
    for root, dir, files in os.walk(data_path):
        for name in files:
            if name == '.DS_Store':
                continue
            if name[:3] == 'add':
                file_path = os.path.join(root, name)
                num = re.findall(r"\d+", file_path) 
                num = num[0]
                new_file_path = os.path.join(split_path, str(num), name)
                print(file_path + ' -> ' + new_file_path)
                shutil.move(file_path, new_file_path)