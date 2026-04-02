from picamzero import Camera
from time import sleep

cam = Camera()
cam.preview_size = (400, 240)
cam.start_preview()
sleep(20)
