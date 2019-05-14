import serial
import time

BAUD_RATE = 9600
COM_PORT = "/dev/ttyUSB1"



class ArduinoSerial:
    def __init__(self):
        self.serial = serial.Serial(baudrate = BAUD_RATE, port = COM_PORT)
        time.sleep(1)

    def serial_send_data(self):
        print("Sending to serial port command: H")
        self.serial.write(b"H")
        time.sleep(10)
        print("Sending to serial port command: L")
        self.serial.write(b"L")


    def list_serial_ports(self):
        import serial.tools.list_ports
        print(ser.tools.list_ports.comports())

if __name__ == "__main__":
    #list_serial_ports()
    arduino_serial = ArduinoSerial()
    arduino_serial.serial_send_data()
    
    
    