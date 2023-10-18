# 用户: Jenny
# 时间: 2021/8/8 22:19

import os
import shutil
import glob

# 可根据需要将所有文件或图片文件移到目标文件夹
# 被移动的文件夹和目标文件夹、任务类型
srcdicts = []
x = ""
while x != "end":
    srcdicts.append(x)
    x = input("请输入待处理文件夹（若无请输入end)：")

dstdict = input("请输入目标文件夹：")
task = int(input("请选择任务类型：1.移动所有文件 2.移动jpg图像"))


def move_all_file(srcdicts, dstdict):
    '''移动所有文件至目标文件夹'''
    if not os.path.isdir(dstdict):
        os.makedirs(dstdict)
    for srcdict in srcdicts:
        if not os.path.isdir(srcdicts):
            print(f"文件夹{srcdict}不存在")
        else:
            file_list = os.listdir(srcdict)
            for file in file_list:
                dstfn = dstdict+file
                shutil.move(f"{srcdict}/file", dstfn)


def move_all_img(srcdicts, dstdict):
    '''移动所有图片至目标文件夹'''
    if not os.path.isdir(dstdict):
        os.makedirs(dstdict)
    for srcdict in srcdicts:
        if not os.path.isdir(srcdicts):
            print(f"文件夹{srcdict}不存在")
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
    print("请重新输入任务")
