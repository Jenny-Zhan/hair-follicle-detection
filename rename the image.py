# user: Jenny
# time: 2021/7/29 13:58
import os

# this program is to add a suffix '_t' to the name of target images

# indicate the directory of target images and show the name of target images
dir_name = "80image_target"
list = os.listdir(dir_name)
print(list)

# add suffix and make sure the number in the name is two digits
for n in range(0, 10):
    os.rename(f"{dir_name}/{list[n]}", f"{dir_name}/0{n}_t.jpg")
for n in range(10, len(list)):
    os.rename(f"{dir_name}/{list[n]}", f"{dir_name}/{n}_t.jpg")

