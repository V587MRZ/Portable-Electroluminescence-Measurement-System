import picamera
def camera_preview():
    with picamera.PiCamera() as camera:
        # 设置预览分辨率
        camera.resolution = (640, 480)
        # 打开预览
        camera.start_preview()
        # 延时
        while True:
            if input("Press any key to stop preview..."):
                break
        # 关闭预览
        camera.stop_preview()