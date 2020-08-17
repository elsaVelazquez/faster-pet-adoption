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

from skimage.io import imread

# from wordcloud import WordCloud
# from make_word_cloud.wordcloud import WordCloud


def read_df(path):
    '''read in file
    '''
    print('read df')
    return pd.read_csv(path) #, parse_dates=True, squeeze=True) 

def explore_data(df):
    print(df.head())
    return df

def make_X_and_y(df):
    # df.fillna("NothingEntered")
    # df.drop(['photos', 'videos', 'distance', 'status_changed_at', 'published_at', 'distance', 'contact', 'organization_animal_id', 'type', 'photos'], axis = 1, inplace= True)
    df = pd.get_dummies(df, columns=['status'])
    y = df.pop("status_adopted")
    df = df.drop('status_adoptable', axis=1)
    X = df.values
    return X, y

if __name__ == "__main__":

    df = read_df('../../../data/csv/running_main_csv.csv')

    explore_data(df)

    # df.drop(['photos', 'videos', 'status_changed_at', 'published_at', 'distance', 'contact', 'organization_animal_id', 'type', 'photos'], axis = 1, inplace= True)
    # df.info()
    
    df_fillna = df.fillna("NothingEntered")
    
    # df_fillna = df.fillna("NothingEntered")
    print("************")
    # print(df_fillna.info())
    
    df_fillna.drop(['photos', 'videos', 'distance', 'status_changed_at', 'published_at', 'distance', 'contact', 'organization_animal_id', 'type', 'photos'], axis = 1, inplace= True)
    print(df_fillna.info())



    # #TODO elsa how do I put everything through to get turned into flattened imgs
    # ravel_photos_df = df['primary_photo_cropped']
    # print("*************")
    
    # # print(type(ravel_photos_df))
                    
                    
    # photos_df = np.array(ravel_photos_df)
    # print(photos_df['primary_photo_cropped'])
    # print(type(photos_df))
    # from skimage.io import imread
    
    # for x in range(len(photos_df)):
    #     print(photos_df)


    # image = imread(r"../data/scraped_dog_adoption_petfinder_img_files/test_img.jpg")
    # # show_img(image)
    # red, yellow =   image.copy(), image.copy()
    # red[:,:,(1,2)] = 0
    # yellow[:,:,2]=0
    # # show_images(images=[red,yellow], titles=['Red Intensity','Yellow Intensity'])
    # from skimage.color import rgb2gray
    # gray_image = rgb2gray(image)
    # # show_images(images=[image,gray_image],titles=["Color","Grayscale"])
    # print("Colored image shape:", image.shape)
    # print("Grayscale image shape:", gray_image.shape)
    # print(image)                
                    
                    
                    

    # df = pd.get_dummies(df, columns=['status'])
    # print(df)
    # X, y_adopted = make_X_and_y(df)

    # print(y_adopted)
    # print(X)