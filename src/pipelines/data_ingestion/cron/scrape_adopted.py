#for the following cron job
#10, 20, 30, 40, 50 * * * * scrape_adopted.py > "../data/json/json_dump/$(date +\%d\%m\%y_\%H\%M\%S).json" 2>&1

# curl_beginning = 'curl -o  adopted_page3.csv -H \"Authorization: Bearer '

from datetime import datetime
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d_%b_%Y_%H_%M_%f")
timestampStr


curl_beginning = "curl -o  '../data/json/json_dump/"

out_txt = timestampStr

curl_middle = ".json -H \"Authorization: Bearer '"

three_hour_token =  open('token.txt', 'r').read()

curl_end = '\"  https://api.petfinder.com/v2/animals?status=adopted&type=Dog&limit=100'

curl_full = curl_beginning + out_txt + curl_middle + three_hour_token + curl_end
print(curl_full)
os.system(curl_full)