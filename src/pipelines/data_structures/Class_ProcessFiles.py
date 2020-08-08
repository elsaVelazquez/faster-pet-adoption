from pipelines.data_structures.text_file_to_string import text_file_to_string
from pipelines.data_structures.text_file_to_csv import text_file_to_csv

file_info = '../data/txt/pipeline_test_data_3.txt'

Class ProcessFiles:
    '''A class for turning scrape files into useable PySpark data strucures'''
    
    
    def __init__(self, name=file_info):
        '''Initialize the file as a text file'''
        self.name = name #create instance variable
        
    def text_file_to_string(self):
        # stop_beginning = "{\"animals\":["
        # line = file.read().replace("\n", " ").replace(stop_beginning, '')
        # stop_end = "\"}}}}"
        # if line.endswith(stop_end):
        #     line = line[:-166]
        # file.close()
        # print(line)
        print("text file has been stripped correctly")
        return text_file_to_string(self)
            
    
    def text_file_to_csv(self):
        return text_file_to_csv(self)
        