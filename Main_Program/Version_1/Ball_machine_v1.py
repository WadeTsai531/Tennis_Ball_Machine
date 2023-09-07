import tkinter as tk
from tkinter import ttk
import serial
import time
import cv2
from PIL import ImageTk, Image


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
        self.Up_Down_Scale = None
        self.Right_Left_Scale = None
        self.show_value_label = None
        self.label_run = None
        self.window = None
        self.window_run = None
        self.count = 0

    def Start_GUI(self, window, x=0, y=0):
        self.window = window
        self.Up_Down_Scale = tk.Scale(window, orient=tk.VERTICAL,
                                      from_=125, to=-125,
                                      width=20, length=200,
                                      font=('Times', 15, 'bold'), command=self.Scale)
        self.Up_Down_Scale.place(x=x, y=y)

        self.Right_Left_Scale = tk.Scale(window, orient=tk.HORIZONTAL,
                                         from_=-125, to=125,
                                         width=20, length=200,
                                         font=('Times', 15, 'bold'), command=self.Scale)
        self.Right_Left_Scale.place(x=x - 40, y=y + 200)

        self.show_value_label = tk.Label(window, text='Show x: 0    y: 0',
                                         font=('Times', 15, 'bold'))
        self.show_value_label.place(x=x - 40, y=y - 50)
        self.window_run = window.after(1, self.Rescale)

    def Scale(self, a):
        print('U-D Scale:{}'.format(self.Up_Down_Scale.get()))
        print('R-L Scale:{}'.format(self.Right_Left_Scale.get()))
        self.show_value_label.configure(text='Show x: {}    y: {}'.format(self.Up_Down_Scale.get(),
                                                                          self.Right_Left_Scale.get()))
        if self.old_Up_Down_value != self.Up_Down_Scale.get():
            self.old_Up_Down_value = self.Up_Down_Scale.get()
        if self.old_R_L_value != self.Right_Left_Scale.get():
            self.old_R_L_value = self.Right_Left_Scale.get()

    def Rescale(self):
        scale_x = self.Up_Down_Scale.get()
        if not self.count == -1:
            if self.old_Up_Down_value == scale_x and scale_x != 0:
                if self.count >= 5:
                    print('clear')
                    self.count = -1
                else:
                    self.count += 1
                print(self.count)
            else:
                self.count = 0
        elif self.count == -1:
            self.count = -2
            self.label_run = self.show_value_label.after(1, self.rest)
        self.window_run = self.window.after(1, self.Rescale)

    def rest(self):
        if self.old_Up_Down_value == self.Up_Down_Scale.get():
            if self.Up_Down_Scale.get() != 0:
                if self.Up_Down_Scale.get() > 0:
                    self.old_Up_Down_value -= 1
                    self.Up_Down_Scale.set(self.old_Up_Down_value)
                else:
                    self.old_Up_Down_value += 1
                    self.Up_Down_Scale.set(self.old_Up_Down_value)

        if self.Up_Down_Scale.get() == 0:
            self.show_value_label.after_cancel(self.label_run)
        else:
            self.show_value_label.after(1, self.rest)

    def Stop(self):
        # self.label_run.after_cancel(self.label_run)
        self.window.after_cancel(self.window_run)


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
        Version_label = tk.Label(self.main_window, text='Version 1.0  Made By Wade Tsai',
                                 font='Times 11 bold', bg='#818286')
        Version_label.place(x=self.main_window_x - 230, y=self.main_window_y - 25)

        # -------- Control Plane --------
        control_x, control_y, control_w, control_h = 660, 50, 300, 300
        self.Control_Frame = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3)
        self.Control_Frame.place(x=control_x, y=control_y)
        self.Control_Canvas = tk.Canvas(self.Control_Frame, width=control_w, height=control_h)
        self.Control_Canvas.pack()

        Vision.Start_Vision(self.main_window)
        Control.Start_GUI(self.main_window, control_x + 60, control_y + 10)

        self.main_window.mainloop()

    def Close_Window(self):
        print('Close Window')
        Vision.Stop_Vision()
        Control.Stop()
        self.main_window.destroy()


Vision = Vision_System()
Control = Control_GUI()
Main()
