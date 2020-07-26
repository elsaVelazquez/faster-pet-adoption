import os

from pipelines.ingest_webscrape_api import webscrape_api
from pipelines.ingest_api_token import get_api_token
from pipelines.crypt import crypt_it   
#need to figure out how to do this securely





if __name__ == "__main__":
    
    #get a token
    # pass 

    start = crypt_it()
    
    
    
    #change three_hour_token accordingly
    three_hour_token = get_api_token(start)
    
    #copy from cmd line and paste your token
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjJmMzYwNmNhZDlhNzFlYzdjOTBkMjVhM2E3ODkzY2E1NGE5MzBiYWJhZDg4ZDExYzhhNDJiMWJlNDQwNDhmZTFlNDk2MGQwMTNkNTFjNzA4IiwiaWF0IjoxNTk1NzI3NzA0LCJuYmYiOjE1OTU3Mjc3MDQsImV4cCI6MTU5NTczMTMwNCwic3ViIjoiIiwic2NvcGVzIjpbXX0.mDyEOOFh-23XQXHrlKxxtYyUCrgVN0wzChFVi7bQo4VJnW-zLAsiu1X2YrRnPDL1XAP23CD-_4OyAI-UcodfMKBF6HL2OzHnTRy_qJIyCcwn17_lRO47Gkj1b8dv66KUYbE6DFmTAfvD91TPNXCC3OiY0VeiU_FmHmLaUEedrccZTcyfgaNImwmNYxZKfG7zsKOYEp8uAOsHWPrPzFCkZ8uO45dhvH5psvq0DNzyu_JjEdLOhfC8h1-P6nJg3dWEEApUiNmMWZUxdV1e_ng4ukmYBwPqRYlXtoOSUy-zyZQo1C0gR8uJ6Wbywb90_KuEZz58U5Rpu8jDfjXAiFa6og"
    
    print("\nyour token is: ")
    print(token)
        
    total_api_calls = 2
    call = webscrape_api(total_api_calls, token)
    print(call)
    
    