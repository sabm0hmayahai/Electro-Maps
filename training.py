# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:08:38 2020

@author: kalpa
"""

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout


dataset = pd.read_excel("15th_3.12.xlsx")


dataset = dataset.iloc[:,1:]

del dataset['Date']


import numpy as np

#lables
y_train = dataset.iloc[:,-1].values
y_train = np.array(y_train, ndmin=2)
y_train = y_train.T

#features
x_train = dataset.iloc[:,:-1].values

#scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)

#splitting
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size = 0.2, random_state = 0)


    classifier = Sequential()
    
#First Hidden Layer
classifier.add(Dense(20, activation='relu', kernel_initializer='random_normal', input_dim=20))
classifier.add(Dense(50, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dense(30, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dense(30, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dense(50, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dense(30, activation='relu', kernel_initializer='random_normal'))


#Output Layer
classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))


#Compiling the neural network
classifier.compile(optimizer ='adam',loss='binary_crossentropy', metrics =['accuracy'])


#Fitting the data to the training dataset
classifier.fit(x_train,y_train, batch_size=100, epochs=500)

#evaluate
eval_model=classifier.evaluate(x_test, y_test)

eval_model

#save model
classifier.save('final_model.h5')








