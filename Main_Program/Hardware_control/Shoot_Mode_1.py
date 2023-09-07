import time
import random
import keyboard
import serial

Serial_BaudRate = 9600
Serial_Port = '/dev/ttyUSB0'

print('Connecting to device ...')
ser = serial.Serial()
ser.baudrate = Serial_BaudRate
ser.port = Serial_Port
ser.open()
print('Connect successful')

while True:
    key = keyboard.read_key()
    if key == 'q':
        break
    elif key == 's':
        ser.write('Right210/'.encode('utf-8'))
        time.sleep(1)
        ser.write('SRotate/'.encode('utf-8'))
    elif key == 'r':
        for i in range(200, 500):
            data = 'Scroll' + str(i) + '/'
            ser.write(data.encode('utf-8'))
            time.sleep(0.5)
    elif key == 'd':
        ser.write('Shot/'.encode('utf-8'))
