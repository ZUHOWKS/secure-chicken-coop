import RPi.GPIO as GPIO
import time

PI_MOTION_CLICK_PIN = 22  # MOVEMENT SENSOR PIN
PI_MAGNET_PIN = 17  # MOVEMENT SENSOR PIN

is_magnet_on = False

def setup(debug=False):
    GPIO.setmode(GPIO.BCM)  # Define pin numeration

    GPIO.setup(PI_MOTION_CLICK_PIN, GPIO.IN)
    GPIO.setup(PI_MAGNET_PIN, GPIO.OUT)

    is_magnet_on = False


def getMotionSensorInput(debug=False):
    retry = 0
    movement_detected = False
    while retry < 5 and not movement_detected:
        retry += 1
        movement_detected = GPIO.input(PI_MOTION_CLICK_PIN)
        time.sleep(1)

    return movement_detected


def activateMagnet(debug=False):
    GPIO.output(PI_MAGNET_PIN, GPIO.HIGH)
    is_magnet_on = True


def disableMagnet(debug=False):
    GPIO.output(PI_MAGNET_PIN, GPIO.LOW)
    is_magnet_on = False

def isMagnetOn():
    return is_magnet_on

def clean(debug=False):
    disableMagnet(debug)
    GPIO.cleanup()
