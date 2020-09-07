



import argparse
import pickle as pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.text import Text
import string, re

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier


from nltk.tag import pos_tag

import sys
sys.path.append('../src/pipelines/data_ingestion/')
from read_in_data import *

import numpy as np
from io import StringIO
import os
import re
import string
import math
from string import digits 

from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

import random






class TextClassifier(object):

    def __init__(self):
        self._vectorizer = TfidfVectorizer()
        self._classifier = MultinomialNB()
        self.data = data


    def predict(self, X):
        # print(self)
        # print(X)
        X = self._vectorizer.transform(X)
        # print(X)
        # print("***%%%%%%%%%%%%%%%%%%%%%%%%*****", X)

        return self._classifier.predict(X)
    
    
    def clean_description(self, data):
        data = str(data)
        # print("string data: ", data)
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in data:  
            if ele in punc:  
                data = data.replace(ele, "")
        # print("cleaned data: ", data)
        return data
    
    
    def tokenize_data(self, data):
        data = str(data)
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in data:  
            if ele in punc:  
                data = data.replace(ele, "")
        data = data.split()
        # print("tokenized data: ", data)
        return data


    def lemmatize_data(self, data):
        data = str(data)
        

    def sentiment(self, data):
        path_csv = '../data/csv/tf_idf_adoptable_csv.csv'
        df = read_df_csv(path_csv)
        X_negative = df["description"] #data
        corpus_dirty = []
        for doc in range(len(X_negative)):
            str_corpus = str(X_negative[doc])
            corpus_dirty.append(str_corpus)

        negative_documents = []
        for doc in range(len(X_negative)):
            record = X_negative[doc]
            record = (record.lower())
            replaced = record.replace(", '...'", "").replace("...", '').replace('\d+', '') 
            remove_digits = str.maketrans('', '', digits) 
            replaced = replaced.translate(remove_digits) 
            clean = replaced.replace(", '...'", "").replace("...", '')
            negative_documents.append(clean)
        # print(documents)
    # #     # 2. Create a set of tokenized documents.
        negative_descriptions = [word_tokenize(content) for content in negative_documents]
        # print("\n\nPositive Descriptions Tokenized: ", positive_descriptions)
        data_negative = str(negative_descriptions)
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in data_negative:  
            if ele in punc:  
                data_negative = data_negative.replace(ele, "")
        data_negative = data_negative.split()
        # print("tokenized data: ", data_negative)
        ##################################################################
        ##################################################################
        ##################################################################

        
        path_csv = '../data/csv/tf_idf_adopted_csv.csv'
        df = read_df_csv(path_csv)
        X_positive = df["description"] #data
        corpus_dirty = []
        for doc in range(len(X_positive)):
            str_corpus = str(X_positive[doc])
            corpus_dirty.append(str_corpus)

        positive_documents = []
        for doc in range(len(X_positive)):
            record = X_positive[doc]
            record = (record.lower())
            replaced = record.replace(", '...'", "").replace("...", '').replace('\d+', '') 
            remove_digits = str.maketrans('', '', digits) 
            replaced = replaced.translate(remove_digits) 
            clean = replaced.replace(", '...'", "").replace("...", '')
            positive_documents.append(clean)
        # print(documents)
    # #     # 2. Create a set of tokenized documents.
        positive_descriptions = [word_tokenize(content) for content in positive_documents]
        # print("\n\nPositive Descriptions Tokenized: ", positive_descriptions)
        data_positive = str(positive_descriptions)
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in data_positive:  
            if ele in punc:  
                data_positive = data_positive.replace(ele, "")
        data_positive = data_positive.split()
        # print("tokenized data: ", data_negative)
        
        ##################################################################
        ##################################################################
        ##################################################################
        
        positive_dataset = [(description_dict, "Positive")
                     for description_dict in data_positive]

        negative_dataset = [(description_dict, "Negative")
                            for description_dict in data_negative]
        
        # print("positive_dataset: ", positive_dataset)
        print("negative_dataset: ", negative_dataset)


        dataset = positive_dataset + negative_dataset
        seventy_percent_of_data = int(len(dataset) * .7)
        thirty_percent_of_data = int(len(dataset) * .3)
        # print(thirty_percent_of_data) #361

        random.shuffle(dataset) #to avoid bias

        train_data = dataset[:seventy_percent_of_data]
        test_data = dataset[thirty_percent_of_data:]
        # print("test_data: ", test_data)
        # print("type: ", type(test_data))


        train_data_dict = {train_data[i]: train_data[i + 1] for i in range(0, len(train_data), 2)} 
        print("train data dict: ", train_data_dict)
        
        # classifier = NaiveBayesClassifier.train(train_data_dict)

        # print("Accuracy is:", classify.accuracy(classifier, test_data))

        # print(classifier.show_most_informative_features(10))
        
        # from nltk.corpus import twitter_samples
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print(twitter_samples)
        data = str(data)
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in data:  
            if ele in punc:  
                data = data.replace(ele, "")
        data = data.split()
        print("tokenized data: ", data)
        
        #breakdown parts of speech
        parts_of_speech = [] 
        parts_of_speech.append(nltk.pos_tag(data))
        print("parts of speech tagging: ", parts_of_speech) 
       #lemmatized data:
        stop_words = [] #left here in case I want to add words in the future
        cleaned_tokens = []
        # classifier = NaiveBayesClassifier.train(parts_of_speech)

        #https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
        # positive_descriptions = ('../data/json/positive_adopted_json.json')
        # negative_descriptions = ('../data/json/positive_adopted_json.json')
        # print(positive_descriptions[0])

    #     path_csv = '../data/csv/tf_idf_adoptable_csv.csv'
    #     df = read_df_csv(path_csv)
    #     X = df["description"] #data
    #     corpus_dirty = []
    #     for doc in range(len(X)):
    #         str_corpus = str(X[doc])
    #         corpus_dirty.append(str_corpus)

    #     documents = []
    #     for doc in range(len(X)):
    #         record = X[doc]
    #         record = (record.lower())
    #         replaced = record.replace(", '...'", "").replace("...", '').replace('\d+', '') 
    #         remove_digits = str.maketrans('', '', digits) 
    #         replaced = replaced.translate(remove_digits) 
    #         clean = replaced.replace(", '...'", "").replace("...", '')
    #         documents.append(clean)
    #     # print(documents)
    # # #     # 2. Create a set of tokenized documents.
    #     negative_descriptions = [word_tokenize(content) for content in documents]
    #     print(negative_descriptions)

    # #     # 3. Strip out stop words from each tokenized document.
    #     stop = set(stopwords.words('english'))
    #     my_stop_words_lst = ["she", "is", "of", "!", "of", "will", "he"] #, "playful"]
    #     docs = [[word for word in words if (word not in stop) and (word not in my_stop_words_lst)] for words in docs]


















        for token, tag in nltk.pos_tag(data):
            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos) 
            print("token: ", token)
            print("lemmatizer: ", lemmatizer) #same as lemmatized sentence
            # classifier = NaiveBayesClassifier.train(token, pos)


            if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
                cleaned_tokens.append(token.lower())
        
            print("***************************************")
        #     print(data, classifier.classify(dict([token, True] for token in custom_tokens)))
            
        # print("Accuracy is:", classify.accuracy(classifier, test_data))

        # print('most informative features: ', classifier.show_most_informative_features(10))

        # print("printing out parts of speech data: ", data)
        
       
        
        return data
    
    # def clean_description(self, data):
    #     data = str(data)
    #     # print("string data: ", data)
    #     punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     for ele in data:  
    #         if ele in punc:  
    #             data = data.replace(ele, "")
    #             # data2 = data1.replace(".", '')
    #     # print("cleaned string: ", data2)

    #     # return clean
    #     print("cleaned data: ", data)
    #     return data

if __name__ == '__main__':

    pass


























#####################################################################################################



# import argparse
# import pickle as pickle
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB


# class TextClassifier(object):

#     def __init__(self):
#         self._vectorizer = TfidfVectorizer()
#         self._classifier = MultinomialNB()

#     # def fit(self, X, y):
#     #     X = self._vectorizer.fit_transform(X)
#     #     self._classifier.fit(X, y)
#     #     return self

#     # def predict_proba(self, X):
#     #     X = self._vectorizer.transform(X)
#     #     return self._classifier.predict_proba(X)

#     def predict(self, X):
#         X = self._vectorizer.transform(X)
#         print("***%%%%%%%%%%%%%%%%%%%%%%%%*****", X)

#         return self._classifier.predict(X)

#     # def score(self, X, y):
#     #     X = self._vectorizer.transform(X)
#     #     return self._classifier.score(X, y)


# # def get_data(filename):
# #     df = pd.read_csv(filename)
# #     X, y = df.body, df.section_name
# #     return X, y


# if __name__ == '__main__':
#     # parser = argparse.ArgumentParser(
#     #     description='Fit a Text Classifier model and save the results.')
#     # parser.add_argument('--data', help='A csv file with input data.')
#     # parser.add_argument('--out', help='A file to save the pickled model object to.')
#     # args = parser.parse_args()
#     # print("***%%%%%%%%%%%%%%%%%%%%%%%%*****", args)

#     # X, y = get_data(args.data)
#     # tc = TextClassifier()
#     # tc.fit(X, y)
#     # with open(args.out, 'wb') as f:
#     #     pickle.dump(tc, f)
#     pass



#####################################################################################################



# """
# Module containing model fitting code for a web application that implements a
# text classification model.

# When run as a module, this will load a csv dataset, train a classification
# model, and then pickle the resulting model object to disk.

# USE:

# python build_model.py --data path_to_input_data --out path_to_save_pickled_model

# """
# import argparse
# import pickle as pickle
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB


# class TextClassifier(object):
#     """A text classifier model:
#         - Vectorize the raw text into features.
#         - Fit a naive bayes model to the resulting features.

#     The work done by this class could also be done with a sklean.pipeline
#     object.  Since the author cannot guarentee that Pipelines have been
#     introduced, he opted to write his own class implementing the model.

#     This class is an example of coding to an interface, it implements the
#     standard sklearn fit, predict, score interface.
#     """

#     def __init__(self):
#         self._vectorizer = TfidfVectorizer()
#         self._classifier = MultinomialNB()

#     def fit(self, X, y):
#         """Fit a text classifier model.

#         Parameters
#         ----------
#         X: A numpy array or list of text fragments, to be used as predictors.
#         y: A numpy array or python list of labels, to be used as responses.

#         Returns
#         -------
#         self: The fit model object.
#         """
#         X = self._vectorizer.fit_transform(X)
#         self._classifier.fit(X, y)
#         return self

#     def predict_proba(self, X):
#         """Make probability predictions on new data.
        
#         Parameters
#         ----------
#         X: A numpy array or list of text fragments, to be used as predictors.

#         Returns
#         -------
#         probs: A (n_obs, n_classes) numpy array of predicted class probabilities. 
#         """
#         X = self._vectorizer.transform(X)
#         return self._classifier.predict_proba(X)

#     def predict(self, X):
#         """Make class predictions on new data.

#         Parameters
#         ----------
#         X: A numpy array or list of text fragments, to be used as predictors.

#         Returns
#         -------
#         preds: A (n_obs,) numpy array containing the predicted class for each
#         observation (i.e. the class with the maximal predicted class probabilitiy.
#         """
#         X = self._vectorizer.transform(X)
#         return self._classifier.predict(X)

#     def score(self, X, y):
#         """Return a classification accuracy score on new data.

#         Parameters
#         ----------
#         X: A numpy array or list of text fragments.
#         y: A numpy array or python list of true class labels.
#         """
#         X = self._vectorizer.transform(X)
#         return self._classifier.score(X, y)


# def get_data(filename):
#     """Load raw data from a file and return training data and responses.

#     Parameters
#     ----------
#     filename: The path to a csv file containing the raw text data and response.

#     Returns
#     -------
#     X: A numpy array containing the text fragments used for training.
#     y: A numpy array containing labels, used for model response.
#     """
#     df = pd.read_csv(filename)
#     X, y = df.body, df.section_name
#     return X, y


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(
#         description='Fit a Text Classifier model and save the results.')
#     parser.add_argument('--data', help='A csv file with input data.')
#     parser.add_argument('--out', help='A file to save the pickled model object to.')
#     args = parser.parse_args()

#     X, y = get_data(args.data)
#     tc = TextClassifier()
#     tc.fit(X, y)
#     with open(args.out, 'wb') as f:
#         pickle.dump(tc, f)
