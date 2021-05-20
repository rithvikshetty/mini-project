import pandas as pd
from pandas import DataFrame
from Plagiarism_Checker.similarity import similar,create_df

class similar_Files:
    def __init__(self,path):
        self.path = path
        #self.threshold = threshold
    def files(self):
        self.compare = pd.DataFrame(self.compare).sort_values('query.txt',ascending=False)
        self.compare.to_excel("comparison_table.xlsx")
        result = [(key,self.compare['query.txt'][key]) for key in self.compare['query.txt'].index if self.compare['query.txt'][key]*100>=0 and key!='query.txt']
        return result[:10],len(result)
    def start_sim(self):
        obj = create_df(self.path)
        self.compare = obj.create()
        return self.files()

#to_run_the_package
#a = similar_Files("Docs")
#print(a.start_sim())