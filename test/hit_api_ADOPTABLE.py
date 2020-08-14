import os



total_calls = 5000


curl_beginning = "curl -o  ../../../data/json/json_dump/"

# out_txt = timestampStr

curl_middle = "-H \"Authorization: Bearer "

three_hour_token =  open('cron/token.txt', 'r').read()

curl_end = '\"  https://api.petfinder.com/v2/animals?status=adoptable&page='

# ouput = '> '

for i in range(1, total_calls+1):
    changing_page = i
    changing_page = str(i)
    # curl_full = (f'curl -o  ../../../data/json/json_dump/ADOPTED_Aug112020_{i}.JSON ' + curl_middle + three_hour_token + curl_end + changing_page)
    curl_full = (f'curl -o  ../../../data/json/json_dump/ADOPTABLE_Aug112020_{i}.JSON ' + curl_middle + three_hour_token + curl_end + changing_page ) #          + '&limit=100') #'>       ADOPTED.JSON 2>&1')

    print(curl_full)
    
    os.system(curl_full)






# curl -o  ../../../../data/json/json_dump/11_Aug_2020_11_23_994659.json -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjE5MzYwZTMzNzZiNjcxZGNkNTBkYmUyMDg3ZDA4NmRiNjdkYWRmZWM3YTkyYWFhM2YyYjJjMzViMTUzYjAxMjNjN2RjYTgxYWI1NjU5YmUwIiwiaWF0IjoxNTk3MTYzMjc1LCJuYmYiOjE1OTcxNjMyNzUsImV4cCI6MTU5NzE2Njg3NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.hTXHqrPedTt8xMcDNLe-vcWOhwVM1oTjwqWnV56MvvWA007-UiOAToUE7-1Isj4fTtnx4OBRGRIspWi60CSfpIaBI64auYnw2xFl4F0UK_hkzt8WC0gt0oCvJgQp2NNTnp-HPG_tcJ2B5IiDdpSfKzZBB_mvx1nsV8-S8eEFYwH-56XoYE_AmKrjhTLATKtQ3P8uIEW7Z0v65ugCaAAUhYtEczIe6srYrkClc6oC_0A12RbgX5EFkV12oEide1Oo8woPovgq0vpR8kBhq08tFAck0sCLpT9WsMrXHSu1bpdxIlhbcF6kFTPGdLUM4RAEF6zmiqarisfK1MS61vdVGQ"  https://api.petfinder.com/v2/animals?status=adopted&type=Dog&limit=100

# curl -o  ../../../data/json/json_dump/ADOPTED_Aug112020_1.JSON .json -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjE5MzYwZTMzNzZiNjcxZGNkNTBkYmUyMDg3ZDA4NmRiNjdkYWRmZWM3YTkyYWFhM2YyYjJjMzViMTUzYjAxMjNjN2RjYTgxYWI1NjU5YmUwIiwiaWF0IjoxNTk3MTYzMjc1LCJuYmYiOjE1OTcxNjMyNzUsImV4cCI6MTU5NzE2Njg3NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.hTXHqrPedTt8xMcDNLe-vcWOhwVM1oTjwqWnV56MvvWA007-UiOAToUE7-1Isj4fTtnx4OBRGRIspWi60CSfpIaBI64auYnw2xFl4F0UK_hkzt8WC0gt0oCvJgQp2NNTnp-HPG_tcJ2B5IiDdpSfKzZBB_mvx1nsV8-S8eEFYwH-56XoYE_AmKrjhTLATKtQ3P8uIEW7Z0v65ugCaAAUhYtEczIe6srYrkClc6oC_0A12RbgX5EFkV12oEide1Oo8woPovgq0vpR8kBhq08tFAck0sCLpT9WsMrXHSu1bpdxIlhbcF6kFTPGdLUM4RAEF6zmiqarisfK1MS61vdVGQ"  https://api.petfinder.com/v2/animals?status=adopted&page=1
# curl -o  ../../../data/json/json_dump/ADOPTED_Aug112020_2.JSON .json -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjE5MzYwZTMzNzZiNjcxZGNkNTBkYmUyMDg3ZDA4NmRiNjdkYWRmZWM3YTkyYWFhM2YyYjJjMzViMTUzYjAxMjNjN2RjYTgxYWI1NjU5YmUwIiwiaWF0IjoxNTk3MTYzMjc1LCJuYmYiOjE1OTcxNjMyNzUsImV4cCI6MTU5NzE2Njg3NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.hTXHqrPedTt8xMcDNLe-vcWOhwVM1oTjwqWnV56MvvWA007-UiOAToUE7-1Isj4fTtnx4OBRGRIspWi60CSfpIaBI64auYnw2xFl4F0UK_hkzt8WC0gt0oCvJgQp2NNTnp-HPG_tcJ2B5IiDdpSfKzZBB_mvx1nsV8-S8eEFYwH-56XoYE_AmKrjhTLATKtQ3P8uIEW7Z0v65ugCaAAUhYtEczIe6srYrkClc6oC_0A12RbgX5EFkV12oEide1Oo8woPovgq0vpR8kBhq08tFAck0sCLpT9WsMrXHSu1bpdxIlhbcF6kFTPGdLUM4RAEF6zmiqarisfK1MS61vdVGQ"  https://api.petfinder.com/v2/animals?status=adopted&page=2


# total_calls = 5000

# curl_beginning = '\"Authorization: Bearer '

# three_hour_token = 'eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjE5MzYwZTMzNzZiNjcxZGNkNTBkYmUyMDg3ZDA4NmRiNjdkYWRmZWM3YTkyYWFhM2YyYjJjMzViMTUzYjAxMjNjN2RjYTgxYWI1NjU5YmUwIiwiaWF0IjoxNTk3MTYzMjc1LCJuYmYiOjE1OTcxNjMyNzUsImV4cCI6MTU5NzE2Njg3NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.hTXHqrPedTt8xMcDNLe-vcWOhwVM1oTjwqWnV56MvvWA007-UiOAToUE7-1Isj4fTtnx4OBRGRIspWi60CSfpIaBI64auYnw2xFl4F0UK_hkzt8WC0gt0oCvJgQp2NNTnp-HPG_tcJ2B5IiDdpSfKzZBB_mvx1nsV8-S8eEFYwH-56XoYE_AmKrjhTLATKtQ3P8uIEW7Z0v65ugCaAAUhYtEczIe6srYrkClc6oC_0A12RbgX5EFkV12oEide1Oo8woPovgq0vpR8kBhq08tFAck0sCLpT9WsMrXHSu1bpdxIlhbcF6kFTPGdLUM4RAEF6zmiqarisfK1MS61vdVGQ'
# curl_end = '\"  https://api.petfinder.com/v2/animals?status=adopted&page=' #api address


# for i in range(1, total_calls+1):
#     changing_page = i
#     changing_page = str(i)
#     curl_full = (f'curl -o  \'../../../data/json/json_dump/ADOPTED_Aug112020_{i}.JSON\' ' + curl_beginning + three_hour_token + curl_end + changing_page)
#     os.system(curl_full)


# import os
# # from datetime import datetime
# # from crontab import CronTab



# def send_curl_cmd(curl_full):
#     return(os.system(curl_full))


# if __name__ == "__main__":

#     total_calls = 2


#     curl_beginning = "curl -o  ../../../data/json/json_dump/"

#     # out_txt = timestampStr

#     curl_middle = ".json -H \"Authorization: Bearer "

#     three_hour_token =  open('cron/token.txt', 'r').read()

#     curl_end = '\"  https://api.petfinder.com/v2/animals?status=adopted&page='
    
#     for i in range(1, total_calls+1):
#         changing_page = i
#         changing_page = str(i)
#         curl_full = (f'curl -o  ../../../data/json/json_dump/ADOPTED_Aug112020_{i}.JSON ' + three_hour_token + curl_end + changing_page)
#         print(curl_full)
        
#         os.system(curl_full)
        
#         # send_curl_cmd(curl_full)