# user: Jenny
# time: 2021/7/31 10:46
import keras

# load and present the segmentation model
conv_autoencoder = keras.models.load_model("se_seg_hairfollicle.h5")
print(conv_autoencoder.summary())
