# from io import BytesIO
# from time import sleep
# from picamera import PiCamera
# my_stream = BytesIO()
# camera = PiCamera()
# camera.start_preview()
# sleep(2)
# camera.capture(my_stream,'jpeg')
# from time import sleep
# from picamera import PiCamera
# my_file = open('my_image.jpg','wb')
# camera = PiCamera()
# camera.capture(my_file)
# my_file.close()
# from io import BytesIO
# from time import sleep
# from picamera import PiCamera
# from PIL import Image
# stream = BytesIO()
# camera = PiCamera()
# camera.capture(stream,format = 'jpeg',resize=(500,500))
# stream.seek(0)
# image = Image.open(stream)
# image.show()

# from time import sleep
# from picamera import PiCamera
# camera = PiCamera()
# for filename in camera.capture_continuous('img{counter:03d}.jpg'):
#     print('captured %s' % filename)
#     sleep(10)

# from time import sleep
# from picamera import PiCamera
# camera = PiCamera(resolution = (3280,2464),framerate = 30)
# camera.iso = 100
# sleep(2)
# camera.shutter_speed = camera.exposure_speed
# camera.exposure_mode = 'off'
# g = camera.awb_gains
# camera.awb_mode = 'off'
# camera.awb_gains = g
# camera.capture_sequence(['img%02d.rgb' % i for i in range(10)])
# camera.close()

# from time import sleep
# from picamera import PiCamera
# from datetime import datetime, timedelta
# def wait():
#     next_10s = (datetime.now()+timedelta(seconds=10))
#     delay = (next_10s-datetime.now()).seconds
#     sleep(delay)

# camera = PiCamera()
# camera.start_preview()
# wait()
# for filename in camera.capture_continuous('img{timestamp:%y-%m-%d-%H-%M-%S}.jpg'):
#     wait()
# from picamera import PiCamera
# from time import sleep
# from fractions import Fraction

# camera = PiCamera(resolution = (1920,1080),framerate=Fraction(1,6),sensor_mode=3)
# camera.shutter_speed = 10000000
# camera.iso = 800
# sleep(10)
# camera.exposure_mode = 'off'
# camera.capture('dark.jpg')

import time 
import picamera
import numpy as np
import cv2
with picamera.PiCamera() as camera:
    camera.resolution = (1920,1080)
    camera.framerate = 51
    time.sleep(1)
    output = np.empty((1920,1080,3),dtype = np.uint8)
    camera.capture(output,'rgb')
cv2.imshow('image',output)
cv2.waitKey(0)