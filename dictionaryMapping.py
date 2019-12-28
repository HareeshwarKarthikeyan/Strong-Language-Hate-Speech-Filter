# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 11:32:33 2019

@author: Akshit
"""
import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from tensorflow import keras
import tensorflow as tf

xtrain = pd.read_csv('data_train_clean.csv')

tokenizer = Tokenizer(num_words=10000, lower=True)

tokenizer.fit_on_texts(xtrain)
tokenizer.texts_to_sequences(xtrain)

dictionary = dict()
data = open("glove.twitter.27B.200d.txt",encoding='utf8')
for line in data:
    values = line.split()
    word = values[0]
    try:
        coefs = np.asarray(values[1:],dtype='float32')
    except Exception as e:
        pass
    dictionary[word] = coefs
data.close()

embedding_matrix = np.zeros((10000, 200))
for word, index in tokenizer.word_index.items():
    if index >= 10000:
        continue
    else:
        embedding_vector = dictionary.get(word)
        if embedding_vector is not None:
            embedding_matrix[index] = embedding_vector
            
def model_hate():
  model = keras.Sequential()
  
  #embed_init=Constant(embedding_matrix)
  model.add(keras.layers.Embedding(10000, 200))
  
  #lstm= LSTM(units=10,return_seq=False)(embed)

  #model.add(Dropout(0.2))
  model.add(keras.layers.GlobalAveragePooling1D())
  model.add(keras.layers.Dense(16, activation=tf.nn.relu))
  model.add(keras.layers.Dense(6, activation=tf.nn.softmax))
  return model

model=model_hate()
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.summary()

class_wt_dict={0:1.5,1:1}

#history=classifier.fit(xtrain,y_train,validation_data=(x_testpad,y_test),class_wt=class_wt_dict,batch_size=100,num_epoch=10)
