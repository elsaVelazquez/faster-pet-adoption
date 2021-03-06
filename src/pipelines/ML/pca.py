'''borrowed heavily from https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html'''


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

from sklearn.decomposition import PCA

import seaborn as sns; sns.set()

from make_X_y import *


if __name__ == '__main__':
    
    #apply my dataset
    X, y, all_images = make_X_y()
    print("nothing is gained by going beyond reducing to 2 dimensions")

    #dimensionality reduction
    pca = PCA(n_components=1)
    pca.fit(X)
    
    
    X_pca = pca.transform(X)
    print("original shape:   ", X.shape)
    print("transformed shape:", X_pca.shape)
    
    print("X[:, 0]: ", X[:, 0])
    print("X[:, 1]: ", X[:, 1])
    
    # TODO ELSA PRINT AND SAVE THIS PLOT
    #Light is original data points, dark is projected data points
    #shows how much "information" is discarded in this reduction of dimensionality.
    #TODO elsa fix this plot
    X_new = pca.inverse_transform(X_pca)
    plt.scatter(X[:, 0], X[:, 1], alpha=0.2, c='red', label="Discarded Information")
    plt.scatter(X_new[:, 0], X_new[:, 1], alpha=0.2, c='green', label="Information Kept")
    plt.axis('equal');
    plt.title('Information Discarded Via Dimensionality Reduction')
    plt.legend(loc="upper left")
    plt.show()
    plt.close()
    
    
    # TODO ELSA PRINT AND SAVE THIS PLOT
    pca = PCA(2)  # project from 1024 to 2 dimensions
    projected = pca.fit_transform(X)
    print(X.data.shape)
    print(projected.shape)
    plt.scatter(projected[:, 0], projected[:, 1],
            c=y, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('Accent', 10))
    plt.xlabel('component 1, flat img vector from a (1*704) matrix')
    plt.ylabel('component 2, flat img vector from a (1*704) matrix')
#     plt.colorbar();
    plt.title('Dimension Reduction from 704*1024 to 704*1 Matrix')
    plt.show()
    plt.close()
    
 