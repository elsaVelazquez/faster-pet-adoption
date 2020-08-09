# Python program to convert 
# JSON file to CSV 
  
  
import json 
import csv 
from get_file_names import get_file_names


# json_file = '../../../data/json/json_dump/test_p8.json'
# print(json_file)
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


    # file_names = get_file_names(dirName='../../../data/json/json_dump')
    # file_names
    
    file_names = ['../../../data/json/json_dump/08_Aug_2020_21_05_146914.json', '../../../data/json/json_dump/08_Aug_2020_19_31_365859.json', '../../../data/json/json_dump/adopted_page9.json', '../../../data/json/json_dump/pipeline_test_data_4.json', '../../../data/json/json_dump/pipeline_test_data_8.json', '../../../data/json/json_dump/pipeline_test_data_9.json', '../../../data/json/json_dump/adopted_page4.json', '../../../data/json/json_dump/08_Aug_2020_20_51_037801.json', '../../../data/json/json_dump/pipeline_test_data_5.json', '../../../data/json/json_dump/adopted_page8.json', '../../../data/json/json_dump/08_Aug_2020_21_34_958713.json', '../../../data/json/json_dump/pipeline_test_data_2.json', '../../../data/json/json_dump/output_4956.JSON', '../../../data/json/json_dump/pipeline_test_data_3.json', '../../../data/json/json_dump/08_Aug_2020_21_26_825509.json', '../../../data/json/json_dump/output_4828.JSON', '../../../data/json/json_dump/08_Aug_2020_21_22_862614.json', '../../../data/json/json_dump/test_p8.json', '../../../data/json/json_dump/08_Aug_2020_22_08_145762.json', '../../../data/json/json_dump/08_Aug_2020_20_43_641331.json', '../../../data/json/json_dump/pipeline_test_data_1.json', '../../../data/json/json_dump/pipeline_test_data_6.json', '../../../data/json/json_dump/adopted_page10.json', '../../../data/json/json_dump/pipeline_test_data_11.json', '../../../data/json/json_dump/adopted_page7.json', '../../../data/json/json_dump/08_Aug_2020_21_54_089282.json', '../../../data/json/json_dump/08_Aug_2020_21_45_210638.json', '../../../data/json/json_dump/scraped_data_1_2020-08-08_03_06_22.json', '../../../data/json/json_dump/08_Aug_2020_20_43_472490.json', '../../../data/json/json_dump/adopted_page6.json', '../../../data/json/json_dump/08_Aug_2020_20_41_567897.json', '../../../data/json/json_dump/pipeline_test_data_10.json', '../../../data/json/json_dump/pipeline_test_data_7.json']

    for file in file_names:
        print("processing", file)
        # json_to_csv(file)
        
    print("done converting batch of json files")