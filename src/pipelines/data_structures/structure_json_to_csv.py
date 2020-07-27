# Python program to convert 
# JSON file to CSV 
  
  
import json 
import csv 
  
def json_to_csv(json_file):
    # Opening JSON file and loading the data 
    # into the variable data 
    #TODO push in only one_giant.json 
    with open('../../../data/json_dump/output_4699.JSON') as json_file: 
        data = json.load(json_file) 
    
    animals_data = data['animals'] 
    
    # now we will open a file for writing 
    data_file = open('animals_data.csv', 'w') 
    
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