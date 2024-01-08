from ia import chicken_detection as ChickenDetection
from camera import picam as Picam
from parameters import *
import time
import os


prefix = "SCC-INFO: "


# Main Function
def openCheckingSession(model, capture_loc):
    retry = 0
    chicken_is_present = False
    while not (retry > 5 or chicken_is_present):
        retry += 1
        print(prefix, "Chicken presence verification retry ", str(retry), ".")
        print(prefix, "Taking picture...")
        if Picam.takeCapture(pi_camera, capture_loc):
            pred = ChickenDetection.predicate(model, os.path.abspath(capture_loc))
            chicken_is_present = ChickenDetection.isChickenPredicated(pred)

            if chicken_is_present:
                return chicken_is_present

        else:
            print(prefix, "Can't take picture.")

    return chicken_is_present


# Main Execute
if __name__ == "__main__":
    print("\n\n\n\n\n\n")

    print("##########################################\n"
          "#    #########    ########    ########   #\n"
          "#   ####        ###         ###          #\n"
          "#   ##         ##          ##            #\n"
          "#    #####     ##          ##            #\n"
          "#     #####    ##          ##            #\n"
          "#        ##     ###         ###          #\n"
          "#  #######        ########    ########   #\n"
          "##########################################\n")

    print("Secure Chicken Coop by ZUHOWKS & Majurax")
    print("All right reserved to ZUHOWKS & Majurax to deliver SCC code.")

    time.sleep(1)
    print("\n")
    print(prefix, "Starting Secure Chicken Coop...")
    # Global SCC variable
    model = ChickenDetection.getIAModel(os.path.abspath(ia_model_file))
    pi_camera = Picam.getCamera()
    on_magnets = True
    was_magnet_disabled = False
    try:
        while True:

            movementDetected = True  # TODO: MOVEMENT DETECTION

            if movementDetected:
                print(prefix, "Movement has been detected !")
                print(prefix, "Enabling magnets...")
                on_magnets = True

                # TODO: ACTIVATE MAGNETS IF IT WAS DISABLED
                print(prefix, "Open checking session...")
                print(prefix, "Starting camera...")
                pi_camera.start()
                time.sleep(3)
                print(prefix, "Camera enabled !")

                chickenIsPresent = openCheckingSession(model, capture_loc)
                if chickenIsPresent:
                    print(prefix, "Chicken presence has been detected.")
                    # TODO: STOP MAGNETS
                    on_magnets = False
                    print(prefix, "Disabling Magnets...")
                else:
                    print(prefix, "Any chicken has been detected.")

                print(prefix, "Stopping camera...")
                pi_camera.stop()
                print(prefix, "Checking session has been closed.")
                time.sleep(15)

    except KeyboardInterrupt:
        print(prefix, "Stopping Secure Chicken Coop...")
        try:
            pi_camera.stop()
        except Exception as e:
            print(prefix, "ERROR: ", e)
        print(prefix, "Secure Chicken Coop has been stopped successfully !")
