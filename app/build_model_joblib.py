import numpy as np 
import pandas as pd 
pd.set_option('display.max_colwidth', -1)
from time import time
import re
import string
import os
# import emoji
from pprint import pprint
import collections
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
sns.set(font_scale=1.3)
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import gensim
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings('ignore')
np.random.seed(37)


#randomize data
df = pd.read_csv('data/Tweets.csv')
df = df.reindex(np.random.permutation(df.index))
df = df[['description', 'sentiment']]

df_dogs = pd.read_csv('../data/csv/sentiment_status_csv.csv')
df_dogs = df_dogs.reindex(np.random.permutation(df_dogs.index))
df_dogs = df_dogs[['description', 'sentiment']]

#EDA
# sns.factorplot(x="sentiment", data=df, kind="count", size=6, aspect=1.5, palette="PuBuGn_d")
# plt.show();
# plt.close()

# sns.factorplot(x="sentiment", data=df_dogs, kind="count", size=6, aspect=1.5, palette="PuBuGn_d") #, title="Dog Descriptions Sentiment Data")
# plt.show();
# plt.close()


# compute basic statistics on the description variable   
class TextDescriptionCounts(BaseEstimator, TransformerMixin):
    
    def count_regex(self, pattern, tweet):
        return len(re.findall(pattern, tweet))
    
    def fit(self, X, y=None, **fit_params):
        #used only on training data
        return self
    
    def transform(self, X, **transform_params):
        count_words = X.apply(lambda x: self.count_regex(r'\w+', x))        
        df = pd.DataFrame({'count_words': count_words })        
        return df  

class CleanTextDescriptions(BaseEstimator, TransformerMixin):
    def remove_mentions(self, input_text):
        return re.sub(r'@\w+', '', input_text)
    
    def remove_urls(self, input_text):
        return re.sub(r'http.?://[^\s]+[\s]?', '', input_text)
    
    def emoji_oneword(self, input_text):
        # By compressing the underscore, the emoji is kept as one word
        return input_text.replace('_','')
    
    def remove_punctuation(self, input_text):
        # Make translation table
        punct = string.punctuation
        trantab = str.maketrans(punct, len(punct)*' ')  # Every punctuation symbol will be replaced by a space
        return input_text.translate(trantab)
    
    def remove_digits(self, input_text):
        return re.sub('\d+', '', input_text)
    
    def to_lower(self, input_text):
        return input_text.lower()
    
    def remove_stopwords(self, input_text):
        stopwords_list = stopwords.words('english')
        # Some words which might indicate a certain sentiment are kept via a whitelist
        whitelist = ["n't", "not", "no"]
        words = input_text.split() 
        clean_words = [word for word in words if (word not in stopwords_list or word in whitelist) and len(word) > 1] 
        return " ".join(clean_words) 
    
    def stemming(self, input_text):
        porter = PorterStemmer()
        words = input_text.split() 
        stemmed_words = [porter.stem(word) for word in words]
        return " ".join(stemmed_words)
    
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X, **transform_params):
        clean_X = X.apply(self.remove_mentions).apply(self.remove_urls).apply(self.emoji_oneword).apply(self.remove_punctuation).apply(self.remove_digits).apply(self.to_lower).apply(self.remove_stopwords).apply(self.stemming)
        return clean_X
    
    
def show_dist(df, col):
    print('Descriptive stats for {}'.format(col))
    print('-'*(len(col)+22))
    print(df.groupby('sentiment')[col].describe())
    bins = np.arange(df[col].min(), df[col].max() + 1)
    g = sns.FacetGrid(df, col='sentiment', size=5, hue='sentiment', palette="PuBuGn_d")
    g = g.map(sns.distplot, col, kde=False, norm_hist=True, bins=bins)
    plt.show();
 
def display_word_freq(giant_string):
    bow = cv.fit_transform(giant_string)
    word_freq = dict(zip(cv.get_feature_names(), np.asarray(bow.sum(axis=0)).ravel()))
    word_counter = collections.Counter(word_freq)
    word_counter_df = pd.DataFrame(word_counter.most_common(10), columns = ['word', 'freq'])
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.barplot(x="word", y="freq", data=word_counter_df, palette="PuBuGn_d", ax=ax)
    plt.show();
    
if __name__ == "__main__":
    #EDA to show counts of words
    tc = TextDescriptionCounts()
    df_eda = tc.fit_transform(df.description)
    df_eda['sentiment'] = df.sentiment
    # show_dist(df_eda, 'count_words')
    
    tc_dogs = TextDescriptionCounts()
    df_eda_dogs = tc_dogs.fit_transform(df_dogs.description)
    df_eda_dogs['sentiment'] = df_dogs.sentiment
    # show_dist(df_eda_dogs, 'count_words')

    #clean data
    ct = CleanTextDescriptions()
    sr_clean = ct.fit_transform(df.description)
    print(sr_clean.sample(5))
    
    ct_dogs = CleanTextDescriptions()
    sr_clean_dogs = ct_dogs.fit_transform(df_dogs.description)
    print(sr_clean_dogs.sample(5))
    

    #impute into empty tweets rows
    #the dog data already was imputed with 'None'
    empty_clean = sr_clean == ''
    print('{} Tweets records have no words left after text cleaning and were imputed with the word "None"'.format(sr_clean[empty_clean].count()))
    sr_clean.loc[empty_clean] = '[None]'
    
    imputed_clean_dogs = (sr_clean_dogs == 'None')
    print('64 Dog records were imputed with the word "None"') #.format(sr_clean_dogs[imputed_clean_dogs].count()))


    #compare word freq by sentiment
    df_dogs_positive = df_dogs[df_dogs['sentiment'] == 'positive']
    sr_clean_dogs_positive = ct.fit_transform(df_dogs_positive.description)
    
    df_dogs_negative = df_dogs[df_dogs['sentiment'] == 'negative']
    sr_clean_dogs_negative = ct.fit_transform(df_dogs_negative.description)
    
    df_tweets_positive = df[df['sentiment'] == 'positive']
    sr_clean_tweets_positive = ct.fit_transform(df_tweets_positive.description)
    
    df_tweets_negative = df[df['sentiment'] == 'negative']
    sr_clean_tweets_negative = ct.fit_transform(df_tweets_negative.description)

    #Display word frequency
    cv = CountVectorizer()

    display_word_freq(sr_clean)
    display_word_freq(sr_clean_tweets_positive)
    display_word_freq(sr_clean_tweets_negative)
    display_word_freq(sr_clean_dogs)
    display_word_freq(sr_clean_dogs_positive)
    display_word_freq(sr_clean_dogs_negative)
