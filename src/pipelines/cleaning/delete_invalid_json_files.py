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

#good json
# text_file = open('../../../data/json/json_dump/animal_id_48549546.JSON','r')


#bad json
file_name = open('../../../data/json/json_dump/animal_id_48549547.JSON','r')

def delete_404_error_jsons(file_name):
    '''    https://www.journaldev.com/14408/python-read-file-open-write-delete-copy
    remove any JSONS that do not uphold key value structure of data-worthy API responses
    '''
    #get the list of line
    line_list = file_name.readlines();

    #for each line from the list, print the line
    for line in line_list:
        print(line) #already in string format
        if '"status":404' in line:
            print(f"ERROR, deleted {file_name}") # {file_name}")
        else:
            pass

    file_name.close() #close the file
    os.remove('../../../data/json/json_dump/animal_id_48549547.JSON') #delete status:404 JSON file with ERROR
    # print(f"ERROR, deleted {file_name}") # {file_name}")
    return None


delete_404_error_jsons(file_name)