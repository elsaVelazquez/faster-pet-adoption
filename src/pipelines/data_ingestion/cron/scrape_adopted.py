import os
from datetime import datetime



def send_curl_cmd(curl_full):
    return(os.system(curl_full))


if __name__ == "__main__":

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d_%b_%Y_%H_%M_%f")


    curl_beginning = "curl -o  ../../../../data/json/json_dump/"

    out_txt = timestampStr

    curl_middle = ".json -H \"Authorization: Bearer "

    three_hour_token =  open('token.txt', 'r').read()

    curl_end = '\"  https://api.petfinder.com/v2/animals?status=adopted&type=Dog&limit=100'

    curl_full = curl_beginning + out_txt + curl_middle + three_hour_token + curl_end
    # print(curl_full)
        
    send_curl_cmd(curl_full)