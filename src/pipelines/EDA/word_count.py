import numpy as np
import pandas as pd
from io import StringIO
import datetime
from datetime import datetime
import time
from datetime import datetime, date, time, timedelta
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np
from create_main_dataframe import create_main_dataframe


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
    # print("**************\n", unique_words)    
    # print(list(set(list_str)))




if __name__ == "__main__":
    
    df = read_df('../../../data/csv/giant_valid_csv.csv')

    ##################################################################################
    #TODO elsa bag of words and sentiment analysis


    df['description'] = (df['description'])
    df_description = df['description']
 
    list_dog_descriptions = str(df_description.values.tolist())
    # print(list_dog_descriptions)
    
    lst_ = list_dog_descriptions.lower().split()
    lst_ = str(lst_).strip('.').replace("'", '').replace(",", '').replace('"', '') #strip("'") #.replace('and', '')
    print(type(lst_))
    lst_ = lst_.split(' ')
    len_list = len(lst_)
    print(len_list)
    # print(lst_)
    
    print_word_stats(lst_)
    

    my_stopwrds = ['an', 'the','is', 'a', 'and', 'to', 'his', 'her', 'we',  "be", 'are', 'this', 'on', "'you", "'none',", 'and', 'my', 'am', 'at', 'who', "'none'", 'is', 'a', 'to', 'the', 'an', 'in', 'with', 'for', 'i', 'of', 'year']

    new_lst = []
    for word in lst_: 
        if word not in my_stopwrds:
            new_lst.append(word)
            # print(word)
    print(new_lst)
    
    #list and count unique words in dog descriptions text
    # LIST = lst_
    '''https://stackoverflow.com/questions/12282232/how-do-i-count-unique-values-inside-a-list'''
    LIST = new_lst
    counts,values = pd.Series(LIST).value_counts().values, pd.Series(LIST).value_counts().index
    df_results = pd.DataFrame(list(zip(values,counts)),columns=["value","count"])
    print(df_results.head(25))

#     lst_arr = []
#     for word in range(len(lst_)):
#         word = np.array([lst_[word]])
#         # print(word)
#         lst_arr = np.append(lst_arr, word)
        
#     print(lst_arr[2][:])
#     lst_arr = str(lst_arr)
#     lst_arr.replace('None', '').replace('...', '').replace('.', '').replace(':', '')

#     print(lst_arr)
# #     # clean_descriptions = lst_arr.tolist()
# #     print(type(clean_descriptions))

# #    list_descriptions =[]
# #    for x in len()
    
#     corpus = (clean_descriptions) + (list_dog_tags)
#     str_corpus = str(corpus)
#     print(str_corpus)
#     clean_corpus = str_corpus.replace('None', '').replace('...', '').replace('.', '').replace(':', '').replace('[]', '').replace('"[', '').replace(']"', '').replace("''", '').replace(', ,', '')
    
    
#     #TODO . try this corpus cleaner instead::
#     # str1 = result_str.replace('"[', '').replace('"]', '').replace('[', '').replace(']', '').replace('"', '').replace("'", '').replace(',', '').replace(',', ' ').replace("\n", ' ').replace("''", '').replace(", '',", ',').replace("  ", ' ').lower().replace("'", '').replace(' ', ',')

#     str_tags = str(df_tags)
#     corpus = clean_corpus + str_tags
#     print(corpus)
# #     # cmd = 'python make_corpus.py > ../../../data/txt/corpus.txt'
# #     # os.system(cmd)