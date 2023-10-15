# 用户: Jenny
# 时间: 2021/7/30 22:42
import numpy as np
import os
from tensorflow import keras
from keras_preprocessing import image
from PIL import Image

# 载入模型
conv_autoencoder = keras.models.load_model("se_seg_hairfollicle.h5")

# 获取测试信息：测试文件夹、测试图片的数量（输入文件夹名称）
folder = "result"
list_test = os.listdir(folder)
file_name = f"{folder}.txt"
num = len(list_test)
print(f"待检测的图像为：{list_test}")
print(f"待检测图像数量：{num}")
with open(file_name, "w") as f:
    f.write(f"待检测的图像：{list_test}"
            f"\n待检测图像数量：{num}")

# 导入图片数据并转换为ndarray
test_arr = []
for n in list_test:
    img = image.load_img(f"{folder}/{n}", color_mode="rgb")
    img_arr = image.img_to_array(img)
    test_arr.append(img_arr)
test_arr = np.array(test_arr)
print(test_arr.shape)

# 预测
test_arr = test_arr.astype("float16")/255
pred_arr = (conv_autoencoder.predict(test_arr, batch_size=num) > 0.5).astype("int32")

# 生成mask图像的ndarray
mask_arr = np.zeros((num, 128, 128, 3))
pred_arr = pred_arr.reshape(num, 128, 128)
mask_arr[:, :, :, 0][pred_arr == 1] = 255
# 保存原始图像、mask图像、最终图像
for n in range(0, num):
    image.save_img(f"{folder}/image_test{n}.jpg", test_arr[n, :, :, :])
    image.save_img(f"{folder}/image_mask{n}.jpg", mask_arr[n, :, :, :])
    img_final = Image.blend(Image.open(f"{folder}/image_test{n}.jpg"), Image.open(f"{folder}/image_mask{n}.jpg"), 0.4)
    img_final.save(f"{folder}/image_final{n}.jpg")
    # 计数：mask图像中红色像素
    red_dot = 0
    mask_arr_n = mask_arr[n, :, :, 0].reshape(16384)
    for i in range(16384):
        if mask_arr_n[i] == 255:
            red_dot = red_dot + 1
    print(f"图像中毛发区域的面积为{red_dot}像素")
    print(f"毛发在图像中的面积比例为：{red_dot/16384}")
    # 保存信息
    with open(file_name, 'a') as f:
        f.write(f"\n\n图像{n}:"
                f"\n图像中毛发区域的面积为{red_dot}像素"
                f"\n毛发在图像中的面积比例为：{red_dot/16384}")
