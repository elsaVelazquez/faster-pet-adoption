import main_ingestion
import main_data_structures

from pipelines.data_ingestion.get_api_token import get_api_token
from pipelines.data_ingestion.crypt import crypt_it 

from pipelines.cleaning.text_file_to_string import text_file_to_string

from pipelines.data_structures.get_file_names import get_file_names
#first run main_ingestion.py
    #ingestion pipeline:
    # 1. paste your api key into crypt_copy.py, then rename the file crypt.py 
    # !!IMPORTANT You should rename crypt_copy.py to crypt.py and leave crypt.py in the .gitignore file for security reasons.
    
    # 2. get api token
        #     1a. paste the key, generated in the command line , into main_ingestion.py
        #  in crypt_copy.py then rename the file as crypt.py ##!! note crypt.py is in .gitignore for security reasons
        # 2. scrape json 
        
        


    #get a token
    # pass 

    start = crypt_it()
    
    
    
    #change three_hour_token accordingly
    three_hour_token = get_api_token(start)
    
    
    
    #data ingestion pipeline
    #TODO . how do i turn this into some batch or cron job?
    #files need to come in as text files
    
    #cleaning pipeline
    file_names = get_file_names(dirName='../data/txt')
    
    
    
    
    
    