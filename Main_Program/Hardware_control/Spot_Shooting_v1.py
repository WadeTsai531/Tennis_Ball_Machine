import time
import serial
import keyboard


def transform(data_in):
    if data_in >= 100:
        data_send = str(data_in)
    elif 100 > data_in >= 10:
        data_send = '0' + str(data_in)
    else:
        data_send = '00' + str(data_in)
    return data_send


Serial_BaudRate = 9600
Serial_Port = '/dev/ttyUSB0'

print('Connecting to device ...')
# ser = serial.Serial(Serial_Port, Serial_BaudRate, timeout=3)fsfs
ser = serial.Serial()
ser.baudrate = Serial_BaudRate
ser.port = Serial_Port

ser.open()
print('Connect successful')

ser.write('Right210/'.encode('utf-8'))
time.sleep(1)
ser.write('SRotate/'.encode('utf-8'))
time.sleep(0.5)
ser.write('Left210/'.encode('utf-8'))
time.sleep(1)
ser.write('SRotate/'.encode('utf-8'))

ser.close()
