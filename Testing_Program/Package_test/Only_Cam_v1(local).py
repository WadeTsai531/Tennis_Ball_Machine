import cv2

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
