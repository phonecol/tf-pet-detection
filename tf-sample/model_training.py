import os
import time
import pickle

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard

from model_data import DATADIR, MODEL_NAME, LOG_NAME, get_training_data


MODEL_NAME = "cats_dogs_cnn_64x2.model"
LOG_NAME = "cats-and-dogs-cnn-64x2-%s" %(int(time.time()))
tensor_board = TensorBoard(log_dir='%s/logs/%s' %(DATADIR, LOG_NAME))


def main():
    # -- get input and output data
    X, y = get_training_data()

    # -- define your convolutional NN model
    model = Sequential()                        # initialize sequential layer
    model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
                                                # start with a Conv2D layer, with size 3x3
    model.add(Activation("relu"))               # use relu activation again
    model.add(MaxPooling2D(pool_size=(2, 2)))   # we usually pair MaxPooling2D with the Conv2D

    model.add(Conv2D(64, (3, 3)))               # another Conv2D layer
    model.add(Activation("relu"))               # activate with relu
    model.add(MaxPooling2D(pool_size=(2, 2)))   # again with the MaxPooling2D pair for the Conv2D

    model.add(Flatten())                        # add last dense layer for good measure
    model.add(Dense(64))                        # but needs to flatten the 2D layer generated by Conv2D and MaxPooling2D
    model.add(Activation("relu"))               # activate with relu

    model.add(Dense(1))                         # output layer
    model.add(Activation('sigmoid'))            

    # -- compile the model
    model.compile(loss="binary_crossentropy",
                  optimizer="adam",
                  metrics=["accuracy"])
    model.fit(X, y, 
              batch_size=32,                    # batch size is how many at a time do we wanna pass
              epochs=10,                        # specify how many epochs
              validation_split=0.1,             # 20 - 100 is generally ok    
              callbacks=[tensor_board])         # add tensor_board as callback

    # -- log to tensorboard then save the model
    model.save(os.path.join(DATADIR, MODEL_NAME))
                                          

if __name__ == "__main__":
    main()