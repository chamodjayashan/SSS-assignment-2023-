
import numpy as np
from flask import Flask, request,render_template
from flask_cors import CORS
import os

import pickle
import flask
import os
import newspaper
from newspaper import Article
import urllib


import joblib


app = Flask(__name__)
CORS(app)
app=flask.Flask(__name__,template_folder='templates')

with open('model.pickle', 'rb') as handle:
	model = pickle.load(handle)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
 
    news = request.get_data(as_text=True)[5:]
   
    pred = model.predict([news])
    return render_template('main.html', prediction_text='The news is "{}"'.format(pred[0]))
    
if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)