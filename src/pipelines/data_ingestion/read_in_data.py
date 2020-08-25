import numpy as np
import pandas as pd

def read_df_csv(path):
    '''read in file
    '''
    # print('read df')
    return pd.read_csv(path) #, parse_dates=True, squeeze=True) 


def read_text_file(fname):
    '''Reads the filename - should have a .txt extension.

       Returns a text string containing the entire description.
    ''' 
    f = open(fname, 'r')
    textstring = f.read()
    return textstring



def explore_data(df):
    # print(df.head())
    return df

if __name__ == "__main__":
    pass