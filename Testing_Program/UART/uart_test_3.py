import serial
import time
import keyboard

Serial_BaudRate = 9600
Serial_Port = 'COM4'

print('Connecting to device ...')
# ser = serial.Serial(Serial_Port, Serial_BaudRate, timeout=3)fsfs
ser = serial.Serial()
ser.baudrate = Serial_BaudRate
ser.port = Serial_Port

ser.open()
print('Connect successful')
#ser.write('S/'.encode('utf-8'))


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
    if key != pre_key:
        pre_key = key
        if key == 'c':
            print('Send Close/')
            ser.write('c140'.encode('utf-8'))
        if key == 'o':
            print('Send Open/')
            ser.write('c40'.encode('utf-8'))
        if key == 's': # base
            for i in range(90, 180):
                print('Send', i)
                data = 'b'+str(i)
                ser.write(data.encode('utf-8'))
                time.sleep(0.05)

            for i in range(180, 90, -1):
                print('Send', i)
                data = 'b'+str(i)
                ser.write(data.encode('utf-8'))
                time.sleep(0.05)
        if key == 'u': # Z
            for i in range(20, 120):
                print('Send', i)
                data = 'z'+str(i)
                ser.write(data.encode('utf-8'))
                time.sleep(0.05)

            for i in range(120, 20, -1):
                print('Send', i)
                data = 'z'+str(i)
                ser.write(data.encode('utf-8'))
                time.sleep(0.05)

        if key == 'f': # Z
            data = 'z' + str(60)
            ser.write(data.encode('utf-8'))
            for i in range(40, 150):
                print('Send', i)
                data = 'f'+str(i)
                ser.write(data.encode('utf-8'))
                time.sleep(0.05)

            for i in range(150, 40, -1):
                print('Send', i)
                data = 'f'+str(i)
                ser.write(data.encode('utf-8'))
                time.sleep(0.05)
        if key == 'q':
            break
    elif key == 'M':
        print(key)
