
from picamera import PiCamera
import numpy as np
import cv2
# 创建相机对象
camera = PiCamera()

# 设置分辨率

camera.resolution = (512, 512)

# camera.iso = 1000
# camera.shutter_speed = 100000
camera.exposure_mode = 'auto'
# 创建一个numpy数组来保存图像
image = np.empty((camera.resolution[1], camera.resolution[0], 3), dtype=np.uint8)

# 拍摄一张BGR格式的照片
camera.capture(image, 'bgr')

# 将图像存储为文件
cv2.imwrite('image.jpg', image)


