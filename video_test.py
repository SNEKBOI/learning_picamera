# import stuff
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


# conf
res = (320, 240)
#res = (640, 480)


# initialize the camera
camera = PiCamera()
camera.resolution = res 
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=res)

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    image = frame.array
    print(image.shape)
    cv2.imshow("frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord('q'):
        break

