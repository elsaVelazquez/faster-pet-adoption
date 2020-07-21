import os

total_calls = 5000

curl_beginning = '\"Authorization: Bearer '

three_hour_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImJkYTQ0OGMzYzA2NjczZmQ0ZDFiZGQwZDQ5YWViMjY2NzIxYWI4NDI5ZWJkNWRjN2M1MmJmMWNkYjhjNTM5OTE0MTE0NTRiNGI1ZmNjMjhmIiwiaWF0IjoxNTk1MzI1NTcyLCJuYmYiOjE1OTUzMjU1NzIsImV4cCI6MTU5NTMyOTE3Miwic3ViIjoiIiwic2NvcGVzIjpbXX0.M1fTBumWpics8_HdptlOSdtnRD2SWiuETQRphrUMknE3eY5xWTdb1kJKRMtLXMU5oY5ZkHOlaZHefFFV7NGHoFJmTHxKqT_XgZEcyXx6CjmeaU5q-SiSQfYIqNks6rrRU9p4qJFE-5Ym0E-223Bo9GxMHoWuwpdxXyT-daV1kXpZMR6tHxJqiFmjSmo8mN2DQeAg_UccjOAVvJ5qd7MQ27btyHD_3l4hDj67poXRMhVSAHWWlglh2i9zOMW1Wv1eKph4Vsd6xr8OdmpM-497AQtsz1El1mN-xGhTlFb7TaCxjKh_oBfPW7cfbXNwvhTLXSGomNDcXfwmfdH_T7VDsw'

curl_end = '\"  https://api.petfinder.com/v2/animals?type=dog&page=' #api address


for i in range(1, total_calls+1):
    changing_page = i
    changing_page = str(i)
    curl_full = (f'curl -o  \'../data/json_dump/output_{i}.JSON\' -H ' + curl_beginning + three_hour_token + curl_end + changing_page)
    os.system(curl_full)
