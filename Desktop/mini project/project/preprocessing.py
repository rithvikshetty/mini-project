import pandas as pd
import glob
import os
from sklearn.preprocessing import StandardScaler

class preprocess:
    def __init__(self):
        c=1
    
    def preprocessing(self):
        dir = './project/docs/processed/data'
        filelist = glob.glob(os.path.join(dir, "*"))
        for f in filelist:
            os.remove(f)
        
        pathl = r'./project/docs/uploaded/data' # use your path
        all_files = glob.glob(pathl + "/*.csv")
        patho=r'./project/docs/processed/data'
        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            delete_row = df[df[" confidence"]<=0.50].index
            df = df.drop(delete_row)
            df=df.drop(['frame',' face_id',' timestamp',' confidence',' success'],axis=1) 
            #fileToBeSaved=filename.replace("./project/docs/uploaded/data","")
            df.to_csv(os.path.join(patho,r"processed.csv"),index=False)
        return