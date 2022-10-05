import tensorflow as tf
import matplotlib.pyplot as plt
import os
import glob
import cv2
import numpy as np
import requests
from matplotlib.image import imread
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import tensorflow_model_optimization as tfmot
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation


saved_model=load_model('model.h5')

test_image = image.load_img('img_path'
                            , target_size = (96, 96),color_mode='grayscale')
plt.imshow(test_image)
plt.show()
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result_2 = saved_model.predict(test_image)

print(result_2[0][0]) # 0 means NoGas 1 mean Smoke