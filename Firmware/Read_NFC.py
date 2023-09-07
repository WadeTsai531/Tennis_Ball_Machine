import serial.tools.list_ports


class Serial_System:
    def __init__(self):
        # -------- Variable define --------
        self.ser = serial.Serial()
        self.list_of_port = serial.tools.list_ports.comports()
        self.serial_open = False

        # -------- Scan Serial Port --------
        list_ports = serial.tools.list_ports.comports()
        print('Scan')
        for port in list_ports:
            self.list_of_port.append(port.name)
            print(port.name)

        self.ser.port = 'COM12'
        self.ser.baudrate = 115200
        self.ser.open()
        print('OK')

        while True:
            print('data:', self.ser.read())




Serial_System()
