import json
from dictor import dictor

with open('big_json.json') as data:
    data = json.load(data)
    
#use photos_url as test string to clean json
photos_url = dictor(data, "id.photos.small")
print(photos_url)