import os

#examples of what args should look like
# total_api_calls = 5000
# three_hour_token = str(eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImRkNmQzMGY2Yjg2Mjk0ZmZlZjFkMTg1MmNmMTAwMTcyYThhMGUwYmMxYzVlNTg3ZDIzNmM4M2JhY2Q3YTA0ODgwYmU0NTNjMGRlZDE4NmZjIiwiaWF0IjoxNTk1MzM0NzI2LCJuYmYiOjE1OTUzMzQ3MjYsImV4cCI6MTU5NTMzODMyNiwic3ViIjoiIiwic2NvcGVzIjpbXX0.vHvby563zSjzhtufg8pmy1a_j3uP82mWinFk2sMJWkgpvUVTKR1k_EHk8x8wfLdbV4OqqCewPG2nuS8XzwziKMR_c0fSTdNqrUYWDUrIeLsXSefCRcE3xgxVe2q-xm63v8PzegLPJPpNShzerULOWxUsBzy7UBSTZdVmnyP9gwUDpVBqEmgnnTu7sJNqW5TCngApvCn59TwrTDmodUOJPi8mMF0odS5kkHS-lFxMtT1tGXGwF_kEGKClVPJ46EWKo8auYEc0pu6GfMg5Y9SHMczB1sMytby-F3d0qzIdk1Qx3ByF2ljA699uwCF941ZFjeytDvdi-9XkBLJCKHAU6g)


def get_api_token(new_token):
    '''Enter total calls to the api, int
    Enter the full 3 hour token to access the api, string'''
    # three_hour_token = str(client_id)
    # print(three_hour_token)
    # return three_hour_token
    curl_beginning = 'curl -d \"grant_type=client_credentials&client_id='
    curl_end = '\" https://api.petfinder.com/v2/oauth2/token #api address'

    #each iteration makes 1 full curl command API call and returns a JSON file
    curl_full = curl_beginning + new_token + curl_end
            
    print("api token request sent as curl cmd")
    return(os.system(curl_full))


