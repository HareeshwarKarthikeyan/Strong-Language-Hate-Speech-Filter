#fitting and training data

import pandas as pd
from keras.preprocessing.text import Tokenizer
from tensorflow import keras
import tensorflow as tf

dataTrain = pd.read_csv('/content/drive/My Drive/data_train_clean.csv')

tokenizer = Tokenizer(num_words=10000, lower=True)

dataTrain = dataTrain['clean_comment']

xtrain = tokenizer.fit_on_texts(dataTrain)
xfinal = tokenizer.texts_to_sequences(dataTrain)

import numpy as np

dictionary = dict()
data = open("/content/drive/My Drive/glove.twitter.27B.200d.txt",encoding='utf8')
for line in data:
    values = line.split()
    word = values[0]
    try:
        coefs = np.asarray(values[1:],dtype='float32')
    except Exception as e:
        pass
    dictionary[word] = coefs
data.close()

dictionary = {k: (v+3) for (k, v) in dictionary.items()}
dictionary["<PAD>"] = 0  # actual zero - means they are like multiplied by 0
dictionary["b'"] = 1
dictionary["<UNK>"] = 2
dictionary["<UNUSED>"] = 3

PAD = 0  # a hyperparameter
xtrain_modified = keras.preprocessing.sequence.pad_sequences(
    xfinal, value=PAD, padding='post', maxlen=64)

dataTrain = pd.read_csv('/content/drive/My Drive/data_train_clean.csv')
# ytrain1 = dataTrain[['toxic','severe_toxic','obscene','threat','insult','identity_hate']] 
ytrain1 = dataTrain['toxic']
ytrain2 = dataTrain['severe_toxic']
ytrain3 = dataTrain['obscene']
ytrain4 = dataTrain['threat']
ytrain5 = dataTrain['insult']
ytrain6 = dataTrain['identity_hate']

xt = xtrain_modified[:70000] 
xv = xtrain_modified[70000:] 

yt1 = ytrain1[:70000]
yv1 = ytrain1[70000:] 

yt2 = ytrain2[:70000]
yv2 = ytrain2[70000:] 

yt3 = ytrain3[:70000]
yv3 = ytrain3[70000:] 

yt4 = ytrain4[:70000]
yv4 = ytrain4[70000:] 

yt5 = ytrain5[:70000]
yv5 = ytrain5[70000:] 

yt6 = ytrain6[:70000]
yv6 = ytrain6[70000:]

def model_hate():
  model = keras.Sequential()
  model.add(keras.layers.Embedding(10000, 200))
  model.add(keras.layers.GlobalAveragePooling1D())
  model.add(keras.layers.Dense(16, activation=tf.nn.relu))
  model.add(keras.layers.Dense(6, activation=tf.nn.sigmoid))
  return model

model=model_hate()
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
print(model.summary())

print("TOXIC")
history = model.fit(xt,yt1,epochs=2,batch_size=512,validation_data=(xv,yv1))
print("SEVERE_TOXIC")
history = model.fit(xt,yt2,epochs=2,batch_size=512,validation_data=(xv,yv2))
print("OBSCENE")
history = model.fit(xt,yt3,epochs=2,batch_size=512,validation_data=(xv,yv3))
print("THREAT")
history = model.fit(xt,yt4,epochs=2,batch_size=512,validation_data=(xv,yv4))
print("INSULT")
history = model.fit(xt,yt5,epochs=2,batch_size=512,validation_data=(xv,yv5))
print("IDENTITY_HATE")
history = model.fit(xt,yt6,epochs=2,batch_size=512,validation_data=(xv,yv6))