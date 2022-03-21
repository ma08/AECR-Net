import torch.utils.data as data
import torchvision.transforms as tfs
from torchvision.transforms import functional as FF
import os,sys
sys.path.append('.')
sys.path.append('..')
import numpy as np
import torch
import random
from PIL import Image
from torch.utils.data import DataLoader
from matplotlib import pyplot as plt
from torchvision.utils import make_grid
from metrics import *
from option import opt
import h5py
import glob

BS = opt.bs
print(BS)
crop_size = 'whole_img'
if opt.crop:
    crop_size = opt.crop_size

class RESIDE_Dataset(data.Dataset):
    def __init__(self,path,train,size=crop_size,format='.png'):
        print(f'path={path}')
        super(RESIDE_Dataset,self).__init__()
        self.size = size
        print('------------------- crop size',size)
        self.train=train

        self.h5path = path # 输入h5文件
        print(f"----len {self.__len__()}")
    def __getitem__(self, index):

        file_name = self.h5path + '/' + str(index) + '.h5'
        f = h5py.File(file_name, 'r')
        haze = f['haze']
        clear = f['gt']

        orig_name = haze.attrs['file_name']

        haze = Image.fromarray(np.array(haze))
        clear = Image.fromarray(np.array(clear))
        #print(f'haze={haze}')
        #exit()
        """
        clear = tfs.CenterCrop(haze.size[::-1])(clear)

        if not isinstance(self.size, str):
            i, j, h, w = tfs.RandomCrop.get_params(haze,output_size=(self.size,self.size))
            haze = FF.crop(haze, i, j, h, w)
            clear = FF.crop(clear, i, j, h, w)
        """

        clear = tfs.CenterCrop(haze.size[::-1])(clear)
        haze2, clear2 = self.augData(haze.convert("RGB"), clear.convert("RGB") )

        #haze2 = tfs.ToTensor()(haze.convert("RGB"))
        #clear2 = tfs.ToTensor()(clear.convert("RGB"))
        #print(f'haze={haze.shape}')
        #exit()
        print("------------ GET ITEM-------")
        print(haze2.size())
        print(clear2.size())
        #return haze2, clear2
        return haze2, clear2, orig_name

    def augData(self, data, target):

        if self.train:
            rand_hor = random.randint(0, 1)
            rand_rot = random.randint(0, 3)
            data = tfs.RandomHorizontalFlip(rand_hor)(data)
            target = tfs.RandomHorizontalFlip(rand_hor)(target)
            if rand_rot:
                data = FF.rotate(data, 90*rand_rot)
                target = FF.rotate(target, 90*rand_rot)

        data = tfs.ToTensor()(data)
        #data = tfs.Normalize(mean=[0.64, 0.6, 0.58],std=[0.14,0.15, 0.152])(data)
        target = tfs.ToTensor()(target)
        return data, target

    def __len__(self):
        train_list = glob.glob(self.h5path + '/*h5')
        return len(train_list)

# root = '/home/why/datasets/h5/'
root = opt.root

print(f"------------------        ROOT {root} -----------------------")

NH_train_loader=DataLoader(dataset=RESIDE_Dataset(root+'NH_train/', train=True,size=crop_size),batch_size=BS,shuffle=True)
NH_test_loader=DataLoader(dataset=RESIDE_Dataset(root+'NH_test/',train=False,size='whole img'),batch_size=1,shuffle=False)
# for debug
#ITS_test = '/home/why/workspace/CDNet/net/debug/test_h5/'
#ITS_test_loader_debug=DataLoader(dataset=RESIDE_Dataset(ITS_test,train=False,size='whole img'),batch_size=1,shuffle=False)

if __name__ == "__main__":
    pass
