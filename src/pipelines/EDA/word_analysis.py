import numpy as np
import pandas as pd
from io import StringIO
import datetime
from datetime import datetime
import time
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from create_main_dataframe import create_main_dataframe
from wordcloud import WordCloud
from make_word_cloud import make_word_cloud_func

import sys 
sys.path.append('../data_ingestion') 
from read_in_data import *


def print_word_stats(words):
    num_words = len(words)
    unique_words = set(words)
    num_unique_words = len(unique_words)
    print(f"The number of words in the description is {num_words}.")
    print(f"The number of unique words in the description is {num_unique_words}.")
    print("The unique words are: ", unique_words)
    
def Convert(string): 
    li = list(string.split(" ")) 
    return li 

if __name__ == "__main__":
    
    df = read_df_csv('../../../data/csv/giant_valid_csv.csv')

    explore_data(df)
    ##################################################################################
    #toggle between adopted and adoptable
  
    # df = df[df['status']=='adopted']
    df = df[df['status']=='adoptable']
    # print(df)
    ##################################################################################

    df['tags'] = (df['tags'])
    df_tags = df['tags']
    list_dog_tags = df_tags.values.tolist()
    # print(df_tags)
    
    df['description'] = (df['description'])
    df_description = df['description']
 
    list_dog_descriptions = str(df_description.values.tolist())
    
    lst_ = list_dog_descriptions.lower().split()
    print(type(lst_))
    # len_list = len(lst)
    # print(len_list)
    lst_arr = []
    for word in range(len(lst_)):
        word = np.array([lst_[word]])
        # print(word)
        lst_arr = np.append(lst_arr, word)
        
    # print(lst_arr)
    # lst_arr = str(lst_arr)
    # lst_arr.replace('None', '').replace('...', '').replace('.', '').replace(':', '')

    
    clean_descriptions = lst_arr.tolist()
    print(type(clean_descriptions))

#    list_descriptions =[]
#    for x in len()
    
    # corpus = (list_dog_descriptions) + (list_dog_tags)
    # print(corpus)
    
    
    new_list = [word for line in list_dog_tags for word in line.split()]
    # print(new_list)
    
    from collections import Iterable
    def flatten(lis):
        for item in lis:
            if isinstance(item, Iterable) and not isinstance(item, str):
                for x in flatten(item):
                    yield x
            else:        
                yield item
    flat_word_list = list(flatten(new_list))
    # print(flat_word_list)
    
    clean_word_list = []
    for x in range (len(flat_word_list)):
        # print(flat_word_list[x])
        if flat_word_list[x] == '[]':
            # print('BAD') 
            # flat_word_list[x]
            pass
        else:
            clean_word_list.append(flat_word_list[x])

    series = pd.Series(clean_word_list)
    result = series.ravel()
    # print(type(result))
    result_str = str(result)

    str1 = result_str.replace('"[', '').replace('"]', '').replace('[', '').replace(']', '').replace('"', '').replace("'", '').replace(',', '').replace(',', ' ').replace("\n", ' ').replace("''", '').replace(", '',", ',').replace("  ", ' ').lower().replace("'", '').replace(' ', ',')
 
    cleaned_text = str(Convert(str1))

    #find out stats
    print_word_stats(result)


    make_word_cloud_func(cleaned_text)
