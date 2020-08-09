import os
from datetime import datetime
from crontab import CronTab



def send_curl_cmd(curl_full):
    return(os.system(curl_full))


if __name__ == "__main__":

    total_calls = 50

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d_%b_%Y_%H_%M_%f")

    for i in range(1, total_calls+1):
        changing_page = i
        # print(i)
        changing_page = str(i)
        curl_beginning = "curl -o  ../../../../data/json/json_dump/"

        out_txt = timestampStr

        curl_middle = (f"_adoptable{i}.json -H \"Authorization: Bearer ")

        three_hour_token =  open('token.txt', 'r').read()

        curl_end = '\"  https://api.petfinder.com/v2/animals?type=dog&page='

        curl_full = curl_beginning + out_txt + curl_middle + three_hour_token + curl_end + changing_page
        print(curl_full)
        send_curl_cmd(curl_full)