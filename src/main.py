from ia import chicken_detection as ChickenDetection
from camera import picam as Picam
from parameters import *
import time
import os

# Constants
model = ChickenDetection.getIAModel(os.path.abspath(ia_model_file))
pi_camera = Picam.getCamera()
on_magnets = True
was_magnet_disabled = False


# Main Function
def checkChickenPresence(model, capture_loc):
    retry = 0
    chicken_is_present = False
    while not (retry > 5 or chicken_is_present):
        retry += 1
        pred = ChickenDetection.predicate(model, os.path.abspath(capture_loc))
        chicken_is_present = ChickenDetection.isChickenPredicated(pred)

        if not chicken_is_present:
            time.sleep(0.25)

    return chicken_is_present


# Main Execute
if __name__ == "__main__":
    while True:

        movementDetected = True  # TODO: MOVEMENT DETECTION

        if movementDetected:
            on_magnets = True
            # TODO: ACTIVATE MAGNETS IF DISABLED

            pi_camera.start()
            time.sleep(2)

            if Picam.takeCapture(pi_camera, capture_loc):
                chickenIsPresent = checkChickenPresence(model, capture_loc)
                if chickenIsPresent:
                    # TODO: STOP MAGNETS
                    on_magnets = False
                    print("SCC-INFO: Disable Magnets...")

            pi_camera.stop()

            time.sleep(10)
