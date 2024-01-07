from camera import picam as Picam
from parameters import capture_loc
import time
import os

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
except:
    captured = False

pi_camera.stop()

print('Picture taken ? ', captured)
