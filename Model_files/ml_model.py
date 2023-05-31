import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from flask import Flask, request, jsonify, app
import pickle
import random
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)

def predict_price(det, model):
    #if type(det) == dict:
        #df = pd.DataFrame(det)
    #else:
        #df = det
    df = pd.DataFrame.from_dict(det)
    return model.predict(df)