import json 
import pandas as pd
import pprint
import sys
import os



#TODO SOMEHOW ADD [ and  ] and make sure there are not duplicates
path = '../../../data/json/json_dump_by_animal'

files_path = path = '../../../data/json/json_dump_by_animal/'

all_file_names = os.listdir(path)
# print(all_file_names)
for file in all_file_names:
    # print(file) #iterates through all files 
    full_path = files_path + file
    # print(full_path) #iterates through all files 
    with open(full_path, "r+") as file:
        # print("**********")
        # print(file)
        # print(full_path)
        temp_name = str(file)
        data_animal_id = temp_name.replace("<_io.TextIOWrapper name='../../../data/json/json_dump_by_animal/", 'data_').replace(".JSON' mode='r+' encoding='UTF-8'>", '')
        # print("^^^^^^^^^^^^^^^^^^^^")

        # print(data_animal_id)
        # print(type(temp_name))
        
        sys.stdout = open('../../../data/json/main_running_json.json', 'a')


        #turn the file name into the data_animal_id_XXX



        data_animal_id = str(json.load(file))
        # print(type(data_animal_id))
        clean_animal_id = data_animal_id.replace('null', '"null"').replace("'", '"').replace('[]', '"[]"').replace("None", '"None"').replace('False', '"False"').replace('True', '"True"')
        # animal_id_48550215 = clean_48550215 
        # print(clean_animal_id[:521])
        print(clean_animal_id + ',' )
        # sys.stdout.close()
    
    
    
    
    
    
    
#THIS  WORKS PERFECTLY FILE BY FILE
# with open("animal_id_48550215.json", "r+") as file:
#     sys.stdout = open('../../../data/json/main_running.json', 'a')

#     data_animal_id_48550215 = str(json.load(file))
#     # print(type(data_animal_id_48550215))
#     clean_48550215 = data_animal_id_48550215.replace('null', '"null"').replace("'", '"').replace('[]', '"[]"').replace("None", '"None"').replace('False', '"False"').replace('True', '"True"')
#     animal_id_48550215 = clean_48550215 
#     # print(animal_id_48550215[:521])
#     print(clean_48550215 + ',' )
#     sys.stdout.close()G
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# with open("animal_id_48550219.json", "r+") as file:
#     data_animal_id_48550219 = str(json.load(file))
#     print(type(data_animal_id_48550219))
#     clean_48550219 = data_animal_id_48550219.replace('null', '"null"').replace("'", '"').replace('[]', "'[]'").replace("None", '"None"')
#     print(clean_48550219)   

    # json_animal_id_48550215 = json.loads(clean_48550215)
    
    
    # with open("animal_id_48550219.json", "r+") as file:

    #     data_animal_id_48550219 = json.load(file)
    #     data_animal_id_48550215.update(data_animal_id_48550219)
    #     file.seek(0)
    #     json.dump(data_animal_id_48550215, file)

# result = json.dumps(dict_str)
# print(type(result))
# dict_str = str(a_dictionary)
# dict_str.replace("null", "Nothing")
# print(dict_str)
# json_dict = json.loads(dict_str)

# with open("animal_id_48550219.JSON", "r+") as file:
#     data = json.load(file)
#     data.update(a_dictionary)
#     file.seek(0)
#     json.dump(data, file)