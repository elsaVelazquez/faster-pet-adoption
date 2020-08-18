import os
from pipelines.data_ingestion.get_api_token import get_api_token
from pipelines.data_ingestion.crypt import crypt_it 
from pipelines.cleaning.text_file_to_string import text_file_to_string
from pipelines.data_structures.get_file_names import get_file_names
from pipelines.data_ingestion.scrape_by_animal_id import scrape_by_id

if __name__ == "__main__":
    '''   
    # MUST DO THE FOLLOWING ON FIRST RUN ONLY
        1. Paste your api key into crypt_copy.py.
        2. Rename the file to crypt.py .
        3. Leave crypt.py in gitignore for security reasons.
    '''

    #grab your key
    start = crypt_it() 
    
    #generate a three-hour token
    three_hour_token = get_api_token(start)
    
    #data ingestion pipeline--> scrape 1 JSON per animal, by animal id
    #add 1000 each day; automatically adds to the end of search, too
    animal_id = 48549546 #will search for this + the next 1000 animals
    scrape_by_id(animal_id) #scrape for 1000 records (per the API limit)
    # scrape_by_animal_id = 'src/pipelines/data_ingestion/scrape_by_animal_id.py'
    # os.system(python scrape_by_animal_id) #might want to keep this as a function to set animal ID from here
    
    
    #CLEANING
    #remove all errored out JSONS -(404-file not found, 429-exceeded rate, species==cat records)
    delete_invalid_json_files = 'src/pipelines/cleaning/delete_invalid_json_files.py'
    os.system(delete_invalid_json_files)
    #TODO elsa move this to README
    '''example output to console=
    ERROR cat record, deleted ../../../data/json/json_dump_by_animal/animal_id_48552870.JSON
    ERROR 404, deleted ../../../data/json/json_dump_by_animal/animal_id_48553125.JSON
    ERROR cat record, deleted ../../../data/json/json_dump_by_animal/animal_id_48552734.JSON
    ERROR 404, deleted ../../../data/json/json_dump_by_animal/animal_id_48552671.JSON
    ERROR 404, deleted ../../../data/json/json_dump_by_animal/animal_id_48553430.JSON
    ERROR 404, deleted ../../../data/json/json_dump_by_animal/animal_id_48553060.JSON
    '''
    
    #remove unnecessary json formatting
    #data structures
    json_to_string = 'src/pipelines/data_structures/json_to_string.py'
    os.system(json_to_string)
    #put everything into 1 giant json file
    #note: if there are issues, there is likely a badly formed json in the bunch
    #TODO elsa how do I print to a file
    #presently, I am copying output from above straight off the console and putting it into the file:
    # ../data/json/prepped_for_csv/all_dogs_copied_off_console.json
    #and adding enclosing [] to the entire output (remove final comma)
    json_to_csv = 'src/pipelines/data_structures/json_to_csv.py'
    os.system(json_to_csv)
    
    
    #EDA
    os.system(make_word_cloud.py)
    
    #saves the console output to data/csv/all_dogs_copied_off_console_json_to_csv.csv
    #copy and paste into own file named with this structure: 'data/csv/aggregated_csv_id_48549546_to_48553546.csv'
    #edit records manually 
    #TODO elsa figure out how to automate dropping bad records ^
    #copy and paste all new clean records to main csv---->    '../../../data/csv/running_main_csv.csv'
    
    
    
    
    
    
    
    
    
    
    
    #TODO elsa can i call these files like this?
    #data structures pipeline--> mash all single-record jsons together into 1 giant json
    data_structs_pipeline = 'src/pipelines/data_structures/create_one_json.py'
    os.system(python data_structs_pipeline)
    
    #data wrangling pipeline--> download images to local drive, push to the cloud
    data_wrangling_pipeline_get_imgs = 'src/pipelines/wrangling/get_images.py'
    os.system(python data_wrangling_pipeline)
    data_wrangling_pipeline_imgs_to_cloud = 'src/pipelines/wrangling/AWS/imgs_to_cloud.py'
    os.system(python data_wrangling_pipeline_imgs_to_cloud)
    
    
    # #removed all errored out JSONS
    # delete_invalid_json_files = 'src/pipelines/cleaning/delete_invalid_json_files.py'
    # os.system(delete_invalid_json_files)
    
    # #mash all jsons together into 1 giant json
    # create_one_json = 'src/pipelines/data_structures/create_one_json.py'
    # os.system(python create_one_json)
    
    #clean the json of any NaN or not found errors
    clean_giant_json = 'clean_giant_json.py' 
    os.system(python clean_giant_json > test.json)
    
    #turn the clean, giant json into a csv
    