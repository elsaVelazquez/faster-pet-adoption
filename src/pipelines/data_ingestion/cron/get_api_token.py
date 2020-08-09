import os
from string import punctuation
import string 


def get_api_token(creds):
    '''Ran by a cron job.
    Outputs the API token to 'token.txt' on the hour at the 0th, every hour.
    The token has a 3 hour life cycle but the token is renewed every 1 hour, just in case.
    '''

    curl_beginning = 'curl -o  "token.txt" -d \"grant_type=client_credentials&client_id='
    curl_end = '\" https://api.petfinder.com/v2/oauth2/token #api address'


    #each iteration makes 1 full curl command API call and returns a JSON file
    curl_full = curl_beginning + creds + curl_end 
    # print(curl_full)
    # print("api token request sent as curl cmd")
    return(os.system(curl_full))

def clean_token(token):
    '''
    strip the json from the token to turn it into pure txt string
    '''
    token_clean = token.strip('{"token_type":"Bearer","expires_in":3600,"access_token":"')
    final_token = token_clean.strip('"}')
    ey = 'ey'
    text_token = ey + final_token
    # print(text_token)
    f= open("token.txt","w+")
    f.write(text_token)
    f.close
    return text_token


if __name__ == "__main__":
    
    creds = open('creds.txt', 'r').read()
    
    dirty_token = get_api_token(creds)


    dirty_token = open('token.txt', 'r').read()
    # print(dirty_token)

    token = clean_token(dirty_token)
    
    
    print(token)