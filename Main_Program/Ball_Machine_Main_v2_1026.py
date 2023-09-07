import tkinter as tk
import cv2
import time
import serial
from PIL import Image, ImageTk


# ---------------- Function ----------------
def transform_timer(data_in):
    if data_in >= 10:
        data_send = str(data_in)
    else:
        data_send = '0' + str(data_in)
    return data_send


class Main_GUI:
    Scroll_value = 250
    Rotate_value = 250

    def __init__(self):
        # -------- Variable Define --------
        self.label = None
        self.Mode = 'random'
        self.Manual_Training = 'Training'
        self.Rotate_Dir = 'S'
        self.Scroll_Dir = 'S'
        # --------------- Manual UI Variable ---------------
        self.Scroll_Scale = None
        self.Rotate_Scale = None
        self.Rotate_value_label = None
        self.Scroll_value_label = None
        self.Manual_Frame = None
        self.Manual_Canvas = None

        # --------------- Mode Select Variable ---------------
        self.Mode_Select_Frame = None
        self.Mode_Select_Canvas = None
        self.Mode_Select_Label = None
        self.Random_Mode_Button = None
        self.Tracking_Mode_Button = None
        self.Avoid_Mode_Button = None

        # --------------- Timer Variable ---------------
        self.timer_hour_data = 0
        self.timer_min_data = 0
        self.timer_sec_data = 0

        self.Timing_Frame = None
        self.Timing_Canvas = None
        self.Timing_Label = None
        self.timer_hour_label = None
        self.timer_min_label = None
        self.timer_sec_label = None
        self.timer_hour_label_2 = None
        self.timer_min_label_2 = None
        self.timer_sec_label_2 = None

        self.invisible_timer = None

        # -------- Serial Setup --------
        Serial_BaudRate = 9600
        Serial_Port = 'COM5'

        print('Connecting to device ...')
        self.ser = serial.Serial()
        self.ser.baudrate = Serial_BaudRate
        self.ser.port = Serial_Port
        # self.ser.open()
        print('Connect successful')

        # -------- UI Setup --------
        self.main_window = tk.Tk()
        self.main_window.geometry('1024x600')
        self.main_window.title('Main GUI')
        self.main_window.configure(bg='#579CD8')
        self.main_window.resizable(width=False, height=False)

        # -------- Open Camera --------
        # self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        gst_str = ('v4l2src device=/dev/video{} ! '
                   'video/x-raw, width=(int){}, height=(int){} ! '
                   'videoconvert ! appsink').format(0, 640, 480)
        self.cam = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

        # -------- UI Layout --------
        # ---------------- Training / Manual Select ----------------
        self.Manual_Button = tk.Button(self.main_window, text='Manual', font=('Times', 20, 'bold'), width=8,
                                       command=self.Manual_mode)
        self.Manual_Button.place(x=10, y=500)

        self.Training_Button = tk.Button(self.main_window, text='Training', font=('Times', 20, 'bold'), width=8,
                                         command=self.Training_mode)
        self.Training_Button.place(x=170, y=500)
        # ---------------- Mode Select ----------------
        self.Mode_Select_UI()

        # ---------------- Timing Setup ----------------
        self.Timer_UI()

        # ---------------- Start / Stop Training ----------------
        self.Start_Stop_UI()

        # ---------------- Close Window ----------------
        self.Close_button = tk.Button(self.main_window, text='Close', width=8,
                                      bg='#F93232', activebackground='#F93232',
                                      font=('Times', 14, 'bold'), command=self.Close_Window)
        self.Close_button.place(x=1024 - 110, y=600 - 90)

        # -------- Function --------
        self.Vision()

        self.main_window.mainloop()

    def Manual_mode(self):
        if self.Manual_Training == 'Training':
            print('Select Manual')
            self.Manual_Training = 'Manual'
            self.Timer_UI_destroy()
            self.Mode_Select_UI_destroy()
            self.Start_Stop_UI_destroy()
            self.Manual_UI()

    def Training_mode(self):
        if self.Manual_Training == 'Manual':
            print('Select Training')
            self.Manual_Training = 'Training'
            self.Timer_UI()
            self.Mode_Select_UI()
            self.Start_Stop_UI()
            self.Manual_UI_destroy()

    def Start_Training(self):
        print('Start Training', self.Mode)

    def Stop_Train(self):
        print('Stop Train', self.Mode)

    def Mode_Select(self, mode):
        print(mode)
        if mode == 'random':
            self.Mode = 'random'
            self.Random_Mode_Button.configure(bg='#008397', state=tk.DISABLED)
            self.Tracking_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL)
            self.Avoid_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL)
        elif mode == 'tracking':
            self.Mode = 'tracking'
            self.Random_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL)
            self.Tracking_Mode_Button.configure(bg='#008397', state=tk.DISABLED)
            self.Avoid_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL)
        else:
            self.Mode = 'avoid'
            self.Random_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL)
            self.Tracking_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL)
            self.Avoid_Mode_Button.configure(bg='#008397', state=tk.DISABLED)

    def Vision(self):
        ret, frame = self.cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_PIL = Image.fromarray(frame)
        frame_tk = ImageTk.PhotoImage(frame_PIL)
        self.label = tk.Label(self.main_window, image=frame_tk, relief=tk.SUNKEN, borderwidth=5, bg='#DCDCDC')
        self.label.place(x=0, y=0)
        self.label.after(1, self.Re_Vision)

    def Re_Vision(self):
        ret, frame = self.cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_PIL = Image.fromarray(frame)
        frame_tk = ImageTk.PhotoImage(frame_PIL)
        self.label.image = frame_tk
        self.label.configure(image=frame_tk)
        self.label.after(1, self.Re_Vision)

    def Manual_UI(self):
        self.Manual_Frame = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3, bg='#DCDCDC')
        self.Manual_Frame.place(x=655, y=5)
        self.Manual_Canvas = tk.Canvas(self.Manual_Frame, width=355, height=480)
        self.Manual_Canvas.pack()
        self.Manual_Label = tk.Label(self.main_window, text='Manual Mode', font=('Times', 20, 'bold'))
        self.Manual_Label.place(x=660, y=10)

        self.Rotate_Right_Button = tk.Button(self.main_window, text='Right', font=('Times', 16, 'bold'),
                                             width=6, bg='#0099E0', activebackground='#0099E0',
                                             command=lambda msg='Right': self.Send_Command(msg))
        self.Rotate_Right_Button.place(x=670, y=120)

        self.Rotate_Left_Button = tk.Button(self.main_window, text='Left', font=('Times', 16, 'bold'), width=6,
                                            bg='#0099E0', activebackground='#0099E0',
                                            command=lambda msg='Left': self.Send_Command(msg))
        self.Rotate_Left_Button.place(x=670, y=180)

        self.Rotate_Stop_Button = tk.Button(self.main_window, text='Stop', font=('Times', 16, 'bold'), width=6,
                                            bg='#F93232', activebackground='#F93232',
                                            command=lambda msg='SRotate': self.Send_Command(msg))
        self.Rotate_Stop_Button.place(x=670, y=240)

        self.Raise_Up_Button = tk.Button(self.main_window, text='Up', font=('Times', 16, 'bold'), width=6,
                                         bg='#0099E0', activebackground='#0099E0',
                                         command=lambda msg='Up': self.Send_Command(msg))
        self.Raise_Up_Button.place(x=790, y=120)

        self.Raise_Down_Button = tk.Button(self.main_window, text='Down', font=('Times', 16, 'bold'), width=6,
                                           bg='#0099E0', activebackground='#0099E0',
                                           command=lambda msg='Down': self.Send_Command(msg))
        self.Raise_Down_Button.place(x=790, y=180)

        self.Raise_Stop_Button = tk.Button(self.main_window, text='Stop', font=('Times', 16, 'bold'), width=6,
                                           bg='#F93232', activebackground='#F93232',
                                           command=lambda msg='SRaise': self.Send_Command(msg))
        self.Raise_Stop_Button.place(x=790, y=240)

        self.Scroll_Button = tk.Button(self.main_window, text='Scroll', font=('Times', 16, 'bold'),
                                       width=6, height=2, bg='#55E900', activebackground='#55E900',
                                       command=lambda msg='Scroll': self.Send_Command(msg))
        self.Scroll_Button.place(x=910, y=120)

        self.Shoot_Button = tk.Button(self.main_window, text='Shoot', font=('Times', 16, 'bold'),
                                      width=6, height=2, bg='#00D3CD', activebackground='#0099E0',
                                      command=lambda msg='SStop': self.Send_Command(msg))
        self.Shoot_Button.place(x=910, y=218)

        # -------- Scroll / Rotate Scale --------
        self.Scroll_value_label = tk.Label(self.main_window, text='Scroll: {}'.format(str(self.Scroll_value)),
                                           font=('Times', 15, 'bold'))
        self.Scroll_value_label.place(x=675, y=295)
        self.Scroll_Scale = tk.Scale(self.main_window, from_=0, to=500, resolution=5, width=26, length=300,
                                     orient=tk.HORIZONTAL, font=('Times', 15, 'bold'), command=self.Scale)
        self.Scroll_Scale.place(x=675, y=320)
        self.Scroll_Scale.set(self.Scroll_value)

        self.Rotate_value_label = tk.Label(self.main_window, text='Rotate: {}'.format(str(self.Rotate_value)),
                                           font=('Times', 15, 'bold'))
        self.Rotate_value_label.place(x=675, y=395)
        self.Rotate_Scale = tk.Scale(self.main_window, from_=0, to=500, resolution=5, width=26, length=300,
                                     orient=tk.HORIZONTAL, font=('Times', 15, 'bold'), command=self.Scale)
        self.Rotate_Scale.place(x=675, y=420)
        self.Rotate_Scale.set(self.Rotate_value)

    def Manual_UI_destroy(self):
        if self.Manual_Frame is not None:
            self.Manual_Frame.destroy()
            self.Manual_Canvas.destroy()
            self.Scroll_value_label.destroy()
            self.Scroll_Scale.destroy()
            self.Rotate_value_label.destroy()
            self.Rotate_Scale.destroy()

            self.Rotate_Right_Button.destroy()
            self.Rotate_Left_Button.destroy()
            self.Rotate_Stop_Button.destroy()
            self.Raise_Up_Button.destroy()
            self.Raise_Down_Button.destroy()
            self.Raise_Stop_Button.destroy()

    def Send_Command(self, fun):
        if fun == 'Right':
            self.Rotate_Dir = 'R'
            print(fun, self.Rotate_Scale.get())
        elif fun == 'Left':
            self.Rotate_Dir = 'L'
            print(fun, self.Rotate_Scale.get())
        elif fun == 'Scroll':
            print('Scroll', self.Scroll_Scale.get())
            self.Scroll_Dir = 'F'
            self.Scroll_Button.configure(text='Stop', bg='#E91B1B',
                                         command=lambda msg='Stop': self.Send_Command(msg))
        elif fun == 'Stop':
            print('Stop')
            self.Scroll_Dir = 'S'
            self.Scroll_Button.configure(text='Scroll', bg='#55E900',
                                         command=lambda msg='Scroll': self.Send_Command(msg))
        elif fun == 'SRotate':
            print('Stop Rotate')
            self.Rotate_Dir = 'S'

    def Scale(self, data):
        print('Scroll Value: {} --- Rotate Value: {}'.format(self.Scroll_Scale.get(), self.Rotate_Scale.get()))
        scroll_color_value = str(hex(255 - int(self.Scroll_Scale.get()) * 255 // 500))
        rotate_color_value = str(hex(255 - int(self.Rotate_Scale.get()) * 255 // 500))

        if len(scroll_color_value) < 4:
            scroll_color_value = '#ff0' + scroll_color_value[2] + '00'
        else:
            scroll_color_value = '#ff' + scroll_color_value[2:] + '00'

        if len(rotate_color_value) < 4:
            rotate_color_value = '#ff0' + rotate_color_value[2] + '00'
        else:
            rotate_color_value = '#ff' + rotate_color_value[2:] + '00'

        self.Scroll_value_label.configure(text='Scroll: {}'.format(self.Scroll_Scale.get()))
        self.Rotate_value_label.configure(text='Rotate: {}'.format(self.Rotate_Scale.get()))
        self.Scroll_Scale.configure(bg=scroll_color_value)
        self.Rotate_Scale.configure(bg=rotate_color_value)

        if self.Rotate_Dir == 'R':
            self.Send_Command('Right')
        elif self.Rotate_Dir == 'L':
            self.Send_Command('Left')
        else:
            self.Send_Command('S')

        if self.Scroll_Dir == 'F':
            self.Send_Command('Scroll')
        else:
            self.Send_Command('S')

    def Mode_Select_UI(self):
        mode_select_y = 5
        self.Mode_Select_Frame = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3, bg='#DCDCDC')
        self.Mode_Select_Frame.place(x=655, y=mode_select_y)
        self.Mode_Select_Canvas = tk.Canvas(self.Mode_Select_Frame, width=355, height=100, bg='#DCDCDC')
        self.Mode_Select_Canvas.pack()
        self.Mode_Select_Label = tk.Label(self.main_window, text='Select Mode:', bg='#DCDCDC',
                                          font=('Times', 20, 'bold'))
        self.Mode_Select_Label.place(x=660, y=mode_select_y + 5)

        self.Random_Mode_Button = tk.Button(self.main_window, text='Random', width=7, font=('Times', 17, 'bold'),
                                            command=lambda mode='random': self.Mode_Select(mode),
                                            bg='#008397', activebackground='#008397', state=tk.DISABLED)
        self.Random_Mode_Button.place(x=662, y=mode_select_y + 50)

        self.Tracking_Mode_Button = tk.Button(self.main_window, text='Tracking', width=7, font=('Times', 17, 'bold'),
                                              command=lambda mode='tracking': self.Mode_Select(mode),
                                              bg='#00D7E2', activebackground='#008397')
        self.Tracking_Mode_Button.place(x=782, y=mode_select_y + 50)

        self.Avoid_Mode_Button = tk.Button(self.main_window, text='Avoid', width=7, font=('Times', 17, 'bold'),
                                           command=lambda mode='avoid': self.Mode_Select(mode),
                                           bg='#00D7E2', activebackground='#008397')
        self.Avoid_Mode_Button.place(x=902, y=mode_select_y + 50)

    def Mode_Select_UI_destroy(self):
        self.Mode_Select_Frame.destroy()
        self.Mode_Select_Canvas.destroy()
        self.Mode_Select_Label.destroy()

        self.Random_Mode_Button.destroy()
        self.Tracking_Mode_Button.destroy()
        self.Avoid_Mode_Button.destroy()

    def Start_Stop_UI(self):
        start_stop_y = 440
        self.start_training_button = tk.Button(self.main_window, text='Start', font=('Times', 24, 'bold'),
                                               width=8, height=1, bg='#06C700', activebackground='#048F00',
                                               command=self.Start_Training)
        self.start_training_button.place(x=660, y=start_stop_y)

        self.stop_training_button = tk.Button(self.main_window, text='Stop', font=('Times', 24, 'bold'),
                                              width=8, height=1, bg='#D5000B', activebackground='#9A0008',
                                              command=self.Stop_Train)
        self.stop_training_button.place(x=850, y=start_stop_y)

    def Start_Stop_UI_destroy(self):
        self.start_training_button.destroy()
        self.stop_training_button.destroy()

    def Timer_UI(self):
        timing_setup_y = 120
        self.Timing_Frame = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3, bg='#DCDCDC')
        self.Timing_Frame.place(x=655, y=timing_setup_y)
        self.Timing_Canvas = tk.Canvas(self.Timing_Frame, width=355, height=180, bg='#DCDCDC')
        self.Timing_Canvas.pack()
        self.Timing_Label = tk.Label(self.main_window, text='Set Training Time:', bg='#DCDCDC',
                                     font=('Times', 20, 'bold'))
        self.Timing_Label.place(x=660, y=timing_setup_y + 5)

        self.timer_hour_label = tk.Label(self.main_window, text='Hour', bg='#DCDCDC',
                                         font=('Times', 14, 'bold'))
        self.timer_hour_label.place(x=695, y=timing_setup_y + 50)

        self.timer_min_label = tk.Label(self.main_window, text='Minute', bg='#DCDCDC',
                                        font=('Times', 14, 'bold'))
        self.timer_min_label.place(x=802, y=timing_setup_y + 50)

        self.timer_sec_label = tk.Label(self.main_window, text='Second', bg='#DCDCDC',
                                        font=('Times', 14, 'bold'))
        self.timer_sec_label.place(x=915, y=timing_setup_y + 50)

        self.timer_hour_label_2 = tk.Label(self.main_window, text='00', bg='#DCDCDC',
                                           font=('Times', 22, 'bold'))
        self.timer_hour_label_2.place(x=705, y=timing_setup_y + 80)

        self.timer_min_label_2 = tk.Label(self.main_window, text='00', bg='#DCDCDC',
                                          font=('Times', 22, 'bold'))
        self.timer_min_label_2.place(x=817, y=timing_setup_y + 80)

        self.timer_sec_label_2 = tk.Label(self.main_window, text='00', bg='#DCDCDC',
                                          font=('Times', 22, 'bold'))
        self.timer_sec_label_2.place(x=930, y=timing_setup_y + 80)

        self.Timer_Button(1, 670, timing_setup_y + 125)
        self.Timer_Button(2, 785, timing_setup_y + 125)
        self.Timer_Button(3, 900, timing_setup_y + 125)

        if self.invisible_timer is not None:
            self.invisible_timer.destroy()

    def Timer_UI_destroy(self):
        self.Timing_Frame.destroy()
        self.Timing_Canvas.destroy()
        self.Timing_Label.destroy()

        self.timer_hour_label.destroy()
        self.timer_min_label.destroy()
        self.timer_sec_label.destroy()

        self.timer_hour_label_2.destroy()
        self.timer_min_label_2.destroy()
        self.timer_sec_label_2.destroy()

        self.Start_Stop_UI_destroy()

        self.invisible_timer = tk.Canvas(self.main_window, bg='#579CD8', width=355, height=50)
        self.invisible_timer.place(x=660, y=240)

    def Timer_Button(self, ch, x, y):
        Add = tk.Button(self.main_window, text='+', bg='#DCDCDC', font=('Times', 18, 'bold'),
                        command=lambda channel=ch: self.Timer_Add(channel), width=1)
        Add.place(x=x, y=y)

        Reduce = tk.Button(self.main_window, text='-', bg='#DCDCDC', font=('Times', 18, 'bold'),
                           command=lambda channel=ch: self.Timer_Reduce(channel), width=1)
        Reduce.place(x=x + 55, y=y)

    def Timer_Add(self, ch):
        print('Add-', ch)
        if ch == 1:
            self.timer_hour_data += 1
            if self.timer_hour_data >= 24:
                self.timer_hour_data = 0
            self.timer_hour_label_2.configure(text=transform_timer(self.timer_hour_data))
        elif ch == 2:
            self.timer_min_data += 1
            if self.timer_min_data >= 60:
                self.timer_min_data = 0
            self.timer_min_label_2.configure(text=transform_timer(self.timer_min_data))
        else:
            self.timer_sec_data += 1
            if self.timer_sec_data >= 60:
                self.timer_sec_data = 0
            self.timer_sec_label_2.configure(text=transform_timer(self.timer_sec_data))

    def Timer_Reduce(self, ch):
        print('Reduce-', ch)
        if ch == 1:
            self.timer_hour_data -= 1
            if self.timer_hour_data <= 0:
                self.timer_hour_data = 0
            self.timer_hour_label_2.configure(text=transform_timer(self.timer_hour_data))
        elif ch == 2:
            self.timer_min_data -= 1
            if self.timer_min_data <= 0:
                self.timer_min_data = 0
            self.timer_min_label_2.configure(text=transform_timer(self.timer_min_data))
        else:
            self.timer_sec_data -= 1
            if self.timer_sec_data <= 0:
                self.timer_sec_data = 0
            self.timer_sec_label_2.configure(text=transform_timer(self.timer_sec_data))

    def Read_Data(self):
        print(self.ser.read())
        self.main_window.after(1, self.Read_Data)

    def Close_Window(self):
        self.label.after_cancel(self.Re_Vision)
        self.main_window.destroy()


Main_GUI()
