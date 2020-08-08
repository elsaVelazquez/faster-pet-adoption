# Python program to convert 
# JSON file to CSV 
  
  
import json 
import csv 

# json_file = '../../../data/json/json_dump/output_4828.JSON'

json_file = '../../../data/json/giant_json.json'
# output_4828.JSON
  
def json_to_csv(json_file):
    # Opening JSON file and loading the data 
    # into the variable data 
    #TODO push in only one_giant.json 
    # with open('../../../data/json/json_dump/output_4828.JSON') as json_file: 
    with open('../../../data/json/giant_json.json') as json_file: 

        data = json.load(json_file) 
    
    animals_data = data['animals'] 
    
    # now we will open a file for writing 
    # data_file = open('../../../data/csv/output_4828.csv', 'w') 
    data_file = open('../../../data/json/giant_json.csv', 'w') 

    
    # create the csv writer object 
    csv_writer = csv.writer(data_file) 
    
    # Counter variable used for writing  
    # headers to the CSV file 
    count = 0
    
    for animal in animals_data: 
        if count == 0: 
    
            # Writing headers of CSV file 
            header = animal.keys() 
            csv_writer.writerow(header) 
            count += 1
    
        # Writing data of CSV file 
        csv_writer.writerow(animal.values()) 
    
    data_file.close() 

json_to_csv(json_file)