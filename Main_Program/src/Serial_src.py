import serial.tools.list_ports
import time
import tkinter as tk


def Data_Transform(data_in):
    if data_in >= 100:
        data_send = str(data_in)
    elif 100 > data_in >= 10:
        data_send = '0' + str(data_in)
    else:
        data_send = '00' + str(data_in)
    return data_send


# ------ Serial Setup & Function ------
class Serial_System:
    def __init__(self, init_flag=True):
        # -------- Variable define --------
        self.ser = serial.Serial()
        self.list_of_port = serial.tools.list_ports.comports()
        self.serial_open = False

        # -------- Object define --------
        self.label = None
        self.combobox = None
        self.Connect_button = None
        self.Disconnect_button = None
        self.Message = None

        if init_flag:
            self.Connect_Serial_Port()

    def Connect_Serial_Port(self):
        print('Connecting .....')
        try:
            self.serial_open = True
            self.ser.port = '/dev/ttyUSB0'
            # '/dev/ttyUSB0'
            self.ser.open()
            print('Connect to device')
            self.Transmit_value('/')
        except EnvironmentError:
            print('Connect Fail !!!!')

    def Disconnect_Serial_Port(self):
        print('Disconnect Serial Port')
        self.serial_open = False
        self.Connect_button.configure(state=tk.NORMAL)
        self.Disconnect_button.configure(state=tk.DISABLED)
        self.ser.close()

    def Transmit_value(self, port, value=None):
        if value is None:
            send_data = port + '/'
        else:
            send_data = port + Data_Transform(int(value)) + '/'

        if self.serial_open:
            # print('Serial Value:', send_data)
            self.ser.write(send_data.encode('utf-8'))
        time.sleep(0.001)

    def Transmit_msg(self, port):
        send_data = port + '/'

        if self.serial_open:
            # print('Serial Msg:', send_data)
            self.ser.write(send_data.encode('utf-8'))
        time.sleep(0.001)
