import numpy as np
import pandas as pd
from io import StringIO
import os
import re
import string
import math
from string import digits 

import nltk #to add my own stopwords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def read_df(path):
    '''read in file
    '''
    # print('read df')
    return pd.read_csv(path) 

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
    Some code borrowed from Galvanize DSI and pythonmachinelearning.pro
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
    and Galvanize DSI
    #text binary classification for discrete features (word counts)
    The multinomial distribution normally requires 
    integer feature counts. 
    '''
    
    ################################################
    #get dataframe of docs
    path_csv = '../../../data/csv/tf_idf_adoptable_csv.csv'
    df = read_df(path_csv)

    X = df["description"] #data
    # print(X.head())

    y = df["status_adopted"] #target
    # print(y.head())

    
    id = df["id"] #dog ID
    # print(id)
    
    corpus_dirty = []
    
    for doc in range(len(X)):
        str_corpus = str(X[doc])

        corpus_dirty.append(str_corpus)

    documents = []
    for doc in range(len(X)):
        record = X[doc]
        record = (record.lower())
        replaced = record.replace(", '...'", "").replace("...", '').replace('\d+', '') 
        remove_digits = str.maketrans('', '', digits) 
        replaced = replaced.translate(remove_digits) 
        clean = replaced.replace(", '...'", "").replace("...", '')
        documents.append(clean)
    # print(documents)
    
    
    
    
# #     # 2. Create a set of tokenized documents.
    docs = [word_tokenize(content) for content in documents]
    # print(docs)

#     # 3. Strip out stop words from each tokenized document.
    stop = set(stopwords.words('english'))
    my_stop_words_lst = ["she", "is", "of", "!", "of", "will", "he", "playful"]
    docs = [[word for word in words if (word not in stop) and (word not in my_stop_words_lst)] for words in docs]


#     # 4. Stemming / Lemmatization--> Stem using both stemmers and the lemmatizer
    porter = PorterStemmer()
    snowball = SnowballStemmer('english')
    wordnet = WordNetLemmatizer()
    docs_porter = [[porter.stem(word) for word in words] for words in docs]
    docs_snowball = [[snowball.stem(word) for word in words] for words in docs]
    docs_wordnet = [[wordnet.lemmatize(word) for word in words] for words in docs]

    # 5. Compare
    for i in range(min(len(docs_porter[0]), len(docs_snowball[0]), len(docs_wordnet[0]))):
        p, s, w = docs_porter[0][i], docs_snowball[0][i], docs_wordnet[0][i]
        if len(set((p, s, w))) != 1:
            print("{}\t{}\t{}\t{}".format(docs[0][i], p, s, w))

    print("End of stemming and lemmatization")
    # Part of speech tagging

    # 1. Create a part of speech tagged version of your already tokenized dataset.
    # commented out because it is slow...
    pos_tagged = [pos_tag(tokens) for tokens in docs]


#     # Bag of words and TF-IDF

    # 1. Create vocab, set of unique words
    docs = docs_snowball # choose which stemmer/lemmatizer to use
    vocab_set = set()
    [[vocab_set.add(token) for token in tokens] for tokens in docs]
    vocab = list(vocab_set)

    # 2. Create word count vectors manually.
    matrix = [[0] * len(vocab) for doc in docs]
    vocab_dict = dict((word, i) for i, word in enumerate(vocab))
    for i, words in enumerate(docs):
        for word in words:
            matrix[i][vocab_dict[word]] += 1

    # 3. Create word count vector over the whole corpus.
    stopwords = nltk.corpus.stopwords.words('english')
    newStopWords = ["she", "is", "of", "!", "of", "will", "he", "playful"]
    all_stopwords = stopwords.extend(newStopWords)
    cv = CountVectorizer(all_stopwords) #stop_words='english')
    vectorized = cv.fit_transform(documents)

    tfidf = TfidfVectorizer(all_stopwords) #stop_words='english')
    tfidfed = tfidf.fit_transform(documents) #my big x matrix, keep targets inline


    # X = tfidf
    # y = targets #this is y 

    # Cosine Similarity using TF-IDF

    # 1. Compute cosine similarity
    cosine_similarities = linear_kernel(tfidfed, tfidfed)

    # 2. Print out similarities
    cosine_distance_acc = []
    for i, doc1 in enumerate(docs):
        for j, doc2 in enumerate(docs):
            # print("Cosine Similarities Using TF-IDF")
            # print("Cosine Similarities Using TF-IDF: ", i, j, cosine_similarities[i, j])
            cosine_distance = 1 - (cosine_similarities[i, j])
            # print('COSINE DISTANCE: ', cosine_distance)
            cosine_distance_acc.append(cosine_distance)
    print("COSINE DISTANCE: ", np.mean(np.array(cosine_distance_acc)))
    # print(tfidf)
    
    
    
    
    
    
##########################
#FUTURE WORK DO NOT DELETE
 #create original df
    #     path_csv = '../../../data/csv/giant_valid_csv.csv'
    # df = read_df(path_csv)
    
    
    #     # print(df.columns)
    # df = pd.get_dummies(df, columns=['status'])
    # df.drop("status_adoptable", axis = 1, inplace=True)
    # print(df.shape)
    # df = df.dropna()
#     # print(df.columns)
#     df = pd.get_dummies(df, columns=['status'])
#     df.drop("status_adoptable", axis = 1, inplace=True)
#     print(df.shape)
#     df_content = df[["status_adopted", "description", "id"]].copy()
#     # print(df_content.head())
#     # df_content_adopted = df_content[df_content.status_adopted  == 1]
#     df_content_adoptable = df_content[df_content.status_adopted  == 0]
#     # print(df_content_adopted.head())  
#     # X = df_content["description"] #data
#     # print(X.head())
#     # X = df_content_adopted["description"] #data
#     X = df_content_adoptable["description"] #data
#     # print(X)
# #     # print(data) 
# #     y = df_content["status_adopted"] #target
#     # y = df_content_adopted["status_adopted"] #target
#     y = df_content_adoptable["status_adopted"] #target
  
#     # id = df_content_adopted["id"] #dog ID
#     id = df_content_adoptable["id"] #dog ID
#     print(id)
    
    
    
    
    #merge the two dataframes together
    #make a csv out of them
    # df_content_adoptable.to_csv('../../../data/csv/tf_idf_adoptable_csv.csv')
    
    

# #     # print(target)
    
#     X = pd.DataFrame(X)
#     y = pd.DataFrame(y)
#     X.reset_index(inplace=True)
#     y.reset_index(inplace=True)
    
    
#     print(X.head())
#     print(type(X))
#     print(y.head())
#     print(len(X))
    
#     ################################################

    # pd.Series(X)
    # pd.Series(y)
    
    
    # print(X.head())
    # print(type(X))
    # print(y.head())
    # print(len(X))
    #for tf-Idf and cosine similarity
    # https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/
    
    # df['tags'] = (df['tags'])
    # df_tags = df['tags']
    # # breakpoint()
    # list_dog_tags = df_tags.values.tolist()
    # print(df_tags)
    