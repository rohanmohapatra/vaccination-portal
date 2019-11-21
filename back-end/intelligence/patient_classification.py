import pandas as pd
from sklearn.preprocessing import OneHotEncoder

import numpy as np
import keras.utils
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense


enc = OneHotEncoder()
enc.fit([["poor"],["medium"],["complete"]])

df = pd.read_csv("patient_classes2.csv")
df = df.drop(["patient_id", "Unnamed: 0"],axis=1)
data = df[df.columns[:7] ]
X = data.values

labels = df[df.columns[-1]].values

train_labels = [enc.transform([[i]]).toarray()[0].tolist() for i in labels]
print(train_labels)
train_lables = np.array(train_labels)

model = Sequential()
model.add(Dense(10, input_shape = (7,),activation='relu'))
model.add(Dense(20,activation='relu'))
model.add(Dense(3, activation='softmax'))

model.summary()

model.compile(optimizer="adam", loss="categorical_crossentropy",metrics=["accuracy"])
model.fit(X, train_lables, epochs=60)
y = np.array([[1, 5, 4, 4, 0 , 4, 0]])
print(np.argmax(model.predict(y)))

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")