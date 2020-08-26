import datetime
import pandas as pd 
from datetime import date
from pandas import Timestamp
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor   


def read_in_csv(path):
    print(f"read in {path}")
    return pd.read_csv(path)

def calculate_vif_(X, thresh=10.0):
    variables = list(range(X.shape[1]))
    dropped = True
    while dropped:
        dropped = False
        vif = [variance_inflation_factor(X.iloc[:, variables].values, ix)
                for ix in range(X.iloc[:, variables].shape[1])]

        maxloc = vif.index(max(vif))
        # print(maxloc, vif)
        # columns = X.columns
        for feature, value in zip(X.columns, vif):
            print(f'{feature}: {value}')
            # print("\n")
        if max(vif) > thresh:
            print('dropping \'' + X.iloc[:, variables].columns[maxloc] +
                  '\' at index: ' + str(maxloc))
            del variables[maxloc]
            dropped = True
            print("\n")
    print('Remaining variables:')
    print(X.columns[variables])
    return X.iloc[:, variables]

if __name__ == "__main__":
    
    path_csv = '../../../data/csv/giant_valid_csv.csv'
    
    df = read_in_csv(path_csv)
    
    df = df.dropna()

    print(df.columns)
    
    df = pd.get_dummies(df, columns=['status'])
    
    
    
    
    # df = pd.get_dummies(df, columns=['breeds'])
    df = pd.get_dummies(df, columns=['gender'])
    df = pd.get_dummies(df, columns=['age'])
    df = pd.get_dummies(df, columns=['size'])
    df = pd.get_dummies(df, columns=['coat'])
    df = pd.get_dummies(df, columns=['colors'])
    df = pd.get_dummies(df, columns=['attributes'])
    df = pd.get_dummies(df, columns=['environment'])
    df = pd.get_dummies(df, columns=['tags'])
    df = pd.get_dummies(df, columns=['name'])
    df = pd.get_dummies(df, columns=['description'])

    df.drop(['organization_id', 'url', 'species', 'breeds',
       'organization_animal_id', 'photos',
       'primary_photo_cropped', 'videos', 'status_changed_at',
       'published_at', 'distance', 'contact', '_links', 'type'], axis = 1, inplace=True)
   
    print(df.columns)


    X = df
    
    vif = calculate_vif_(X, thresh=5.0)
    
    