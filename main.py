from Camera import capture_and_diff
if __name__ == '__main__':
    mode = input("auto mode or manual mode: ")
    if mode == "auto":
        wait = int(input("input waiting time: "))
        iso = int(input("input iso (0 ~ 800): "))
        capture_and_diff(wait_time=wait, iso=iso)

    else:
        num = input("input the number of samples: ")
        num = 50 if num == "" else int(num)
        iso = input("input iso (0 ~ 800): ")
        iso = 800 if iso == "" else int(iso)
        wait = input("input waiting time(s): ")
        wait = 1 if wait == "" else int(wait)
        res = input("resolution(512,512): ")
        res = (512,512) if res== "" else eval(res)
        speed = input("input shutter_speed(us): ")
        if speed == "":
            capture_and_diff(
                num_photos=num, iso=iso, wait_time=wait, resolution=res)
        else:
            capture_and_diff(
                int(speed), num_photos=num, iso=iso, wait_time=wait, resolution=res)
