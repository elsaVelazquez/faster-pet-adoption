



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
        positive_tweets = twitter_samples.strings('positive_tweets.json')
        negative_tweets = twitter_samples.strings('negative_tweets.json')

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
            print("lemmatizer: ", lemmatizer)
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
