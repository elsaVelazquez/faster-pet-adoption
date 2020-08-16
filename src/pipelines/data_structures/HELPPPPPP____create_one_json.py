#TODO elsa HELLLLLLPPPPPP
#can't get it to put all jsons into 1 file 


#TODO why doesn't get file names work???
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




import os
# from get_file_names import get_file_names
# from cleaning.string_cleaning import create_cleaned_textline_from_words 

def create_cleaned_textline_from_words(words):
    '''Takes in a list, returns a single string.
    '''
    text = ' '.join([word for word in words])
    return text


if __name__ == '__main__':
    
    
    # dirName = '../../../data/json/json_dump' #_by_animal'
    dirName =  '../../../data/json/prepped_for_csv/' #all_dogs_copied_off_console.json'
    # dirName = '../../../data/json/json_dump'

    # print(dirName)
    mash_jsons_together = get_file_names(dirName)
    # print(mash_jsons_together)


    clean_mashed_json_str = create_cleaned_textline_from_words(mash_jsons_together) 

    # print(clean_mashed_json_str)

    # #jq will output any compile errors 
    # cmd_line_string = 'jq -s  ' + clean_mashed_json_str + '> mashed_jsons_together.json'
    # cmd_line_string = 'cat' + clean_mashed_json_str + '> mashed_jsons_together.json'

    # print(cmd_line_string)

    # # # #right now it is outputting into the data structures folder
    cmd_line_string = 'jq -s  ' + clean_mashed_json_str + '> clean_json_49546to_54546.json' #../../../data/json/clean_json_49546to_54546.json'
    # cmd_line_string = 'cat ' + clean_mashed_json_str + '> mashed_jsons_together.json'
    # print(cmd_line_string)
    os.system(cmd_line_string)
