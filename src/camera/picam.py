from picamera2 import Picamera2, Preview


def getCamera():
    picam = Picamera2()
    camera_config = picam.create_preview_configuration()
    picam.configure(camera_config)
    return picam
