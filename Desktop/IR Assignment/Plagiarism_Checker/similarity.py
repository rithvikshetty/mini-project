import pandas as pd
from pandas import DataFrame
from Plagiarism_Checker.create_inverted_index import Inverted_Index
import itertools
import math
import os


class similar:
    def __init__(self,df):
        self.df=df

    def normalize_tf(self,df):
        for column in df:
            m = max(df[column])
            if m!=0:
                df[column] = df[column]/m
        return df

    def calculate_idf(self,df):
        idf_score = {}
        N = df.shape[1]
        all_words = df.index
        word_count = df.astype(bool).sum(axis=1)
        for word in all_words:
            idf_score[word] = math.log10(N/word_count[word])
        return idf_score

    def calculate_tfidf(self,data, idf_score):
        scores = {}
        for key,value in data.items():
            scores[key] = data[key]
        for doc,tf_scores in scores.items():
            for token, score in tf_scores.items():
                tf = score
                idf = idf_score[token]
                tf_scores[token] = tf * idf
        return scores

    def compare_documents(self,tf_idf_docs,tokens):
        compare = {}
        for column in tf_idf_docs:
            compare[column] = {}
            query_length = math.sqrt(sum(tf_idf_docs[column].loc[value] ** 2 for value in tokens))
            
            num = 0
            sum_of_squares = 0
            
            for value in tokens :
                sum_of_squares+=tf_idf_docs['query.txt'].loc[value] ** 2
                num+= tf_idf_docs['query.txt'].loc[value] * tf_idf_docs[column].loc[value] 
                
            doc_len = math.sqrt(sum_of_squares)
            cosine_sim = num/(doc_len*query_length)
            compare['query.txt'][column] = cosine_sim
            #compare[column]['query.txt'] = cosine_sim
        return compare
    
    def begin_sim(self):
        normalized_tf = self.normalize_tf(self.df)
        idf_score = self.calculate_idf(normalized_tf)
        tf_idf_docs = self.calculate_tfidf(normalized_tf,idf_score)
        tf_idf_df = pd.DataFrame(tf_idf_docs).T
        tf_idf_df.to_excel("tf_idf.xlsx")
        with open(os.path.join(os.getcwd(),"vocabulary.txt"),"r") as rf:
                tokens = rf.read().split()
        compare = self.compare_documents(tf_idf_docs,tokens)
        return compare

class create_df:
    def __init__(self,path):
        self.path=path

    def create(self):
        obj = Inverted_Index(self.path)
        df = obj.create_iit()
        obj2 = similar(df)
        return obj2.begin_sim()
