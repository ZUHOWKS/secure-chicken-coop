import RPi.GPIO as GPIO
import time

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

    GPIO.setmode(GPIO.BCM)  # Define pin numeration

    PI_MOTION_CLICK_PIN = 16  # MOVEMENT SENSOR PIN
    GPIO.setup(PI_MOTION_CLICK_PIN, GPIO.IN)

    print("Testing movement sensor...")
    time.sleep(2)

    try:
        while True:
            if GPIO.input(PI_MOTION_CLICK_PIN):
                print("Movement detected!")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Test of the movement senor has been close.")
        GPIO.cleanup()
