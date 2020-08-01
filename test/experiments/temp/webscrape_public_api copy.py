import os

total_calls = 5

curl_beginning = '\"Authorization: Bearer '

three_hour_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImIyYTc1MDcxNTMzNzM2NTNhM2VhZDlmZGIzNWI1ZmRkYWY4OGJmMzAyZDYzN2NkZDkzOGQ5YjcyMGI2ZjJiZjY3ZTkwOTU5OTdlNWIxNjgzIiwiaWF0IjoxNTk1NzMyMTM4LCJuYmYiOjE1OTU3MzIxMzgsImV4cCI6MTU5NTczNTczOCwic3ViIjoiIiwic2NvcGVzIjpbXX0.UEdJ7yTIYJzOAEPXkTizpNAsItX1yvCz3ZV2ARoKegu0ssLkjrTD-5-oByceW8BlbZ7mE9csgZtQSyXz2mBzr15k4B8JYNDXqt93DTbRVKncW2o-mconiglpIUcve0Uf80-NtHEV8ZytRIYhvPurtxYbYUAevbe-bfvThN3i7w8zaWIu4aeWYrwBDzuyRrfTtbvfJgP7yd5h7wQxYAYoQKQv56wwEGpuEkQzw6SfnwBQt-UwNrrS7fJ9YVzfPBbD8-lsvHzZuYEjrpG2YBOxqh8G9LUEf_Jihy7LjBjgT4l1mAAJUsP7tUfFs92377dZKI-mYffNY5rVDXqso_B4vA'
curl_end = '\"  https://api.petfinder.com/v2/animals?type=dog&page=' #api address


for i in range(1, total_calls+1):
    changing_page = i
    changing_page = str(i)
    curl_full = (f'curl -o  \'../data/output_{i}.JSON\' ' + curl_beginning + three_hour_token + curl_end + changing_page)
    os.system(curl_full)
