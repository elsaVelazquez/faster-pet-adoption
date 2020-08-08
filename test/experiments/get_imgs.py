import json
from string import punctuation
import string 
import re #to grep URLs
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords = ENGLISH_STOP_WORDS


  
# Opening JSON file 
files_lst = get_file_names(dirName)
for name in files_lst:
    
    with open(name) as json_file: 
        data = json.load(json_file) 
    
        # for reading nested data [0] represents 
        # the index value of the list 
        print(data['animals'][0]) 
        
        # for printing the key-value pair of 
        # nested dictionary for looop can be used 
        print("\nPrinting nested dicitonary as a key-value pair\n") 
        for i in data['animals']: 
            #the url link includes the id for relating data back to animal
            print("url:", i['url'])

            print() 