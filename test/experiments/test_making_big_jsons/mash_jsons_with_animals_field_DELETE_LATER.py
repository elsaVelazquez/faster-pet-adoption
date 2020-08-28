import json 
import pandas as pd

# dict_str = pd.DataFrame({"animal":{"id":48550215,"organization_id":"PA142","url":"https:\/\/www.petfinder.com\/cat\/bertha-48550215\/pa\/york\/york-county-spca-pa142\/?referrer_id=5957d654-0b8d-4a02-bbae-6c7dd49e1074","type":"Cat","species":"Cat","breeds":{"primary":"Domestic Short Hair","secondary":null,"mixed":false,"unknown":false},"colors":{"primary":"Brown \/ Chocolate","secondary":null,"tertiary":null},"age":"Adult","gender":"Female","size":"Medium","coat":null,"attributes":{"spayed_neutered":true,"house_trained":false,"declawed":false,"special_needs":false,"shots_current":true},"environment":{"children":null,"dogs":null,"cats":null},"tags":[],"name":"Bertha","description":"I was brought into the shelter because my owner is ill and can no longer care for me. I am...","organization_animal_id":"YORK-A-263","photos":[{"small":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/1\/?bust=1597179667\u0026width=100","medium":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/1\/?bust=1597179667\u0026width=300","large":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/1\/?bust=1597179667\u0026width=600","full":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/1\/?bust=1597179667"},{"small":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/2\/?bust=1597179677\u0026width=100","medium":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/2\/?bust=1597179677\u0026width=300","large":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/2\/?bust=1597179677\u0026width=600","full":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/2\/?bust=1597179677"}],"primary_photo_cropped":{"small":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/1\/?bust=1597179667\u0026width=300","medium":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/1\/?bust=1597179667\u0026width=450","large":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/1\/?bust=1597179667\u0026width=600","full":"https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/48550215\/1\/?bust=1597179667"},"videos":[],"status":"adoptable","status_changed_at":"2020-07-21T13:50:18+0000","published_at":"2020-07-21T13:50:18+0000","distance":null,"contact":{"email":"sslate@ycspca.org","phone":"(717) 764-6109","address":{"address1":"3159 N. Susquehanna Trail","address2":null,"city":"York","state":"PA","postcode":"17406","country":"US"}},"_links":{"self":{"href":"\/v2\/animals\/48550215"},"type":{"href":"\/v2\/types\/cat"},"organization":{"href":"\/v2\/organizations\/pa142"}}}})

import json
import pprint

# with open('animal_id_48550215.json', "r+") as f:
#     data_animal_id_48550215 = json.load(f)
#     pprint.pprint(data_animal_id_48550215["animal"])
#     # print(data['animal'])

# with open('animal_id_48550215.json') as f:
#     data_animal_id_48550215 = json.load(f)
#     pprint.pprint(data_animal_id_48550215["animal"])

import sys
path = 'data/json/json_dump_by_animal'
all_file_names = os.listdir(path)
with open("animal_id_48550215.json", "r+") as file:
    sys.stdout = open('some.json', 'a')

    data_animal_id_48550215 = str(json.load(file))
    # print(type(data_animal_id_48550215))
    clean_48550215 = data_animal_id_48550215.replace('null', '"null"').replace("'", '"').replace('[]', '"[]"').replace("None", '"None"').replace('False', '"False"').replace('True', '"True"')
    animal_id_48550215 = clean_48550215 
    # print(animal_id_48550215[:521])
    print(clean_48550215 + ',' )
    sys.stdout.close()

# with open("animal_id_48550219.json", "r+") as file:
#     data_animal_id_48550219 = str(json.load(file))
#     print(type(data_animal_id_48550219))
#     clean_48550219 = data_animal_id_48550219.replace('null', '"null"').replace("'", '"').replace('[]', "'[]'").replace("None", '"None"')
#     print(clean_48550219)   

    # json_animal_id_48550215 = json.loads(clean_48550215)
    
    
    # with open("animal_id_48550219.json", "r+") as file:

    #     data_animal_id_48550219 = json.load(file)
    #     data_animal_id_48550215.update(data_animal_id_48550219)
    #     file.seek(0)
    #     json.dump(data_animal_id_48550215, file)

# result = json.dumps(dict_str)
# print(type(result))
# dict_str = str(a_dictionary)
# dict_str.replace("null", "Nothing")
# print(dict_str)
# json_dict = json.loads(dict_str)

# with open("animal_id_48550219.JSON", "r+") as file:
#     data = json.load(file)
#     data.update(a_dictionary)
#     file.seek(0)
#     json.dump(data, file)