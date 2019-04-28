import os
import time
import random
import cv2
import pickle
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# -- path constants
CWD = os.getcwd()
DATADIR = CWD + "/data"
MODEL_NAME = "cats_dogs_cnn_64x2.model"
LOG_NAME = "cats-and-dogs-cnn-64x2-%s" %(int(time.time()))
CATEGORIES = ["Cat", "Dog"]
IMG_SIZE = 50

def get_data_to_predict(file_path, file):
    path = os.path.join(DATADIR, file_path)
    path_img = os.path.join(path, file)
    # class_num = CATEGORIES.index(category)
    
    img_array = cv2.imread(path_img, cv2.IMREAD_GRAYSCALE)
                                                # read the imgs through array, converting to grayscale 
                                                # because color doesn't matter, and only takes more size/space
    resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                                                # some images are large, resizing to 50x50
                                                # you may need to see the resized image if it's still recognizable
    reshaped_array = resized_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    return reshaped_array

def detect_img():
    EXTERNAL_IMG = "image.jpg"    #str(input("Input the name of the img: "))

    # -- get dataset from local 
    data_in = get_data_to_predict("External", EXTERNAL_IMG)

    # -- open the model and run predictions
    model = tf.keras.models.load_model(DATADIR + '/cats_dogs_cnn_64x2.model')
    prediction = model.predict([data_in])
    
    # -- print the results
    print("prediction probabilistic array: %d" %(prediction))

    img_detected = CATEGORIES[int(prediction[0][0])]
    print(img_detected)
    return img_detected