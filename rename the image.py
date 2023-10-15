# 用户: Jenny
# 时间: 2021/7/29 13:58
import os

dir_name = "80image_target"
list = os.listdir(dir_name)
print(list)

# 请检查文件夹中文件命名数字位数是否相同
for n in range(0, 10):
    os.rename(f"{dir_name}/{list[n]}", f"{dir_name}/0{n}_t.jpg")
for n in range(10, len(list)):
    os.rename(f"{dir_name}/{list[n]}", f"{dir_name}/{n}_t.jpg")

