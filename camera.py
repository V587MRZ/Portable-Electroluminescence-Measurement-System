from picamera import PiCamera
import time 
import cv2

camera = PiCamera()

camera.capture('/home/portableel/image1.jpg')
print("first pic being taken")
time.sleep(5)
camera.capture('/home/portableel/image2.jpg')
print("second pic being taken")

img1 = cv2.imread('/home/portableel/image1.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('/home/portableel/image2.jpg',cv2.IMREAD_GRAYSCALE)
diff = cv2.absdiff(img1,img2)
cv2.imwrite('/home/portableel/diff.jpg',diff)