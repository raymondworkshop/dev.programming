# -*- coding: utf-8 -*-
"""
The ML models
  * liner Regression model is used here

@author
"""

import sys

# The data
from ml_service import db
import db_model

#sklearn
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

#
import json
from pprint import pprint

entries = []

# the model
regr = linear_model.LinearRegression()

def load_data():
    # load all data
    #entries = db_model.Entry.all()
    global entries
    f = open('data.json', 'r')
    for line in f.readlines():
        entry = json.loads(line)
        if entry['species'] == 'cat':
            entry['species'] = 0
        if entry['species'] == 'dog':
            entry['species'] = 1
        entries.append(entry)

    #import pdb; pdb.set_trace()
    print(entries)

    return entries


def train():
    # load the data
    load_data()
    #[{'age': 1.1, 'score': 3.1, 'species': 0}, {'age': 1.1, 'score': 3.1, 'species': 1}]
    X1 = [] #age
    X2 = [] # species
    #X = np.matrix()
    y = [] # score
    global entries
    global regr
    for entry in entries:
        X1.append(entry['age'])
        X2.append(entry['species'])

        y.append(entry['score'])

    X = np.array([X1, X2])
    print("X1: ", X1)
    print("X2: ", X2)
    print("X: ", X)
    print('y: ', y)

    # ignore to split it into training/testing setsampwidth
    #Y = 0 # define dog->0, cat->1

    # linear regression model
    global regr
    #regr = linear_model.LinearRegression()
    #global regr

    # train the model using training data
    regr.fit(X, y)

    # Metric - The mean squared error
    #print("Mean squared error: %.2f"
    #  % mean_squared_error(X, y))

    return

def predict(_data):
    sdict = {}
    global regr

    data = json.loads(_data)

    #print
    if data['species'] == 'cat':
        data['species'] = 0
    if data['species'] == 'dog':
        data['species'] = 1

    pred_X1 =[]
    pred_X2 =[]
    print("The entry: ", data)
    pred_X1.append(data['age'])
    pred_X2.append(data['species'])
    _pred_X = [data['age'], data['species']]

    #There is a problem here
    pred_X = np.array(_pred_X).reshape(1, -1)
    print("The predict data: ", pred_X)

    score_pred = 0
    score_pred = regr.predict(pred_X)

    #
    sdict['score'] = float(score_pred[0])
    #print('score:', sdict)

    return sdict

def main():
    #load_data()
    #train()
    predict()

if __name__ == "__main__":
    main()
