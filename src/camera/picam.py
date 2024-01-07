from picamera2 import Picamera2, Preview
import os


def getCamera():
    prefix = "SCC-INFO: "

    print(prefix, "Configuration of the camera...")
    picam = Picamera2()
    print(prefix, "Applying preview configuration...")
    camera_config = picam.create_preview_configuration()
    picam.configure(camera_config)
    print(prefix, "Camera has been configured successfully")
    return picam


def takeCapture(picam, img):
    try:
        picam.capture_file(os.path.abspath(img))
        return True
    except Exception as e:
        print("Error: ", e)
        return False
