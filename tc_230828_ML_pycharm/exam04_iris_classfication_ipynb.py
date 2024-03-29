# -*- coding: utf-8 -*-
"""exam04_iris_classfication.ipynb의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zw3PqmOo05IfdcLCyIucs6tiHnnIZ3d8
"""

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

iris = load_iris()
print(type(iris))
print('================data shape===============')
print('Data', iris.data.shape)
print('Label', iris.target.shape)
print('First five data :', iris.data[0:5])
print('First five label :', iris.target[0:5])
print('iris dataset keys\n', iris.keys())

iris.feature_names

iris.target_names

import pandas as pd

iris_dataframe = pd.DataFrame(iris.data, columns=iris.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c=iris.target,
                           figsize=(7, 7),
                           marker='o',
                           hist_kwds={'bins':5},
                           s=100, alpha=0.7)
plt.show()

x = iris.data
y = iris.target.reshape(-1, 1)
print(y[0:5])

encoder = OneHotEncoder(sparse_output=False)
encoded_y = encoder.fit_transform(y)
print(encoded_y.shape)
print(encoded_y[50:55])

X_train, X_test, Y_train, Y_test = train_test_split(
    x, encoded_y, test_size=0.2)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

model = Sequential()
model.add(Dense(256, input_dim=4, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.summary()

"""#경사하강알고리즘
http://shuuki4.github.io/deep%20learning/2016/05/20/Gradient-Descent-Algorithm-Overview.html
"""

opt = Adam(lr=0.001)
model.compile(opt, loss='categorical_crossentropy', metrics=['accuracy'])

fit_hist = model.fit(X_train, Y_train, batch_size=5, epochs=50, verbose=1)

score = model.evaluate(X_test, Y_test, verbose=0)
print('Final test set accuracy :', score[1])

score

plt.plot(fit_hist.history['accuracy'])
plt.show()

labels = iris.target_names
my_sample = np.random.randint(30)
sample = X_test[my_sample]
print(sample)
sample = sample.reshape(1,4)
print(sample)
pred = model.predict(sample)
print('pred is',pred)
print('actual is :', Y_test[my_sample])
print('Target :', labels[np.argmax(Y_test[my_sample])])
print('Prediction after learning is :', labels[np.argmax(pred)])

