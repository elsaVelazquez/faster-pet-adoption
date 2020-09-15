

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import random
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score




#######################################



class TextClassifier(object):

    def __init__(self):
        # self._vectorizer = TfidfVectorizer()
        # self._classifier = MultinomialNB()
        # self.data = data
        # self.model = MultinomialNB()
        
        with open('pickled_algos/pickled_nb.pickle', 'rb') as f:
            self.model = pickle.load(f)

        with open('pickled_algos/tfidf_transformer.pickle', 'rb') as f:
            self.tfidf = pickle.load(f)

        with open('pickled_algos/count_vect.pickle', 'rb') as f:
            self.cv = pickle.load(f)
   
    def predict_one(self, data):
        cv_transformed = self.cv.transform(data) #counts how many words
        tfidf_transformed = self.tfidf.transform(cv_transformed)  #tf == cv . 
        string_predicted = self.model.predict(tfidf_transformed) 
        res = str(string_predicted[0])
        if res == '0':
            res = ('Negative Sentiment')
        else:
            res = ("Positive Sentiment")
        return res 

if __name__ == '__main__':

    my_classifier = TextClassifier()
    test_string_pred = ['this girl is a foster pit and has none of her teeth']
    res = my_classifier.predict_one(test_string_pred)
    print(res)


    