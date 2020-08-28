'''borrowed heavily from https://365datascience.com/linear-regression/'''


print(__doc__)

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm 

from sklearn import svm, datasets
from sklearn.metrics import auc
from sklearn.metrics import plot_roc_curve
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LinearRegression

from make_X_y import *

if __name__ == '__main__':
    
    #apply my dataset
    X, y, all_images = make_X_y()

    #make my dataset to use with sklearn
    X_df = pd.DataFrame(X)
    y_df = pd.DataFrame(y)
    all_images_df = pd.DataFrame(all_images)
    
    data_df = pd.concat([X_df, y_df], axis=1, join='inner')
   
    data_df.to_csv(r'../../../data/csv/data_X_y.csv', index = False)
    #manually changed final column to y in csv

    data = pd.read_csv('../../../data/csv/data_X_y.csv')
    # print(data)
    # print(data.describe())

    
    # y_data_target = (data.iloc[:,-1])
    # print(y_data_target)
    y = (data.iloc[:,-1])
    print(y)


    # X_data_feature = (data.iloc[:,2])
    # print(X_data_feature)
    x1 = (data.iloc[:,2])
    print(x1)

    x = sm.add_constant(x1)
 
    results = sm.OLS(y,x).fit()
    
    print(results.summary())
    
    plt.scatter(x1,y)
    
    yhat = 0.6097*x1 + 0.1613
    
    fig = plt.plot(x1,yhat, lw=4, c='red', label = 'regression line')
    
    plt.xlabel('X data feature flat img column no. 2', fontsize = 16)
    
    plt.ylabel('y data target', fontsize = 16)
    
    plt.title('Linear Regression on 1 Image Feature', fontsize=18)
    
    plt.show()
    
