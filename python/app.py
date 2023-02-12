from flask import Flask
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from flask_cors import CORS, cross_origin

dataset = pd.read_csv("perfect.csv")

dataset = pd.get_dummies(dataset, columns=['city'], prefix='city')
dataset = pd.get_dummies(dataset, columns=['usedesc'], prefix="useDesc")

X = dataset.loc[:, dataset.columns != 'landval']
y = dataset['landval']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=101)

s_scaler = StandardScaler()
X_train = s_scaler.fit_transform(X_train)

regressor = LinearRegression()  
regressor.fit(X_train, y_train)

app = Flask(__name__)
CORS(app)


cityCodes = {
    'Dallas': [1, 0, 0],
    'Philadelphia': [0, 1, 0],
    'Socal': [0, 0, 1],
}

useDescCodes = {
    'Commercial': [1, 0, 0, 0, 0, 0, 0],
    'Commercial Office': [0, 1, 0, 0, 0, 0, 0],
    'Commercial Store': [0, 0, 1, 0, 0, 0, 0],
    'Industrial': [0, 0, 0, 1, 0, 0, 0],
    'Unzoned': [0, 0, 0, 0, 1, 0, 0],
    'Residential': [0, 0, 0, 0, 0, 1, 0],
    'Single Residential': [0, 0, 0, 0, 0, 0, 1],
}

@app.route("/<ll_gissqft>/<ll_gisacre>/<parval>/<usedesc>/<city>")
@cross_origin(origin='*')
def value(ll_gissqft, ll_gisacre, parval, usedesc, city):

    if parval == -1:
        50000
    
    json = [ll_gissqft, ll_gisacre, parval]
    cityCode = cityCodes[city]
    useDescCode = useDescCodes[usedesc]

    for item in cityCode:
        json.append(item)
    for item in useDescCode:
        json.append(item)

    dataframe = pd.DataFrame(json)
    dataframe = dataframe.transpose()

    scaled_data = s_scaler.transform(dataframe)

    y_pred = regressor.predict(scaled_data)
    value = y_pred[0]
    if value < 0:
        value = -value
    return {'value': value}, 201