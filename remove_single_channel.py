import os
import shutil
import PIL.Image as I
from random import Random
import re
import numpy as np

if __name__ == '__main__':
    data_path = 'D:\\iMaterial_kaggle\\furniture\\unzip\\aug'
    for root, dir, files in os.walk(data_path):
        for name in files:
            file_path = os.path.join(root, name)
            file_path_0 = os.path.splitext(file_path)[0]
            file_path_1 = os.path.splitext(file_path)[1]
            # print(file_path)
            try:
                im = I.open(file_path)
                im = np.asarray(im)
                if len(im) < 3:
                    print(file_path)
            except OSError:
                os.remove(file_path)
                pass
            continue