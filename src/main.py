import os
from pipelines.data_ingestion.get_api_token import get_api_token
from pipelines.data_ingestion.crypt import crypt_it 
from pipelines.cleaning.text_file_to_string import text_file_to_string
from pipelines.data_structures.get_file_names import get_file_names
from pipelines.data_ingestion.scrape_by_animal_id import scrape_by_id

if __name__ == "__main__":
    '''   
    # MUST DO STEPS 1, 2 ON FIRST RUN ONLY

      1. paste your api key into crypt_copy.py, then rename the file crypt.py 
      !!IMPORTANT You should rename crypt_copy.py to crypt.py and leave crypt.py in the .gitignore file for security reasons.
    
      2. get api token
        1a. paste the key, generated in the command line , into main_ingestion.py
         in crypt_copy.py then rename the file as crypt.py ##!! note crypt.py is in .gitignore for security reasons
        2. scrape json 
    '''

    #grab your key
    start = crypt_it() 
    
    #generate a three-hour token
    three_hour_token = get_api_token(start)
    
    #data ingestion pipeline
    # scrape_by_animal_id.py
    animal_id = 48549546 #will search for this + the next 1000 animals
    scrape_by_id(animal_id) #scrape for 1000 records (per the API limit)
    data_ingestion_pipeline = 'src/pipelines/data_ingestion/scrape_by_animal_id.py'
    os.system(python data_ingestion_pipeline) #might want to keep this as a function to set animal ID from here
    
    #TODO elsa can i call these files like this?
    #data structures pipeline--> mash all single-record jsons together into 1 giant json
    data_structs_pipeline = 'src/pipelines/data_structures/create_one_json.py/create_one_json.py'
    os.system(python data_structs_pipeline)
    
    #data wrangling pipeline--> download images to local drive, push to the cloud
    data_wrangling_pipeline_get_imgs = 'src/pipelines/wrangling/get_images.py'
    os.system(python data_wrangling_pipeline)
    data_wrangling_pipeline_imgs_to_cloud = 'src/pipelines/wrangling/AWS/imgs_to_cloud.py'
    os.system(python data_wrangling_pipeline_imgs_to_cloud)
    
    
    

    
    #cleaning pipeline
    file_names = get_file_names(dirName='../data/txt')
    
    
    
    
    
    