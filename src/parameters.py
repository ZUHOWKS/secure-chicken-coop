from datetime import datetime

# File location from secure-chicken-coop/ directory

ia_model_file = "./resources/ia/models/mdl.pkl"
capture_loc = "./resources/camera/captures/latest_capture.jpg"
chicken_test = "./resources/camera/captures/chicken_test.jpg"
logs_loc = "./logs/scc-log-" + str(datetime.today().replace(microsecond=0).isoformat('-')) + ".log"


# SCC Console variable

debug = False
log = True


