
from __future__ import print_function

import pandas as pd
from pandas import Series,DataFrame

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np
import matplotlib.pyplot as plt

import keras
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras.optimizers import Adam

air = pd.read_csv("air.csv",sep=";",header=0)

x = DataFrame(air.drop("C6H6(GT)",axis=1))

y = DataFrame(air["C6H6(GT)"])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=5)

x_train = x_train.astype(np.float)
x_test = x_test.astype(np.float)

y_train = keras.utils.to_categorical(y_train,10)
y_test = keras.utils.to_categorical(y_test,10)

model = Sequential()

model.add(Dense(50, activation='relu', input_shape=(11,)))
model.add(Dropout(0.2))

model.add(Dense(50, activation='relu', input_shape=(11,)))
model.add(Dropout(0.2))

model.add(Dense(50, activation='relu', input_shape=(11,)))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))

model.summary()
print("\n")

model.compile(loss='mean_squared_error',optimizer=RMSprop(),metrics=['accuracy'])
history = model.fit(x_train, y_train,batch_size=200,epochs=1000,verbose=1,validation_data=(x_test, y_test))
score = model.evaluate(x_test,y_test,verbose=1)

print("\n")
print("Test loss:",score[0])
print("Test accuracy:",score[1])

sample = [11.9, 9.4, 9.0]
print("\n")