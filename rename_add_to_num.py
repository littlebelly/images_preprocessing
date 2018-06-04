import os
import shutil
import PIL.Image as I
from random import Random
import re

if __name__ == '__main__':
    c_num = 194829
    count = 0
    data_path = '/Users/zhijie/data/datasets/kaggle_iMaterialist_fashion/aug'
    for root, dir, files in os.walk(data_path):
        for name in files:
            if name == '.DS_Store':
                continue
            file_path = os.path.join(root, name)
            file_path_0 = os.path.splitext(file_path)[0]
            file_path_1 = os.path.splitext(file_path)[1]
            if name[:3] == 'add':
                new_path = str(c_num) + file_path_1
                new_path = os.path.join(root, new_path)
                shutil.move(file_path, new_path)
                c_num += 1
