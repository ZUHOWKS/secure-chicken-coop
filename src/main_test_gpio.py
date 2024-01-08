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

    PI_MOTION_CLICK_PIN = 22  # MOVEMENT SENSOR PIN
    PI_MAGNET_PIN = 17  # MOVEMENT SENSOR PIN

    GPIO.setup(PI_MOTION_CLICK_PIN, GPIO.IN)
    GPIO.setup(PI_MOTION_CLICK_PIN, GPIO.OUT)

    print("Testing movement sensor...")
    time.sleep(2)

    try:
        print("Enabling magnet...")
        GPIO.output(17, GPIO.HIGH)
        print("Enabling was enabled")
        while True:
            if GPIO.input(PI_MOTION_CLICK_PIN):
                print("Movement detected!")
            time.sleep(1)



    except KeyboardInterrupt:
        print("Stopping magnet...")
        GPIO.output(17, GPIO.LOW)
        print("Magnet has been disabled.")
        time.sleep(2)
        print("Test of the movement senor has been close.")
        GPIO.cleanup()
