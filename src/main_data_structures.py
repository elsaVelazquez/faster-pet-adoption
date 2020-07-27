
import pandas as pd
from pipelines.data_structures.structure_json_to_csv import json_to_csv

#get one big json

#turn it into a csv

#turn csv into pandas df

if __name__ == "__main__":
    
    #enter file directory relative to /src
    big_json_file = '../../../data/big_json.json'
    
    
    #turn jsons into csv's
    
    # create_csv = json_to_csv(big_json_file)
    
    #turn csv's into df
    df_animals = pd.read_csv("pipelines/data_structures/v1_animals_data.csv")
    
    # print(df_animals.columns)    
    '''
    Index(['id', 'organization_id', 'url', 'type', 'species', 'breeds', 'colors',
       'age', 'gender', 'size', 'coat', 'attributes', 'environment', 'tags',
       'name', 'description', 'organization_animal_id', 'photos',
       'primary_photo_cropped', 'videos', 'status', 'status_changed_at',
       'published_at', 'distance', 'contact', '_links'],
      dtype='object')
    '''