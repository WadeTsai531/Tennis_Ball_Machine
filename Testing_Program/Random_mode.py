import serial
import time
import keyboard
import random

Serial_BaudRate = 9600
Serial_Port = 'COM5'

print('Connecting to device ...')
ser = serial.Serial()
ser.baudrate = Serial_BaudRate
ser.port = Serial_Port

ser.open()
print('Connect successful')
ser.write('S/'.encode('utf-8'))


def transform(data_in):
    if data_in >= 100:
        data_send = str(data_in)
    elif 100 > data_in >= 10:
        data_send = '0' + str(data_in)
    else:
        data_send = '00' + str(data_in)
    return data_send


def turn():
    dir_n = random.randint(0, 1)
    tm = random.random()
    if tm < 0.1:
        tm *= 10
    tm = round(tm, 2) + 1
    if dir_n:
        dir_m = 'R'
    else:
        dir_m = 'L'
    print(dir_m, tm)
    return tm


def shoot():
    ser.write('Shot/'.encode('utf-8'))
    time.sleep(0.5)
    ser.write('ShSot/'.encode('utf-8'))
    time.sleep(0.01)
    ser.write('/'.encode('utf-8'))


keyboard.wait('s')
print('Send SRotate/')
ser.write('SRotate/'.encode('utf-8'))
time.sleep(0.005)
while True:
    print('Send Right/')
    ser.write('Right350/'.encode('utf-8'))
    data = 0
    while data != b'S':
        data = ser.read()
        print('Receive', data)
    print('Stop')
    ser.write('SRotate/'.encode('utf-8'))
    time.sleep(1)
    # shoot()
    time.sleep(1)
    print('Send Left/')
    ser.write('Left350/'.encode('utf-8'))
    time.sleep(2)
    print('Stop')
    ser.write('SRotate/'.encode('utf-8'))
    time.sleep(1)
    # shoot()
    time.sleep(1)
    print('Send Left/')
    ser.write('Left350/'.encode('utf-8'))
    data = 0
    while data != b'S':
        data = ser.read()
        print('Receive', data)
    print('Stop')
    ser.write('SRotate/'.encode('utf-8'))
    time.sleep(1)
    # shoot()
    time.sleep(1)
