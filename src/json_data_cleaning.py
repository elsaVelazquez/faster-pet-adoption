import json
from string import punctuation
import string 
import re #to grep URLs
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords = ENGLISH_STOP_WORDS


  
# Opening JSON file 
with open('/Users/elsa/Documents/faster-pet-adoption/data/api_dumps/api_dump_2020-07.json') as json_file: 
    data = json.load(json_file) 
  
    # for reading nested data [0] represents 
    # the index value of the list 
    print(data['animals'][0]) 
      
    # for printing the key-value pair of 
    # nested dictionary for looop can be used 
    print("\nPrinting nested dicitonary as a key-value pair\n") 
    for i in data['animals']: 
        print("id:", i['id']) 
        print("organization_animal_id", i['organization_animal_id'])
        print("photos:", i['photos']) 
        print("status_changed_at:", i['status_changed_at']) 
        print("description:", i['description']) 
        print("url:", i['url'])
        # print("total_count", i['total_count'])


        print() 




####################################################################
#please disregard everything below ^ line 
#i will remove it before Capstone 1


# def read_the_file(fname):
#     '''Reads the filename - should have a .txt extension.
#     Returns a text string containing the entire JSON output.
#     ''' 
#     f = open(fname, 'r')
#     textstring = f.read()
#     return textstring


# def lowercase_text(text):
#     '''Returns a text string with all characters lower-cased.
#     Organization IDs are in 
#     '''    
#     text_lowercased = text.lower()
#     return text_lowercased

# def remove_escape_char(text):
#     '''Remove \ from JSON dump'''
#     text_no_esc = text.replace('\/','/') #.replace("\"", '')
#     # print(text_no_esc)
#     return text_no_esc
    

# if __name__ == '__main__':
#     # to help test functions and pipeline:

#     #read in a sample scraped txt file
#     path_including_filename = "../data/api_dumps/api_dump_2018-10.txt"

#     #TODO put back after testing pipeline with test string text
#     text = read_the_file(path_including_filename)
#     text_ne = remove_escape_char(text)
#     # print(type(text_ne))
#     # print(text_ne)
    
#     # text_strp_end = text_ne[:-1]
    
#     str_to_dict = text_ne.replace("{\"animals\":[", '')
#     text_strp_end = str_to_dict[:-1]
#     dict1 = text_strp_end
#     print(type(dict1))
#     print(dict1)
    
    
    
    
    
    
    
    # print(type(text_strp_end))
    # print(text_strp_end)
    
    # print(json.dumps(text_strp_end,  sort_keys=True))

    # print(json.dumps(text_ne, indent=4))

    # text_ne = remove_escape_char(text)
    # for x in text:
    #   print(text[x])
    # print(text_ne)
    # print(json.dumps(text_ne))

    # x = text_ne
    # json.dumps(x, indent=4, separators=(",", "\\"))























# from string import punctuation
# import string 
# import re #to grep URLs
# from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
# stopwords = ENGLISH_STOP_WORDS

# def read_the_file(fname):
#     '''Reads the filename - should have a .txt extension.
#        Returns a text string containing the entire JSON output.
#     ''' 
#     f = open(fname, 'r')
#     textstring = f.read()
#     return textstring

# def lowercase_text(text):
#     '''Returns a text string with all characters lower-cased.
#        Organization IDs are in 
#     '''    
#     text_lowercased = text.lower()
#     return text_lowercased

# def remove_escape_char(text):
#     '''Remove \ from JSON dump'''
#     text_no_esc = text.replace('\/','/').replace("\"", '')
#     print(text_no_esc)
#     return text_no_esc

# #TODO not sure if to remove stop words
# def remove_stopwords(word_lst, stopwords_set):
#     '''Removes words from description if in the stopwords_set
#     '''
#     words_nsw = [(lambda x: re.sub(r'|'.join(stopwords_set), '', x))(x) for x in word_lst]
#     return words_nsw

# def grep_dog_data(text):
#     '''keep a dict per dog of:
#     petfinder dogs's IDs (int)
#     pet status (string)
#     dog description (string)
#     date into shelter (date)
#     date out of shelter (date)
#     img url (string)
    
#     '''  
#     pass

# def img_urls(text):
#     # lst_url = []
#     # lst_url = re.findall("(?P<url>https?://[^\s]+)", text)
#     # # lst_url = []
#     # # for url in str(text):
#     # #     for mask_url in str(text):
#     # #         lst_url.append(url) 
#     # # print(lst_url)
#     # return lst_url  
#     # findall() has been used  
#     # with valid conditions for urls in string 
#     lst_img_url = []
#     regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
#     url = re.findall(regex,text)
#     # print( [x[0] for x in url] )
#     print(url)
#     return url
    
 




# def download_imgs(text):
#     pass

# def df_dog_data(text):
#     pass

# if __name__ == '__main__':
#     # to help test functions and pipeline:
#     # text_str1 = "<kw>dance</kw> breaks during the school-day help her kids reset, \n and on Fridays, they usually do a 10-minute <kw>dance</kw> party.  "
#     # text = text_str1 #for testing pipline


#     #read in a sample scraped txt file
#     path_including_filename = "../data/api_dumps/api_dump_2018-10.txt"

#     #TODO put back after testing pipeline with test string text
#     text = read_the_file(path_including_filename)
#     # print(text)
    
#     #use test string to test pipeline
#     # text = '{"animals":[{"id":48504318,"organization_id":"TX487","url":"https:\/\/www.petfinder.com\/dog\/fiona-48504318\/tx\/san-antonio\/animal-care-services-division-city-of-san-antonio-tx487\/?referrer_id=5957d654-0b8d-4a02-bbae-6c7dd49e1074","type":"Dog","species":"Dog","breeds":{"primary":"Chihuahua","secondary":null,"mixed":true,"unknown":false},"colors":{"primary":null,"secondary":null,"tertiary":null},"age":"Adult","gender":"Female","size":"Small","coat":null,"attributes":{"spayed_neutered":false,"house_trained":false,"declawed":null,"special_needs":false,"shots_current":false},"environment":{"children":null,"dogs":null,"cats":null},"tags":[],"name":"FIONA","description":null,"organization_animal_id":"A579309","photos":[],"primary_photo_cropped":null,"videos":[],"status":"adoptable","status_changed_at":"2020-07-16T03:38:29+0000","published_at":"2020-07-16T03:38:29+0000","distance":null,"contact":{"email":"ACSAdoptions@sanantonio.gov","phone":"(210) 207-6666","address":{"address1":"4710 State Hwy 151","address2":null,"city":"San Antonio","state":"TX","postcode":"78227","country":"US"}},"_links":{"self":{"href":"\/v2\/animals\/48504318"},"type":{"href":"\/v2\/types\/dog"},"organization":{"href":"\/v2\/organizations\/tx487"}}},{"id":48504319,"organization_id":"TX487","url":"https:\/\/www.petfinder.com\/dog\/shiloh-48504319\/tx\/san-antonio\/animal-care-services-division-city-of-san-antonio-tx487\/?referrer_id=5957d654-0b8d-4a02-bbae-6c7dd49e1074","type":"Dog","species":"Dog","breeds":{"primary":"Chihuahua","secondary":null,"mixed":true,"unknown":false},"colors":{"primary":null,"secondary":null,"tertiary":null},"age":"Young","gender":"Male","size":"Small","coat":null,"attributes":{"spayed_neutered":false,"house_trained":false,"declawed":null,"special_needs":false,"shots_current":false},"environment":{"children":null,"dogs":null,"cats":null},"tags":[],"name":"SHILOH","description":null,"organization_animal_id":"A579308","photos":[],"primary_photo_cropped":null,"videos":[],"status":"adoptable","status_changed_at":"2020-07-16T03:38:29+0000","published_at":"2020-07-16T03:38:29+0000","distance":null,"contact":{"email":"ACSAdoptions@sanantonio.gov","phone":"(210) 207-6666","address":{"address1":"4710 State Hwy 151","address2":null,"city":"San Antonio","state":"TX","postcode":"78227","country":"US"}},"_links":{"self":{"href":"\/v2\/animals\/48504319"},"type":{"href":"\/v2\/types\/dog"},"organization":{"href":"\/v2\/organizations\/tx487"}}},{"id":48504293,"organization_id":"CA1722","url":"https:\/\/www.petfinder.com\/dog\/beasley-48504293\/ca\/rolling-hills-estates\/smooch-pooch-dog-rescue-ca1722\/?referrer_id=5957d654-0b8d-4a02-bbae-6c7dd49e1074","type":"Dog","species":"Dog","breeds":{"primary":"Maltese","secondary":"Yorkshire Terrier","mixed":true,"unknown":false},"colors":{"primary":"Yellow \/ Tan \/ Blond \/ Fawn","secondary":null,"tertiary":null},"age":"Adult","gender":"Male","size":"Small","coat":"Wire","attributes":{"spayed_neutered":true,"house_trained":true,"declawed":null,"special_needs":false,"shots_current":true},"environment":{"children":'
#     # print(text)
    
#     text_ne = remove_escape_char(text)
#     print(text_ne)
    
#     # listToStr = ' '.join([str(elem) for elem in text_ne]).replace(' ', '') 
  


#     # listToStr = ''.join(map(str, text_ne)) 
#     # print(type(listToStr))
#     # print(listToStr)
    
#     # #TODO help stopping grep where it's supposed to stop?
#     # lst_img_url = img_urls(listToStr)

    
    
#     # #TODO not returning a grepped list of url's
#     # print(type(lst_img_url))



#     # # example of list with img data:
#     # lst_imgs_urls = ['']
    
    
#     import json
    

#     # some JSON:
#     # x =  '{ "name":"John", "age":30, "city":"New York"}'

#     # parse x:
#     # y = json.loads(text)

#     # the result is a Python dictionary:
#     # print(y["animal"])
    
#     # json.dumps(text, indent=4)
    
    
    
