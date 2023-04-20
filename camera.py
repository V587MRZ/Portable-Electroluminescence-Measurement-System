from picamera import PiCamera
from time import sleep
import numpy as np
import cv2
import RPi.GPIO as GPIO


def capture_and_diff(
        *shutter_speed, num_photos=50, resolution=(1024, 1024), iso=800, wait_time=1, ):
    # 读取相机配置
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    camera = PiCamera()
    camera.iso = iso
    camera.resolution = resolution
    # Wait for the automatic gain control to settle
    sleep(2)
    # Now fix the values
    if not shutter_speed:
        camera.shutter_speed = camera.exposure_speed
    else:
        camera.shutter_speed = int(shutter_speed[0])
    camera.exposure_mode = 'off'
    print(camera.shutter_speed)
     

    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    print(g)
    # 设置差异图像的累加器
    diff_accumulator = np.zeros(
        (camera.resolution[1], camera.resolution[0]), dtype=np.float32)

    # 拍照并计算差异图像
    for i in range(num_photos):
        # 拍摄第一张照片
        GPIO.output(17, GPIO.HIGH)
        sleep(wait_time)
        prev_image = np.empty(
            (camera.resolution[1], camera.resolution[0], 3), dtype=np.uint8)
        camera.capture(prev_image, format='bgr')
        gray1 = cv2.cvtColor(prev_image, cv2.COLOR_BGR2GRAY)
        print("the", i, "picture, power off")
        # 等待一段时间
        sleep(wait_time)

        # 拍摄第二张照片
        GPIO.output(17, GPIO.LOW)
        sleep(wait_time)
        current_image = np.empty(
            (camera.resolution[1], camera.resolution[0], 3), dtype=np.uint8)
        camera.capture(current_image, format='bgr')
        gray2 = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
        print("the", i, "picture, power on")
        sleep(wait_time)
        # 计算两张照片的差异图像
        diff_image = cv2.absdiff(gray1, gray2)

        # 将差异图像叠加到累加器中
        diff_accumulator += diff_image.astype(np.float32)

    # 计算平均差异图像
    average_diff_image = (diff_accumulator / num_photos).astype(np.uint8)
    cv2.imwrite("average_diff_image.jpg", average_diff_image)

    # 在屏幕上显示图像
    # cv2.imshow("Average Diff Image", average_diff_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # average_diff_image[average_diff_image < 5] = 0
    # return average_diff_image

    # for tkinter only
    camera.close()

