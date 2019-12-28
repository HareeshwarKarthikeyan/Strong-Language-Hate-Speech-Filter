from tensorflow import keras
import tensorflow as tf
import numpy as np
import pandas as pd

from keras.preprocessing.text import Tokenizer

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
            

#Main Model

def model_hate():
  inputlayer=Input(shape=(INPUT_LENGTH,))
  embed=Embedding(ip_dim=10000,op_dim=200,embed_init=Constant(embedding_matrix))
  lstm= LSTM(units=10,return_seq=False)(embed)

  dropout=Dropout(0.2)(lstm)
  dense=Dense(op_dim=3,init='uniform',activation='relu')(dropout)
  op=Dense(op_dim=1,init='uniform',activation='softmax')(dense)

  model=Model(inputs=input_layer,outputs=output)
  return model

classifier=model_hate()
classifier.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
classifier.summary()

class_wt_dict={0:1.5,1:1}

history=classifier.fit(x_trainpad,y_train,validation_data=(x_testpad,y_test),class_wt=class_wt_dict,batch_size=100,num_epoch=10)