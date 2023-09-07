import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports
import time
import cv2
from PIL import ImageTk, Image


# ---------------- Function ----------------
def Data_Transform(data_in):
    if data_in >= 100:
        data_send = str(data_in)
    elif 100 > data_in >= 10:
        data_send = '0' + str(data_in)
    else:
        data_send = '00' + str(data_in)
    return data_send


# ---------------- Program ----------------
# ------ Serial Setup & Function ------
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

        # -------- Object define --------
        self.label = None
        self.combobox = None
        self.Connect_button = None
        self.Disconnect_button = None
        self.Message = None

    def GUI(self, window, x, y):
        self.label = tk.Label(window, text='Select Serial Port:', font=('Times', 16, 'bold'))
        self.label.place(x=x, y=y)

        self.combobox = ttk.Combobox(window, values=['COM5'],
                                     font=('Times', 14, 'bold'))
        self.combobox.place(x=x, y=y + 30)

        self.Connect_button = tk.Button(window, text='Connect', width=10,
                                        font=('Times', 14, 'bold'),
                                        command=self.Connect_Serial_Port)
        self.Connect_button.place(x=x + 240, y=y)

        self.Disconnect_button = tk.Button(window, text='Disconnect', width=10,
                                           font=('Times', 14, 'bold'),
                                           command=self.Disconnect_Serial_Port)
        self.Disconnect_button.place(x=x + 240, y=y + 50)

        self.Message = tk.Label(window, text='Disconnect',
                                font=('Times', 12, 'bold'))
        self.Message.place(x=x + 10, y=y+65)

        if self.serial_open:
            self.Connect_button.configure(state=tk.DISABLED)
            self.Disconnect_button.configure(state=tk.NORMAL)
        else:
            self.Connect_button.configure(state=tk.NORMAL)
            self.Disconnect_button.configure(state=tk.DISABLED)

    def Connect_Serial_Port(self):
        print('Connecting .....')
        try:
            self.serial_open = True
            self.ser.port = self.combobox.get()
            self.ser.open()
            print('Connect to device')
            self.Message.configure(text='Connect')
            self.Connect_button.configure(state=tk.DISABLED)
            self.Disconnect_button.configure(state=tk.NORMAL)
        except EnvironmentError:
            self.Message.configure(text='Connect Fail')
            print('Connect Fail !!!!')

    def Disconnect_Serial_Port(self):
        print('Disconnect Serial Port')
        self.serial_open = False
        self.Connect_button.configure(state=tk.NORMAL)
        self.Disconnect_button.configure(state=tk.DISABLED)
        self.ser.close()

    def Transmit_value(self, port, value):
        send_data = port + Data_Transform(int(value)) + '/'

        if self.serial_open:
            print('Serial Value:', send_data)
            self.ser.write(send_data.encode('utf-8'))
        time.sleep(0.003)

    def Transmit_msg(self, port):
        send_data = port + '/'

        if self.serial_open:
            print('Serial Msg:', send_data)
            self.ser.write(send_data.encode('utf-8'))
        time.sleep(0.005)


class Vision_System:
    def __init__(self):
        # -------- Variable --------
        self.image = None
        self.image_F = None
        self.image_Tk = None
        self.canvas = None
        self.img_canvas = None
        self.canvas_run = None

        # -------- Camera Setup --------
        print('[INFO] ----------------------------------')
        print('Using default camera 1')
        self.cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        if not self.cam.isOpened():
            print('Cannot open camera 1')
            print('Switch to camera 0')
            self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cam_width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cam_height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Camera is Open \n')

    def Start_Vision(self, window, x=5, y=5):
        print('[INFO] ----------------------------------')
        print('Start Vision System \n')
        ret, image = self.cam.read()
        self.image_F = Image.fromarray(image)
        self.image_Tk = ImageTk.PhotoImage(self.image_F)
        self.canvas = tk.Canvas(window, width=self.cam_width, height=self.cam_height, bg='black')
        self.canvas.place(x=x, y=y)
        self.img_canvas = self.canvas.create_image(self.cam_width / 2 + 2,
                                                   self.cam_height / 2 + 2,
                                                   image=self.image_Tk)
        self.canvas_run = self.canvas.after(1, self.Refresh_Vision)

    def Refresh_Vision(self):
        ret, self.image = self.cam.read()
        image = cv2.flip(self.image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.image_F = Image.fromarray(image)
        self.image_Tk = ImageTk.PhotoImage(self.image_F)
        self.canvas.itemconfig(self.img_canvas, image=self.image_Tk)
        self.canvas_run = self.canvas.after(1, self.Refresh_Vision)

    def Stop_Vision(self):
        cv2.destroyAllWindows()
        self.canvas.after_cancel(self.canvas_run)


class Control_GUI:
    def __init__(self):
        # -------- Variable --------
        self.old_Up_Down_value = 0
        self.old_R_L_value = 0

        print('[INFO] ----------------------------------')
        print('Control GUI Open')
        self.Shoot_Scale = None
        self.Rotate_Scale = None
        self.show_value_label = None
        self.Shoot_Button = None
        self.shoot_button_flag = True
        self.Right_Button = None
        self.Left_Button = None
        self.Rotate_Stop_Button = None
        self.label_run = None
        self.window = None
        self.window_run = None
        self.count = 0

    def Start_GUI(self, window, x=0, y=0):
        self.window = window
        self.Shoot_Scale = tk.Scale(window, orient=tk.VERTICAL,
                                    from_=500, to=0, resolution=5,
                                    width=25, length=250,
                                    font=('Times', 15, 'bold'), command=self.Scale)
        self.Shoot_Scale.place(x=x - 40, y=y)

        self.Rotate_Scale = tk.Scale(window, orient=tk.VERTICAL,
                                     from_=500, to=0, resolution=5,
                                     width=25, length=250,
                                     font=('Times', 15, 'bold'), command=self.Scale)
        self.Rotate_Scale.place(x=x + 40, y=y)

        self.show_value_label = tk.Label(window, text='Rotate Speed: 0    Shoot Speed: 0',
                                         font=('Times', 15, 'bold'))
        self.show_value_label.place(x=x - 40, y=y - 50)

        self.Shoot_Button = tk.Button(window, text='Shoot', width=8,
                                      font=('Times', 15, 'bold'), bg='#55E900', activebackground='#55E900',
                                      command=self.Shoot)
        self.Shoot_Button.place(x=x + 40 + 100, y=y + 10)

        self.Right_Button = tk.Button(window, text='Right', width=8,
                                      font=('Times', 15, 'bold'),
                                      command='')
        self.Right_Button.place(x=x + 40 + 100, y=y + 10 + 70)

        self.Left_Button = tk.Button(window, text='Left', width=8,
                                     font=('Times', 15, 'bold'),
                                     command='')
        self.Left_Button.place(x=x + 40 + 100, y=y + 10 + 140)

        self.Left_Button = tk.Button(window, text='Rotate Stop', width=10,
                                     font=('Times', 15, 'bold'),
                                     command='')
        self.Left_Button.place(x=x + 40 + 100, y=y + 10 + 210)

    def Scale(self, a):
        print('U-D Scale:{}'.format(self.Shoot_Scale.get()))
        print('R-L Scale:{}'.format(self.Rotate_Scale.get()))
        self.show_value_label.configure(text='Shoot Speed: {}    Rotate Speed: {}'.
                                        format(self.Shoot_Scale.get(), self.Rotate_Scale.get()))
        if self.old_Up_Down_value != self.Shoot_Scale.get():
            self.old_Up_Down_value = self.Shoot_Scale.get()
        if self.old_R_L_value != self.Rotate_Scale.get():
            self.old_R_L_value = self.Rotate_Scale.get()

    def Shoot(self):
        if self.shoot_button_flag:
            print('Shoot')
            self.shoot_button_flag = False
            self.Shoot_Button.configure(text='Stop', bg='#F93232', activebackground='#F93232')
        else:
            print('Stop')
            self.shoot_button_flag = True
            self.Shoot_Button.configure(text='Shoot', bg='#55E900', activebackground='#55E900')

    def Right(self):
        print('Right')

    def Left(self):
        print('Left')

    def Rotate_Stop(self):
        print('Rotate Stop')


class Main:
    def __init__(self):
        # -------- Variable --------
        self.main_window_x = 1530
        self.main_window_y = 540

        # -------- Window Setup --------
        self.main_window = tk.Tk()
        self.main_window.title = 'Ball Machine'
        self.main_window.geometry(str(self.main_window_x) + 'x' + str(self.main_window_y))
        self.main_window.resizable(False, False)

        # -------- Vision Canvas --------
        self.vision_canvas = tk.Canvas(self.main_window, bg='black',
                                       width=640, height=480)
        self.vision_canvas.place(x=5, y=5)

        # -------- Close Button --------
        self.Close_button = tk.Button(self.main_window, text='Close', width=8,
                                      bg='#F93232', activebackground='#F93232',
                                      font=('Times', 14, 'bold'), command=self.Close_Window)
        self.Close_button.place(x=self.main_window_x - 110, y=self.main_window_y - 90)

        # -------- Version Canvas --------
        self.version_canvas = tk.Canvas(self.main_window, bg='#818286',
                                        width=1640, height=30)
        self.version_canvas.place(x=-2, y=self.main_window_y - 28)
        Version_label = tk.Label(self.main_window, text='Version 1.1  Made By Wade Tsai',
                                 font='Times 11 bold', bg='#818286')
        Version_label.place(x=self.main_window_x - 230, y=self.main_window_y - 25)

        # -------- Control Plane --------
        control_x, control_y, control_w, control_h = 660, 160, 330, 300
        self.Control_Frame = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3)
        self.Control_Frame.place(x=control_x, y=control_y)
        self.Control_Canvas = tk.Canvas(self.Control_Frame, width=control_w, height=control_h)
        self.Control_Canvas.pack()

        Vision.Start_Vision(self.main_window)
        Control.Start_GUI(self.main_window, control_x + 50, control_y + 10)

        # --------- Serial Plane --------
        self.Frame_Serial = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3)
        self.Frame_Serial.place(x=650, y=5)
        self.Frame_Canvas = tk.Canvas(self.Frame_Serial, width=380, height=100)
        self.Frame_Canvas.pack()

        Serial.GUI(self.main_window, 660, 15)

        self.main_window.mainloop()

    def Close_Window(self):
        print('Close Window')
        Vision.Stop_Vision()
        self.main_window.destroy()


Serial = Serial_System()
Vision = Vision_System()
Control = Control_GUI()
Main()
