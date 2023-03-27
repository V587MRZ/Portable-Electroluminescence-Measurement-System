from picamera import PiCamera
from time import sleep
import numpy as np
import cv2
camera = PiCamera()
camera.resolution = (512,512)
width, height = camera.resolution
for i in range(5):
    
    prev_image = np.empty((height, width, 3), dtype=np.uint8)
    # 捕获第一张图像 capture the first img
    camera.capture(prev_image,format='bgr')
    gray1 = cv2.cvtColor(prev_image, cv2.COLOR_BGR2GRAY)
    # 等待10秒钟 wait for 10s
    sleep(10)
    current_image = np.empty((height, width, 3), dtype=np.uint8)
    # 捕获第二张图像 capture the second img
    camera.capture(current_image, format='bgr')
    gray2 = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)

    # 计算两个图像的差异 diffenet img
    diff_image = cv2.absdiff(gray1, gray2)
    cv2.imshow('Difference Image%02d' % i, diff_image)
    cv2.waitKey(1000)
#cv2.destroyAllWindows()


