

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

    def __init__(self, model):
        self._vectorizer = TfidfVectorizer()
        self._classifier = MultinomialNB()
        self.data = data
        self.model = MultinomialNB()


    def predict_one(self, data):
        with open('pickled_algos/pickled_nb.pickle', 'rb') as f:
            model = pickle.load(f)

        with open('pickled_algos/tfidf_transformer.pickle', 'rb') as f:
            tfidf = pickle.load(f)

        with open('pickled_algos/count_vect.pickle', 'rb') as f:
            cv = pickle.load(f)

        cv_transformed = cv.transform(string_pred) #counts how many words
        tfidf_transformed = tfidf.transform(cv_transformed)  #tf == cv . 
        string_predicted = model.predict(tfidf_transformed) 
        res = str(string_predicted[0])
        if res == '0':
            print('Negative Sentiment')
        else:
            print("Positive Sentiment")

if __name__ == '__main__':

    # test_string_pred = ['this girl is a foster pit and has none of her teeth']
    # TextClassifier.predict_one(test_string_pred)

