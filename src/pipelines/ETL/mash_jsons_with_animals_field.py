import json 
import pandas as pd
import pprint
import sys



#TODO SOMEHOW ADD [ and  ] and make sure there are not duplicates

with open("animal_id_48550215.json", "r+") as file:
    sys.stdout = open('../../../data/json/main_running.json', 'a')

    data_animal_id_48550215 = str(json.load(file))
    # print(type(data_animal_id_48550215))
    clean_48550215 = data_animal_id_48550215.replace('null', '"null"').replace("'", '"').replace('[]', '"[]"').replace("None", '"None"').replace('False', '"False"').replace('True', '"True"')
    animal_id_48550215 = clean_48550215 
    # print(animal_id_48550215[:521])
    print(clean_48550215 + ',' )
    sys.stdout.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

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