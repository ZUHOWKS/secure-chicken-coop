from camera import picam as Picam
from parameters import capture_loc
import time
import os


if __name__ == "__main__":

    print("##########################################\n"
          "#    #########    ########    ########   #\n"
          "#   ####        ###         ###          #\n"
          "#   ##         ##          ##            #\n"
          "#    #####     ##          ##            #\n"
          "#     #####    ##          ##            #\n"
          "#        ##     ###         ###          #\n"
          "#  #######        ########    ########   #\n"
          "##########################################\n")

    pi_camera = Picam.getCamera()

    pi_camera.start()

    time.sleep(2)

    try:
        pi_camera.capture_file(os.path.abspath(capture_loc))
        captured = True
    except Exception as e:
        print("Error: ", e)
        captured = False

    pi_camera.stop()
    print('Picture taken ? ', captured)
