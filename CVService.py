from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
# Configure the camera
config = picam2.create_preview_configuration()
picam2.configure(config)
picam2.start()

# Start the preview window
picam2.start_preview()

try:
    while True:
        time.sleep(1) # Keeps the script running to hold the window
except KeyboardInterrupt:
    pass
finally:
    picam2.stop()
