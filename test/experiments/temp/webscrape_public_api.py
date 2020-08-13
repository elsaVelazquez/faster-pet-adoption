import os

total_calls = 5000

curl_beginning = '\"Authorization: Bearer '

three_hour_token = 'eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjE5MzYwZTMzNzZiNjcxZGNkNTBkYmUyMDg3ZDA4NmRiNjdkYWRmZWM3YTkyYWFhM2YyYjJjMzViMTUzYjAxMjNjN2RjYTgxYWI1NjU5YmUwIiwiaWF0IjoxNTk3MTYzMjc1LCJuYmYiOjE1OTcxNjMyNzUsImV4cCI6MTU5NzE2Njg3NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.hTXHqrPedTt8xMcDNLe-vcWOhwVM1oTjwqWnV56MvvWA007-UiOAToUE7-1Isj4fTtnx4OBRGRIspWi60CSfpIaBI64auYnw2xFl4F0UK_hkzt8WC0gt0oCvJgQp2NNTnp-HPG_tcJ2B5IiDdpSfKzZBB_mvx1nsV8-S8eEFYwH-56XoYE_AmKrjhTLATKtQ3P8uIEW7Z0v65ugCaAAUhYtEczIe6srYrkClc6oC_0A12RbgX5EFkV12oEide1Oo8woPovgq0vpR8kBhq08tFAck0sCLpT9WsMrXHSu1bpdxIlhbcF6kFTPGdLUM4RAEF6zmiqarisfK1MS61vdVGQ'
curl_end = '\"  https://api.petfinder.com/v2/animals?status=adopted&page=' #api address


for i in range(1, total_calls+1):
    changing_page = i
    changing_page = str(i)
    curl_full = (f'curl -o  \'../data/ADOPTED_Aug112020_{i}.JSON\' ' + curl_beginning + three_hour_token + curl_end + changing_page)
    os.system(curl_full)




