from picamera import PiCamera
from picamera.array import PiYUVArray
from time import sleep
import numpy as np
import cv2
import RPi.GPIO as GPIO



def capture_and_diff(
        *shutter_speed, num_photos=10, wait_time=1, resolution=(1024, 1024), iso=100):
    # 读取相机配置
    # camera_preview()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(7,GPIO.OUT)
    camera = PiCamera()
    camera.iso = iso

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
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        sleep(wait_time)

        # Capture YUV data
        yuv_data = np.empty(
            (camera.resolution[1] * 3 // 2, camera.resolution[0]), dtype=np.uint8)
        camera.capture(yuv_data, format='yuv')
        print("the", i, "picture, power off")
        # # Convert YUV data to grayscale using cv2.cvtColor
        # rgb_data = cv2.cvtColor(yuv_data, cv2.COLOR_YUV2RGB_I420)
        # Save the RGB image
        # cv2.imwrite('image.jpg', rgb_data)
        gray1 = cv2.cvtColor(yuv_data, cv2.COLOR_YUV2GRAY_I420)
        cv2.imwrite('gray1.png', gray1)

        # stream = BytesIO()
        # camera.capture(stream, format='raw', bayer=True)
        # stream.seek(0)
        # data = stream.getvalue()

        # width = resolution[0]
        # height = resolution[1]
        # img = np.frombuffer(data, dtype=np.uint16).reshape(
        #     height, width)
        # gray1 = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2GRAY)
        # cv2.imwrite('gray1.png', gray1)
        # # 拍摄第二张照片
        GPIO.output(17, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        sleep(wait_time)
        camera.capture(yuv_data, format='yuv')
        print("the", i, "picture, power on")
        # Convert YUV data to grayscale using cv2.cvtColor
        gray2 = cv2.cvtColor(yuv_data, cv2.COLOR_YUV2GRAY_I420)
        cv2.imwrite('gray2.png', gray2)
        # stream = BytesIO()
        # camera.capture(stream, format='raw')  # Capture RAW data
        # # Convert to numpy array
        # data = np.frombuffer(stream.getvalue(), dtype=np.uint16)
        # # Reshape array to match resolution
        # data = data.reshape((camera.resolution[1], camera.resolution[0]))

        # # Demosaic RAW Bayer data
        # rgb = cv2.cvtColor(data, cv2.COLOR_BayerRG2RGB_EA)

        # # Convert to grayscale
        # gray2 = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
        # cv2.imwrite('gray1.png', gray1)
        # 计算两张照片的差异图像
        diff_image = cv2.absdiff(gray1, gray2)

        # 将差异图像叠加到累加器中
        diff_accumulator += diff_image.astype(np.float32)
    # 计算平均差异图像
    # scale = math.floor(255/np.max(diff_accumulator))
    # diff_accumulator = diff_accumulator * scale
    average_diff_image = (diff_accumulator / num_photos).astype(np.uint8)
    cv2.imwrite("average_diff_image.png", average_diff_image)

    # 在屏幕上显示图像
    # cv2.imshow("Average Diff Image", average_diff_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # average_diff_image[average_diff_image < 5] = 0
    # return average_diff_image

    # for tkinter only
    camera.close()
