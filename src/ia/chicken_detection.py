import pickle


def getIAModel(src):
    assert isinstance(src, str)
    return pickle.load(open(src, 'rb'))


def predicate(model, img):
    assert isinstance(img, str)
    return (model.predict(img, confidence=40, overlap=30).json())['predictions']


def isChickenPredicated(pred):
    if len(pred) != 0:
        for i in range(len(pred)):
            if pred[i]['class'] == 'rooster' and pred[i]['confidence'] > 0.6:  # 60% needed to predicate a chicken
                return True
    return False
