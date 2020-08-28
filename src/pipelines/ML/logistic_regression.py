'''borrowed heavily from https://365datascience.com/linear-regression/'''


print(__doc__)

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

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
    # print(y)


    # X_data_feature = (data.iloc[:,2])
    # print(X_data_feature)
    X = (data.iloc[:,2])
    # print(X)
    
    
    import matplotlib.pyplot as plt
    import numpy as np
    plt.scatter(X,y, c='lightgreen', alpha=0.2)
    plt.title("Dog's Adoption Status- Initial Image Data Exploration", fontsize=20)
    plt.xlabel('Image Data', fontsize=16)
    plt.ylabel('Status (1:Adopted, 0:Adoptable)', fontsize=16)
    plt.show()
    plt.close()
    
    
    logreg = LogisticRegression(C=1.0, solver='lbfgs', multi_class='ovr')
    
    #Convert a 1D array to a 2D array in numpy
    X = X.values.reshape(-1,1)
    
    #Run Logistic Regression
    logreg.fit(X, y)
    
    logreg.predict(X)
    
    print(logreg.predict_proba([[ 0.761894]])) #predict proba with a known adoptable dog

    X = np.arange(0, 730, 0.2)
    probabilities= []
    for i in X:
        p_loss, p_win = logreg.predict_proba([[i]])[0]
        probabilities.append(p_win)
        
    plt.scatter(X,probabilities, c='black', alpha=0.2)
    plt.title("Logistic Regression On Dog's Img Data")
    plt.xlabel('Image Data', fontsize=16)
    plt.ylabel('Status (1:Adopted, 0:Adoptable)', fontsize=16)
    plt.show()

    
