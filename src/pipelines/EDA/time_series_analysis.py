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

def read_df(path):
    '''read in file
    '''
    print('read df')
    return pd.read_csv(path, parse_dates=True, squeeze=True) 

def explore_data(df):
    # print(df.head())
    return df

def create_time_year(year):
    '''https://stackoverflow.com/questions/52685239/just-create-a-column-with-all-days-of-one-month-with-pandas
    creates the y column for a year in a time series
    '''
    #add another column, count
    #make it equal to 0
    #go through series of adoption date
    #every time a dog is found add 1 to count column in here
    df_time_yr = pd.DataFrame({
        'date': pd.date_range(
            start = pd.Timestamp(year),                        
            end = pd.Timestamp(year) + pd.offsets.YearEnd(0),  
            freq = 'D'
        )
    })
    # df_time_yr["counts"] = np.zeros(len(df_time_yr))
    # print("---------------------")
    # print(df_time_yr)
    # print(type(df_time_yr))
    # print("---------------------")
    # dogs_that_day = []
    # for day in s:
    #     df_time_yr["counts"]=df_time_yr["counts"]get(day,0)
    # dict_[day] += 1
    return df_time_yr



def count_unique_dogs(s):
    dict_ = {}
    # unique_days = df_time_yr
    # dogs_that_day = []
    for day in s:
        dict_[day]=dict_.get(day,0)
        dict_[day] += 1
    # print(dict_)
    # print(type(dict_))
    # df_time_yr["counts"]
    # df = pd.DataFrame(list(dict_.items()),columns = ['date','counts']) 
    return dict_




# create a new dictionary that is every single day 
# the key is the day, the value is 0
# then, use the same logic in count unique dogs -->
#   so every time we get a day, increment by 1
# result is every day has a value that is either 0 or hte count from there

def counts_per_day(dict_):
    counts_df = pd.DataFrame.from_dict(dict_, orient='index')
    counts_df.sort_index(inplace=True)
    # print(counts_df)
    return None

if __name__ == "__main__":
    
    #TODO elsa compare aggregated_csv_1 to running_main_csv.csv 
    #why does csv_1 work but not main?
    
    df = read_df('../../../data/csv/aggregated_csv_1.csv')
    # df = read_df('../../../data/csv/running_main_csv.csv')

    # explore_data(df)
    ##################################################################################

    
    year = '2020'
    y = create_time_year(year)
    print(y) 
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    
    #set every day to time 0/ midnight
    df['date'] = pd.to_datetime(df['status_changed_at'], infer_datetime_format=True).dt.normalize()
    df_normalised = df['date']
    df_dates = pd.DataFrame([df_normalised]).T


    
    dict_count = count_unique_dogs(df['date'] )
    #turn the dictionary into a dataframe for joining later
    df_counts = pd.DataFrame(list(dict_count.items()),columns = ['date','counts']) 
    print("***************\n") #, type(df_counts))
    # print(df_counts.head())
    print("***************\n")
    
    
    #join pandas df's together (originally a time series and a dictionary)
    df_tallies = y.join(df_counts.set_index('date'), on='date').fillna(0)
    # df_tallies.fillna(0)
    print(df_tallies)
    
    
    y = df_tallies["counts"]
    x = df_tallies["date"]

    import matplotlib
    matplotlib.use("agg")

    import matplotlib.pyplot as plt
    import numpy as np


    fig = plt.figure()
    ax = fig.gca()

    # x = y.index #np.linspace(1, 20)
    # y = np.linspace(1,365) #np.sinc(x)    
    # y = dict_count #= np.sinc(x) 

    ax.plot(x, y)
    ax.set_xlabel("Each day of the year", fontsize=16)
    ax.set_ylabel("Count of dogs adopted that day", fontsize=16)
    ax.set_title("Dog Adoption Trends", fontsize=18)

    fig.savefig("dog_adoption_trends_y_sinc.png")
