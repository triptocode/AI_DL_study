# -*- coding: utf-8 -*-
"""exam05_heart_disease_predict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zxpW3BxWOTP7dFVluQqNs5OZPSP5WH9u
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

"""age : 나이

sex : 성별

cp : 가슴 통증 종류

treshbps : 안정시 혈압

chol : 콜레스테롤

fbs : 공복시 혈당 (1:120초과,2:120이하)

restecg : 안정시 심전도 0:normal, 1:ST-T파 이상, 2:좌심실 비대

thalach : 최대 심박수

exang : 운동 유발 협심증 1:yes, 0:no

oldpeak : ST depression induced by exercise relative to rest

slope : the slope of the peak exercise ST segment 1:upsloping, 2:flat, 3:downsloping

ca : 조영제에 착색된 혈관수

thal : 3:normal, 6:고정 결함, 7:가역적 결함

HeartDisease : 심장병 유무
"""

column_name = ['age', 'sex', 'cp', 'treshbps', 'chol', 'fbs', 'restecg',
               'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal',
               'HeartDisease']
raw_data = pd.read_excel('/content/datasets/heart-disease.xlsx',
                         header=None, names=column_name)
raw_data.head()

print(raw_data.describe())

raw_data.info()

clean_data = raw_data.replace('?', np.nan)
clean_data = clean_data.dropna()
clean_data.info()

keep = column_name.pop()
print(keep)
print(column_name)

training_data = clean_data[column_name]
target = clean_data[[keep]]
print(training_data.head())
print(target.head())

print(target['HeartDisease'].sum())

print(target['HeartDisease'].mean())

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(training_data)
scaled_data = pd.DataFrame(scaled_data, columns=column_name)
print(scaled_data.head())

print(scaled_data.describe().T)

boxplot = scaled_data.boxplot(column=column_name, showmeans=True)
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    scaled_data, target, test_size=0.3)
print('X_train shape :', X_train.shape)
print('Y_train shape :', Y_train.shape)
print('X_test shape :', X_test.shape)
print('Y_test shape :', Y_test.shape)

model = Sequential()
model.add(Dense(512, input_dim=13, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

model.compile(loss='mse', optimizer='adam', metrics=['binary_accuracy'])
fit_hist = model.fit(
    X_train, Y_train, batch_size=50, epochs=50,
    validation_split=0.2, verbose=1)

plt.plot(fit_hist.history['binary_accuracy'])
plt.plot(fit_hist.history['val_binary_accuracy'])
plt.show()

score = model.evaluate(X_test, Y_test, verbose=0)
print('Keras DNN model loss :', score[0])
print('Keras DNN model accuracy :', score[1])

from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
pred = model.predict(X_test)
pred = (pred > 0.9)
print(confusion_matrix(Y_test, pred))
print(f1_score(Y_test, pred, average='micro'))





