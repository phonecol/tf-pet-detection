import os
import RPi.GPIO as GPIO
import time
from img_data import take_img
from tflow import get_data_to_predict, detect_img
from ultrasonic_distance import distance
from serials import ArduinoSerial

if __name__ == '__main__':
    arduino_serial = ArduinoSerial()
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %0.1f cm" %dist)
            time.sleep(0)
                
           
                    
            if dist < 20:
            
                take_img()
                img_detected = detect_img()
            
                if img_detected == "Dog":
                # open door
                #kulang pa sa servo na function
                    print ("Opens the door for 10 sec")
                    arduino_serial.serial_send_data()
                

                     
                # wait 30 secs then close door
                   
                    print ("Close door")
            
            time.sleep(5)
            

    except KeyboardInterrupt:
        print("Program override")
        GPIO.cleanup()

