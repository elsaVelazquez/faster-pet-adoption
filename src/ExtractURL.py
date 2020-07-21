import os

total_calls = 5000

curl_beginning = '\"Authorization: Bearer '

three_hour_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImRkNmQzMGY2Yjg2Mjk0ZmZlZjFkMTg1MmNmMTAwMTcyYThhMGUwYmMxYzVlNTg3ZDIzNmM4M2JhY2Q3YTA0ODgwYmU0NTNjMGRlZDE4NmZjIiwiaWF0IjoxNTk1MzM0NzI2LCJuYmYiOjE1OTUzMzQ3MjYsImV4cCI6MTU5NTMzODMyNiwic3ViIjoiIiwic2NvcGVzIjpbXX0.vHvby563zSjzhtufg8pmy1a_j3uP82mWinFk2sMJWkgpvUVTKR1k_EHk8x8wfLdbV4OqqCewPG2nuS8XzwziKMR_c0fSTdNqrUYWDUrIeLsXSefCRcE3xgxVe2q-xm63v8PzegLPJPpNShzerULOWxUsBzy7UBSTZdVmnyP9gwUDpVBqEmgnnTu7sJNqW5TCngApvCn59TwrTDmodUOJPi8mMF0odS5kkHS-lFxMtT1tGXGwF_kEGKClVPJ46EWKo8auYEc0pu6GfMg5Y9SHMczB1sMytby-F3d0qzIdk1Qx3ByF2ljA699uwCF941ZFjeytDvdi-9XkBLJCKHAU6g'
curl_end = '\"  https://api.petfinder.com/v2/animals?type=dog&page=' #api address


for i in range(1, total_calls+1):
    changing_page = i
    changing_page = str(i)
    curl_full = (f'curl -o  \'../data/json_dump/output_{i}.JSON\' ' + curl_beginning + three_hour_token + curl_end + changing_page)
    os.system(curl_full)
