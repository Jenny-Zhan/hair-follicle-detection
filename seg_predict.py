# user: Jenny
# time: 2021/7/30 22:42
import numpy as np
import os
from tensorflow import keras
from keras_preprocessing import image
from PIL import Image

# load the model
conv_autoencoder = keras.models.load_model("se_seg_hairfollicle.h5")

# indicate the processed test photos and the record file
folder = "result"
list_test = os.listdir(folder)
file_name = f"{folder}.txt"
num = len(list_test)
print(f"processed test photos are：{list_test}")
print(f"the amount of processed photos is：{num}")
with open(file_name, "w") as f:
    f.write(f"processed test photos are：{list_test}"
            f"\nthe amount os processed photo is：{num}")

# import the test photos and convert them into ndarray
test_arr = []
for n in list_test:
    img = image.load_img(f"{folder}/{n}", color_mode="rgb")
    img_arr = image.img_to_array(img)
    test_arr.append(img_arr)
test_arr = np.array(test_arr)
print(test_arr.shape)

# predict, the pixels which are predicted as hair area will be indicated as '1' in pred_arr 
test_arr = test_arr.astype("float16")/255
pred_arr = (conv_autoencoder.predict(test_arr, batch_size=num) > 0.5).astype("int32")

# generate the ndarray of mask image based on pred_arr, the predicted hair area will be red
mask_arr = np.zeros((num, 128, 128, 3))
pred_arr = pred_arr.reshape(num, 128, 128)
mask_arr[:, :, :, 0][pred_arr == 1] = 255

# save the test image, mask image and the final image
# hair area will be delineated as red
for n in range(0, num):
    image.save_img(f"{folder}/image_test{n}.jpg", test_arr[n, :, :, :])
    image.save_img(f"{folder}/image_mask{n}.jpg", mask_arr[n, :, :, :])
    img_final = Image.blend(Image.open(f"{folder}/image_test{n}.jpg"), Image.open(f"{folder}/image_mask{n}.jpg"), 0.4)
    img_final.save(f"{folder}/image_final{n}.jpg")
    # count the red pixel in the mask image
    red_dot = 0
    mask_arr_n = mask_arr[n, :, :, 0].reshape(16384)
    for i in range(16384):
        if mask_arr_n[i] == 255:
            red_dot = red_dot + 1
    print(f"The hair area is {red_dot} pixels")
    print(f"The ratio of hair area is：{red_dot/16384}")
    # save the predicted results in 
    with open(file_name, 'a') as f:
        f.write(f"\n\n image{n}:"
                f"\n The hair area is {red_dot} pixels"
                f"\n The ratio of hair area is：{red_dot/16384}")
