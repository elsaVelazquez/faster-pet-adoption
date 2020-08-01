import os

total_calls = 5

curl_beginning = '\"Authorization: Bearer '

three_hour_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjE4MWE0YjM2Nzg1ODVmYmFhZTkzNWJlYTkwMTcwODA1Mzg3YzY3OTMyZGEyMDk2YTk3MWI4Y2ZiZDU2YmRjYjVjMjNkYjBmZjljZmU1MDk0IiwiaWF0IjoxNTk2MjUyMjEyLCJuYmYiOjE1OTYyNTIyMTIsImV4cCI6MTU5NjI1NTgxMiwic3ViIjoiIiwic2NvcGVzIjpbXX0.Gm4Ly8kAjdutgNB3ggfOXdAK6Rpbn2tI1hrMAYZhpZKAczvvYFGrmDzFKlvnDGsvszqMSco8xaxvCUbt0TG7FdGW800sAhUfzJxi4Gr-MClviSqoKdD7IqF4TTe-0xwvwCtCvdp0Oz7o8C6f8unJBKrntlJnAGC8zNJI62QGPlH_ndXOOW9_LH4-mk8rYo2tH-gcxsu44mrXvM6Ed6RXNZLm8wo1lLFqxnRJ_QaGZKSm72ur-7DnlX516NZVaIJVmjkh9SQpA8z5zqpN2ErZ90LGzoM4fDihYnk4LbCCgAbe9XoC34Zsye3kE1-y600A58kXtIHTKBR9adhc29imuQ'
curl_end = '\"  https://api.petfinder.com/v2/animals?type=dog&page=' #api address


for i in range(1, total_calls+1):
    changing_page = i
    changing_page = str(i)
    curl_full = (f'curl -o  \'../data/output_{i}.JSON\' ' + curl_beginning + three_hour_token + curl_end + changing_page)
    os.system(curl_full)
