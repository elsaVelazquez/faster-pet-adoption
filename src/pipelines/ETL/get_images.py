import requests
import bs4 as BeautifulSoup
import json

#TODO Elsa test this today 

if __name__ == "__main__":
    # breakpoint()
    with open(f"../../../data/json/main_running_json.json", "r") as f:
        dict_data = json.load(f)

        # len(dict_data)
        lst_urls = [] #TODO Delete?
        # dogs_count = 0 #TODO Delete?
        total_animals = len(dict_data)
        for i in range(total_animals) : 
            animal_id = dict_data[i]["animal"]["id"]
            # print(animal_id)

            if(dict_data[i]["animal"]["primary_photo_cropped"]) != "None" and dict_data[i]["animal"]["species"] == "Dog":
                animal_id = dict_data[i]["animal"]["id"]
                animal_status = dict_data[i]["animal"]["status"]
                url = (dict_data[i]["animal"]["primary_photo_cropped"]["medium"])
                lst_urls.append(url) #TODO Delete?
                # print(lst_urls)
                    
                r = requests.get(url)
                file_name = str(animal_id) + '_' +  animal_status
                # print(file_name)
                fname= (f'../../../data/img/img_dumps/{file_name}.jpg')
                
                with open(f"../../../data/img/img_dumps/{file_name}.jpg", "wb") as f:
                    f.write(r.content)
            else:
                pass