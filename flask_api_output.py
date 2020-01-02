# Load libraries
import flask
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model

# instantiate flask 
app = flask.Flask(__name__)

# load the model, and pass in the custom metric function
global graph
graph = tf.get_default_graph()
model = load_model('Model_final.h5')

@app.route('/apitest/<arg>')
def apitest(arg):
    return 'API working'+arg

app.run(host='0.0.0.0', debug=False, port=5005)
