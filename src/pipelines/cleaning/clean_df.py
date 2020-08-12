import numpy as np
import pandas as pd
from io import StringIO
from datetime import datetime


def read_df(path):
    '''read in file
    '''
    print('read df')
    return pd.read_csv(path, parse_dates=True, squeeze=True) 

def explore_data(df):
    print(df.head())
    return df


if __name__ == "__main__":
    df = read_df('../../../data/csv/aggregated_csv_1.csv')
    explore_data(df)
    
    #from https://www.youtube.com/watch?v=1KGcmLP65uo
    df_clean_rows = df[df.id.apply(lambda x: x.isnumeric())].set_index('id')
    explore_data(df_clean_rows)
    
    type(df_clean_rows['status_changed_at'])
    
    df_time_series = df['status_changed_at']
    df_time_series
    type(df_time_series)
    
    df_time_series.plot()
    
    df_right = pd.merge(df_time_series, df_clean_rows,  on='status_changed_at', how='right')

    df_right.head()
    type(df_right['status_changed_at'])
    
    df_right.plot()

