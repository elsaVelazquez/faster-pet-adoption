

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
        
        #import dog database data
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
        length = len(data)-1
        print("size of string:", len(data))
        res = str(string_predicted[0])
        if res == '0' :
            res = ('Less Likely to be Adopted')
        else:
            res = ("More Likely to be Adopted")
        return res 
    
    def predict_one_twitter(self, data):
        #import twitter data
        with open('pickled_algos/pickled_nb_tweets.pickle', 'rb') as f:
            self.model = pickle.load(f)

        with open('pickled_algos/tfidf_transformer_tweets.pickle', 'rb') as f:
            self.tfidf = pickle.load(f)

        with open('pickled_algos/count_vect_tweets.pickle', 'rb') as f:
            self.cv = pickle.load(f)
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
    pass

    ### BEGIN test the script 
    
    # # instantiate object
    # my_classifier = TextClassifier()
    
    # #test negative sentiment
    # # test_string_pred = ['this girl is a foster pit and has none of her teeth']
    
    # # #test negative sentimnet
    # test_string_pred = ['fill out an online form to find this male puppy a forever home']
    
    # res = my_classifier.predict_one(test_string_pred)
    # print("sentiment: ", res)

    
    #### END test the script 
