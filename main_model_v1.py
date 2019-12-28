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