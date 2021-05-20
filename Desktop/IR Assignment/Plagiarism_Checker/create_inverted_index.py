import pandas as pd
#from preprocessing import preprocess,preprocessed_data
from Plagiarism_Checker.preprocessing import Data

class Inverted_Index:
    def __init__(self,path):
        self.path = path
    
    def create_iit(self):
        preprocess = Data(self.path)
        preprocessed_data = preprocess.start()
        inverted_index = preprocess.generate_inverted_index(preprocessed_data)
        inverted_index_df = pd.DataFrame(inverted_index).T
        inverted_index_df.to_excel("inverted_index.xlsx")
        return inverted_index_df