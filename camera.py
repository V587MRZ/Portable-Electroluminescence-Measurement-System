from picamera import PiCamera
from picamera.array import PiYUVArray
from time import sleep
import numpy as np
import cv2
import RPi.GPIO as GPIO
from io import BytesIO


def capture_and_diff(
        *shutter_speed, num_photos=50, wait_time=1, resolution=(4056, 3040), iso=100):
    # 读取相机配置
    # camera_preview()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    camera = PiCamera()
    camera.iso = iso
    camera.sensor_mode = 3  # Set sensor mode for 12-bit capture
    camera.resolution = resolution
    camera.framerate = 10
    camera.raw_format = 'yuv'  # Capture YUV data
    # Wait for the automatic gain control to settle
    sleep(2)
    # Now fix the values
    # exposure time
    if not shutter_speed:
        camera.shutter_speed = camera.exposure_speed
    else:
        camera.shutter_speed = int(shutter_speed[0])

    camera.exposure_mode = 'off'
    print(camera.shutter_speed)

    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    # 设置差异图像的累加器
    diff_accumulator = np.zeros(
        (camera.resolution[1], camera.resolution[0]), dtype=np.float32)

    # 拍照并计算差异图像
    for i in range(num_photos):
        # 拍摄第一张照片
        GPIO.output(17, GPIO.HIGH)
        sleep(wait_time)

        # Capture YUV data
        yuv_data = np.empty(
            (camera.resolution[1] * 3 // 2, camera.resolution[0]), dtype=np.uint8)
        camera.capture(yuv_data, format='yuv', use_video_port=False)

        print("the", i, "picture, power off")
        # Convert YUV data to grayscale using cv2.cvtColor
        gray1 = cv2.cvtColor(yuv_data, cv2.COLOR_YUV2GRAY_I420)
        # stream = BytesIO()


        # camera.capture(stream, format='raw')  # Capture RAW data
        # # Convert to numpy array
        # data = np.frombuffer(stream.getvalue(), dtype=np.uint16)
        # # Reshape array to match resolution
        # data = data.reshape((camera.resolution[1], camera.resolution[0]))

        # # Demosaic RAW Bayer data
        # rgb = cv2.cvtColor(data, cv2.COLOR_BayerRG2RGB_EA)

        # # Convert to grayscale
        # gray1 = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('gray1.jpg', gray1)
        # 等待一段时间

        # 拍摄第二张照片
        GPIO.output(17, GPIO.LOW)
        sleep(wait_time)
        camera.capture(yuv_data, format='yuv', use_video_port=False)
        print("the", i, "picture, power on")
        # Convert YUV data to grayscale using cv2.cvtColor
        gray2 = cv2.cvtColor(yuv_data, cv2.COLOR_YUV2GRAY_I420)
        cv2.imwrite('gray2.jpg', gray2)

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

