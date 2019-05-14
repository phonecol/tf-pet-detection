#libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD /BCM)

GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 4
GPIO_ECHO = 17

#set GPIO direction (IN/ OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    #set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)

    StartTime = time.time()
    StopTime = time.time()
    print(StartTime)
    startTimeCount = 0
    #Save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        print("StartTime: ",StartTime)
        
        startTimeCount += 1
        if startTimeCount == 10:
            startTimeCount = 0
            break

    #Save time of arrival
    while GPIO.input(GPIO_ECHO)==1:
        StopTime = time.time()
        #print("StopTime: ", StopTime)

    #time difference between start and arrival
    TimeElapsed = StopTime - StartTime

    #multiply with sonic speed (34300cm/s)
    #divide by 2, because there and back
    distance = (TimeElapsed*34300)/2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %0.1f cm" %dist)
            time.sleep(1)
            

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

