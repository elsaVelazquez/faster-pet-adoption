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


#TODO why can't i put this in a function?
def delete_404_error_jsons(list_of_json_files):
    '''    https://www.journaldev.com/14408/python-read-file-open-write-delete-copy
    remove any JSONS that do not uphold key value structure of data-worthy API responses
    '''
    return None


if __name__ == "__main__":

    
    dir_name = '../../../data/json/json_dump/'

    list_of_files = get_file_names(dir_name)
            
    for file in range(len(list_of_files)):     
        file_name = list_of_files[file] 
        # print(file_name)
        with open(file_name, 'r') as file:
            zinput1 = '"status":404'
            zinput2 = '"status":429'
            for line in file:    
                if (zinput1 in line): # or (zinput2 in line): 
                    # print(line)
                    os.remove(file_name)
                    print(f"ERROR, deleted {file_name}") # {file_name}")
                if (zinput2 in line): # or (zinput2 in line): 
                    # print(line)
                    os.remove(file_name)
                    print(f"ERROR, deleted {file_name}")

            file.close()
                                    