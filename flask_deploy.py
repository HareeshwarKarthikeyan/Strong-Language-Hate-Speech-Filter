from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import sys

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	clf = load_model('model_final.h5')

	if request.method == 'POST':
		message = request.form['message']
		message = [message]
		
		from tensorflow.keras.preprocessing.text import Tokenizer
		from tensorflow.keras.preprocessing.sequence import pad_sequences
		
		df = pd.DataFrame(data=message, columns=["message"])
		xtestdata = tokenizer.texts_to_sequences(df['message'])
		xtestdata = pad_sequences(xtestdata, padding='post', maxlen=64)
		print(xtestdata)
		my_prediction = clf.predict(xtestdata)
		print(my_prediction)
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True, use_reloader=False)