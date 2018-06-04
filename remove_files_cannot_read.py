import os
import shutil
from  PIL import Image
from random import Random
import re
import numpy as np

if __name__ == '__main__':
    c_num = 194829
    count = 0
    data_path = 'D:\\iMaterial_kaggle\\furniture\\unzip\\baidu_images_add'
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
            # try:
            #     img = Image.open(file_path)
            #     img_np = np.asarray(img)
            #     shape = img_np.shape
            #     if len(shape) == 0:
            #         img.close()
            #         print(file_path)
            #         os.remove(file_path)
            # except IOError:
            #     print(file_path + ' cannot read')
            #     os.remove(file_path)
            # img = Image.open(file_path)
            # img_np = np.asarray(img)
            # shape = img_np.shape
            # if len(shape) < 3:
            #     print(file_path + ' dim < 3 and convert')
            #     img_n = img.convert('RGB')
            #     img.close()
            #     # os.remove(file_path)
            #     img_n.save(file_path_0 + '.jpeg')
            # else:
            #     if shape[2] != 3:
            #         img.close()
            #         print(file_path + ' final_dim !=3')
            #         os.remove(file_path)
            # except IOError:
            #     print(file_path + ' cannot read')
            #     os.remove(file_path)