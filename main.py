import os
import time
from img_data import take_img
from tflow import get_data_to_predict, detect_img


if __name__ == '__main__':
    try:
        while True:
            # take picture
            take_img()

            # detect image
            img_detected = detect_img()
            if img_detected == "Dog":
                # open door
                #kulang pa sa servo na function
                print ("Opens the door for 30 sec")

                time.sleep(30)  
                # wait 30 secs then close door
                print ("Close door")
            
            time.sleep(10)

    except KeyboardInterrupt:
        print("Program override")

