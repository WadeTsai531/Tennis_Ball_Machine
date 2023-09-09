import serial
import time
import keyboard

Serial_BaudRate = 9600
Serial_Port = 'COM3'

print('Connecting to device ...')
ser = serial.Serial()
ser.baudrate = Serial_BaudRate
ser.port = Serial_Port

ser.open()
print('Connect successful')
# ser.write('S/'.encode('utf-8'))

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
    if keyboard.is_pressed('s'):
        print('Host Send Data')
        time.sleep(1)
        ser.write('Hello kk'.encode('utf-8'))
    if keyboard.is_pressed('q'):
        print('break')
        break
    if ser.inWaiting() > 0:
        data = ser.read()
        print('Data Read:', data)
