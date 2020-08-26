import numpy as np
import pandas as pd
from io import StringIO
import datetime
from datetime import datetime
import time
from datetime import datetime, date, time, timedelta
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("agg")
# from src.pipelines.cleaning.string_cleaning import *


def read_df(path):
    '''read in file
    '''
    print('read df')
    return pd.read_csv(path) 

def explore_data(df):
    # print(df.head())
    return df

def create_time_year(year):
    '''https://stackoverflow.com/questions/52685239/just-create-a-column-with-all-days-of-one-month-with-pandas
    creates the y column for a year in a time series
    '''
    df_time_yr = pd.DataFrame({
        'date': pd.date_range(
            start = pd.Timestamp(year),                        
            end = pd.Timestamp(year) + pd.offsets.YearEnd(0),  
            freq = 'D'
        )
    })
    return df_time_yr



def count_unique_dogs(s):
    dict_ = {}
    for day in s:
        dict_[day]=dict_.get(day,0)
        dict_[day] += 1
    return dict_


def counts_per_day(dict_):
    counts_df = pd.DataFrame.from_dict(dict_, orient='index')
    counts_df.sort_index(inplace=True)
    return None

if __name__ == "__main__":

    df = read_df('../../../data/csv/time_series_csv.csv') 
     
    year = '2020'
    month = 'August'
    y = create_time_year(year)


    #ADOPTED
    df_adopted = df[df['status']=='adopted']
    df['date'] = pd.to_datetime(df_adopted['status_changed_at'], infer_datetime_format=True).dt.normalize()
    dict_count_adopted = count_unique_dogs(df['date'] )
    df_counts_adopted = pd.DataFrame(list(dict_count_adopted.items()),columns = ['date','counts']) #turn the dictionary into a dataframe for joining later
    df_tallies_adopted = y.join(df_counts_adopted.set_index('date'), on='date').fillna(0) #join pandas df's together (originally a time series and a dictionary)
    y_adopted = df_tallies_adopted["counts"]
    x_adopted = df_tallies_adopted["date"]


    #ADOPTABLE
    df_adoptable = df[df['status']=='adoptable']
    df['date'] = pd.to_datetime(df_adoptable['status_changed_at'], infer_datetime_format=True).dt.normalize()
    dict_count_adoptable = count_unique_dogs(df['date'] )
    df_counts_adoptable = pd.DataFrame(list(dict_count_adoptable.items()),columns = ['date','counts']) #turn the dictionary into a dataframe for joining later
    df_tallies_adoptable = y.join(df_counts_adoptable.set_index('date'), on='date').fillna(0) #join pandas df's together (originally a time series and a dictionary)
    y_adoptable = df_tallies_adoptable["counts"]
    x_adoptable = df_tallies_adoptable["date"]
    
    
    #x_limit, y_limit
    #zip adopted and adoptable and remove 
    
    fig = plt.figure()
    # labels = ['monday', 'tues']
    plt.xticks( rotation='vertical')
    plt.plot(x_adoptable, y_adoptable, label="adoptable", color='red')
    plt.plot(x_adopted, y_adopted, label="adopted", color='green')
    plt.legend(loc="upper right")

    ax = fig.gca()
    ax.set_ylim(0, 200)
    ax.set_xlim([date(2020,7,14), date(2020,8,23)])
    ax.plot(x_adopted, y_adopted, label="adopted", color='green')
    ax.plot(x_adoptable, y_adoptable, label="adoptable", color='red')
 
    # counts, bins, patches = ax.hist(x_adoptable, facecolor='yellow', edgecolor='gray')
    # bins = ['week1', 'week2']
# Set the ticks to be at 
# the edges of the bins.
    # plt.xticks(np.arange(date(2020,7,14), date(2020,8,23), 1.0))
    # 1970-01-01T00:00:00.000042
    # ax.legend((line1, line2), ('adoptable', 'adopted'))


    ax.set_xlabel("July 14, 2020 to August 23, 2020", fontsize=16)
    ax.set_ylabel("Count of dogs shuffled that day", fontsize=14)
    ax.set_title("Dog Shelter Activity Snapshot 7-14-20 to 8-23-20", fontsize=16)
    fig.savefig("../../../src/readme/capstone_2_readme/dog_adoption_trends_time_series.png")
