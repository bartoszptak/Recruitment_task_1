import requests, os
import re
import numpy as np
import xgboost as xgb
import pandas as pd
from sklearn.externals import joblib

DARK_SKY_API_KEY = os.environ['DARK_SKY_KEY']
option_list = "exclude=currently,minutely,hourly,alerts&units=si"

p = re.compile('\d+(\.\d+)?')
model = joblib.load('model.joblib.data')

class Controller:
    
    def check_data(self, data):
        for key in data.keys():
            if len(data[key])==0 or p.match(data[key]) is None:
                return '{} is empty or is not number'.format(key)
                
        return None


    def get_decision(self, data):
       
        scoreXgpa = float(data['gpa'])*float(data['score'])
        examsXgpa = (float(data['maths_exam'])+float(data['art_exam'])+float(data['language_exam']))*float(data['gpa'])
        scoresXgpa = (float(data['essay_score'])+float(data['interview_score']))*float(data['gpa'])

        test_X = np.array([[float(data['gpa']), float(data['score']), scoreXgpa, examsXgpa, scoresXgpa]], dtype=np.float32)

        df = pd.DataFrame(test_X, columns=['gpa', 'score', 'scoreXgpa', 'examsXgpa', 'scoresXgpa'])

        result = model.predict(df)[0]

        if result == 1:
            return 'Decision: Yes'
        else:
            return 'Decision: No'
