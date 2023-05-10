from camera_class import Camera_class
from picamera import PiCamera
from time import sleep
if __name__ == '__main__':
    print("Calibration process wait 2s")
    
    camera = PiCamera()
    sleep(2)
    resolution = camera.resolution
    iso = camera.iso
    speed = camera.exposure_speed
    light_gain = camera.awb_gains
    num = input("input the number of samples: ")
    num = 50 if num == "" else int(num)
    wait = input("input waiting time(s): ")
    wait = 1 if wait == "" else int(wait)
    print("resolution: ",resolution)
    print("iso: ", iso)
    print("speed: ", speed)
    print("light_gain: ",light_gain)
    camera.close()
    mode = input("done, please select auto mode or manual mode: ")

    if mode == "auto":
        # wait = int(input("input waiting time: "))
        # iso = int(input("input iso (0 ~ 800): "))
        Camera_class(shutter_speed=speed,
                     num_photos=num,
                     iso=iso,
                     resolution=resolution,
                     wait_time=wait,
                     gain = light_gain)

    else:

        iso = input("input iso (0 ~ 800): ")
        iso = 800 if iso == "" else int(iso)
        res = input("max resolution(4272,2848): ")
        res = (512, 512) if res == "" else eval(res)
        speed = input("input shutter_speed(us) max 35000: ")
        Camera_class(shutter_speed=int(speed),
                     num_photos=num,
                     iso=iso,
                     resolution=res,
                     wait_time=wait,
                     gain = light_gain)
