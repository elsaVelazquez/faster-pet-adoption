

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
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.metrics import pairwise_distances 
from sklearn.metrics.pairwise import euclidean_distances 
from scipy.spatial import distance 

from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.metrics import pairwise_distances 
from sklearn.metrics.pairwise import euclidean_distances 
from scipy.spatial import distance 
import pandas as pd 
import numpy as np 
# from tfidf_helpers import arr_convert_1d, cosine, manhatten_distance, euclidean_function

'''heavily inspired by https://www.geeksforgeeks.org/sklearn-feature-extraction-with-tf-idf/'''

txt_adopted = '../app/data/adopted_csv.csv'
scraped_data_adopted = open('../app/data/adopted_corpus.txt', 'r').read()
txt_adoptable = '../app/data/adoptable_csv.csv'
scraped_data_adoptable = open('../app/data/adoptable_corpus.txt', 'r').read()

## Converting 3D array of array into 1D array 
def arr_convert_1d(arr): 
	arr = np.array(arr) 
	arr = np.concatenate( arr, axis=0 ) 
	arr = np.concatenate( arr, axis=0 ) 
	return arr 

## Cosine Similarity 
cos = [] 
def cosine(trans): 
	cos.append(cosine_similarity(trans[0], trans[1])) 

# Manhatten Distance 
manhatten = [] 
def manhatten_distance(trans): 
	manhatten.append(pairwise_distances(trans[0], trans[1], 
										metric = 'manhattan')) 

## Euclidean Distance 
euclidean = [] 
def euclidean_function(vectors): 
	euc=euclidean_distances(vectors[0], vectors[1]) 
	euclidean.append(euc) 
 
def convert(): 
	dataf = pd.DataFrame() 
	lis2 = arr_convert_1d(manhatten) 
	dataf['manhatten'] = lis2 
	lis2 = arr_convert_1d(cos) 
	dataf['cos_sim'] = lis2 
	lis2 = (arr_convert_1d(euclidean) ) - 1
	if lis2 < 0.005:
		lis2 = 0
	dataf['euclidean'] = lis2 
	return dataf 

# def tfidf(data): 
#     txt=txt_adopted
#     scraped_data=scraped_data_adopted
#     df1 = pd.read_csv(str(txt))
#     df = df1.fillna("None")  #impute empty records
#     # df.drop(['index', 'status_adopted'], axis = 1, inplace= True)
#     df_str = df[["description"]].copy()
#     document = ' '.join(df_str['description'].tolist())
#     document =[] 
  
#     # Iterate over each row 
#     for index, rows in df_str.iterrows(): 
#         document.append(rows.description) 

#     vect = TfidfVectorizer() 
#     vect.fit(document) 

#     corpus = [scraped_data,user_input] #the scraped data compared to the input string
#     trans = vect.transform(corpus) 

#     euclidean_function(trans) 
#     cosine(trans) 
#     manhatten_distance(trans) 
#     return     cosine(trans) 
# #convert() 

def convert(): 
    dataf = pd.DataFrame() 
    lis2 = arr_convert_1d(manhatten) 
    dataf['manhatten'] = lis2 
    lis2 = arr_convert_1d(cos) 
    dataf['cos_sim'] = lis2 
    lis2 = (arr_convert_1d(euclidean) ) - 1
    if lis2 < 0.005:
        lis2 = 0
    dataf['euclidean'] = lis2 
    return dataf 




class TextClassifier(object):
    def __init__(self):
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
        length = str(len((str(data))))
        if length == '4':
            error = 'Error.  You do not input a description.  Please try agian.'
            return error
        res_mnb = str(string_predicted[0])
        if res_mnb == '0':
            res_mnb = ('Less Likely to be Adopted')
        else:
            res_mnb = ("More Likely to be Adopted")
        return res_mnb 
    
    def tfidf_(self, data): 
        txt=txt_adopted
        scraped_data=scraped_data_adopted
        df1 = pd.read_csv(str(txt))
        df = df1.fillna("None")  #impute empty records
        # df.drop(['index', 'status_adopted'], axis = 1, inplace= True)
        df_str = df[["description"]].copy()
        document = ' '.join(df_str['description'].tolist())
        document =[] 
    
        # Iterate over each row 
        for index, rows in df_str.iterrows(): 
            document.append(rows.description) 

        vect = TfidfVectorizer() 
        vect.fit(document) 
        

        corpus = [scraped_data, (str(data))] #the scraped data compared to the input string
        trans = vect.transform(corpus) 

        euclidean_function(trans) 
        cosine(trans) 
        manhatten_distance(trans) 
        return convert() 


if __name__ == '__main__':
    pass

    ### BEGIN test the script 
    
    # # instantiate object
    my_classifier = TextClassifier()
    # my_tfidf = TextTFIDF()
    #test negative sentiment
    test_string_pred = ['this girl is a foster pit and has none of her teeth']
    
    # #test positive sentimnet
    # test_string_pred = ['fill out an online form to find this male puppy a forever home']
    
    # #test empty string
    # test_string_pred = ['bad']

    res_mnb = my_classifier.predict_one(test_string_pred)
    print("Your MNB description yields: ", res_mnb)


    res_tfidf = my_classifier.tfidf_(str(test_string_pred)); 
    print(res_tfidf); 

    
    #### END test the script 
