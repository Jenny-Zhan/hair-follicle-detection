# user: Jenny
# time: 2021/7/29 14:39
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
from keras_preprocessing import image

# This is the construction and training of the Auto-encoder model for detecting and calculating hair area. 
# The training dataset is in the directory '80image' (sample) and '80image_target' (target). 
# The validation dataset is in the directory '20image' (sample) and '20image_target' (target). 

# import sample images, convert to ndarray
img_80_arr = []
list_80 = os.listdir("dataset/80image")
print(list_80)
for n in list_80:
    img = image.load_img(f"dataset/80image/{n}", color_mode="rgb")
    img_arr = image.img_to_array(img)
    img_80_arr.append(img_arr)
print(len(img_80_arr))
img_80_arr = np.array(img_80_arr)
print(img_80_arr.shape)

img_20_arr = []
list_20 = os.listdir("dataset/20image")
print(list_20)
for n in list_20:
    img = image.load_img(f"dataset/20image/{n}", color_mode="rgb")
    img_arr = image.img_to_array(img)
    img_20_arr.append(img_arr)
print(len(img_20_arr))
img_20_arr = np.array(img_20_arr)
print(img_20_arr.shape)

# import target images, convert to ndarray
tar_80_arr = []
list_80 = os.listdir("dataset/80image_target")
print(list_80)
for n in list_80:
    img = image.load_img(f"dataset/80image_target/{n}", color_mode="rgb")
    img_arr = image.img_to_array(img)
    tar_80_arr.append(img_arr)
print(len(tar_80_arr))
tar_80_arr = np.array(tar_80_arr)
print(tar_80_arr.shape)

tar_20_arr = []
list_20 = os.listdir("dataset/20image_target")
print(list_20)
for n in list_20:
    img = image.load_img(f"dataset/20image_target/{n}", color_mode="rgb")
    img_arr = image.img_to_array(img)
    tar_20_arr.append(img_arr)
print(len(tar_20_arr))
tar_20_arr = np.array(tar_20_arr)
print(tar_20_arr.shape)


# designate sample training data
x_train = img_80_arr.astype("float16")/255
x_valid = img_20_arr.astype("float16")/255
# in the target images, set white pixel as 0, other pixel as 1
y_train = tar_80_arr.copy()
y_valid = tar_20_arr.copy()
y_train[tar_80_arr != [255, 255, 255]] = 1
y_train[tar_80_arr == [255, 255, 255]] = 0
y_valid[tar_20_arr != [255, 255, 255]] = 1
y_valid[tar_20_arr == [255, 255, 255]] = 0
y_train = y_train[:, :, :, :1]
y_valid = y_valid[:, :, :, :1]


# set GPU as conputing device
physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

# construct autoencoder
conv_encoder = keras.models.Sequential([
    keras.layers.InputLayer(input_shape=[128, 128, 3]),
    keras.layers.Conv2D(4, kernel_size=3, padding="same", activation="selu"),
    keras.layers.Conv2D(8, kernel_size=3, padding="same", activation="selu"),
    keras.layers.MaxPool2D(pool_size=2),
    keras.layers.Conv2D(16, kernel_size=3, padding="same", activation="selu"),
    keras.layers.MaxPool2D(pool_size=2),
    keras.layers.Conv2D(16, kernel_size=3, padding="same", activation="selu"),
    keras.layers.MaxPool2D(pool_size=2),
    keras.layers.Flatten()])
print(conv_encoder.summary())

conv_decoder = keras.models.Sequential([
    keras.layers.Reshape([16, 16, 16], input_shape=[4096]),
    keras.layers.Conv2DTranspose(16, kernel_size=3, strides=2, padding="same", activation="selu"),
    keras.layers.Conv2DTranspose(16, kernel_size=3, strides=2, padding="same", activation="selu"),
    keras.layers.Conv2DTranspose(8, kernel_size=3, strides=2, padding="same", activation="selu"),
    keras.layers.Conv2DTranspose(4, kernel_size=3, padding="same", activation="selu"),
    keras.layers.Conv2DTranspose(3, kernel_size=3, padding="same", activation="selu"),
    keras.layers.Conv2DTranspose(1, kernel_size=3, padding="same", activation="sigmoid")])
print(conv_decoder.summary())

conv_autoencoder = keras.models.Sequential([conv_encoder, conv_decoder])
conv_autoencoder.compile(loss="binary_crossentropy", metrics="acc",
                         optimizer=keras.optimizers.Adam(learning_rate=5e-4,))


# train
conv_autoencoder.fit(x_train, y_train, epochs=200, batch_size=5,
                     validation_data=(x_valid, y_valid), validation_batch_size=5)
print(conv_autoencoder.summary())


# save the model
conv_autoencoder.save("se_seg_hairfollicle.h5")
