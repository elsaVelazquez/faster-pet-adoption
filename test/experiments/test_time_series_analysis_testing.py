


import numpy as np
import pandas as pd
from io import StringIO
import datetime
from datetime import datetime
import time
from datetime import datetime, date, time, timedelta
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def read_df(path):
    '''read in file
    '''
    print('read df')
    return pd.read_csv(path) #, parse_dates=True, squeeze=True) 

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
    
    # df = read_df('../../../data/csv/aggregated_csv_1_copy_3.csv') #aggregated_csv_1.csv') #TODO elsa other csv are not working right, why
    # df = read_df('../../../data/csv/aggregated_csv_1_copy_3.csv') 
    # df = read_df('../../../data/csv/time_series_csv.csv') 
    df = read_df('../../../data/csv/time_series_adopted_csv.csv') 

    
    
    # df = read_df('../../../data/csv/running_main_csv.csv')

    # explore_data(df)
    ##################################################################################

    
    year = '2020'
    y = create_time_year(year)
    print(y) 
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    
    #set every day to time 0/ midnight
    
    #TODO elsa
    #in our new csv, running_main_csv.csv, 
    # we need all the dates to look like this: 2020-08-07T02:49:12+0000
    # so we will tak the column df_normalised = df['date']
    # turn it into a string, 
    # slice to omit the end and replace that with  T02:49:12+0000
    
    

    df['date'] = pd.to_datetime(df['status_changed_at'], infer_datetime_format=True).dt.normalize()
    df_normalised = df['date']
    
    
    
    #THIS CODE IS CORRECTLY CHANGING DATETIME AS A STRING BUT THEN DOESN'T WORK WITH REST OF THE CODE
    # I THINK CUZ IT'S NOT IN VALID DATETIME FORM BUT IT DOESN'T SEEM IT SHOULD MATTER
    #POSSIBLY CHANGE IT AS A DATAFRAME BEFORE EVEN SENDING IT HERE
    # normalization_mask = 'T02:49:12+0000'
    # for x in range(len(df_normalised)):
    #     df_normalised[x] = str(df_normalised[x])
    #     df_normalised[x] = df_normalised[x][:-9]
    #     df_normalised[x] = df_normalised[x] + normalization_mask 
    #     # df_normalised[x] = pd.to_datetime(df_normalised[x])
    #     print(df_normalised[x])
  
  
  #THE CONTENTS OF THE WORKING running_main_csv.csv
# id,organization_id,url,type,species,breeds,colors,age,gender,size,coat,attributes,environment,tags,name,description,organization_animal_id,photos,primary_photo_cropped,videos,status,status_changed_at,published_at,distance,contact,_link
# 48719630,MN330,https://www.petfinder.com/dog/milo-48719630/mn/brooklyn-center/no-dog-left-behind-rescue-h-mn330/?referrer_id=5957d654-0b8d-4a02-bbae-6c7dd49e1074,Dog,Dog,"{'primary': 'Mountain Cur', 'secondary': None, 'mixed': True, 'unknown': False}","{'primary': None, 'secondary': None, 'tertiary': None}",Baby,Male,Large,,"{'spayed_neutered': True, 'house_trained': True, 'declawed': None, 'special_needs': False, 'shots_current': True}","{'children': True, 'dogs': True, 'cats': True}",[],Milo,You can fill out an adoption application online on our official website.Milo is a perfect puppy! He is a mix...,15770362-3267,"[{'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/1/?bust=1596855564&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/1/?bust=1596855564&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/1/?bust=1596855564&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/1/?bust=1596855564'}, {'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/3/?bust=1596855564&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/3/?bust=1596855564&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/3/?bust=1596855564&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/3/?bust=1596855564'}, {'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/2/?bust=1596855565&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/2/?bust=1596855565&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/2/?bust=1596855565&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/2/?bust=1596855565'}]","{'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/1/?bust=1596855564&width=300', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/1/?bust=1596855564&width=450', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/1/?bust=1596855564&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48719630/1/?bust=1596855564'}",[],adopted,2020-08-07T02:49:12+0000,2020-08-08T02:49:12+0000,,"{'email': 'info@NDLBrescue.org', 'phone': '(612) 354-6352', 'address': {'address1': 'PO Box 29461', 'address2': None, 'city': 'Brooklyn Center', 'state': 'MN', 'postcode': '55429', 'country': 'US'}}","{'self': {'href': '/v2/animals/48719630'}, 'type': {'href': '/v2/types/dog'}, 'organization': {'href': '/v2/organizations/mn330'}}"
# 48550730,KY519,https://www.petfinder.com/dog/louie-48550730/oh/cincinnati/little-hills-of-kentucky-animal-rescue-inc-ky519/?referrer_id=5957d654-0b8d-4a02-bbae-6c7dd49e1074,Dog,Dog,"{'primary': 'Labrador Retriever', 'secondary': 'Black Mouth Cur', 'mixed': True, 'unknown': False}","{'primary': None, 'secondary': None, 'tertiary': None}",Young,Male,Medium,,"{'spayed_neutered': True, 'house_trained': True, 'declawed': None, 'special_needs': False, 'shots_current': True}","{'children': True, 'dogs': True, 'cats': True}",[],Louie,Louie is 15 months old and 42 lbs. He is a German Shepherd/Black Mouth Curr mix. He is friendly and...,,"[{'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/3/?bust=1595361932&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/3/?bust=1595361932&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/3/?bust=1595361932&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/3/?bust=1595361932'}, {'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/1/?bust=1595361739&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/1/?bust=1595361739&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/1/?bust=1595361739&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/1/?bust=1595361739'}, {'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/2/?bust=1595361743&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/2/?bust=1595361743&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/2/?bust=1595361743&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/2/?bust=1595361743'}]","{'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/3/?bust=1595361932&width=300', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/3/?bust=1595361932&width=450', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/3/?bust=1595361932&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48550730/3/?bust=1595361932'}",[],adopted,2020-08-07T02:49:12+0000,2020-07-21 20:05:39+00:00,,"{'email': 'lhkyrescue@gmail.com', 'phone': None, 'address': {'address1': None, 'address2': None, 'city': 'Cincinnati', 'state': 'OH', 'postcode': '45211', 'country': 'US'}}","{'self': {'href': '/v2/animals/48550730'}, 'type': {'href': '/v2/types/dog'}, 'organization': {'href': '/v2/organizations/ky519'}}"
# 48551137,NM42,https://www.petfinder.com/dog/copper-48551137/nm/las-cruces/animal-service-center-of-the-mesilla-valley-nm42/?referrer_id=5957d654-0b8d-4a02-bbae-6c7dd49e1074,Dog,Dog,"{'primary': 'Mixed Breed', 'secondary': None, 'mixed': False, 'unknown': False}","{'primary': 'Black', 'secondary': 'White / Cream', 'tertiary': None}",Adult,Female,Medium,,"{'spayed_neutered': False, 'house_trained': False, 'declawed': None, 'special_needs': False, 'shots_current': True}","{'children': None, 'dogs': None, 'cats': None}",[],Copper,,ASC-A-29708,"[{'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48551137/1/?bust=1597340741&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48551137/1/?bust=1597340741&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48551137/1/?bust=1597340741&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48551137/1/?bust=1597340741'}]","{'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48551137/1/?bust=1597340741&width=300', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48551137/1/?bust=1597340741&width=450', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48551137/1/?bust=1597340741&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/48551137/1/?bust=1597340741'}",[],adoptable,2020-07-21T02:49:12+0000,2020-07-21 15:35:14+00:00,,"{'email': 'pdeal@las-cruces.org', 'phone': '(575) 382-0018', 'address': {'address1': '3551 Bataan Memorial West', 'address2': None, 'city': 'Las Cruces', 'state': 'NM', 'postcode': '88012', 'country': 'US'}}","{'self': {'href': '/v2/animals/48551137'}, 'type': {'href': '/v2/types/dog'}, 'organization': {'href': '/v2/organizations/nm42'}}"
  
    
    
    df_dates = pd.DataFrame([df_normalised]).T
    print("%%%%%%%%%%%%%%%%%%%%%%%%")

    print(df_dates)
    print("%%%%%%%%%%%%%%%%%%%%%%%%")
    
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

    fig.savefig("../../../src/readme/capstone_2_readme/ADOPTED_dogs_dog_adoption_trends_time_series.png")
