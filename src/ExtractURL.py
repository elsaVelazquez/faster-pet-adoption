import os

total_calls = 300

curl_beginning = '\"Authorization: Bearer '

three_hour_token = 'blahblahblabhlbhalbha'

curl_end = '\"  https://api.petfinder.com/v2/animals?type=dog&page=' #api address



for i in range(1, total_calls+1):
    changing_page = i
    changing_page = str(i)
    curl_full = (f'curl -o  \'../data/json_dump/output_{i}.JSON\' -H ' + curl_beginning + three_hour_token + curl_end + changing_page)
    os.system(curl_full)
