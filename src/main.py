from ia import chicken_detection as ChickenDetection
from camera import picam as Picam
import parameters
from gpio import pigpio as PiGPIO
from logger import scc_logger as SCCLogger
import time
import os
import sys


# Main Function
def openCheckingSession(model, capture_loc):
    retry = 0
    chicken_is_present = False
    while retry < 5 and not chicken_is_present:
        retry += 1
        SCCLogger.debug("Chicken presence verification retry " + str(retry) + ".")

        if Picam.takeCapture(pi_camera, capture_loc):
            pred = ChickenDetection.predicate(model, os.path.abspath(capture_loc))
            chicken_is_present = ChickenDetection.isChickenPredicated(pred)

    SCCLogger.debug("Chicken presence verification finished.")
    return chicken_is_present


# Main Execute
if __name__ == "__main__":
    SCCLogger.setupSCCLogger(os.path.abspath(parameters.logs_loc), debug=parameters.debug)
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

    SCCLogger.info("Secure Chicken Coop by ZUHOWKS & Majurax")
    SCCLogger.info("All right reserved to ZUHOWKS & Majurax to deliver SCC code.")

    time.sleep(1)

    print("\n")

    for commandParam in sys.argv[1:]:
        if commandParam == "-debug":
            debug = True

    if parameters.debug:
        SCCLogger.debug("Debugger mod has been enabled.")

    if not parameters.log:
        SCCLogger.info("Logs has been disabled.")

    SCCLogger.info("Starting Secure Chicken Coop...")

    # Global SCC variable
    model = ChickenDetection.getIAModel(os.path.abspath(parameters.ia_model_file).replace(":", "-"))
    pi_camera = Picam.getCamera()

    SCCLogger.info("Setup GPIO Raspberry Pi...")
    PiGPIO.setup()

    try:
        while True:

            movementDetected = PiGPIO.getMotionSensorInput()

            if movementDetected:
                SCCLogger.info("Movement has been detected !")
                SCCLogger.info("Enabling magnets...")

                if not PiGPIO.isMagnetOn():
                    PiGPIO.activateMagnet()

                SCCLogger.info("Open checking session...")
                SCCLogger.info("Starting camera...")
                pi_camera.start()

                time.sleep(3)
                SCCLogger.info("Camera enabled !")

                chickenIsPresent = openCheckingSession(model, parameters.capture_loc)
                if chickenIsPresent:
                    SCCLogger.info("Chicken presence has been detected.")
                    if PiGPIO.isMagnetOn():
                        PiGPIO.disableMagnet()

                    SCCLogger.info("Disabling Magnets...")
                else:
                    SCCLogger.info("Any chicken has been detected.")

                SCCLogger.info("Stopping camera...")
                pi_camera.stop()
                SCCLogger.info("Checking session has been closed.")
                time.sleep(15)

            else:
                PiGPIO.disableMagnet()

    except KeyboardInterrupt:
        SCCLogger.info("Stopping Secure Chicken Coop...")
        try:
            SCCLogger.info("Stopping camera...")
            pi_camera.stop()
        except Exception as e:
            SCCLogger.fatal(e)
        SCCLogger.info("Clean GPIO Raspberry Pi...")
        PiGPIO.clean()
        SCCLogger.info("Secure Chicken Coop has been stopped successfully !")
