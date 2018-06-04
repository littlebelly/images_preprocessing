import os
import glob
import numpy as np

if __name__ == '__main__':
    ckpt_list = glob.glob(os.path.join('./', '*.meta'))
    ckpt_num_list = []
    for ckpt in ckpt_list:
        ckpt = ckpt[13:-5]
        ckpt = int(ckpt)
        ckpt_num_list.append(ckpt)
    ckpt_num_list.sort()
    for i in range(50):
        ckpt_num = ckpt_num_list[i]
        for _add in ['data-00000-of-00001', 'index', 'meta']:
            file_name = 'model.ckpt-' + str(ckpt_num) + '.' + _add
            os.remove(file_name)
            print(file_name)
