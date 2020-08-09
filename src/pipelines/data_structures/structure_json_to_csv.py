# Python program to convert 
# JSON file to CSV 
  
  
import json 
import csv 
from pipelines.data_structures.get_file_names import get_file_names


json_file = '../../../data/json/json_dump/test_p8.json'
print(json_file)
# output_4828.JSON
  
def json_to_csv(json_file):
    # Opening JSON file and loading the data into the variable data 
    open_file = json_file
    with open(open_file) as json_file: 

        data = json.load(json_file) 
    
    animals_data = data['animals'] 
    
    #open a file for writing to
    data_file = open('../../../data/csv/aggregated_csv_1.csv', 'a+') 

    
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


if __name__ == "__main__":


file_names = get_file_names(dirName='../data/txt')

json_to_csv(json_file)
