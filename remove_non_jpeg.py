import os
import shutil
import PIL.Image as I
from random import Random
import re

if __name__ == '__main__':
    data_path = 'D:\\iMaterial_kaggle\\furniture\\unzip\\aug'
    for root, dir, files in os.walk(data_path):
        for name in files:
            if name == '.DS_Store':
                continue
            file_path = os.path.join(root, name)
            file_path_0 = os.path.splitext(file_path)[0]
            file_path_1 = os.path.splitext(file_path)[1]
            if file_path_1 != '.jpeg':
                print(file_path)
                os.remove(file_path)
