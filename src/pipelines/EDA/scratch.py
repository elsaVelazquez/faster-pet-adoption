return self.as_string().strip()
    df1 = pd.read_csv('../data/playgolf.csv')
    #convert categoricals to dummy variables --> Outlook, Result to 1's 0's
    df = pd.get_dummies(df1, columns=['Outlook', 'Result'])
    print(df)
        #then pop off results which is the y, and pop also removes it
    
    y = df.pop('Result_Play')
    df = df.drop("Result_Don't Play", axis = 1) 
    
    X = df.values

    dt = DecisionTree()
    dt.fit(X, y)
    
    print(dt) #print the tree
    
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    rf = RandomForestClassifier(n_estimators=len(y), max_features='auto')
    rf.fit(X_train, y_train)
    y_predict = rf.predict(X_test)
    print("Accuracy score of this model:", rf.score(X_test, y_test))
    
    
    #################################
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
    # return pd.read_json(path, convert_dates=True) 

def explore_data(df):
    print(df.head())
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
    unique_days = []
    dogs_that_day = []
    for day in s:
        dict_[day]=dict_.get(day,0)
        dict_[day] += 1
    return dict_

if __name__ == "__main__":
    df_original = read_df('../../../data/csv/aggregated_csv_1.csv')
    # df_original = read_df('../../../data/json/big_json_v4.json')
    # explore_data(df_original)
    ##################################################################################

    ######HOW TO PLOT FOR ADOPTABLE DOGS USING GET DUMMIES AND:
    # [~mask] maybe?
    
    
    df = pd.get_dummies(df_original, columns=['status'] )
    # print(df)
    
    df = df.drop("status_adoptable", axis=1)
    print(df)
    
    # year = '2020'
    # y = create_time_year(year)

    # df['normalised_date'] = pd.to_datetime(df['status_changed_at'], infer_datetime_format=True).dt.normalize()
   
    # X = count_unique_dogs(df['normalised_date'])  #, infer_datetime_format=True).dt.normalize()    #.values

    # import matplotlib
    # matplotlib.use("agg")

    # import matplotlib.pyplot as plt
    # import numpy as np

    # fig = plt.figure()
    # ax = fig.gca()

    # x = np.linspace(-6, 6, 500)
    # y = np.sinc(x)

    # ax.plot(x, y)
    # ax.set_xlabel("Each day of the year", fontsize=16)
    # ax.set_ylabel("Count of dogs adopted that day", fontsize=16)
    # ax.set_title("Dog Adoption Trends", fontsize=18)

    # fig.savefig("dog_adoption_trends.png")
