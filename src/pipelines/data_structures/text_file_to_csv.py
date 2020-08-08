import pandas as pd

file_info = 'output_4699.txt'
file_info

def text_file_to_csv(file_info):
    
    read_file = pd.read_csv (file_info)
    read_file.to_csv ('output_4699.csv', index=None)
    
text_file_to_csv(file_info)



# arg_csv = str('r ' + file_info)
# arg_csv
# read_file = pd.read_csv(arg_csv )



# read_file = pd.read_csv('output_4699.txt')
# read_file.to_csv('output_4699.csv', index=None)




