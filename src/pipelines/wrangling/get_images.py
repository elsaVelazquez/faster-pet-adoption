import requests
import bs4 as BeautifulSoup
import json



if __name__ == "__main__":
    with open(f"../../../data/json/big_json_v3.json", "r") as f:
        dict_data = json.load(f)

        # len(dict_data)
        lst_urls = []
        dogs_count = 0
        total_animals = len(dict_data)
        for i in range(total_animals) : 
            animal_id = dict_data[i]["animal"]["id"]
            # print(animal_id)

            if(dict_data[i]["animal"]["primary_photo_cropped"]) != None and dict_data[i]["animal"]["species"] == "Dog":
                # dogs_count += 1
                animal_id = dict_data[i]["animal"]["id"]
                animal_status = dict_data[i]["animal"]["status"]
             
                
                
                url = (dict_data[i]["animal"]["primary_photo_cropped"]["medium"])
                lst_urls.append(url)
                # print(lst_urls)

                # for url in lst_urls:
                    
                r = requests.get(url)
                file_name = str(animal_id) + '_' +  animal_status
                print(file_name)
                with open(f"../../../data/img/img_dumps/{file_name}.jpg", "wb") as f:
                    f.write(r.content)
            else:
                pass








    # df.head()
    # df.info()

    # # for i in range(len(df)) : 
    # for i in range(5) : 
    #     print(df["animal"]["id"])

    #     animal_id=

    #     print(df[photos])
    #     ["small"]) 

    #     # url = "http://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Bundt_Cake_with_Grapes_001.jpg/267px-Bundt_Cake_with_Grapes_001.jpg?"
    #     url = df["photos"][0]

    #     r = requests.get(url)

    #     # with open(f"images/bundt_cake_{i}.jpg", "wb") as f:
            
    #     with open(f"../../../data/img/img_dumps/{animal_id}.jpg", "wb") as f:
            
    #     f.write(r.content)