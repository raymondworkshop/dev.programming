# -*- coding: utf-8 -*-
"""
@author Raymond ZHAO Wenlong
"""
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

#import requests
#import json

#flask
from flask import Flask, url_for, g
from flask import request
from flask import json
from flask import Response

#database - sqlite3
from sqlite3 import dbapi2 as sqlite3
from flask_sqlalchemy import SQLAlchemy


ml_service = Flask(__name__)

# Database
ml_service.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(_basedir, 'ml.db')
ml_service.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(ml_service)

import db_model


"""
#load the default config
ml_service.config.update(dict(
    DATABASE=os.path.join(ml_service.root_path, 'ml.db'),
))
"""

# models
import ml_models


"""
def curl_request(url,method,headers,payloads):
    # construct the curl command from request
    command = "curl -v -H {headers} {data} -X {method} {uri}"
    data = ""
    if payloads:
        payload_list = ['"{0}":"{1}"'.format(k,v) for k,v in payloads.items()]
        data = " -d '{" + ", ".join(payload_list) + "}'"
    header_list = ['"{0}: {1}"'.format(k, v) for k, v in headers.items()]
    header = " -H ".join(header_list)
    print("The data:", data)
    #print(command.format(method=method, headers=header, data=data, uri=url))
"""

@ml_service.route('/')
def root():
    return 'Welcom the ML service ...'

@ml_service.route('/learn', methods=['POST'])
def get_data():
    print("Sending data ...")
    data = ""
    entry = ""
    age = 0.0
    species = ""
    score = 0.0
    #"Content-Type: application/json" \
    #-X POST -d '{"age": 4.5, "species": "dog"}'
    if request.headers['Content-Type'] == 'application/json':
        #data = json.dumps(request.json)
        data = request.json
        """
        f = open('data.json', 'wb')
        f.write(data)
        f.close()
        """
        #print("JSON data: " + data)
        # store the entry into database

        #import pdb; pdb.set_trace()
        age = data['age']
        #print("age", age)
        species = data['species']
        score = data['score']
        entry = db_model.Entry(age, species, score)
        #print("The entry: " + str(db_model.Entry.query.all()))
        
        db.session.add(entry)
        db.session.commit()
        print("The entry: " + str(db_model.Entry.query.all()))

        #also store in text
        data = json.dumps(request.json)
        f = open('data.json', 'a')
        f.write(data + '\n')
        f.close()
        
        return Response('ok')

    else:
        return 'Unsupported type'

def _train_model():
    """"""
    ml_models.train()
    return 
    
@ml_service.route('/train', methods=['POST'])
def train_model():
    print("Training the model ...")
    #_train_model()
    ml_models.train()
    
    return Response('ok')

@ml_service.route('/predict', methods=['POST', 'GET'])
def predict():
    #train_model()
    score = 0
    #score = _train_model()
    if request.headers['Content-Type'] == 'application/json':
    #data = json.dumps(request.json)
        data = request.json
        age = data['age']
        species = data['species']
        #score = data['score']
    #entry = db_model.Entry(age, species, score)

        #also store in text
        predict_data = json.dumps(request.json)
        f = open('predict_data.json', 'w')
        f.write(predict_data + '\n')
        f.close()

        # predict the score
        sdict = ml_models.predict(predict_data)
        print("the score: ", sdict)

        js = json.dumps(sdict)
        #resp = Response(js)
        return Response(js)

    return 

"""
def main():
    get_data()
    #train_model()
    #predict()
"""
if __name__ == "__main__":
    ml_service.run(debug=True)
