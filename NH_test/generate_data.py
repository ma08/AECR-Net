import enum
from tkinter import image_names
import h5py
import glob
import numpy as np
from PIL import Image


def generate_h5():
    image_list = glob.glob("*jpg")


    for i, image_name in enumerate(image_list):
        img_np = np.array(Image.open(image_name))
        ground_img_np = np.array(Image.open(f"./ground/{image_name}"))
        hf = h5py.File(f"{i}.h5", 'a') # open a hdf5 file
        print(i, image_name)
        dset = hf.create_dataset('haze', data=img_np)  # write the data to hdf5 file
        gset = hf.create_dataset('gt', data=ground_img_np)  # write the data to hdf5 file
        dset.attrs['file_name'] = image_name
        hf.close()  # close the hdf5 file


def open_h5():
    image_list = glob.glob('./*h5')

    for i,image_name in enumerate(image_list):
        f = h5py.File(image_name, 'r')
        haze = f['haze']
        print(haze.attrs['file_name'])
        clear = f['gt']
        haze = Image.fromarray(np.array(haze))
        clear = Image.fromarray(np.array(clear))


        #haze.show()
        #clear.show()

if __name__ == "__main__":
    generate_h5()
    #open_h5()
