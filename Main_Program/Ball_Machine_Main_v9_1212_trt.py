import random
import tkinter as tk
import cv2
import time
from src import Serial_src
from PIL import Image, ImageTk
from utils.yolo_with_plugins import TrtYOLO
import pycuda.autoinit  # This is needed for initializing CUDA driver


# ---------------- Function ----------------
def transform_timer(data_in):
    if data_in >= 10:
        data_send = str(data_in)
    else:
        data_send = '0' + str(data_in)
    return data_send


def convert2relative(bbox, width, height):
    x, y, w, h = bbox
    _height = height
    _width = width
    return x / _width, y / _height, w / _width, h / _height


def convert2original(image, bbox):
    x, y, w, h = bbox
    image_h, image_w, __ = image.shape
    orig_x = int(x * image_w)
    orig_y = int(y * image_h)
    orig_width = int(w * image_w)
    orig_height = int(h * image_h)
    bbox_converted = (orig_x, orig_y, orig_width, orig_height)
    return bbox_converted


class Main_GUI:
    Scroll_value = 250
    Rotate_value = 340
    scale_gap = 70
    CONFIDENCE_THRESHOLD = 0.45
    trt_path = '../Training_Process/Person_Training_yolov4-tiny-L3_288-1115_all/' \
               'Person_Training_yolov4-tiny-L3_288-1115_all.trt'
    weights_path = '../Training_Process/COCO_Data/yolov4-tiny.weights'
    config_path = '../Training_Process/COCO_Data/yolov4-tiny.cfg'
    data_file = '../Training_Process/COCO_Data/inf.data'

    def __init__(self):
        # -------- Variable Define --------
        self.label = None
        self.Mode = 'random'
        self.Degree = 'Medium'
        self.Manual_Training = 'Training'
        self.Training_Flag = False
        self.Rotate_Dir = 'S'
        self.Scroll_Dir = 'S'
        # --------------- Manual UI Variable ---------------
        self.Scroll_Scale = None
        self.Rotate_Scale = None
        self.Rotate_value_label = None
        self.Scroll_value_label = None
        self.Manual_Frame = None
        self.Manual_Canvas = None
        self.turn_right_flag = False
        self.turn_Left_flag = False
        self.Tracking_Flag = False

        # --------------- Mode Select Variable ---------------
        self.Mode_Select_Frame = None
        self.Mode_Select_Canvas = None
        self.Mode_Select_Label = None
        self.Random_Mode_Button = None

        self.old_gap = 1

        # --------------- Random Mode Variable ---------------
        self.Random_mode_init_time = 0
        self.Random_mode_run_time = 0

        # --------------- Tracking Mode Variable ---------------
        self.Tracking_mode_init_time = 0
        self.Tracking_mode_run_time = 0
        self.Tracking_mode_random_time = 0

        # --------------- Timer Variable ---------------
        self.timer_min_data = 0
        self.timer_sec_data = 0

        self.Timing_Frame = None
        self.Timing_Canvas = None
        self.Timing_Label = None
        self.timer_min_label = None
        self.timer_sec_label = None
        self.timer_min_label_2 = None
        self.timer_sec_label_2 = None

        self.invisible_timer = None

        # -------- Serial Setup --------
        self.Serial = Serial_src.Serial_System(False)

        # -------- UI Setup --------
        self.main_window = tk.Tk()
        self.main_window.geometry('1024x600')
        self.main_window.title('Main GUI')
        self.main_window.configure(bg='#579CD8')
        self.main_window.resizable(width=False, height=False)
        # self.main_window.attributes('-fullscreen', True)

        # -------- Open Camera --------
        gst_str = ('v4l2src device=/dev/video{} ! '
                   'video/x-raw, width=(int){}, height=(int){} ! '
                   'videoconvert ! appsink').format(0, 640, 480)
        self.cam = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
        # self.cam = cv2.VideoCapture(0)
        self.Darknet_Setup()

        # -------- UI Layout --------
        # ---------------- Training / Manual Select ----------------
        self.Manual_Button = tk.Button(self.main_window, text='Manual', font=('Times', 20, 'bold'), width=8,
                                       command=self.Manual_mode, bg='#DCDCDC')
        self.Manual_Button.place(x=10, y=500)

        self.Training_Button = tk.Button(self.main_window, text='Training', font=('Times', 20, 'bold'), width=8,
                                         command=self.Training_mode, state=tk.DISABLED, relief=tk.SUNKEN, bg='#646464')
        self.Training_Button.place(x=170, y=500)
        # ---------------- Mode Select ----------------
        if self.Manual_Training == 'Training':
            self.Training_UI()
            self.Manual_Button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#DCDCDC')
            self.Training_Button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#646464')
        else:
            self.Manual_UI()
            self.Manual_Button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#646464')
            self.Training_Button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#DCDCDC')

        # ---------------- Close Window ----------------
        self.Close_button = tk.Button(self.main_window, text='Close', width=8,
                                      bg='#F93232', activebackground='#9A0008',
                                      font=('Times', 14, 'bold'), command=self.Close_Window)
        self.Close_button.place(x=1024 - 110, y=600 - 90)

        # -------- Function --------
        self.Vision()

        self.version_canvas = tk.Canvas(self.main_window, bg='#818286',
                                        width=1024, height=30)
        self.version_canvas.place(x=-2, y=600 - 28)
        Version_label = tk.Label(self.main_window, text='Version 3.1    Made By Wade Tsai',
                                 font='Times 11 bold', bg='#818286')
        Version_label.place(x=1024 - 240, y=600 - 25)

        self.main_window.mainloop()

    def Manual_mode(self):
        if self.Manual_Training == 'Training':
            print('Select Manual')
            self.Manual_Training = 'Manual'
            self.Manual_Button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#646464')
            self.Training_Button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#DCDCDC')
            self.Training_UI_destroy()
            self.Manual_UI()
            self.Tracking_Flag = False

    def Training_mode(self):
        if self.Manual_Training == 'Manual':
            print('Select Training')
            self.Manual_Training = 'Training'
            self.Training_Button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#646464')
            self.Manual_Button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#DCDCDC')
            self.Manual_UI_destroy()
            self.Training_UI()
            self.Degree_Select(self.Degree)
            self.Mode_Select(self.Mode)
            self.Tracking_Flag = False

    def Start_Training(self):
        print('Start Training', self.Mode)
        self.Training_Flag = True

        self.Manual_Button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#646464')
        self.start_training_button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#05880B')
        self.stop_training_button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#D5000B')

        self.Timer_Counting()
        if self.Mode == 'random':
            self.Random_Mode_Button.after(1, self.Random_Mode)
            self.Random_mode_run_time = 0
        elif self.Mode == 'tracking':
            self.Tracking_Mode_Button.after(1, self.Tracking_Mode)
            self.Tracking_mode_run_time = 0

    def Stop_Training(self):
        print('Stop Train', self.Mode)
        self.Training_Flag = False

        self.Manual_Button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#DCDCDC')
        self.start_training_button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#06C700')
        self.stop_training_button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#880505')

    def Timer_Counting(self):
        if self.timer_min_data == 0 and self.timer_sec_data == 0:
            print('Counting Over')
            self.Stop_Training()
        else:
            print('Counting Min:{} Second:{}'.format(self.timer_min_data, self.timer_sec_data))
            if self.timer_min_data > 0:
                if self.timer_sec_data == 0:
                    self.timer_min_data -= 1
                    self.timer_sec_data = 59
                else:
                    self.timer_sec_data -= 1
            else:
                if self.timer_sec_data == 0:
                    self.timer_min_data -= 1
                else:
                    self.timer_sec_data -= 1
            if self.Training_Flag:
                self.start_training_button.after(1000, self.Timer_Counting)
            else:
                self.timer_min_data = 0
                self.timer_sec_data = 0
                print('Counting Stop')
        self.timer_min_label_2.configure(text=transform_timer(self.timer_min_data))
        self.timer_sec_label_2.configure(text=transform_timer(self.timer_sec_data))

    def Mode_Select(self, mode):
        print('Current Mode:', mode)
        if mode == 'random':
            self.Mode = 'random'
            self.Random_Mode_Button.configure(bg='#008397', state=tk.DISABLED, relief=tk.SUNKEN)
            self.Tracking_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL, relief=tk.RAISED)
            self.Avoid_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL, relief=tk.RAISED)
        elif mode == 'tracking':
            self.Mode = 'tracking'
            self.Random_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL, relief=tk.RAISED)
            self.Tracking_Mode_Button.configure(bg='#008397', state=tk.DISABLED, relief=tk.SUNKEN)
            self.Avoid_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL, relief=tk.RAISED)
        else:
            self.Mode = 'avoid'
            self.Random_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL, relief=tk.RAISED)
            self.Tracking_Mode_Button.configure(bg='#00D7E2', state=tk.NORMAL, relief=tk.RAISED)
            self.Avoid_Mode_Button.configure(bg='#008397', state=tk.DISABLED, relief=tk.SUNKEN)

    def Degree_Select(self, degree):
        print('Current Degree:', degree)
        if degree == 'Easy':
            self.Degree = 'Easy'
            self.degree_easy_button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#1B9700')
            self.degree_medium_button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#D4E500')
            self.degree_hard_button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#D60000')
            self.Rotate_value = 340
            self.Scroll_value = 300
        elif degree == 'Medium':
            self.Degree = 'Medium'
            self.degree_easy_button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#2CD100')
            self.degree_medium_button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#949700')
            self.degree_hard_button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#D60000')
            self.Rotate_value = 340
            self.Scroll_value = 400
        else:
            self.Degree = 'Hard'
            self.degree_easy_button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#2CD100')
            self.degree_medium_button.configure(state=tk.NORMAL, relief=tk.RAISED, bg='#D4E500')
            self.degree_hard_button.configure(state=tk.DISABLED, relief=tk.SUNKEN, bg='#970000')
            self.Rotate_value = 340
            self.Scroll_value = 500
        print('Setup Rotate Speed: {} Scroll Speed: {}'.format(self.Rotate_value, self.Scroll_value))

    def Random_Mode(self):
        if self.Random_mode_run_time == 0 and self.Training_Flag:
            if self.Random_mode_init_time == 0:
                self.Random_mode_init_time = time.time()
            elif time.time() - self.Random_mode_init_time > 7:
                self.Random_mode_run_time += 1
                print('Scroll')
                self.Serial.Transmit_value('Scroll', self.Scroll_value)
                print('Rotate Right')
                self.Serial.Transmit_value('Right', self.Rotate_value)
        elif self.Random_mode_run_time == 1 and self.Training_Flag:  # Right Rotate when sensor detect
            if self.Serial.ser.inWaiting() > 0:
                if self.Serial.ser.read() == b'S':
                    print('Stop Rotate')
                    self.Serial.Transmit_value('SRotate')
                    time.sleep(0.01)
                    self.shoot()
                    self.Random_mode_run_time += 1
                    self.Random_mode_init_time = 0
        elif self.Random_mode_run_time == 2 and self.Training_Flag:  # Delay 1 Second
            if self.Random_mode_init_time == 0:
                self.Random_mode_init_time = time.time()
            elif time.time() - self.Random_mode_init_time > 2:  # << delay
                self.Random_mode_init_time = 0
                self.Random_mode_run_time += 1
            else:
                print(time.time() - self.Random_mode_init_time)
        elif self.Random_mode_run_time == 3 and self.Training_Flag:  # Left Rotate 1.5 Second
            if self.Random_mode_init_time == 0:
                self.Random_mode_init_time = time.time()
                print('Rotate Left')
                self.Serial.Transmit_value('Left', 350)
            elif time.time() - self.Random_mode_init_time > 1.5:  # << delay
                print('Stop Rotate')
                self.Serial.Transmit_value('SRotate')
                time.sleep(0.01)
                self.shoot()
                self.Random_mode_init_time = 0
                self.Random_mode_run_time += 1
        elif self.Random_mode_run_time == 4 and self.Training_Flag:  # Delay 2 Second and Left Rotate
            if self.Random_mode_init_time == 0:
                self.Random_mode_init_time = time.time()
            elif time.time() - self.Random_mode_init_time > 2:  # << delay
                print('Rotate Left')
                self.Serial.Transmit_value('Left', 350)
                self.Random_mode_init_time = 0
                self.Random_mode_run_time += 1
            else:
                print(time.time() - self.Random_mode_init_time)
        elif self.Random_mode_run_time == 5 and self.Training_Flag:  # Left Rotate when sensor detect
            if self.Serial.ser.inWaiting() > 0:
                if self.Serial.ser.read() == b'S':
                    print('Stop Rotate')
                    self.Serial.Transmit_value('SRotate')
                    time.sleep(0.01)
                    self.shoot()
                    self.Random_mode_run_time += 1
                    self.Random_mode_init_time = 0
        elif self.Random_mode_run_time == 6 and self.Training_Flag:  # Delay 1 Second
            if self.Random_mode_init_time == 0:
                self.Random_mode_init_time = time.time()
            elif time.time() - self.Random_mode_init_time > 2:  # << delay
                self.Random_mode_init_time = 0
                self.Random_mode_run_time += 1
            else:
                print(time.time() - self.Random_mode_init_time)
        elif self.Random_mode_run_time == 7 and self.Training_Flag:  # Left Rotate 1 Second
            if self.Random_mode_init_time == 0:
                self.Random_mode_init_time = time.time()
                print('Rotate Right')
                self.Serial.Transmit_value('Right', 350)
            elif time.time() - self.Random_mode_init_time > 2:  # << delay
                print('Stop Rotate')
                self.Serial.Transmit_value('SRotate')
                time.sleep(0.01)
                self.shoot()
                self.Random_mode_init_time = 0
                self.Random_mode_run_time += 1
            else:
                print(time.time() - self.Random_mode_init_time)
        elif self.Random_mode_run_time == 8 and self.Training_Flag:  # Delay 1 Second
            if self.Random_mode_init_time == 0:
                self.Random_mode_init_time = time.time()
            elif time.time() - self.Random_mode_init_time > 2:  # << delay
                self.Random_mode_init_time = 0
                self.Random_mode_run_time = 0
            else:
                print(time.time() - self.Random_mode_init_time)

        if not self.Training_Flag:
            self.Serial.Transmit_value('SRotate')
            time.sleep(0.005)
            self.Serial.Transmit_value('Stop')
            time.sleep(0.005)
            self.Serial.Transmit_value('ShSot')
            time.sleep(0.005)
            self.Serial.Transmit_value('Stop')
            time.sleep(0.005)
            self.Random_mode_init_time = 0
            self.Random_Mode_Button.after_cancel(self.Random_Mode)
        else:
            self.Random_Mode_Button.after(1, self.Random_Mode)

    def Tracking_Mode(self):
        if self.Tracking_mode_run_time == 0 and self.Training_Flag:
            print('Start Tracking Mode')
            self.Tracking_Flag = True
            self.Tracking_mode_run_time += 1
            self.Tracking_mode_random_time = random.randint(3, 6)
            print('Scroll')
            self.Serial.Transmit_value('Scroll', self.Scroll_value)
            self.Tracking_mode_init_time = time.time()
        elif self.Tracking_mode_run_time == 1 and self.Training_Flag:
            if time.time() - self.Tracking_mode_init_time > self.Tracking_mode_random_time:
                print('Shot', self.Tracking_mode_random_time)
                self.Serial.Transmit_value('SRotate')
                self.shoot()
                self.Tracking_mode_init_time = time.time()
                self.Tracking_mode_random_time = random.randint(3, 5)

        if not self.Training_Flag:
            print('Stop Shot')
            self.Serial.Transmit_value('SRotate')
            time.sleep(0.005)
            self.Serial.Transmit_value('Stop')
            time.sleep(0.005)
            self.Serial.Transmit_value('ShSot')
            time.sleep(0.005)
            self.Serial.Transmit_value('Stop')
            time.sleep(0.005)
            self.Tracking_Flag = False
            self.Tracking_mode_init_time = 0
        else:
            self.Tracking_Mode_Button.after(1, self.Tracking_Mode)

    def shoot(self):
        self.Serial.Transmit_value('Shot')
        time.sleep(0.01)
        self.Serial.Transmit_value('ShSot')
        time.sleep(0.01)
        self.Serial.Transmit_value('')

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
        if self.Tracking_Flag:
            frame = self.Tracking(frame)
        frame_PIL = Image.fromarray(frame)
        frame_tk = ImageTk.PhotoImage(frame_PIL)
        self.label.image = frame_tk
        self.label.configure(image=frame_tk)
        self.label.after(1, self.Re_Vision)

    def Darknet_Setup(self):
        # -------- Yolov4 Setup --------
        self.center = [int(640) // 2, int(480) // 2]
        self.xy_range = [150, 100]
        with open("./classes.txt", "r") as f:
            self.class_names = [cname.strip() for cname in f.readlines()]

        # Load Network
        # ---- TRT ----
        self.trt_yolo = TrtYOLO(self.trt_path, 1)
        # ---- Darknet ----
        # self.network, self.class_name, class_colors = darknet.load_network(self.config_path,
        #                                                                    self.data_file,
        #                                                                    self.weights_path)
        # self.darknet_width = darknet.network_width(self.network)
        # self.darknet_height = darknet.network_height(self.network)
        # self.darknet_image = darknet.make_image(self.darknet_width, self.darknet_height, 3)

    def Tracking(self, frame):
        point_x, point_y = 0, 0
        x_min, y_min, x_max, y_max = 0, 0, 0, 0
        # ---- TRT ----
        boxes, scores, classes = self.trt_yolo.detect(frame, 0.4)

        # ---- Darknet ----
        # frame_process = frame.copy()
        # frame_resize = cv2.resize(frame_process, (self.darknet_height, self.darknet_height),
        #                           interpolation=cv2.INTER_LINEAR)
        # darknet.copy_image_from_bytes(self.darknet_image, frame_resize.tobytes())
        # detections = darknet.detect_image(self.network, self.class_name, self.darknet_image, 0.5)

        for label, confidence, bbox in zip(classes, scores, boxes):
            if label == 0:   # 'person':
                # ---- trt ----
                label = self.class_names[int(label)]
                x_min, y_min, x_max, y_max = bbox

                # ---- darknet ----
                # relative_bbox = convert2relative(bbox, self.darknet_width, self.darknet_height)
                # new_bbox = convert2original(frame, relative_bbox)
                # x_min = new_bbox[0] - new_bbox[2] // 2
                # y_min = new_bbox[1] - new_bbox[3] // 2
                # x_max = new_bbox[0] + new_bbox[2] // 2
                # y_max = new_bbox[1] + new_bbox[3] // 2

                x_center = (x_max + x_min) // 2
                y_center = (y_max + y_min) // 2
                if (self.center[0] - self.xy_range[0]) <= x_center <= (self.center[0] + self.xy_range[0]):
                    point_x, point_y = x_center, y_center
                    cv2.circle(frame, (x_center, y_center), 5, (0, 255, 0), 5)
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 255, 0), 2)
                    cv2.putText(frame, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

        cv2.line(frame, (320 - self.xy_range[0], 0), (320 - self.xy_range[0], 480), (255, 0, 0), 2)
        cv2.line(frame, (320 + self.xy_range[0], 0), (320 + self.xy_range[0], 480), (255, 0, 0), 2)

        if point_x != 0 and point_y != 0:
            gap = point_x - self.center[0]
            if gap < -self.scale_gap:
                status = 'Right'
                if not self.turn_right_flag:
                    self.turn_right_flag = True
                    self.Serial.Transmit_value('Right', int(self.Rotate_value + (abs(gap) - 80)))
                    print('Turn Right -- {}'.format(int(self.Rotate_value + (abs(gap) - 80))))
                elif (abs(gap) - self.old_gap) / self.old_gap > 0.05:
                    self.old_gap = abs(gap)
                    self.Serial.Transmit_value('Right', int(self.Rotate_value + (abs(gap) - 80) * 5))
                    print('Turn Right -- {}'.format(int(self.Rotate_value + (abs(gap) - 80))))
            elif gap > self.scale_gap:
                status = 'Left'
                if not self.turn_Left_flag:
                    self.turn_Left_flag = True
                    self.Serial.Transmit_value('Left', int(self.Rotate_value + (abs(gap) - 80)))
                    print('Turn Left')
                elif (abs(gap) - self.old_gap) / self.old_gap > 0.05:
                    self.old_gap = abs(gap)
                    self.Serial.Transmit_value('Left', int(self.Rotate_value + (abs(gap) - 80)))
                    print('Turn Left -- {}'.format(int(self.Rotate_value + (abs(gap) - 80))))
            else:
                status = 'Stop'
                if self.turn_Left_flag or self.turn_right_flag:
                    self.turn_Left_flag = False
                    self.turn_right_flag = False
                    self.Serial.Transmit_value('SRotate')
                    print('Stop')
            size = round((x_max - x_min) * (y_max - y_min) / 1000, 1)
            scale = 5
            offset = 40
            cv2.line(frame, (320 - int(size * scale) - offset, y_min),
                     (320 - int(size * scale) - offset, y_max), (0, 0, 255), 2)
            cv2.line(frame, (320 + int(size * scale) + offset, y_min),
                     (320 + int(size * scale) + offset, y_max), (0, 0, 255), 2)
            print('Point-x: {} Point-y: {} - Status: {} Gap: {} Size: {}'.format(point_x, point_y, status, gap, size))
        return frame

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
                                      command=lambda msg='Shot': self.Send_Command(msg))
        self.Shoot_Button.place(x=910, y=218)

        self.Tracking_Test_Button = tk.Button(self.main_window, text='Tracking Test', font=('Times', 16, 'bold'),
                                              width=12, bg='#55E900', activebackground='#55E900',
                                              command=self.Tracking_Test)
        self.Tracking_Test_Button.place(x=670, y=60)

        self.Calibration_Button = tk.Button(self.main_window, text='Calibration', font=('Times', 16, 'bold'),
                                            width=11, bg='#00E088', activebackground='#00E088',
                                            command=lambda msg='Cab': self.Send_Command(msg))
        self.Calibration_Button.place(x=850, y=60)

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
                                            command=lambda mode='random': self.Mode_Select(mode), relief=tk.SUNKEN,
                                            bg='#008397', activebackground='#008397', state=tk.DISABLED)
        self.Random_Mode_Button.place(x=662, y=mode_select_y + 50)

        self.Tracking_Mode_Button = tk.Button(self.main_window, text='Tracking', width=7, font=('Times', 17, 'bold'),
                                              command=lambda mode='tracking': self.Mode_Select(mode), relief=tk.RAISED,
                                              bg='#00D7E2', activebackground='#008397')
        self.Tracking_Mode_Button.place(x=782, y=mode_select_y + 50)

        self.Avoid_Mode_Button = tk.Button(self.main_window, text='Avoid', width=7, font=('Times', 17, 'bold'),
                                           command=lambda mode='avoid': self.Mode_Select(mode), relief=tk.RAISED,
                                           bg='#00D7E2', activebackground='#008397')
        self.Avoid_Mode_Button.place(x=902, y=mode_select_y + 50)

    def Start_Stop_UI(self):
        start_stop_y = 430
        self.start_training_button = tk.Button(self.main_window, text='Start', font=('Times', 24, 'bold'),
                                               width=8, height=1, bg='#06C700', activebackground='#048F00',
                                               command=self.Start_Training)
        self.start_training_button.place(x=660, y=start_stop_y)

        self.stop_training_button = tk.Button(self.main_window, text='Stop', font=('Times', 24, 'bold'),
                                              width=8, height=1, bg='#880505', activebackground='#9A0008',
                                              command=self.Stop_Training, state=tk.DISABLED, relief=tk.SUNKEN)
        self.stop_training_button.place(x=850, y=start_stop_y)

    def Timer_UI(self):
        timing_setup_y = 120
        self.Timing_Frame = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3, bg='#DCDCDC')
        self.Timing_Frame.place(x=655, y=timing_setup_y)
        self.Timing_Canvas = tk.Canvas(self.Timing_Frame, width=355, height=175, bg='#DCDCDC')
        self.Timing_Canvas.pack()
        self.Timing_Label = tk.Label(self.main_window, text='Set Training Time:', bg='#DCDCDC',
                                     font=('Times', 20, 'bold'))
        self.Timing_Label.place(x=660, y=timing_setup_y + 5)

        self.timer_min_label = tk.Label(self.main_window, text='Minute', bg='#DCDCDC',
                                        font=('Times', 18, 'bold'))
        self.timer_min_label.place(x=720, y=timing_setup_y + 50)

        self.timer_sec_label = tk.Label(self.main_window, text='Second', bg='#DCDCDC',
                                        font=('Times', 18, 'bold'))
        self.timer_sec_label.place(x=870, y=timing_setup_y + 50)

        self.timer_min_label_2 = tk.Label(self.main_window, text='00', bg='#DCDCDC',
                                          font=('Times', 22, 'bold'))
        self.timer_min_label_2.place(x=740, y=timing_setup_y + 83)

        colon = tk.Label(self.main_window, text=':', bg='#DCDCDC', font=('Times', 26, 'bold'))
        colon.place(x=825, y=timing_setup_y + 78)

        self.timer_sec_label_2 = tk.Label(self.main_window, text='00', bg='#DCDCDC',
                                          font=('Times', 22, 'bold'))
        self.timer_sec_label_2.place(x=890, y=timing_setup_y + 83)

        self.Timer_Button(1, 700, timing_setup_y + 125)
        self.Timer_Button(2, 850, timing_setup_y + 125)

        if self.invisible_timer is not None:
            self.invisible_timer.destroy()

    def Training_UI(self):
        self.Mode_Select_UI()
        self.Start_Stop_UI()
        self.Timer_UI()

        degree_y = 310
        self.degree_frame = tk.Frame(self.main_window, relief=tk.RAISED, borderwidth=3, bg='#DCDCDC')
        self.degree_frame.place(x=655, y=degree_y)
        self.degree_canvas = tk.Canvas(self.degree_frame, width=355, height=100, bg='#DCDCDC')
        self.degree_canvas.pack()
        self.degree_label = tk.Label(self.main_window, text='Degree of Difficulty', font=('Times', 18, 'bold'),
                                     bg='#DCDCDC')
        self.degree_label.place(x=660, y=degree_y + 7)

        self.degree_hard_button = tk.Button(self.main_window, text='Hard', font=('Times', 16, 'bold'),
                                            width=7, bg='#D60000', activebackground='#970000',
                                            command=lambda degree='Hard': self.Degree_Select(degree))
        self.degree_hard_button.place(x=670, y=degree_y + 50)

        self.degree_medium_button = tk.Button(self.main_window, text='Medium', font=('Times', 16, 'bold'),
                                              width=7, bg='#949700', activebackground='#949700',
                                              command=lambda degree='Medium': self.Degree_Select(degree),
                                              state=tk.DISABLED, relief=tk.SUNKEN)
        self.degree_medium_button.place(x=790, y=degree_y + 50)

        self.degree_easy_button = tk.Button(self.main_window, text='Easy', font=('Times', 16, 'bold'),
                                            width=7, bg='#2CD100', activebackground='#1B9700',
                                            command=lambda degree='Easy': self.Degree_Select(degree))
        self.degree_easy_button.place(x=910, y=degree_y + 50)

    def Training_UI_destroy(self):
        self.Mode_Select_Frame.destroy()
        self.Mode_Select_Canvas.destroy()
        self.Mode_Select_Label.destroy()

        self.Random_Mode_Button.destroy()
        self.Tracking_Mode_Button.destroy()
        self.Avoid_Mode_Button.destroy()

        self.start_training_button.destroy()
        self.stop_training_button.destroy()

        self.Timing_Frame.destroy()
        self.Timing_Canvas.destroy()
        self.Timing_Label.destroy()

        self.timer_min_label.destroy()
        self.timer_sec_label.destroy()

        self.timer_min_label_2.destroy()
        self.timer_sec_label_2.destroy()

        self.invisible_timer = tk.Canvas(self.main_window, bg='#579CD8', width=355, height=50)
        self.invisible_timer.place(x=660, y=240)

    def Send_Command(self, fun):
        if fun == 'Right':
            self.Serial.Transmit_value('SRotate')
            time.sleep(0.001)
            self.Rotate_Dir = 'R'
            print(fun, self.Rotate_Scale.get())
            self.Serial.Transmit_value('Right', int(self.Rotate_Scale.get()))
        elif fun == 'Left':
            self.Serial.Transmit_value('SRotate')
            time.sleep(0.001)
            self.Rotate_Dir = 'L'
            print(fun, self.Rotate_Scale.get())
            self.Serial.Transmit_value('Left', int(self.Rotate_Scale.get()))
        elif fun == 'Scroll':
            print('Scroll', self.Scroll_Scale.get())
            self.Scroll_Dir = 'F'
            self.Scroll_Button.configure(text='Stop', bg='#E91B1B',
                                         command=lambda msg='Stop': self.Send_Command(msg))
            self.Serial.Transmit_value('Scroll', int(self.Scroll_Scale.get()))
        elif fun == 'Stop':
            print('Stop')
            self.Scroll_Dir = 'S'
            self.Scroll_Button.configure(text='Scroll', bg='#55E900',
                                         command=lambda msg='Scroll': self.Send_Command(msg))
            self.Serial.Transmit_value('Stop')
        elif fun == 'SRotate':
            print('Stop Rotate')
            self.Rotate_Dir = 'S'
            self.Serial.Transmit_value('SRotate')
        elif fun == 'Shot':
            print('Shot')
            self.Shoot_Button.configure(text='Stop', bg='#E91B1B',
                                        command=lambda msg='SShot': self.Send_Command(msg))
            self.Serial.Transmit_value('Shot')
        elif fun == 'SShot':
            print('SShot')
            self.Shoot_Button.configure(text='Shoot', bg='#00D3CD',
                                        command=lambda msg='Shot': self.Send_Command(msg))
            self.Serial.Transmit_value('ShSot')
        elif fun == 'Cab':
            print('Calibration')
            self.Serial.Transmit_value('Cab')
            time.sleep(0.01)
            self.Serial.Transmit_value('SRotate')
        else:
            self.Serial.Transmit_value(fun)

    def Tracking_Test(self):
        if self.Tracking_Flag:
            self.Tracking_Flag = False
            self.Tracking_Test_Button.configure(text='Tracking Test', bg='#55E900', activebackground='#55E900')
        else:
            self.Tracking_Flag = True
            self.Tracking_Test_Button.configure(text='Stop Testing', bg='#F93232', activebackground='#F93232')

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

        self.Rotate_value = int(self.Rotate_Scale.get())
        self.Scroll_value = int(self.Scroll_Scale.get())

        self.Scroll_value_label.configure(text='Scroll: {}'.format(self.Scroll_Scale.get()))
        self.Rotate_value_label.configure(text='Rotate: {}'.format(self.Rotate_Scale.get()))
        self.Scroll_Scale.configure(bg=scroll_color_value)
        self.Rotate_Scale.configure(bg=rotate_color_value)

        if self.Rotate_Dir == 'R':
            self.Send_Command('Right')
        elif self.Rotate_Dir == 'L':
            self.Send_Command('Left')
        else:
            self.Send_Command('N')

        if self.Scroll_Dir == 'F':
            self.Send_Command('Scroll')
        else:
            self.Send_Command('N')

    def Timer_Button(self, ch, x, y):
        Add = tk.Button(self.main_window, text='+', bg='#DCDCDC', font=('Times', 18, 'bold'),
                        command=lambda channel=ch: self.Timer_Add(channel), width=2)
        Add.place(x=x, y=y)

        Reduce = tk.Button(self.main_window, text='-', bg='#DCDCDC', font=('Times', 18, 'bold'),
                           command=lambda channel=ch: self.Timer_Reduce(channel), width=2)
        Reduce.place(x=x + 75, y=y)

    def Timer_Add(self, ch):
        if ch == 1:
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
        if ch == 1:
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
        self.main_window.after(1, self.Read_Data)

    def Close_Window(self):
        self.label.after_cancel(self.Re_Vision)
        self.cam.release()
        self.main_window.destroy()


Main_GUI()
