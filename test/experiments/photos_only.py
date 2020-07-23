import json
from dictor import dictor

with open('big_json.json') as data:
    data = json.load(data)
    
photos_url = dictor(data, "id.photos.small")
print(photos_url)