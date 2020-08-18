

import numpy as np
import pandas as pd
from skimage.io import imread

def read_df(path):
    '''read in file
    '''
    print('read df')
    return pd.read_csv(path) #, parse_dates=True, squeeze=True) 

def explore_data(df):
    print(df.head())
    return df

def create_main_dataframe(df):
    # df.fillna("NothingEntered")
    df_fillna = df.fillna("NothingEntered")
    df_fillna.drop(['photos', 'videos', 'distance', 'status_changed_at', 'published_at', 'distance', 'contact', 'organization_animal_id', 'type', 'photos'], axis = 1, inplace= True)
    df_dummies = pd.get_dummies(df_fillna, columns=['status'])
    y = df_dummies.pop("status_adopted")
    df_dummies = df_dummies.drop('status_adoptable', axis=1)
    X = df_dummies.values
    print(df_dummies.info())
    return X, y

if __name__ == "__main__":

    df = read_df('../../../data/csv/running_main_csv.csv')

    explore_data(df)

    print("************")

    X, y_adopted = create_main_dataframe(df)

    print(y_adopted)
    print(X)
    
    #to call this from another function 


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


    #sample of df.info()
     #   Column           Non-Null Count  Dtype
        # ---  ------           --------------  -----
        # 0   id               165 non-null    int64
        # 1   organization_id  165 non-null    object
        # 2   url              165 non-null    object
        # 3   species          165 non-null    object
        # 4   breeds           165 non-null    object
        # 5   colors           165 non-null    object
        # 6   age              165 non-null    object
        # 7   gender           165 non-null    object
        # 8   size             165 non-null    object
        # 9   coat             79 non-null     object
        # 10  attributes       165 non-null    object
        # 11  environment      165 non-null    object
        # 12  tags             165 non-null    object
        # 13  name             165 non-null    object
        # 14  description      151 non-null    object
        # 15  photos           165 non-null    object
        # 16  status           165 non-null    object
        # 17  _links           165 non-null    object