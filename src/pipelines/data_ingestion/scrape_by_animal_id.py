# import os

# animal_id = 48549546 



# #TODO Elsa test this script

# def scrape_by_id(animal_id):
    
#     last_id = animal_id + 1000 

#     curl_middle = "-H \"Authorization: Bearer "

#     three_hour_token =  open('cron/token.txt', 'r').read()

#     curl_end = '\"  https://api.petfinder.com/v2/animals/'

#     for i in list(range(animal_id, last_id+1)):
        
#         print(i)
#         animal_id = animal_id+1
#         curl_full = (f'curl -o  ../../../data/json/json_dump_by_animal/animal_id_{i}.JSON ' + curl_middle + three_hour_token + curl_end + str(i) ) #          + '&limit=100') #'>       ADOPTED.JSON 2>&1')

#         os.system(curl_full)
        
        
# if __name__ == "__main__":
        
# scrape_by_id(animal_id)       
    
    
    
    
#################
# . this worked perfectly:

import os

animal_id = 48549546 
last_id = animal_id + 1000 


curl_middle = "-H \"Authorization: Bearer "

three_hour_token =  open('cron/token.txt', 'r').read()

curl_end = '\"  https://api.petfinder.com/v2/animals/'

    

for i in list(range(animal_id, last_id+1)):
    
    print(i)
    animal_id = animal_id+1
    curl_full = (f'curl -o  ../../../data/json/json_dump_by_animal/animal_id_{i}.JSON ' + curl_middle + three_hour_token + curl_end + str(i) ) #          + '&limit=100') #'>       ADOPTED.JSON 2>&1')

    os.system(curl_full)