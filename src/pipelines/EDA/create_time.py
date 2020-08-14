import pandas as pd
import datetime
import numpy as np
from io import StringIO
import time
from datetime import datetime, date, time, timedelta


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

def create_time_month(year):
    '''https://stackoverflow.com/questions/52685239/just-create-a-column-with-all-days-of-one-month-with-pandas
    creates the y column for a year in a time series
    '''
    df_time_month = pd.DataFrame({
        'date': pd.date_range(
            start = pd.Timestamp(month),                        
            end = pd.Timestamp(month) + pd.offsets.MonthEnd(0),  
            freq = 'D'
        )
    })
    return df_time_month


if __name__ == "__main__":
 

    year = '2020'
    generate_y_axis = create_time_year(year)
    print(generate_y_axis) 
    
    
    
    
    
    
    
    
    
    # df['normalised_date'] = pd.to_datetime(df['status_changed_at'], infer_datetime_format=True).dt.normalize()
    # # print(df['normalised_date'])
    # # 0    2020-08-07
    # # 1    2020-09-08
    # # 2    2020-08-08
    # # 3    2020-08-02
    # # 4    2020-04-08
    
    
    
    # #create our X's to plot 
    # def count_unique_dogs(s):
    #     dict_ = {}
    #     unique_days = []
    #     dogs_that_day = []
    #     for day in s:
    #         dict_[day]=dict_.get(day,0)
    #         dict_[day] += 1
    #     # print(dict_)
    
    # count_unique_dogs(df['normalised_date'])
    
