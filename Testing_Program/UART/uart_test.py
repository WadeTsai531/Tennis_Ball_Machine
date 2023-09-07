import serial
import time
import keyboard

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


pre_key = ''
while True:
    key = keyboard.read_key()
    if key != '':
        if key == 'c':
            print('Rotate Clear')
            ser.write('Cab/'.encode('utf-8'))
            time.sleep(0.01)
            ser.write('SRotate/'.encode('utf-8'))
        if key == 'f':
            print('Send Scroll500/')
            ser.write('Scroll500/'.encode('utf-8'))
        if key == 'r':
            print('Send SRotate/')
            ser.write('SRotate/'.encode('utf-8'))
            time.sleep(0.005)
            print('Send Right/')
            ser.write('Right350/'.encode('utf-8'))
        if key == 'l':
            print('Send SRotate/')
            ser.write('SRotate/'.encode('utf-8'))
            time.sleep(0.005)
            print('Send Left/')
            ser.write('Left350/'.encode('utf-8'))
        if key == 'm':
            print('Send SRotate/')
            ser.write('SRotate/'.encode('utf-8'))
        if key == 'u':
            print('Send Up/')
            ser.write('Up/'.encode('utf-8'))
        if key == 'd':
            print('Send Down/')
            ser.write('Down/'.encode('utf-8'))
        if key == 'k':
            print('Send SRaise/')
            ser.write('SRaise/'.encode('utf-8'))
        if key == 's':
            print('Send Stop/')
            ser.write('Stop/'.encode('utf-8'))
            time.sleep(0.01)
            ser.write('SShot/'.encode('utf-8'))
        if key == 'e':
            print('Send Shot')
            ser.write('Shot/'.encode('utf-8'))
        if key == 'w':
            print('Send Shot Sensor')
            ser.write('Shot/'.encode('utf-8'))
            time.sleep(0.5)
            ser.write('ShSot/'.encode('utf-8'))
            time.sleep(0.01)
            ser.write('/'.encode('utf-8'))
        if key == 'q':
            break
    if ser.inWaiting() > 0:
        data = ser.read()
        print(data)
