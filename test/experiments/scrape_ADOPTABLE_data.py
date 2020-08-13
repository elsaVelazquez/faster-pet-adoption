import os
import time

#examples of what args should look like
total_api_calls = 1

three_hour_token = 'eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjZkNjAwNjExYmJhMmU3NDFhOGYzYmY3NjQwZjNmZTExZGUxNTg4MzBjYzE3ZDNlZDg1OWNlODAzMmYxZWI2NjAyNGM4OTIxNGM0NzNkYjViIiwiaWF0IjoxNTk2ODU1NzMyLCJuYmYiOjE1OTY4NTU3MzIsImV4cCI6MTU5Njg1OTMzMiwic3ViIjoiIiwic2NvcGVzIjpbXX0.E2YRUAOiyv3pFKrLsbYdRSkVI-_nVwefUfyR8D7TDuj3xN_UpoEnF6EZne2Q8UiLL4BWysvlOgTfccBxqt2WjGUP7wt_7InK0l_xW8mxYeFN2Kk9tPNk1H3STNcv0ANMog11u6YGOn7Squz6O-m-tq4CeQzc1rORLfYrWVOf6ZyRNLIQgTRpDGragWaMJ0RJetoroDwWdDlU70XbNONH5e3RptToP0aSMhxwGYv1-W5VlJ-6eyofjUPYzqOcI4a03147dUiy5HyQ1GMZmapm4undPYx-aBYI5TvOCCuwBPN9VYxLdHGlKfv5f2HVntELtlAEjTasEW-xr6ORX3QoxQ'
#example of full working API call:
'''
curl -o adoptable.json -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjRlYmM0ZmEwNDc5ODE3NTIwMDZjZTEzMGEzMTUyZGUxYjM5MWJlMWNhNjM2YTNlNTc1OWI3NGU0YTZkYWFiYTM1NzMyYTVhZTE5OWRhODlhIiwiaWF0IjoxNTk1NzMzMTM0LCJuYmYiOjE1OTU3MzMxMzQsImV4cCI6MTU5NTczNjczNCwic3ViIjoiIiwic2NvcGVzIjpbXX0.uLhARB9iytUKoLJnvAbieIhBA57rpNwEpeinbvWbtpP5AsFDQxb3PwC_z3ExOCZRztWFxEkTzAcUR1oHGfFY5IMQ1LxHB4vBzKZzHeBLnuxR692YX0-Al7dtgVPDVTKEwTtNI-WwC_uLNEX3Sf-AHf3spaGGV0dOpJR_PXJ1457_b6mOAn2soFoCgXpUIzq_kxzbwfq3QNJiYPcfUMzeNU5I_5HPGsuLe9EhyWqU86sU0AEJ_b5OSv9svqUaoUqYQOkL7dHds4MkoOPUnYE0jNJV6pStg9cZ7abWZ2h-4_Ra5kiarH39AxTVsZFpTkgyeZZaAQTXeMJypBJ5bdUWJw" https://api.petfinder.com/v2/animals?type=dog&page=2 GET https://api.petfinder.com/v2/status/{status}/adopted > output.json
'''
# ts = time.gmtime()
# time_stamp = (time.strftime("%Y-%m-%d_%H_%M_%S", ts))
# print(time_stamp)
x=1

def helper_send_curl(curl_full, i):
    print("called helper_send_curl")
    print("curl_full: ", curl_full)
    print("i: ", i)
    curl = curl_full + str(i)
    return (os.system(curl))

def scrape_data(total_api_calls, three_hour_token):
    ts = time.gmtime()
    time_stamp = (time.strftime("%Y-%m-%d_%H_%M_%S", ts))
    for i in range(x, total_api_calls+1):
        # changing_page = i
        # changing_page = str(i)
        curl_full = (f'curl -o  scraped_data_{i}_{time_stamp}.csv -H \"Authorization: Bearer {three_hour_token}\" https://api.petfinder.com/v2/animals?status=adopted&page=') #&animals?type=dog')
        print("curl_full: \n", curl_full)
        print("\n")
        # print(type(curl_full))
        # print(changing_page)
        # print(type(changing_page))
        # (os.system(curl_full))
        # helper_send_curl(curl_full, i)
        
        
scrape_data(total_api_calls, three_hour_token)      
        
        
        
        
        
# curl -o  scraped_data_1.csv -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjllYWQ2ODkyYzFmNTU1MjgxNjIxZDBhMTJmOTkyNGRlNTc3ZmVjZjQyNzYyNzAxZTAwMDg2YTdlZmI1ZDkxYWNjNmZhYzM0MTQ3OWRhNjBlIiwiaWF0IjoxNTk2MzIwNzE0LCJuYmYiOjE1OTYzMjA3MTQsImV4cCI6MTU5NjMyNDMxNCwic3ViIjoiIiwic2NvcGVzIjpbXX0.lAls-ifIjGW9gOVmli-DqboDSnvUROztXn2gJaTLZagRFB5sRl_8DtYLSbiW-NuqxLoWuULy0Ax4uZzfEIxR9AbkEhQCT42K124ZERcV1JvLPvxtWNm69X8CB3RG2o-lWARRfm4nEyN6HL6xNS4-PjlVwL6JEgXxXDktLF4OntdOSSNBkRW1QbrPwvf_0zlbQbZ0Jj42Ijfwwhi_M_pdina2sRc93rxBSwH28mknJyopop-3ap4vurnDVW3AIhWlB3zJvrMjaafaEUzemN_mLtMUfLK1UtAtxClSpmpOSUw1DWRDU6K4oLyZvqUdEzKOxKKVjn_SGP5mlY7Tc0MqJw" https://api.petfinder.com/v2/animals?status=adopted&page=1        
        
# curl -o  scraped_data_2.csv -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjllYWQ2ODkyYzFmNTU1MjgxNjIxZDBhMTJmOTkyNGRlNTc3ZmVjZjQyNzYyNzAxZTAwMDg2YTdlZmI1ZDkxYWNjNmZhYzM0MTQ3OWRhNjBlIiwiaWF0IjoxNTk2MzIwNzE0LCJuYmYiOjE1OTYzMjA3MTQsImV4cCI6MTU5NjMyNDMxNCwic3ViIjoiIiwic2NvcGVzIjpbXX0.lAls-ifIjGW9gOVmli-DqboDSnvUROztXn2gJaTLZagRFB5sRl_8DtYLSbiW-NuqxLoWuULy0Ax4uZzfEIxR9AbkEhQCT42K124ZERcV1JvLPvxtWNm69X8CB3RG2o-lWARRfm4nEyN6HL6xNS4-PjlVwL6JEgXxXDktLF4OntdOSSNBkRW1QbrPwvf_0zlbQbZ0Jj42Ijfwwhi_M_pdina2sRc93rxBSwH28mknJyopop-3ap4vurnDVW3AIhWlB3zJvrMjaafaEUzemN_mLtMUfLK1UtAtxClSpmpOSUw1DWRDU6K4oLyZvqUdEzKOxKKVjn_SGP5mlY7Tc0MqJw" https://api.petfinder.com/v2/animals?status=adopted&page=2
# curl -O -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjllYWQ2ODkyYzFmNTU1MjgxNjIxZDBhMTJmOTkyNGRlNTc3ZmVjZjQyNzYyNzAxZTAwMDg2YTdlZmI1ZDkxYWNjNmZhYzM0MTQ3OWRhNjBlIiwiaWF0IjoxNTk2MzIwNzE0LCJuYmYiOjE1OTYzMjA3MTQsImV4cCI6MTU5NjMyNDMxNCwic3ViIjoiIiwic2NvcGVzIjpbXX0.lAls-ifIjGW9gOVmli-DqboDSnvUROztXn2gJaTLZagRFB5sRl_8DtYLSbiW-NuqxLoWuULy0Ax4uZzfEIxR9AbkEhQCT42K124ZERcV1JvLPvxtWNm69X8CB3RG2o-lWARRfm4nEyN6HL6xNS4-PjlVwL6JEgXxXDktLF4OntdOSSNBkRW1QbrPwvf_0zlbQbZ0Jj42Ijfwwhi_M_pdina2sRc93rxBSwH28mknJyopop-3ap4vurnDVW3AIhWlB3zJvrMjaafaEUzemN_mLtMUfLK1UtAtxClSpmpOSUw1DWRDU6K4oLyZvqUdEzKOxKKVjn_SGP5mlY7Tc0MqJw" https://api.petfinder.com/v2/animals?status=adopted&page=3 >> atext3.txt   
        
        
        
        
# curl -o adopted.json -H "Authorization: Bearer 
# eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6Ijg4NGUwYWUwMjUwYzU4OGRjMGY4YzliZTAzMjNjYzM0Zjc4MGMyNjg3NGYzZWFkOTU4YzJlNGM1MWJlNGNmYmU4ZjgxNDMzMDYzZTI5ZWY3IiwiaWF0IjoxNTk1OTYzNTQyLCJuYmYiOjE1OTU5NjM1NDIsImV4cCI6MTU5NTk2NzE0Miwic3ViIjoiIiwic2NvcGVzIjpbXX0.uL-v9XWUvpugVmKwLpU4irvxfGg0MprzKZCG8-UEGZyjgkSwgFr0Ek8UeAMM4b8Jksg36xT1Jmp8BuVxtLb1C17dXcHYk9CE9OMZrm7dUCVgE3EexyzoGKr0DbrkGJ-EBzTjQXdn2iLwPj5TQtOrR532uXzLIlvVouMMT1vq_1Ory2eZtWhn18e-8gaQ1jGgp5_3rUuqB3f_Kh1uBMHPN4wAMsvfmuGKoofK7C8Rs31oSK0zwNOfuwKbb9S9ig9LPvLGRjj-ZPqkoKjjUy0hd3ZrrGd5rg6VEoWOfTdLgQaKSH_P5S2UNenqtb3pqjJCEiVHLuz9HXmaXMqMu4Jacg" 
# GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog

# def scrape_data(total_api_calls, three_hour_token):
#     '''Enter total calls to the api, int
#     Enter the full 3 hour token to access the api, string'''
#     # three_hour_token = str(three_hour_token)
#     curl_beginning = '\"Authorization: Bearer '
#     curl_end = '\"  GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog' #api address
#     output_file = '> a_output.csv'

#     # ts = time.gmtime()
#     # time_stamp = (time.strftime("%Y-%m-%d_%H_%M_%S", ts))
#     #each iteration makes 1 full curl command API call and returns a JSON file
#     print("sending api requests via curl cmd")
#     for i in range(1, total_api_calls+1):
#         changing_page = i
#         changing_page = str(i)
#         # curl_full = (f'curl -o  \'../data/json_dump/output_{i}_{time_stamp}.JSON\' -H' + curl_beginning + three_hour_token + curl_end + changing_page + output_file + '\'../data/json/json_dump/output_{i}_{time_stamp}.JSON')

#         curl_full = (f'curl -o  scraped_data_{i}.csv -H' + curl_beginning + three_hour_token + curl_end + changing_page)
#         print(curl_full)
#         return(os.system(curl_full))


# scrape_data(total_api_calls, three_hour_token)


# curl -o  scraped_data_3.csv -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjRmZTc2Y2I1NjQ3ZWYzNDllMWNiZjJlMWM1ZDhmMjg5MjIzNzMxZTg1ZWQ1NmZkYWRjZWM2YmQwYmZhM2NhMzM0YzAxOWE4NDRlY2ZlYjZkIiwiaWF0IjoxNTk2MzE2NTk3LCJuYmYiOjE1OTYzMTY1OTcsImV4cCI6MTU5NjMyMDE5Nywic3ViIjoiIiwic2NvcGVzIjpbXX0.XDrHSf2LBY8UKrlOsStwiXaKTl_ws1YV8dFAfx8UkWIcYNmW7jwe0oAjeDxzsRIGyBdjFCEWjVPWeHxN_5Fvv_kvlmZ0dq8HQgIGqUeYxMMwYzKasiFcwMYS5FAYlEu68GLypeSw4TvWgk0p7ehuvVfhjYs2y8PDfAuMq1Y1140dDD_78lLVarh7HgS1YJJwGxbcozToymFDOaqDTUPldcOm-JO8ZV7jGvsrsOggaOeXYwD3K2LJWqQdh01MhpQjfN_WPoSPuSiBE6mzBLya5LKW5SvCgVmfQma1NzCL2K4AOHc5rU179FbC9Wmk6CPtyai9f9M6VqBs0Jw5O_mlAw" https://api.petfinder.com/v2/animals?status=adopted&page=3