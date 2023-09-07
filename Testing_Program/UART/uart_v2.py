import serial
import keyboard

ser = serial.Serial()
ser.port = 'COM5'
ser.baudrate = 9600

ser.open()
print('Connected')
start = 0
index = 0
num = 0
while True:
	if ser.inWaiting() > 0:
		data = ser.read()
		if data == b'/':
			pass
		else:
			if index == 0:
				for d in data:
					num = d
				index += 1
			else:
				for d in data:
					num += d*256
				index = 0
				print('Data:', num)

	if keyboard.is_pressed('q'):
		print('Close')
		ser.close()
		break
