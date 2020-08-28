import numpy as np
import pandas as pd
from io import StringIO
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from create_main_dataframe import create_main_dataframe
import six #for table

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

def render_mpl_table(data, col_width=.70, row_height=0.625, font_size=14,
                     header_color='#00cc99', row_colors=['#d9d9d9', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    '''from stack overflow'''
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    ax.set_title('Adopted', fontsize=20, fontname="Times New Roman Bold")
    plt.show()
    return ax


if __name__ == "__main__":
    
    # df = read_df('../../../data/csv/giant_valid_csv.csv')
    df = read_df('../../../data/csv/tf_idf_adopted_csv.csv')
    ##################################################################################
    #TODO --> capstone 3
    # elsa bag of words and sentiment analysis


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
    # print(new_lst)
    
    #list and count unique words in dog descriptions text
    # LIST = lst_
    '''https://stackoverflow.com/questions/12282232/how-do-i-count-unique-values-inside-a-list'''
    LIST = new_lst
    counts,values = pd.Series(LIST).value_counts().values, pd.Series(LIST).value_counts().index
    df_results = pd.DataFrame(list(zip(values,counts)),columns=["value","count"])
    # print(df_results.head(25))

    df_final = df_results.head(25)
    # print(df_final)

    render_mpl_table(df_final, header_columns=0, col_width=2.0)