# 用户: Jenny
# 时间: 2021/7/31 10:46
import keras

conv_autoencoder = keras.models.load_model("se_seg_hairfollicle.h5")
print(conv_autoencoder.summary())
