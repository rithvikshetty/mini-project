from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd
import numpy as np

class TOP:
    def __init__(self):
        c=1
    def extract_features(self):
        df1=pd.read_csv("./project/processed/engaged.csv")
        df2=pd.read_csv("./project/processed/notEngaged.csv")
        dft=pd.concat([df1,df2])
        y_train=dft["Result"]
        x_train=dft.drop("Result",axis=1)
        model = ExtraTreesClassifier()
        model.fit(x_train,y_train)
        feat_importances = pd.Series(model.feature_importances_, index=x_train.columns)
        list_top=feat_importances.nlargest(50)

        list_top=list_top.index
        list_top = pd.DataFrame(list_top)
        list_top.to_csv("TopFeatures.csv",index=None)
        return