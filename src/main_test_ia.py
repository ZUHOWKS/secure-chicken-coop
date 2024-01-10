from ia import chicken_detection as ChickenDetection
from parameters import ia_model_file, chicken_test
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


    model = ChickenDetection.getIAModel(os.path.abspath(ia_model_file))
    pred = ChickenDetection.predicate(model, os.path.abspath(chicken_test))
