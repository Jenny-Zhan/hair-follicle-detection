# user: Jenny
# time: 2021/8/8 22:19

import os
import shutil
import glob

# this program is to move croped images in directory 'output' to new directories for train set and test set
# this program can be used in other task involving massive movement of files

# srcdicts is the list of source directory
srcdicts = []
x = ""
while x != "end":
    srcdicts.append(x)
    x = input("Please input the source directory. Input one directory at a time until all directories are input. If you have finished the input, please type 'end'：")
    
# dstdict is the destination directory used to accommodate train set
dstdict = input("please indicate the directory used to accommodate train set：")

# assign variable task to 
task = int(input("Please choose the files you want to move：1.all the files 2.only images. Then type 1 or 2:"))

# define the task
def move_all_file(srcdicts, dstdict):
    '''move all files to the destination directory'''
    if not os.path.isdir(dstdict):
        os.makedirs(dstdict)
    for srcdict in srcdicts:
        if not os.path.isdir(srcdicts):
            print(f"directory {srcdict} does not exist")
        else:
            file_list = os.listdir(srcdict)
            for file in file_list:
                dstfn = dstdict+file
                shutil.move(f"{srcdict}/file", dstfn)

def move_all_img(srcdicts, dstdict):
    '''move all images to the destination directory'''
    if not os.path.isdir(dstdict):
        os.makedirs(dstdict)
    for srcdict in srcdicts:
        if not os.path.isdir(srcdicts):
            print(f"directory {srcdict} does not exist")
        else:
            img_list = glob.glob(f"{srcdict}/*.jpg")
            for img in img_list:
                dstimg = dstdict+img
                shutil.move(f"{srcdict}/img", dstimg)


if task == 1:
    move_all_file(srcdicts, dstdict)
if task == 2:
    move_all_img(srcdicts, dstdict)
else:
    print("please choose your ")
