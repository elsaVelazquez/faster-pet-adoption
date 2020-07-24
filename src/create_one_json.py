
import os
from get_file_names import getListOfFiles
from string_cleaning import create_cleaned_textline_from_words 


dirName = '../data/json_dump';  
mash_jsons_together = getListOfFiles(dirName)

clean_mashed_json_str = create_cleaned_textline_from_words(mash_jsons_together) 

clean_mashed_json_str


cmd_line_string = 'jq -s . ' + clean_mashed_json_str + '> big_json.json'
os.system(cmd_line_string)
