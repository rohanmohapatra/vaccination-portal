import numpy as np
from keras.models import model_from_json
from keras import backend as K


def get_prediction(listOfVaccine):
    labels = ["poor","medium","complete"]
    # load json and create model
    json_file = open('/home/rohan/Desktop/Semester7/WebTechnologies2/Project/vaccination-portal/back-end/intelligence/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    K.clear_session()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("/home/rohan/Desktop/Semester7/WebTechnologies2/Project/vaccination-portal/back-end/intelligence/model.h5")
    print("Loaded model from disk")
    model._make_predict_function()
    print(listOfVaccine)
    y = np.array([listOfVaccine])
    prediction = model.predict(y)
    print(prediction)
    label = np.argmax(prediction)
    print(label)
    K.clear_session()
    return labels[label]

