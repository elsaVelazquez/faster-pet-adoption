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
# from wordcloud import WordCloud
# from make_word_cloud.wordcloud import WordCloud


def read_df(path):
    '''read in file
    '''
    print('read df')
    return pd.read_csv(path) #, parse_dates=True, squeeze=True) 

def explore_data(df):
    print(df.head())
    return df

def print_word_stats(words):
    num_words = len(words)
    unique_words = set(words)
    num_unique_words = len(unique_words)
    print(f"The number of words in the description is {num_words}.")
    print(f"The number of unique words in the description is {num_unique_words}.")
    


if __name__ == "__main__":
    
    #TODO elsa compare aggregated_csv_1 to running_main_csv.csv 
    #why does csv_1 work but not main?
    

    df = read_df('../../../data/csv/running_main_csv.csv')

    explore_data(df)
    ##################################################################################
    #TODO elsa bag of words and sentiment analysis
    #id,organization_id,url,type,species,breeds,colors,age,gender,size,coat,attributes,environment,tags,name,description,organization_animal_id,photos
    # ,videos,status,status_changed_at,published_at,distance,contact,_links

    # df.drop(['photos', 'videos', 'status_changed_at', 'published_at', 'distance', 'contact', 'organization_animal_id', 'type'], axis = 1, inplace= True)
    # df.info()
    


    df['tags'] = (df['tags'])
    df_tags = df['tags']
    # print(df_tags)
    # print(type(df_tags))
    
    list_dog_descriptions = df_tags.values.tolist()
    # print(list_dog_descriptions)
    # print(type(list_dog_descriptions))
    new_list = [word for line in list_dog_descriptions for word in line.split()]
    print(new_list)
    
    from collections import Iterable
    def flatten(lis):
        for item in lis:
            if isinstance(item, Iterable) and not isinstance(item, str):
                for x in flatten(item):
                    yield x
            else:        
                yield item
    flat_word_list = list(flatten(new_list))
    print(flat_word_list)
    
    clean_word_list = []
    for x in range (len(flat_word_list)):
        print(flat_word_list[x])
        if flat_word_list[x] == '[]':
            # print('BAD') 
            # flat_word_list[x]
            pass
        else:
            clean_word_list.append(flat_word_list[x])
            
        print(clean_word_list) 
        
    # final_dog_word_list = list(flatten(clean_word_list))      
    # print(type(final_dog_word_list))

    series = pd.Series(clean_word_list)
    result = series.ravel()
    print(type(result))
    result_str = str(result)
    print(result_str)
    print(type(result_str))
    str1 = result_str.replace('"[', '').replace('"]', '').replace('[', '').replace(']', '').replace('"', '').replace("'", '').replace(',', '').replace(' ', ', ').replace("\n", ' ')
    print(str1)

    # word_list = new_list.remove('[]')
    # print(word_list)
    # df_clean = df[df['tags'].map(lambda d: (d)) != '[]']
    # print(df_clean)
    
    # X, y_adopted = create_main_dataframe(df)

    # print(X)
    # print(y_adopted)
    
    # print(X['tags'])
    # # dt.fit(X, y)
    
    # X_train, X_test, y_train, y_test = train_test_split(X, y)

    
    # print(dt) #print the tree
    # phrases = []
    # for x in range(len(df_tags)):
    #     if df_tags[x] == '[]':
    #         pass
    #     else:
    #         phrases.append(df_tags[x])
    # print(phrases)
                
    
    # from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
    # stopwords = ENGLISH_STOP_WORDS

    # words_nsw = [word for word in words if word not in stopwords]


    # print_word_stats(words_nsw)

    # words_nsw

    

    
    
    # y = df_tallies["counts"]
    # x = df_tallies["date"]

    # import matplotlib
    # matplotlib.use("agg")

    # import matplotlib.pyplot as plt
    # import numpy as np


    # fig = plt.figure()
    # ax = fig.gca()

    # # x = y.index #np.linspace(1, 20)
    # # y = np.linspace(1,365) #np.sinc(x)    
    # # y = dict_count #= np.sinc(x) 

    # ax.plot(x, y)
    # ax.set_xlabel("Each day of the year", fontsize=16)
    # ax.set_ylabel("Count of dogs adopted that day", fontsize=16)
    # ax.set_title("Dog Adoption Trends", fontsize=18)

    # fig.savefig("dog_adoption_trends_y_sinc.png")
