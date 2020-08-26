import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.model_selection import train_test_split

from statsmodels.stats.outliers_influence import variance_inflation_factor   
from calculate_vif import calculate_vif_
from IPython.display import display


# from datetime import date
# import datetime

# from pandas import Timestamp

def read_in_csv(path):
    print(f"read in {path}")
    return pd.read_csv(path)


def draw_corr_heatmap(df, display=True):
    font_size = 16
    mpl.rcParams.update({'font.size': font_size})
    mpl.rcParams['xtick.labelsize'] = font_size-2
    mpl.rcParams['ytick.labelsize'] = font_size-2
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,10))
    # sns.heatmap(df.corr(), annot=False, fmt=".2f", ax=ax);
    sns.heatmap(df.corr(), fmt=".2f", ax=ax).set_title('VIF: Severity of Multicolinearity');
# VIF Heatmap of Dog Data Showing 
    
    if display:
        plt.show()
    else:
        plt.savefig(f'images/correlation_heatmap.png')  
    plt.close()



if __name__ == "__main__":
    
    path_csv = '../../../data/csv/giant_valid_csv.csv'
    
    df = read_in_csv(path_csv)
    
    df = df.dropna()

    print(df.columns)
    
    df = pd.get_dummies(df, columns=['status'])
    
    
    # 'status_adopted', 'gender_Male', 'age_Baby', 'age_Senior', 'age_Young',
    #    'size_Extra Large', 'size_Large', 'size_Small', 'coat_Long',
    #    'coat_None',
    
    # df = pd.get_dummies(df, columns=['breeds'])
    df = pd.get_dummies(df, columns=['gender'])
    df = pd.get_dummies(df, columns=['age'])
    df = pd.get_dummies(df, columns=['size'])
    df = pd.get_dummies(df, columns=['coat'])
    # df = pd.get_dummies(df, columns=['colors'])
    # df = pd.get_dummies(df, columns=['attributes'])
    # df = pd.get_dummies(df, columns=['environment'])
    # df = pd.get_dummies(df, columns=['tags'])
    # df = pd.get_dummies(df, columns=['name'])
    # df = pd.get_dummies(df, columns=['description'])

    df.drop(['organization_id', 'url', 'species', 'breeds', 'colors', 'name', 'environment', 'age_Senior', 'age_Baby',
       'tags', 'organization_animal_id', 'photos', 'description', 'id','age_Adult', 'size_Medium', 'size_Small', 
       'size_Large', 'primary_photo_cropped', 'videos', 'status_changed_at', 'attributes', 
       'published_at', 'distance', 'contact', '_links', 'type', 'status_adoptable', 'gender_Female', 'coat_None'], axis = 1, inplace=True)
   
    print(df.columns)

    df.rename(columns = {'gender_Male':'gender'}, inplace = True)
    df.rename(columns = {'size_Extra_Large':'size'}, inplace = True)
    df.rename(columns = {'age_Young':'age'}, inplace = True)

    X = df
    
    vif = calculate_vif_(X, thresh=5.0)
    
    draw_corr_heatmap(df)
    
    
    '''
    add this into the heatmask params declaration:
    To make a masked correlation heatmap:
mask = np.triu(np.ones_like(correlation_matrix.corr(), dtype=np.bool))
heat = sns.heatmap(correlation_matrix, mask=mask,
                       vmin=-1, vmax=1)
                       '''
    