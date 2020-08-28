import numpy as np
import pandas as pd
from io import StringIO

import numpy as np
from create_main_dataframe import create_main_dataframe

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


import os
import re
import string
import math

'''Code borrowed from Galvanize DSI'''

def read_df(path):
    '''read in file
    '''
    # print('read df')
    return pd.read_csv(path) #, parse_dates=True, squeeze=True) 

def print_word_stats(words):
    num_words = len(words)
    unique_words = set(words)
    num_unique_words = len(unique_words)
    print(f"The number of words in the description is {num_words}.")
    print(f"The number of unique words in the description is {num_unique_words}.")
    

class AdoptedOrNot(object):
    """Implementation of Naive Bayes for binary classification
    Exploration into understanding classes using real-life example data
    https://pythonmachinelearning.pro/text-classification-tutorial-with-naive-bayes/#Dataset
    """
    def clean(self, s):
        translator = str.maketrans("", "", string.punctuation)
        return s.translate(translator)
 
    def tokenize(self, text):
        text = self.clean(text).lower()
        return re.split("\W+", text)
 
    def get_word_counts(self, words):
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0.0) + 1.0
        return word_counts

    def fit(self, X, Y):
        self.num_messages = {}
        self.log_class_priors = {}
        self.word_counts = {}
        self.vocab = set()

        n = len(X)
        self.num_messages['adoptable'] = sum(1 for label in Y if label == 1)
        self.num_messages['adopted'] = sum(1 for label in Y if label == 0)
        self.log_class_priors['adoptable'] = math.log(self.num_messages['adoptable'] / n)
        self.log_class_priors['adopted'] = math.log(self.num_messages['adopted'] / n)
        self.word_counts['adoptable'] = {}
        self.word_counts['adopted'] = {}

        for x, y in zip(X, Y):
            c = 'adoptable' if y == 1 else 'adopted'
            counts = self.get_word_counts(self.tokenize(x))
            for word, count in counts.items():
                if word not in self.vocab:
                    self.vocab.add(word)
                if word not in self.word_counts[c]:
                    self.word_counts[c][word] = 0.0

                self.word_counts[c][word] += count

    def predict(self, X):
        result = []
        for x in X:
            counts = self.get_word_counts(self.tokenize(x))
            adoptable_score = 0
            adopted_score = 0
            for word, _ in counts.items():
                if word not in self.vocab: continue
                
                # add Laplace smoothing
                log_w_given_adoptable = math.log( (self.word_counts['adoptable'].get(word, 0.0) + 1) / (self.num_messages['adoptable'] + len(self.vocab)) ) #+1 is Laplace Smoothing
                log_w_given_adopted = math.log( (self.word_counts['adopted'].get(word, 0.0) + 1) / (self.num_messages['adopted'] + len(self.vocab)) )

                adoptable_score += log_w_given_adoptable
                adopted_score += log_w_given_adopted

            adoptable_score += self.log_class_priors['adoptable']
            adopted_score += self.log_class_priors['adopted']

            if adoptable_score > adopted_score:
                result.append(1)
            else:
                result.append(0)
        return result
    
    
if __name__ == "__main__":
    
    '''heavily borrowed from https://pythonmachinelearning.pro/text-classification-tutorial-with-naive-bayes/#Dataset
    #text binary classification for discrete features (word counts)
    The multinomial distribution normally requires 
    integer feature counts. 
    '''
    
    ################################################
    #get dataframe of docs
    path_csv = '../../../data/csv/giant_valid_csv.csv'
    df = read_df(path_csv)
    df = df.dropna()
    # print(df.columns)
    df = pd.get_dummies(df, columns=['status'])
    df.drop("status_adoptable", axis = 1, inplace=True)
    print(df.shape)
    # new = old[['A', 'C', 'D']].copy()

    df_content = df[["status_adopted", "description"]].copy()
    # print(df_content.head())
    
    X = df_content["description"] #data
    # print(data)
    
    y = df_content["status_adopted"] #target
    # print(target)
    ################################################
    
    #split classes into half training, half testing
    NaiveBayes = AdoptedOrNot()
    NaiveBayes.fit(X[361:], y[361:])
    

    pred = NaiveBayes.predict(X[:361])
    true = y[:361]

    accuracy = sum(1 for i in range(len(pred)) if pred[i] == true[i]) / float(len(pred))
    print("Accuracy using text: {0:.4f}".format(accuracy))
    
    #####################################################
    # result
    # Accuracy using text: 0.7900
 