#conver json to text file

filename = "big_json_v4.json"
with open(filename, 'r') as fr:
    pre_ = fr.read()
    lines = pre_.split('\n')
    new_filename = filename.split('.')[0]+".txt" # To keep the same name except ext
    with open(new_filename, "a") as fw:
        fw.write("\n".join(lines))
        
        
        
        
import json 
import os
  
with open(filename, 'r') as file:
    
    data = file.read().replace('404', "'404'").replace("  },", "},").replace("{\"animal\": {", "").replace('"', "'").replace(",\n  {\n    'type': 'https://www.petfinder.com/developers/v2/docs/errors/ERR-'404'/',\n    'status': '404',\n    'title': 'Not Found',\n    'detail': 'Not Found'\n  }", '').replace("    'status': '404',", "").replace("    'title': 'Not Found',", '').replace("    'detail': 'Not Found'\n},", '').replace("  {\n    'type': 'https://www.petfinder.com/developers/v2/docs/errors/ERR-'404'/',\n\n\n", '').replace("'", '"')
    os.system('>' + 'test.json')
    # with open(filename, 'a') as clean_json.json:

print(data)
file.close()   
    
    # .replace("    'status': '404',", "")
    # 'title': 'Not Found',
    # 'detail': 'Not Found'
    
    
    # .replace(",\n  {\n    'type': 'https://www.petfinder.com/developers/v2/docs/errors/ERR-'404'/',\n    'status': '404',\n    'title': 'Not Found',\n    'detail': 'Not Found'\n},", ',')


    
    
    #.replace(",\n  {\n    'type': 'https://www.petfinder.com/developers/v2/docs/errors/ERR-'404'/',", '')
# replace(",  {    'type': 'https://www.petfinder.com/developers/v2/docs/errors/ERR-'404'/',    'status': '404',    'title': 'Not Found',    'detail': 'Not Found'},", ",")

#     data1.replace('"', "'")
# print(data1)
    # .replace("\{ \"type\": \"https://www.petfinder.com/developers/v2/docs/errors/ERR-404/","status": 404,"title": "Not Found","detail": "Not Found"\},", '')


# .replace(",\n  {\n    'type': 'https://www.petfinder.com/developers/v2/docs/errors/ERR-'404'/',\n    'status': '404',\n    'title': 'Not Found',\n    'detail': 'Not Found'\n  }", '')



# .replace(",\n  {\n    'type': 'https://www.petfinder.com/developers/v2/docs/errors/ERR-'404'/',\n    'status': '404',\n    'title': 'Not Found',\n    'detail': 'Not Found'\n},", ',')

print(data)



# print(y) 
# print(type(y))         
        
        
        

# replace("  },", "},")
# replace("{\"animal\": {", "") 

# replace("
# \{
#     "type": "https://www.petfinder.com/developers/v2/docs/errors/ERR-404/",
#     "status": 404,
#     "title": "Not Found",
#     "detail": "Not Found"
#   \},
# ", '')



import pandas as pd
df = pd.read_json (r'big_json_v4.json')
df_animal = df['animal']
df_animal.fillna(0)
 
print(df['animal'])
df.fillna(0)
 
# df_animal = df.pop(df['animal'])
# print (df_animal)