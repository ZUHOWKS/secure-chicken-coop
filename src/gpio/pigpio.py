import RPi.GPIO as GPIO
import time
from src.logger import scc_logger as SCCLogger

PI_MOTION_CLICK_PIN = 22  # MOVEMENT SENSOR PIN
PI_MAGNET_PIN = 17  # MOVEMENT SENSOR PIN

is_magnet_on = False


def setup():
    SCCLogger.debug("Setting GPIO mode...")
    GPIO.setmode(GPIO.BCM)  # Define pin numeration

    SCCLogger.debug("Setup GPIO pin attribution...")
    GPIO.setup(PI_MOTION_CLICK_PIN, GPIO.IN)
    GPIO.setup(PI_MAGNET_PIN, GPIO.OUT)

    global is_magnet_on
    is_magnet_on = False


def getMotionSensorInput():
    retry = 0
    movement_detected = False
    while retry < 5 and not movement_detected:
        retry += 1
        movement_detected = GPIO.input(PI_MOTION_CLICK_PIN)
        time.sleep(1)

    return movement_detected


def activateMagnet():
    SCCLogger.debug("Changing magnet to HIGH...")
    GPIO.output(PI_MAGNET_PIN, GPIO.HIGH)

    global is_magnet_on
    is_magnet_on = True
    SCCLogger.debug("Magnet activated.")


def disableMagnet():
    SCCLogger.debug("Changing magnet to LOW...")
    GPIO.output(PI_MAGNET_PIN, GPIO.LOW)

    global is_magnet_on
    is_magnet_on = False
    SCCLogger.debug("Magnet disabled.")


def isMagnetOn():
    SCCLogger.debug("Checking magnet value")
    global is_magnet_on
    return is_magnet_on


def clean():
    SCCLogger.debug("Disabling magnet...")
    global is_magnet_on
    disableMagnet()

    SCCLogger.debug("Cleaning GPIO...")
    GPIO.cleanup()
    SCCLogger.debug("GPIO has been cleaned.")
