import pickle
from logger import scc_logger as SCCLogger


def getIAModel(src):

    assert isinstance(src, str)
    SCCLogger.debug("Getting Chicken Detection model...")
    try:
        model = pickle.load(open(src, 'rb'))
        SCCLogger.debug("Model has been gotten.")
        return model
    except Exception as e:
        SCCLogger.error("Can't get IA Model")
        SCCLogger.error(str(e))
    return None


def predicate(model, img):
    assert isinstance(img, str)
    SCCLogger.debug("Predicating image...")
    try:
        pred = (model.predict(img, confidence=40, overlap=30).json())['predictions']
        SCCLogger.debug("Predicated successfully")
        return pred

    except Exception as e:
        SCCLogger.error("Prediction has been failed.")
        SCCLogger.error(str(e))

    return None


def isChickenPredicated(pred):
    SCCLogger.debug("Checking chicken prediction...")
    if len(pred) != 0:
        for i in range(len(pred)):
            if pred[i]['class'] == 'rooster' and pred[i]['confidence'] > 0.6:  # 60% needed to predicate a chicken
                SCCLogger.debug("Chicken has been predicated.")
                return True
    SCCLogger.debug("No chicken has been predicated.")
    return False
