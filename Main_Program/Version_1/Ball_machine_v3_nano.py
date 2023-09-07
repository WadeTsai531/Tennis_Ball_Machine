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

        self.Transmit_value('S')
        self.Transmit_value('k')
        self.Transmit_value('m')

    def GUI(self, window, x, y):
        self.label = tk.Label(window, text='Select Serial Port:', font=('Times', 16, 'bold'))
        self.label.place(x=x, y=y)

        self.combobox = ttk.Combobox(window, values=self.list_of_port,
                                     font=('Times', 14, 'bold'))
        self.combobox.place(x=x, y=y + 30)
        self.combobox.current(1)

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
        self.Message.place(x=x + 10, y=y + 65)

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
            self.ser.port = '/dev/ttyUSB0'
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

    def Transmit_value(self, port, value=None):
        if value is None:
            send_data = port + '/'
        else:
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
        self.Tracking_Button = None
        self.Tracking_flag = False

        self.turn_right_flag = False
        self.turn_Left_flag = False

        self.delay_count = 0

        # -------- Camera Setup --------
        print('[INFO] ----------------------------------')
        print('Using default camera 1')
        gst_str = ('v4l2src device=/dev/video{} ! '
                   'video/x-raw, width=(int){}, height=(int){} ! '
                   'videoconvert ! appsink').format(0, 640, 480)
        self.cam = cv2.VideoCapture(gst_str)
        if not self.cam.isOpened():
            print('Cannot open camera 1')
            print('Switch to camera 0')
            gst_str = ('v4l2src device=/dev/video{} ! '
                       'video/x-raw, width=(int){}, height=(int){} ! '
                       'videoconvert ! appsink').format(0, 640, 480)
            self.cam = cv2.VideoCapture(gst_str)
        self.cam_width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cam_height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Camera is Open \n')

        # -------- Yolov4 Setup --------
        self.center = [int(self.cam_width) // 2, int(self.cam_height) // 2]
        self.xy_range = [150, 100]

        self.CONFIDENCE_THRESHOLD = 0.6
        self.NMS_THRESHOLD = 0.4
        self.COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

        with open("../../Training_Process/coco_test/classes.txt", "r") as f:
            self.class_names = [cname.strip() for cname in f.readlines()]
        config_path = '../../Training_Process/coco_test/yolov4-tiny.cfg'
        weights_path = '../../Training_Process/coco_test/yolov4-tiny.weights'

        net = cv2.dnn.readNet(weights_path, config_path)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(288, 288), scale=1 / 255, swapRB=True)

    def Start_Vision(self, window, x=5, y=5):
        print('[INFO] ----------------------------------')
        print('Start Vision System \n')
        self.Tracking_Button = tk.Button(window, text='Start Tracking',
                                         font=('Times', 15, 'bold'), width=11,
                                         bg='#55E900', activebackground='#55E900',
                                         command=self.Enable)
        self.Tracking_Button.place(x=x + 1053, y=y + 40)
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
        if self.Tracking_flag:
            image = self.Tracking(image)
        self.image_F = Image.fromarray(image)
        self.image_Tk = ImageTk.PhotoImage(self.image_F)
        self.canvas.itemconfig(self.img_canvas, image=self.image_Tk)
        self.canvas_run = self.canvas.after(1, self.Refresh_Vision)

    def Tracking(self, frame):
        classes, scores, boxes = self.model.detect(frame,
                                                   self.CONFIDENCE_THRESHOLD,
                                                   self.NMS_THRESHOLD)
        cv2.rectangle(frame,
                      (self.center[0] - self.xy_range[0], self.center[1] - self.xy_range[1]),
                      (self.center[0] + self.xy_range[0], self.center[1] + self.xy_range[1]), (0, 255, 0), 3)

        point_x, point_y = 0, 0
        for (class_id, score, box) in zip(classes, scores, boxes):
            color = self.COLORS[int(class_id) % len(self.COLORS)]
            label = "%s : %f" % (self.class_names[class_id], score)
            if class_id == 0:
                x_min, y_min, w, h = box
                x_max = x_min + w
                y_max = y_min + h

                x_center = (x_max + x_min) // 2
                y_center = (y_max + y_min) // 2

                if (self.center[0] - self.xy_range[0]) <= x_center <= (self.center[0] + self.xy_range[0]) and \
                        (self.center[1] - self.xy_range[1]) <= y_center <= (self.center[1] + self.xy_range[1]):
                    point_x, point_y = x_center, y_center
                    cv2.circle(frame, (x_center, y_center), 5, (0, 255, 0), 5)
                    cv2.rectangle(frame, box, color, 2)
                    cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                break

        if point_x != 0 and point_y != 0:
            gap = point_x - self.center[0]
            print(gap)
            if gap < -100:
                if not self.turn_right_flag:
                    Serial.Transmit_value('R', 210)
                    self.turn_right_flag = True
                    print('Turn Right')
            else:
                if self.turn_right_flag:
                    Serial.Transmit_value('m')
                    self.turn_right_flag = False
                    print('Stop')

            if gap > 100:
                if not self.turn_Left_flag:
                    Serial.Transmit_value('L', 210)
                    self.turn_Left_flag = True
                    print('Turn Left')
            else:
                if self.turn_Left_flag:
                    Serial.Transmit_value('m')
                    self.turn_Left_flag = False
                    print('Stop')
        return frame

    def Enable(self):
        if self.Tracking_flag:
            self.Tracking_flag = False
            self.Tracking_Button.configure(text='Start Tracking', bg='#55E900', activebackground='#55E900')
        else:
            self.Tracking_flag = True
            self.Tracking_Button.configure(text='Stop Tracking', bg='#F93232', activebackground='#F93232')

    def Stop_Vision(self):
        cv2.destroyAllWindows()
        self.canvas.after_cancel(self.canvas_run)


class Control_GUI:
    def __init__(self):
        # -------- Variable --------
        self.old_Shoot_value = 0
        self.old_Rotate_value = 0

        print('[INFO] ----------------------------------')
        print('Control GUI Open')
        self.Shoot_Scale = None
        self.Rotate_Scale = None
        self.show_value_label = None

        self.Shoot_Button = None
        self.Right_Button = None
        self.Left_Button = None
        self.Rotate_Stop_Button = None
        self.Rotate_Calibration_Button = None
        self.Up_Button = None
        self.Down_Button = None
        self.Raise_Stop_Button = None

        self.shoot_button_flag = True
        self.Rotate_Status = 'Stop'  # Right, Left, Stop

    def Start_GUI(self, window, x=0, y=0):
        self.Shoot_Scale = tk.Scale(window, orient=tk.VERTICAL,
                                    from_=500, to=0, resolution=5,
                                    width=25, length=250,
                                    font=('Times', 15, 'bold'), command=self.Scale)
        self.Shoot_Scale.place(x=x - 45, y=y)
        self.Shoot_Scale.set(200)

        self.Rotate_Scale = tk.Scale(window, orient=tk.VERTICAL,
                                     from_=500, to=0, resolution=5,
                                     width=25, length=250,
                                     font=('Times', 15, 'bold'), command=self.Scale)
        self.Rotate_Scale.place(x=x + 35, y=y)
        self.Rotate_Scale.set(230)

        self.show_value_label = tk.Label(window, text='Shoot Speed: 0    Rotate Speed: 0',
                                         font=('Times', 15, 'bold'))
        self.show_value_label.place(x=x - 50, y=y - 50)

        self.Shoot_Button = tk.Button(window, text='Shoot', width=9,
                                      font=('Times', 15, 'bold'), bg='#55E900', activebackground='#55E900',
                                      command=self.Shoot)
        self.Shoot_Button.place(x=1040, y=y + 5)

        self.Right_Button = tk.Button(window, text='Right', width=9,
                                      font=('Times', 15, 'bold'), bg='#0099E0', activebackground='#0099E0',
                                      command=self.Right)
        self.Right_Button.place(x=x + 40 + 100, y=y + 5 + 70)

        self.Left_Button = tk.Button(window, text='Left', width=9,
                                     font=('Times', 15, 'bold'), bg='#0099E0', activebackground='#0099E0',
                                     command=self.Left)
        self.Left_Button.place(x=x + 40 + 100, y=y + 5 + 140)

        self.Rotate_Calibration_Button = tk.Button(window, text='Calibration', width=9,
                                                   font=('Times', 15, 'bold'), bg='#00E088', activebackground='#00E088',
                                                   command=self.Calibration)
        self.Rotate_Calibration_Button.place(x=x + 40 + 100, y=y + 5)

        self.Rotate_Stop_Button = tk.Button(window, text='Rotate Stop', width=9,
                                            font=('Times', 15, 'bold'), bg='#F93232', activebackground='#F93232',
                                            command=self.Rotate_Stop)
        self.Rotate_Stop_Button.place(x=x + 40 + 100, y=y + 5 + 210)

        self.Up_Button = tk.Button(window, text='Up', width=9,
                                   font=('Times', 15, 'bold'), bg='#0099E0', activebackground='#0099E0',
                                   command=self.Up)
        self.Up_Button.place(x=1040, y=y + 5 + 70)

        self.Down_Button = tk.Button(window, text='Down', width=9,
                                     font=('Times', 15, 'bold'), bg='#0099E0', activebackground='#0099E0',
                                     command=self.Down)
        self.Down_Button.place(x=1040, y=y + 5 + 140)

        self.Raise_Stop_Button = tk.Button(window, text='Stop Raise', width=9,
                                           font=('Times', 15, 'bold'), bg='#F93232', activebackground='#F93232',
                                           command=self.Raise_Stop)
        self.Raise_Stop_Button.place(x=1040, y=y + 5 + 210)

    def Scale(self, a):
        print('Shoot Scale:{} -- Rotate Scale:{}'.format(self.Shoot_Scale.get(), self.Rotate_Scale.get()))
        self.show_value_label.configure(text='Shoot Speed: {}    Rotate Speed: {}'.
                                        format(self.Shoot_Scale.get(), self.Rotate_Scale.get()))
        if self.old_Shoot_value != self.Shoot_Scale.get():
            self.old_Shoot_value = self.Shoot_Scale.get()
        if self.old_Rotate_value != self.Rotate_Scale.get():
            self.old_Rotate_value = self.Rotate_Scale.get()

        if not self.shoot_button_flag:
            Serial.Transmit_value('F', self.old_Shoot_value)

    def Shoot(self):
        if self.shoot_button_flag:
            print('Shoot')
            self.shoot_button_flag = False
            self.Shoot_Button.configure(text='Stop', bg='#F93232', activebackground='#F93232')
            Serial.Transmit_value('F', self.old_Shoot_value)
        else:
            print('Stop')
            self.shoot_button_flag = True
            self.Shoot_Button.configure(text='Shoot', bg='#55E900', activebackground='#55E900')
            Serial.Transmit_value('S')

    def Right(self):
        self.Rotate_Status = 'Right'
        self.Rotate_Calibration_Button.configure(state=tk.NORMAL)
        print('Right', self.old_Rotate_value)
        Serial.Transmit_value('R', self.old_Rotate_value)

    def Left(self):
        self.Rotate_Status = 'Left'
        self.Rotate_Calibration_Button.configure(state=tk.NORMAL)
        print('Left', self.old_Rotate_value)
        Serial.Transmit_value('L', self.old_Rotate_value)

    def Calibration(self):
        if self.Rotate_Status == 'Right':
            print('Calibration Right to Left')
            Serial.Transmit_value('r')
            time.sleep(0.1)
            Serial.Transmit_value('m')
        else:
            print('Calibration Left to Right')
            Serial.Transmit_value('l')
            time.sleep(0.1)
            Serial.Transmit_value('m')
        self.Rotate_Status = 'Stop'

    def Rotate_Stop(self):
        print('Rotate Stop')
        Serial.Transmit_value('m')

    def Up(self):
        print('Up')
        Serial.Transmit_value('U')

    def Down(self):
        print('Down')
        Serial.Transmit_value('D')

    def Raise_Stop(self):
        print('Raise Stop')
        Serial.Transmit_value('k')


class Main:
    def __init__(self):
        # -------- Variable --------
        self.main_window_x = 1230
        self.main_window_y = 540

        # -------- Window Setup --------
        self.main_window = tk.Tk()
        self.main_window.geometry(str(self.main_window_x) + 'x' + str(self.main_window_y))
        self.main_window.resizable(False, False)
        self.main_window.title('Ball Machine')

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
        Version_label = tk.Label(self.main_window, text='Version 1.3  Made By Wade Tsai',
                                 font='Times 11 bold', bg='#818286')
        Version_label.place(x=self.main_window_x - 230, y=self.main_window_y - 25)

        # -------- Tracking Control Plane --------
        self.Frame_Track = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3)
        self.Frame_Track.place(x=1050, y=5)
        self.Canvas_Track = tk.Canvas(self.Frame_Track, width=150, height=100)
        self.Canvas_Track.pack()
        Label_Track = tk.Label(self.main_window, text='Tracking Plane',
                               font=('Times', 14, 'bold'))
        Label_Track.place(x=1055, y=8)

        # -------- Control Plane --------
        control_x, control_y, control_w, control_h = 660, 160, 330, 270
        self.Control_Frame = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3)
        self.Control_Frame.place(x=control_x, y=control_y)
        self.Control_Canvas = tk.Canvas(self.Control_Frame, width=control_w, height=control_h)
        self.Control_Canvas.pack()

        self.Control_2_Frame = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3)
        self.Control_2_Frame.place(x=1020, y=160)
        self.Control_2_Canvas = tk.Canvas(self.Control_2_Frame, width=155, height=270)
        self.Control_2_Canvas.pack()

        Vision.Start_Vision(self.main_window)
        Control.Start_GUI(self.main_window, control_x + 50, control_y + 10)

        # --------- Serial Plane --------
        self.Frame_Serial = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3)
        self.Frame_Serial.place(x=650, y=5)
        self.Canvas_Serail = tk.Canvas(self.Frame_Serial, width=380, height=100)
        self.Canvas_Serail.pack()

        Serial.GUI(self.main_window, 660, 15)

        self.main_window.mainloop()

    def Close_Window(self):
        print('Close Window')
        Vision.Stop_Vision()
        Serial.Disconnect_Serial_Port()
        self.main_window.destroy()


Serial = Serial_System()
Vision = Vision_System()
Control = Control_GUI()
Main()
