# curl -o  'output_1.JSON' "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjZkNjAwNjExYmJhMmU3NDFhOGYzYmY3NjQwZjNmZTExZGUxNTg4MzBjYzE3ZDNlZDg1OWNlODAzMmYxZWI2NjAyNGM4OTIxNGM0NzNkYjViIiwiaWF0IjoxNTk2ODU1NzMyLCJuYmYiOjE1OTY4NTU3MzIsImV4cCI6MTU5Njg1OTMzMiwic3ViIjoiIiwic2NvcGVzIjpbXX0.E2YRUAOiyv3pFKrLsbYdRSkVI-_nVwefUfyR8D7TDuj3xN_UpoEnF6EZne2Q8UiLL4BWysvlOgTfccBxqt2WjGUP7wt_7InK0l_xW8mxYeFN2Kk9tPNk1H3STNcv0ANMog11u6YGOn7Squz6O-m-tq4CeQzc1rORLfYrWVOf6ZyRNLIQgTRpDGragWaMJ0RJetoroDwWdDlU70XbNONH5e3RptToP0aSMhxwGYv1-W5VlJ-6eyofjUPYzqOcI4a03147dUiy5HyQ1GMZmapm4undPYx-aBYI5TvOCCuwBPN9VYxLdHGlKfv5f2HVntELtlAEjTasEW-xr6ORX3QoxQ"  https://api.petfinder.com/v2/animals?type=dog&limit=100&page=1

# #renew the key every 1 hours
# 0 * * * *



# # scrape the site every ten minutes
# # run every hour starting at every ten minute mark

# 10, 20, 30, 40, 50 * * * *




# import os 
# import time
# print("scraped")
# os.touch(str(int(time.time())))




from crontab import CronTab
import datetime
 
with open('dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))