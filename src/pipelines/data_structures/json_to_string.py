import json 
import os

#TODO why does't get file names work here?
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
    # print(all_files)                
    return all_files  


# data/json/json_dump/animal_id_48549546.JSON
filename = "../../../data/json/json_dump/animal_id_48549546.JSON"
output_directory = '../../../data/json/json_dump/prepped_for_csv'

dir_name = '../../../data/json/json_dump_by_animal/'
list_of_files = get_file_names(dir_name)

def text_file_to_string(file):
    # for file in range(len(list_of_files)):     
#         file_name = list_of_files[file] 
    file_name = open(file, 'r')
    stop_beginning = "{\"animals\":["
    line = file_name.read().replace('{"animal":', '')
    stop_end = "}}}}"
    if line.endswith(stop_end):
        line = line[:-1]
        print(line)
        # cmd_line = line + '>' + output_directory +'test.json'
        # cmd_line = line + '>' +'test.json'
        #TODO elsa can't figure out how to print it to file directly
        # os.system(cmd_line)
    file_name.close()


# text_file_to_string(filename)

for x in range(len(list_of_files)):
    # print(list_of_files[x])
    current_file = list_of_files[x]
    text_file_to_string(current_file)
    print(",")

# for file in range(len(list_of_files)):     
#         file_name = list_of_files[file] 
#         # print(file_name)
#         with open(file_name, 'r') as file:
#             stop_beginning = "{\"animals\":["
#             stop_end = "}}}}"
#             for line in file:    
#                 if (stop_beginning in line): # or (zinput2 in line): 
#                     # print(line)
#                     # os.remove(file_name)
#                     # print(f"ERROR 404, deleted {file_name}") # {file_name}")
#                     line = file_name.read().replace('{"animal":', '')
#                 if (stop_end in line): # or (zinput2 in line): 
#                     print(line)
#                     # os.remove(file_name)
#                     # print(f"ERROR 429, deleted {file_name}")

#             file.close()
                                 

# with open(filename, 'r') as file:
    
#     data = file.read().replace('{"animal":', '')[:-1]
#     os.system('>' + output_directory +'test.json')
#     # with open(filename, 'a') as clean_json.json:

# print(data)
# file.close() 


# def text_file_to_string_many_records_in_one_file(filename):
#     stop_beginning = "{\"animals\":["
#     line = file.read().replace("\n", " ").replace(stop_beginning, '')
#     stop_end = "\"}}}}"
#     if line.endswith(stop_end):
#         line = line[:-166]
#     file.close()
#     print(line)










# filename = "big_json_v4.json"
# with open(filename, 'r') as fr:
#     pre_ = fr.read()
#     lines = pre_.split('\n')
#     new_filename = filename.split('.')[0]+".txt" # To keep the same name except ext
#     with open(new_filename, "a") as fw:
#         fw.write("\n".join(lines))
        
        
        
# filename =  '../../../data/json/json_dump_by_animal/animal_id_48549546_copy.JSON'

 