
from picamera import PiCamera
from time import sleep
import numpy as np
import cv2
import RPi.GPIO as GPIO
from io import BytesIO


class Camera_class:
    def __init__(self, shutter_speed, num_photos, wait_time, iso, resolution, gain):
        self.num_photos = num_photos
        self.wait_time = wait_time
        self.resolution = resolution
        self.iso = iso
        self.camera = PiCamera()
        self.camera.exposure_mode = 'off'
        self.camera.shutter_speed = shutter_speed
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = gain
        self.capture_and_diff()

    def capture_and_diff(self):
        # 读取相机配置
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        # 设置差异图像的累加器
        diff_accumulator = np.zeros(
            (self.camera.resolution[1], self.camera.resolution[0]), dtype=np.float32)

        # 拍照并计算差异图像
        for i in range(self.num_photos):
            # 拍摄第一张照片
            GPIO.output(17, GPIO.HIGH)
            print("wait", self.wait_time, "seconds to power on")
            sleep(self.wait_time)
``
            stream = BytesIO()
            self.camera.capture(stream, format='raw', bayer=True)
            stream.seek(0)
            data = stream.getvalue()
            print(data)
            print(len(data))
            width = self.resolution[0]
            height = self.resolution[1]
            img = np.frombuffer(data, dtype=np.uint16).reshape(
                height, width)
            gray1 = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2GRAY)

            print("the", i, "picture")
            print("wait the camera exposure")
            # 等待一段时间
            sleep(self.camera.shutter_speed / 1000000)

            # 拍摄第二张照片
            GPIO.output(17, GPIO.LOW)
            print("wait", self.wait_time, "seconds")
            sleep(self.wait_time)
            stream = BytesIO()
            self.camera.capture(stream, format='raw', bayer=True)
            stream.seek(0)
            data = stream.getvalue()

            width = self.resolution[0]
            height = self.resolution[1]
            img = np.frombuffer(data, dtype=np.uint16).reshape(
                height, width)
            gray2 = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2GRAY)
            print("the", i, "picture, power on")
            print("wait the camera exposure")
            sleep(self.camera.shutter_speed / 1000000)

            # 计算两张照片的差异图像
            diff_image = cv2.absdiff(gray1, gray2)

            # 将差异图像叠加到累加
