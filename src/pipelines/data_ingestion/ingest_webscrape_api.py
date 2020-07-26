import os
import time

#examples of what args should look like
# total_api_calls = 50
# three_hour_token = str(eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImRkNmQzMGY2Yjg2Mjk0ZmZlZjFkMTg1MmNmMTAwMTcyYThhMGUwYmMxYzVlNTg3ZDIzNmM4M2JhY2Q3YTA0ODgwYmU0NTNjMGRlZDE4NmZjIiwiaWF0IjoxNTk1MzM0NzI2LCJuYmYiOjE1OTUzMzQ3MjYsImV4cCI6MTU5NTMzODMyNiwic3ViIjoiIiwic2NvcGVzIjpbXX0.vHvby563zSjzhtufg8pmy1a_j3uP82mWinFk2sMJWkgpvUVTKR1k_EHk8x8wfLdbV4OqqCewPG2nuS8XzwziKMR_c0fSTdNqrUYWDUrIeLsXSefCRcE3xgxVe2q-xm63v8PzegLPJPpNShzerULOWxUsBzy7UBSTZdVmnyP9gwUDpVBqEmgnnTu7sJNqW5TCngApvCn59TwrTDmodUOJPi8mMF0odS5kkHS-lFxMtT1tGXGwF_kEGKClVPJ46EWKo8auYEc0pu6GfMg5Y9SHMczB1sMytby-F3d0qzIdk1Qx3ByF2ljA699uwCF941ZFjeytDvdi-9XkBLJCKHAU6g)


def webscrape_api(total_api_calls, three_hour_token):
    '''Enter total calls to the api, int
    Enter the full 3 hour token to access the api, string'''
    # three_hour_token = str(three_hour_token)
    curl_beginning = '\"Authorization: Bearer '
    curl_end = '\"  https://api.petfinder.com/v2/animals?type=dog&status=adopted&page=' #api address
    output_file = '> '

    ts = time.gmtime()
    time_stamp = (time.strftime("%Y-%m-%d_%H_%M_%S", ts))
    #each iteration makes 1 full curl command API call and returns a JSON file
    print("sending api requests via curl cmd")
    for i in range(1, total_api_calls+1):
        changing_page = i
        changing_page = str(i)
        curl_full = (f'curl -o  \'../data/json_dump/output_{i}_{time_stamp}.JSON\' -H' + curl_beginning + three_hour_token + curl_end + changing_page + output_file + '\'../data/json_dump/output_{i}_{time_stamp}.JSON')
        print(curl_full)
        return(os.system(curl_full))


#example of full working API call:
'''
curl -o adoptable.json -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjRlYmM0ZmEwNDc5ODE3NTIwMDZjZTEzMGEzMTUyZGUxYjM5MWJlMWNhNjM2YTNlNTc1OWI3NGU0YTZkYWFiYTM1NzMyYTVhZTE5OWRhODlhIiwiaWF0IjoxNTk1NzMzMTM0LCJuYmYiOjE1OTU3MzMxMzQsImV4cCI6MTU5NTczNjczNCwic3ViIjoiIiwic2NvcGVzIjpbXX0.uLhARB9iytUKoLJnvAbieIhBA57rpNwEpeinbvWbtpP5AsFDQxb3PwC_z3ExOCZRztWFxEkTzAcUR1oHGfFY5IMQ1LxHB4vBzKZzHeBLnuxR692YX0-Al7dtgVPDVTKEwTtNI-WwC_uLNEX3Sf-AHf3spaGGV0dOpJR_PXJ1457_b6mOAn2soFoCgXpUIzq_kxzbwfq3QNJiYPcfUMzeNU5I_5HPGsuLe9EhyWqU86sU0AEJ_b5OSv9svqUaoUqYQOkL7dHds4MkoOPUnYE0jNJV6pStg9cZ7abWZ2h-4_Ra5kiarH39AxTVsZFpTkgyeZZaAQTXeMJypBJ5bdUWJw" https://api.petfinder.com/v2/animals?type=dog&page=2 GET https://api.petfinder.com/v2/status/{status}/adopted > output.json
'''


##############################################################################################
##############################################################################################
# !!!!!!!!!!!!!!!!!!!!!!!!testing pipeline
## this code works, backup code to pipeline
# import os

# total_calls = 5000

# curl_beginning = '\"Authorization: Bearer '

# three_hour_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImRkNmQzMGY2Yjg2Mjk0ZmZlZjFkMTg1MmNmMTAwMTcyYThhMGUwYmMxYzVlNTg3ZDIzNmM4M2JhY2Q3YTA0ODgwYmU0NTNjMGRlZDE4NmZjIiwiaWF0IjoxNTk1MzM0NzI2LCJuYmYiOjE1OTUzMzQ3MjYsImV4cCI6MTU5NTMzODMyNiwic3ViIjoiIiwic2NvcGVzIjpbXX0.vHvby563zSjzhtufg8pmy1a_j3uP82mWinFk2sMJWkgpvUVTKR1k_EHk8x8wfLdbV4OqqCewPG2nuS8XzwziKMR_c0fSTdNqrUYWDUrIeLsXSefCRcE3xgxVe2q-xm63v8PzegLPJPpNShzerULOWxUsBzy7UBSTZdVmnyP9gwUDpVBqEmgnnTu7sJNqW5TCngApvCn59TwrTDmodUOJPi8mMF0odS5kkHS-lFxMtT1tGXGwF_kEGKClVPJ46EWKo8auYEc0pu6GfMg5Y9SHMczB1sMytby-F3d0qzIdk1Qx3ByF2ljA699uwCF941ZFjeytDvdi-9XkBLJCKHAU6g'
# curl_end = '\"  https://api.petfinder.com/v2/animals?type=dog&page=' #api address


# for i in range(1, total_calls+1):
#     changing_page = i
#     changing_page = str(i)
#     curl_full = (f'curl -o  \'../data/json_dump/output_{i}.JSON\' ' + curl_beginning + three_hour_token + curl_end + changing_page)
#     os.system(curl_full)

###############################################################################################