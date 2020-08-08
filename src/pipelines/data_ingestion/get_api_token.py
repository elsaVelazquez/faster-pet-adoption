import os


def get_api_token(creds = ""):

    curl_beginning = 'curl -d \"grant_type=client_credentials&client_id='
    curl_end = '\" https://api.petfinder.com/v2/oauth2/token #api address'

    #each iteration makes 1 full curl command API call and returns a JSON file
    curl_full = curl_beginning + creds + curl_end
            
    print("api token request sent as curl cmd")
    return(os.system(curl_full))

# get_api_token(creds)

