#remove external dictionary key "animal" to pump into pyspark pipeline more easily
#commmand line prompt to print out one giant json file with all data
# . from src folder
#   python json_data_cleaning.py > ../data/one_giant_json.JSON


import json
from string import punctuation
import string 
# import re #to grep URLs
# from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
# stopwords = ENGLISH_STOP_WORDS


print('[')
# Opening JSON files
for i in range(1, 20): 
    file_location = (f'/Users/elsa/Documents/faster-pet-adoption/data/json_dump/output_{i}.JSON')
    with open(file_location) as json_file: 
        data = json.load(json_file) 
    
        # for reading nested data [0] represents 
        # the index value of the list 
        print(data['animals'][i]) 
        print(',')
 
    # for printing the key-value pair of 
    # nested dictionary for looop can be used 
    # print("\nPrinting nested dicitonary as a key-value pair\n") 
    # for i in data['animals']: 
    #     print("id:", i['id']) 
    #     print("organization_animal_id", i['organization_animal_id'])
    #     print("photos:", i['photos']) 
    #     print("status_changed_at:", i['status_changed_at']) 
    #     print("description:", i['description']) 
    #     print("url:", i['url'])
        # print("total_count", i['total_count'])


    # print() 


