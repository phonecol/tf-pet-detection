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


def create_training_data():
    training_data = []
    for category in CATEGORIES:                 # loop through the categories
        path = os.path.join(DATADIR, category)  # join DATADIR + category file path
        imgs = os.listdir(path)
        class_num = CATEGORIES.index(category)  # convert category to number, so use the index on the list instead
        for img in imgs:                        # loop through the images on the path
            img_path = os.path.join(path, img)
            try:
                img_array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                                                # read the imgs through array, converting to grayscale
                                                # because color doesn't matter, and only takes more size/space
                resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                                                # some images are large, resizing to 50x50
                                                # you may need to see the resized image if it's still recognizable
                training_data.append([resized_array, class_num])
                                                # append the array to training_data
            except Exception as e:
                print("Error at %s: %s " %(img_path, str(e)))
    random.shuffle(training_data)               # shuffle data so that NN won't be biased
    print("training data: ")
    print(training_data)
    return training_data


def save_training_data(X, y):
    pickle_out = open(DATADIR + "/X.pickle", "wb")         # use pickle to save X to X.pickle
    pickle.dump(X, pickle_out)
    pickle_out.close()

    pickle_out = open(DATADIR + "/y.pickle", "wb")         # use pickle to save y to y.pickle
    pickle.dump(y, pickle_out)
    pickle_out.close()


def get_training_data():
    X = pickle.load(open(DATADIR + "/X.pickle", "rb"))     # get input data X through pickle
    y = pickle.load(open(DATADIR + "/y.pickle", "rb"))     # get output data y through pickle
    X = X / 255.0                                          # normalize data, simpler way to normalize pictures

    return X, y


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

def prepare(filepath):
    IMG_SIZE = 70  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


def main():
    X = []
    y = []

    training_data = create_training_data()      # get training data from function

    for features, label in training_data:       # loop through training data and append features and label
        X.append(features)
        y.append(label)

    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)  # reshape array (necessary for keras)
    save_training_data(X, y)                    # save training data


if __name__ == '__main__':
    main()

