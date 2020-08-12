
import os
from get_file_names import get_file_names
# from cleaning.string_cleaning import create_cleaned_textline_from_words 

def create_cleaned_textline_from_words(words):
    '''Takes in a list, returns a single string.
    '''
    text = ' '.join([word for word in words])
    return text

dirName = '../../../data/json/json_dump_by_animal';  
mash_jsons_together = get_file_names(dirName)

clean_mashed_json_str = create_cleaned_textline_from_words(mash_jsons_together) 

clean_mashed_json_str


# cmd_line_string = 'jq -s . ' + clean_mashed_json_str + '> big_json_v2.json'
#right now it is outputting into the data structures folder
cmd_line_string = 'jq -s . ' + clean_mashed_json_str + '> big_json_v3.json'
os.system(cmd_line_string)
