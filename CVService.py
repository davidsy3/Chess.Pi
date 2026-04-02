Skip to content
 
Search Gists
Search...
All gists
Back to GitHub
@gilbertfrancois
gilbertfrancois/pi_camera.py
Last active 4 years ago • Report abuse
Code
Revisions
3
Clone this repository at &lt;script src=&quot;https://gist.github.com/gilbertfrancois/82d18b8531651fe27e875a41409e1096.js&quot;&gt;&lt;/script&gt;
<script src="https://gist.github.com/gilbertfrancois/82d18b8531651fe27e875a41409e1096.js"></script>
Raspberry Pi Camera test with python
pi_camera.py
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

CAMERA_RESOLUTION = (640, 480)

def capture_video():
    # Press 'q' to stop the program.
    try:
        # Setup
        camera = PiCamera()
        camera.resolution = CAMERA_RESOLUTION
        output = PiRGBArray(camera)
        # Update and draw
        is_running = True
        while (is_running):
            camera.capture(output, "bgr", use_video_port=True)
            image = output.array
            output.truncate(0)
            # Display on screen
            cv2.imshow("frame", image)
            # Exit the loop on event
            key = cv2.waitKey(10) & 0xFF
            if key == ord("q"):
                is_running = False
    finally:
        # Release resources
        output.close()
        camera.close()


def capture_still():
    try:
        # Setup
        camera = PiCamera()
        output = PiRGBArray(camera)
        # Capture
        camera.capture(output, format="bgr", use_video_port=False)
        frame = output.array
        # Save the image to disk.
        cv2.imwrite("frame.jpg", frame)
    finally:
        # Release resources
        output.close()
        camera.close()

if __name__ == "__main__":
    # capture_still()
    capture_video()
@davidsy3
Comment
 
Leave a comment
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
