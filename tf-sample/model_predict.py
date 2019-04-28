import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from model_data import DATADIR, CATEGORIES, get_data_to_predict

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
session = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

# EXTERNAL_IMG = "mingming3.jpg"                  # replace this to change the img to predict


def main():
    EXTERNAL_IMG = str(input("Input the name of the img: "))

    # -- get dataset from local 
    data_in = get_data_to_predict("External", EXTERNAL_IMG)

    # -- open the model and run predictions
    model = tf.keras.models.load_model(DATADIR + '/cats_dogs_cnn_64x2.model')
    prediction = model.predict([data_in])
    
    # -- print the results
    print("prediction probabilistic array: %d" %(prediction))
    print(CATEGORIES[int(prediction[0][0])])

if __name__ == "__main__":
    main()


