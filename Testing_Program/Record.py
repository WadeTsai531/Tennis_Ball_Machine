import cv2
import numpy as np
from PIL import ImageGrab

# gst_str = ('v4l2src device=/dev/video{} ! '
#            'video/x-raw, width=(int){}, height=(int){} ! '
#            'videoconvert ! appsink').format(0, 640, 480)
# cam = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

while True:
    frame = ImageGrab.grab([0, 0, 1920, 1160])
    frame = np.array(frame)[190: 1100, 300: 1210]

    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
out.release()
