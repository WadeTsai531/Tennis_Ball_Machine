import darknet
import cv2
import time


def convert2relative(bbox, width, height):
    """
    YOLO format use relative coordinates for annotation
    """
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


config_path = '../Training_Process/Person_Training-yolov4_tiny_288-1214-coco/' \
              'Person_Training-yolov4_tiny_288-1214-coco.cfg'
weights_path = '../Training_Process/Person_Training-yolov4_tiny_288-1214-coco/weights/' \
               'Person_Training-yolov4_tiny_288-1214-coco_final.weights'
data_file = '../Training_Process/Person_Training-yolov4_tiny_288-1214-coco/inf.data'

# Load Network
network, class_name, class_colors = darknet.load_network(config_path, data_file, weights_path)
width = darknet.network_width(network)
height = darknet.network_height(network)
darknet_image = darknet.make_image(width, height, 3)

video_path = '../Videos/Video_from_Web/test_v2.mp4'
video = cv2.VideoCapture(0)
video_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
video_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    ret, frame = video.read()
    if not ret:
        print('Video Over')
        break
    frame_origin = frame.copy()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resize = cv2.resize(frame_rgb, (width, height), interpolation=cv2.INTER_LINEAR)
    darknet.copy_image_from_bytes(darknet_image, frame_resize.tobytes())
    start_time = time.time()
    detections = darknet.detect_image(network, class_name, darknet_image, 0.6)
    stop_time = time.time()

    for label, confidence, bbox in detections:
        relative_bbox = convert2relative(bbox, width, height)
        new_bbox = convert2original(frame_origin, relative_bbox)
        print('Label: {} Confidence: {} bbox: {}'.format(label, confidence, new_bbox))
        color = class_colors[label]
        label = "{} : {}%".format(label, float(confidence))
        cv2.rectangle(frame_origin,
                      (new_bbox[0] - new_bbox[2] // 2, new_bbox[1] - new_bbox[3] // 2),
                      (new_bbox[0] + new_bbox[2] // 2, new_bbox[1] + new_bbox[3] // 2), color, 2)
        cv2.putText(frame_origin, label, (new_bbox[0] - new_bbox[2] // 2, new_bbox[1] - new_bbox[3] // 2 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    cv2.putText(frame_origin, "FPS: %.2f" % (1 / (stop_time - start_time)),
                (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('frame', frame_origin)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
