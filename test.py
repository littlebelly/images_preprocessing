import os
import shutil
import PIL.Image as I
from random import Random
import re
import numpy as np

if __name__ == '__main__':
    test_file = 'D:\\iMaterial_kaggle\\furniture\\unzip\\aug\\73\\249468.jpeg'
    im = I.open(test_file)
    im = np.asarray(im)
    print(im)