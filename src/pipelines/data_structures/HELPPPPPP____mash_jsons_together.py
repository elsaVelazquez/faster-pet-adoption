#TODO elsa HELLLLLLPPPPPP
#can't get it to put all jsons into 1 file 

import json
import glob
import os




directory = '../../../data/json/json_dump_by_animal'
# print(directory)
all_jsons = os.listdir(f'{directory}') 
print(all_jsons)
all_names = set() # use a set to avoid duplicates


import json
import glob

result = []
for f in glob.glob("../../../data/json/json_dump_by_animal/*.json"):
    with open(f, "r") as infile:
        try:
            result.append(json.load(infile))
        except ValueError:
            print(f)
        print(result)

        with open("merged_file.json", "w", encoding="utf8") as outfile:
            json.dump(result, outfile)



# # put all your files in there
# for filename in all_jsons:
#     try:
#         with open(filename, 'rt') as finput:
#             data = json.load(finput)
#         for animal in data.get('animal'):
#             all_names.add(animal.get('id'))
#     except Exception as exc:
#         print("Skipped file {} because exception {}".format(filename, str(exc)))
# print("***************************")
# print(all_names)

# directory = '../../../data/json/json_dump_by_animal'
# print(directory)
# all_jsons = os.listdir(f'{directory}') #[:10]
# for file in directory:
    
#     for all_dogs in all_jsons:
#         path = glob.glob(f'../../../data/json/json_dump_by_animal/*.JSON')
#         label = fruit_veg
#         get_fruits_veggies(X, y, path, label)



# result = []
# for f in glob.glob("../../../data/json/json_dump_by_animal/*.json"):
#     with open(f, "rb") as infile:
#         result.append(json.load(infile))

# with open("merged_file_mashed_jsons_together.json", "wb") as outfile:
#      json.dump(result, outfile)
     
     
     
     
# import glob
# glob_data = []
# for file in glob.glob('../../../data/json/json_dump_by_animal/*.json'):
#     with open(file) as json_file:
#         data = json.load(json_file)

#         i = 0
#         while i < len(data):
#             glob_data.append(data[i])
#             i += 1

# with open('merged_file_mashed_jsons_together.json', 'w') as f:
#     json.dump(glob_data, f, indent=4)