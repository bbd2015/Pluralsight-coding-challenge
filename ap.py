
import sys
import os
import shutil
import time
import traceback

from flask import Flask, request, jsonify
import pandas as pd
from sklearn.externals import joblib
import numpy as np


app = Flask(__name__)

model_directory = 'model'
model_file_name_eu = '%s/knn_eu.pkl' % model_directory
model_file_name_cos = '%s/knn_cosine.pkl' % model_directory
model_columns_file_name = '%s/knn_columns.pkl' % model_directory

@app.route('/predict', methods=['GET'])
def predict():
    if clf_eu or clf_cos:
        try:
#             json_ = request.json
    
#             query = np.array([0,0,138] + [0] * 6741)
            query = joblib.load('test_user.pkl')
            user_id = joblib.load('users.pkl')
            print (query)
            if clf_eu:
                prediction_eu = clf_eu.kneighbors(query, return_distance = False)
                prediction_eu = prediction_eu.tolist()
                prediction_eu = [user_id[i] for i in prediction_eu[0]]
                print ("euclidean distance")
                print (prediction_eu[0])
            if clf_cos:
                prediction_cos = clf_cos.kneighbors(query, return_distance = False)
                prediction_cos = prediction_cos.tolist()
                prediction_cos = [user_id[i] for i in prediction_cos[0]]
                print ("cosine similarity")
                print (prediction_cos)

            return jsonify({'Similar users id using euclidean distance': prediction_eu, 'Similar users id using cosine': prediction_cos})

        except Exception as e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print ('train first')
        return 'no model here'




@app.route('/wipe', methods=['GET'])
def wipe():
    try:
        shutil.rmtree('model')
        os.makedirs(model_directory)
        return 'Model wiped'

    except Exception as e:
        print (str(e))
        return 'Could not remove and recreate the model directory'


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80

    try:
        clf_eu = joblib.load(model_file_name_eu)
        print ('model_eu loaded')
        clf_cos = joblib.load(model_file_name_cos)
        print ('model_cos loaded')
        model_columns = joblib.load(model_columns_file_name)
        print ('model columns loaded')

    except Exception as e:
        print ('No model here')
        print ('Train first')
        print (str(e))
        clf = None

    app.run(host='0.0.0.0', port=port, debug=True)



