# 用户: Jenny
# 时间: 2022/5/2 16:04

from keras_preprocessing import image

# 从PUT PHOTO HERE导入图片
img = image.load_img("PUT PHOTO HERE/patient.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# 裁剪图片patient1_1.jpg
height = img_array.shape[0]
width = img_array.shape[1]
a = 0
num = 0
while a <= height-128:
    b = 0
    while b <= width-128:
        img_array_div = img_array[a:a+128, b:b+128, :]
        b = b+128
        num = num+1
        image.save_img(f"result/test_{num}.jpg", img_array_div)
    a = a+128
print(num)
