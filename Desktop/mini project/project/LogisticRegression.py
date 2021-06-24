import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.preprocessing import StandardScaler
import glob
import os
from project.top_features import TOP

class LR:
    def __init__(self):
        #x = TOP()
        #x.extract_features()
        c=1

    def top_features(self):
        dff=pd.read_csv("./TopFeatures.csv")
        feat=dff.to_numpy()
        feat=feat.reshape(-1)
        return feat

    def dimension_reduction(self):
        dff=pd.read_csv("./TopFeatures.csv")

    def LogisticRegression(self):
        path = r'./project/docs/processed/data' # use your path
        all_files = glob.glob(path + "/*.csv")
        scaler = StandardScaler()
        feat = self.top_features()

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            df = df[feat]
            model = scaler.fit(df)
            x_train = model.transform(df)
            fileNameActual=filename.replace("./project/docs/processed/data/","")
            mj = joblib.load('./project/models/model_joblib_logistic_regression')
            y_pred = mj.predict(x_train)
            column_values = ['Result']
            dFrame = pd.DataFrame(data = y_pred, columns = column_values)
            patho=r'./project/reports'
            dFrame.to_csv(os.path.join(patho,r''+"report.csv"))
        return