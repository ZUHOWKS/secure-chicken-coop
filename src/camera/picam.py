from picamera2 import Picamera2, Preview
import os


def getCamera():
    picam = Picamera2()
    camera_config = picam.create_preview_configuration()
    picam.configure(camera_config)
    return picam


def takeCapture(picam, img):
    try:
        picam.capture_file(os.path.abspath(img))
        return True
    except:
        return False
