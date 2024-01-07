from ia import chicken_detection as ChickenDetection
from camera import picam as Picam
from parameters import *
import time


print(ia_model_file)
print(capture_loc)

# Constants
model = ChickenDetection.getIAModel(ia_model_file)
pi_camera = Picam.getCamera()

# TODO: Capture image process from the camera
pi_camera.start()

time.sleep(2)
pi_camera.capture_file(capture_loc)
pred = ChickenDetection.predicate(model, capture_loc)

pi_camera.stop()

print(ChickenDetection.isChickenPredicated(pred))
