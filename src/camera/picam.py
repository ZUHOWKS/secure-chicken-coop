from picamera2 import Picamera2, Preview
from src.logger import scc_logger as SCCLogger
import os


def getCamera():

    SCCLogger.debug("Configuration of the camera...")
    picam = Picamera2()
    
    SCCLogger.debug("Applying preview configuration...")
    camera_config = picam.create_preview_configuration()
    
    picam.configure(camera_config)
    SCCLogger.debug("Camera has been configured successfully.")
    
    return picam


def takeCapture(picam, img):
    try:
        SCCLogger.debug("Capturing image...")
        picam.capture_file(os.path.abspath(img))
        SCCLogger.debug("Capture has been taken successfully.")
        return True
    except Exception as e:
        SCCLogger.fatal("Capture has been not taken.")
        SCCLogger.fatal(str(e))
        return False
