import os
# import time

#examples of what args should look like
total_api_calls = 2
three_hour_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjRkZWQ1ZmY3ZWM2MDllMzdkNDE1ZDgzMWUyYzY1MzAxOThhM2I3MDM5M2EwMmQ5MWZkYzk4ZDk0MGVkYmEzNWIzNzJjMWVmZmVmNjI4YTk5IiwiaWF0IjoxNTk2MjQ4NzcwLCJuYmYiOjE1OTYyNDg3NzAsImV4cCI6MTU5NjI1MjM3MCwic3ViIjoiIiwic2NvcGVzIjpbXX0.lB3nuF-2CljpcLY5dfYKhYgJ90r9LbfA_6Px-ZxTagKCro5MIOfz2X_q3a8IshFNzryB4E9ZOr1D1kfdbB8wkTkX1Abh7FflJsaM8tCaq0QcrDrNIIGephg9h_ybaRBkgjpsj-WsV1hzPsskfx56ocAsjcqZ2pbOmMqESHWUuF4jciEWQzHCjxaJ27nQMQWfoOZkLFHvGfuTbCJG620-52zLFUVXxNkX42WzXkzSPR3weUcVsIV9tix68HgbK4FKa_jDoDbD_H5YKlgDVFRRZUy0rx_jylBY3oTOUnofiBKRSuycPIn2MxOjqGzhe8Fy0Ouxk9XamPQZ2SoA52Nyyw'


# curl -o adopted.json -H "Authorization: Bearer 
# eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6Ijg4NGUwYWUwMjUwYzU4OGRjMGY4YzliZTAzMjNjYzM0Zjc4MGMyNjg3NGYzZWFkOTU4YzJlNGM1MWJlNGNmYmU4ZjgxNDMzMDYzZTI5ZWY3IiwiaWF0IjoxNTk1OTYzNTQyLCJuYmYiOjE1OTU5NjM1NDIsImV4cCI6MTU5NTk2NzE0Miwic3ViIjoiIiwic2NvcGVzIjpbXX0.uL-v9XWUvpugVmKwLpU4irvxfGg0MprzKZCG8-UEGZyjgkSwgFr0Ek8UeAMM4b8Jksg36xT1Jmp8BuVxtLb1C17dXcHYk9CE9OMZrm7dUCVgE3EexyzoGKr0DbrkGJ-EBzTjQXdn2iLwPj5TQtOrR532uXzLIlvVouMMT1vq_1Ory2eZtWhn18e-8gaQ1jGgp5_3rUuqB3f_Kh1uBMHPN4wAMsvfmuGKoofK7C8Rs31oSK0zwNOfuwKbb9S9ig9LPvLGRjj-ZPqkoKjjUy0hd3ZrrGd5rg6VEoWOfTdLgQaKSH_P5S2UNenqtb3pqjJCEiVHLuz9HXmaXMqMu4Jacg" 
# GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog

def webscrape_api(total_api_calls, three_hour_token):
    '''Enter total calls to the api, int
    Enter the full 3 hour token to access the api, string'''
    # three_hour_token = str(three_hour_token)
    curl_beginning = '\"Authorization: Bearer '
    curl_end = '\"  GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog' #api address
    output_file = '> a_output.csv'

    # ts = time.gmtime()
    # time_stamp = (time.strftime("%Y-%m-%d_%H_%M_%S", ts))
    #each iteration makes 1 full curl command API call and returns a JSON file
    print("sending api requests via curl cmd")
    for i in range(1, total_api_calls+1):
        changing_page = i
        changing_page = str(i)
        # curl_full = (f'curl -o  \'../data/json_dump/output_{i}_{time_stamp}.JSON\' -H' + curl_beginning + three_hour_token + curl_end + changing_page + output_file + '\'../data/json/json_dump/output_{i}_{time_stamp}.JSON')

        curl_full = (f'curl -o  adoptable.csv -H' + curl_beginning + three_hour_token + curl_end + changing_page + output_file)
        print(curl_full)
        return(os.system(curl_full))


webscrape_api(total_api_calls, three_hour_token)

#example of full working API call:
'''
curl -o adoptable.json -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjRlYmM0ZmEwNDc5ODE3NTIwMDZjZTEzMGEzMTUyZGUxYjM5MWJlMWNhNjM2YTNlNTc1OWI3NGU0YTZkYWFiYTM1NzMyYTVhZTE5OWRhODlhIiwiaWF0IjoxNTk1NzMzMTM0LCJuYmYiOjE1OTU3MzMxMzQsImV4cCI6MTU5NTczNjczNCwic3ViIjoiIiwic2NvcGVzIjpbXX0.uLhARB9iytUKoLJnvAbieIhBA57rpNwEpeinbvWbtpP5AsFDQxb3PwC_z3ExOCZRztWFxEkTzAcUR1oHGfFY5IMQ1LxHB4vBzKZzHeBLnuxR692YX0-Al7dtgVPDVTKEwTtNI-WwC_uLNEX3Sf-AHf3spaGGV0dOpJR_PXJ1457_b6mOAn2soFoCgXpUIzq_kxzbwfq3QNJiYPcfUMzeNU5I_5HPGsuLe9EhyWqU86sU0AEJ_b5OSv9svqUaoUqYQOkL7dHds4MkoOPUnYE0jNJV6pStg9cZ7abWZ2h-4_Ra5kiarH39AxTVsZFpTkgyeZZaAQTXeMJypBJ5bdUWJw" https://api.petfinder.com/v2/animals?type=dog&page=2 GET https://api.petfinder.com/v2/status/{status}/adopted > output.json
'''


##############################################################################################
##############################################################################################
# !!!!!!!!!!!!!!!!!!!!!!!!testing pipeline
## this code works, backup code to pipeline
import os

total_calls =2

curl_beginning = '\"Authorization: Bearer '

three_hour_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjRkZWQ1ZmY3ZWM2MDllMzdkNDE1ZDgzMWUyYzY1MzAxOThhM2I3MDM5M2EwMmQ5MWZkYzk4ZDk0MGVkYmEzNWIzNzJjMWVmZmVmNjI4YTk5IiwiaWF0IjoxNTk2MjQ4NzcwLCJuYmYiOjE1OTYyNDg3NzAsImV4cCI6MTU5NjI1MjM3MCwic3ViIjoiIiwic2NvcGVzIjpbXX0.lB3nuF-2CljpcLY5dfYKhYgJ90r9LbfA_6Px-ZxTagKCro5MIOfz2X_q3a8IshFNzryB4E9ZOr1D1kfdbB8wkTkX1Abh7FflJsaM8tCaq0QcrDrNIIGephg9h_ybaRBkgjpsj-WsV1hzPsskfx56ocAsjcqZ2pbOmMqESHWUuF4jciEWQzHCjxaJ27nQMQWfoOZkLFHvGfuTbCJG620-52zLFUVXxNkX42WzXkzSPR3weUcVsIV9tix68HgbK4FKa_jDoDbD_H5YKlgDVFRRZUy0rx_jylBY3oTOUnofiBKRSuycPIn2MxOjqGzhe8Fy0Ouxk9XamPQZ2SoA52Nyyw'
curl_end = '\"  https://api.petfinder.com/v2/animals?type=dog&page=' #api address


for i in range(1, total_calls+1):
    changing_page = i
    changing_page = str(i)
    curl_full = (f'curl -o  \'../data/json_dump/output_{i}.JSON\' ' + curl_beginning + three_hour_token + curl_end + changing_page)
    os.system(curl_full)

###############################################################################################