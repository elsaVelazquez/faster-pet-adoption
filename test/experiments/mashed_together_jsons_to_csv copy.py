# Python program to convert 
# JSON file to CSV 


#does not work when started with "id"
  
  
import json 
import csv 
# from get_file_names import get_file_names


import os


def get_file_names(dir_name):
    '''
    For the given path, get the List of all files in the directory tree 
    '''
    # create a list of file and sub directories 
    # names in the given directory 
    files_list = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for file_n in files_list:
        # Create full path
        full_path = os.path.join(dir_name, file_n)
        # If file_n is a directory then get the list of files in this directory 
        if os.path.isdir(full_path):
            all_files = all_files + get_file_names(full_path)
        else:
            all_files.append(full_path)
    print(all_files)                
    return all_files  


# json_file = '../../../data/json/json_dump/test_p8.json'
# print(json_file)
# output_4828.JSON
  
  
  
def json_to_csv(json_file):
    # Opening JSON file and loading the data into the variable data 
    open_file = json_file
    with open(open_file) as json_file: 

        data = json.load(json_file) 
    
    animals_data = data['animal']
    # animals_data = data[0]

    
    
    #open a file for writing to
    # data_file = open('../../../data/csv/TESTING_MASHING_JSONS_TOGETHER.csv', 'a+') 
    data_file = open('../../../data/csv/TESTING_MASHING_JSONS_TOGETHER.csv', 'a+') 

    
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


    dirName = '../../../data/json/prepped_for_csv/' #all_dogs_copied_off_console.json'
    file_names = get_file_names(dirName)
    file_names
    
    # file_names = ['../../../data/json/json_dump/08_Aug_2020_21_05_146914.json', '../../../data/json/json_dump/08_Aug_2020_19_31_365859.json', '../../../data/json/json_dump/adopted_page9.json', '../../../data/json/json_dump/pipeline_test_data_4.json', '../../../data/json/json_dump/pipeline_test_data_8.json', '../../../data/json/json_dump/pipeline_test_data_9.json', '../../../data/json/json_dump/adopted_page4.json', '../../../data/json/json_dump/08_Aug_2020_20_51_037801.json', '../../../data/json/json_dump/pipeline_test_data_5.json', '../../../data/json/json_dump/adopted_page8.json', '../../../data/json/json_dump/08_Aug_2020_21_34_958713.json', '../../../data/json/json_dump/pipeline_test_data_2.json', '../../../data/json/json_dump/output_4956.JSON', '../../../data/json/json_dump/pipeline_test_data_3.json', '../../../data/json/json_dump/08_Aug_2020_21_26_825509.json', '../../../data/json/json_dump/output_4828.JSON', '../../../data/json/json_dump/08_Aug_2020_21_22_862614.json', '../../../data/json/json_dump/test_p8.json', '../../../data/json/json_dump/08_Aug_2020_22_08_145762.json', '../../../data/json/json_dump/08_Aug_2020_20_43_641331.json', '../../../data/json/json_dump/pipeline_test_data_1.json', '../../../data/json/json_dump/pipeline_test_data_6.json', '../../../data/json/json_dump/adopted_page10.json', '../../../data/json/json_dump/pipeline_test_data_11.json', '../../../data/json/json_dump/adopted_page7.json', '../../../data/json/json_dump/08_Aug_2020_21_54_089282.json', '../../../data/json/json_dump/08_Aug_2020_21_45_210638.json', '../../../data/json/json_dump/scraped_data_1_2020-08-08_03_06_22.json', '../../../data/json/json_dump/08_Aug_2020_20_43_472490.json', '../../../data/json/json_dump/adopted_page6.json', '../../../data/json/json_dump/08_Aug_2020_20_41_567897.json', '../../../data/json/json_dump/pipeline_test_data_10.json', '../../../data/json/json_dump/pipeline_test_data_7.json']

    # file_names = ['../../../data/json/json_dump_by_animal/animal_id_48549607.JSON', '../../../data/json/json_dump_by_animal/animal_id_48550426.JSON', '../../../data/json/json_dump_by_animal/animal_id_48550076.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549980.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549579.JSON', '../../../data/json/json_dump_by_animal/animal_id_48550308.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549596.JSON', '../../../data/json/json_dump_by_animal/animal_id_48550164.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549715.JSON', '../../../data/json/json_dump_by_animal/animal_id_48550021.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549650.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549996.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549979.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549580.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549703.JSON', '../../../data/json/json_dump_by_animal/animal_id_48550172.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549646.JSON', '../../../data/json/json_dump_by_animal/animal_id_48550037.JSON', '../../../data/json/json_dump_by_animal/animal_id_48550349.JSON', '../../../data/json/json_dump_by_animal/animal_id_48549884.JSON']
    for file in file_names:
        print("processing", file)
        json_to_csv(file)
        
    # print("done converting batch of json files")