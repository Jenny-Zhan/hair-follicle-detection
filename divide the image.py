# user: Jenny
# time: 2021/7/28 16:21

from keras_preprocessing import image

# import the picture: patient1_1.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient1_1.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)

# import the picture: patient1_2.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient1_2.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)

# import the picture: patient1_3.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient1_3.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)

# import the picture: patient1_4.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient1_4.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)

# import the picture: patient2_1.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient2_1.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)

# import the picture: patient2_2.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient2_2.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)

# import the picture: patient2_3.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient2_3.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)

# import the picture: patient3_1.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient3_1.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)

# import the picture: patient3_2.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient3_2.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)

# import the picture: patient3_3.jpg
img = image.load_img("input/patient3_3.jpg", color_mode="grayscale")
img_array = image.img_to_array(img)
print(img_array.shape)
# crop the picture: patient3_3.jpg
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
        image.save_img(f"output/3_3_{num}.jpg", img_array_div)
    a = a+128
print(num)
