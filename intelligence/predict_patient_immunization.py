import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json


def get_prediction(listOfVaccine):
    labels = ["poor","medium","complete"]
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("model.h5")
    print("Loaded model from disk")
    y = np.array([listOfVaccine])
    label = np.argmax(model.predict(y))
    return labels[label]

