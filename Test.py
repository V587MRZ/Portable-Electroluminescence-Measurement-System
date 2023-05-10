from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.exposure_mode = 'off'
camera.shutter_speed = 4000000
camera.iso = 800
camera.resolution = (1024,1024)
camera.capture("test1.jpg")
print("off")
sleep(5)

camera.capture("test2.jpg")
camera.close()

# with picamera.PiCamera() as camera:
#     # 设置预览分辨率
#     camera.resolution = (640, 480)
#     # 打开预览
#     camera.start_preview()
#     # 延时
#     while True:
#         pass
