import pandas as pd
import nltk
import itertools
import math
import operator
from statistics import mean
from nltk.corpus import stopwords
from nltk.stem import *
import os,sys
import re, string, unicodedata
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize

class Data:
    def __init__(self,path):
        self.path = path

    def strip_html(self,text):
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()

    def remove_non_ascii(self,words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words

    def to_lowercase(self,words):
        """Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words

    def remove_punctuation(words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.translate(str.maketrans("","",string.punctuation))
            if new_word != '':
                new_words.append(new_word)
        return new_words

    def remove_numbers(self,words):
        """Replace all interger occurrences in list of tokenized words with textual representation"""
        new_words = []
        for word in words:
            new_word = re.sub(r'\d+','',word)
            if new_word != '':
                new_words.append(new_word)
        return new_words

    def remove_stopwords(self,words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        stop_words = set(stopwords.words("english"))
        for word in words:
            if word not in stop_words:
                new_words.append(word)
        return new_words

    def stem_words(self,words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems

    def lexical_analysis(self,words):
        words = self.remove_non_ascii(words)
        words = self.to_lowercase(words)
        words = self.remove_numbers(words)
        return words

    def read_data(self):
        contents = []
        for filename in os.listdir(self.path):
            data = self.strip_html(open(self.path+'/'+filename,"rb").read())
            #filename = re.sub('\D',"",filename)
            contents.append((filename,data))
        return contents

    def get_vocabulary(self,data):
        tokens = []
        with open(os.path.join(os.getcwd(),"vocabulary.txt"),"r") as rf:
            tokens = rf.read().split()
        return tokens

    def preprocess_data(self,contents):
        dataDict = {}
        vocabulary=[]
        for content in contents:
            sample = content[1]
            sample = sample.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
            tokens = word_tokenize(sample)
            lexical = self.lexical_analysis(tokens)
            filtered_tokens = self.remove_stopwords(lexical)
            stemmed_tokens = self.stem_words(filtered_tokens)
            filtered_tokens1 = self.remove_stopwords(stemmed_tokens)
            vocabulary=vocabulary+filtered_tokens1
            dataDict[content[0]] = filtered_tokens1
        vocabulary = list(set(vocabulary))
        vocabulary.sort()
        with open(os.path.join(os.getcwd(),"vocabulary.txt"),"w") as wf:
            wf.write(" ".join(vocabulary))
        return dataDict

    def generate_inverted_index(self,t_data):
        all_words = self.get_vocabulary(t_data)
        index = {}
        for word in all_words:
            index[word] = {}
            for doc, tokens in t_data.items():
                index[word][doc] = tokens.count(word)
        return index

    def start(self):
        data = self.read_data()
        preprocessed_data = self.preprocess_data(data)
        return preprocessed_data