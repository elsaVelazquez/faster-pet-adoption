# from every json file

#drop this
,"pagination":{"count_per_page":20,"total_count":59056,"current_page":1,"total_pages":2953,"_links":{"next":{"href":"\/v2\/animals?type=dog\u0026page=2"}}}}]


#drop this
  [{"animals":[
    
    


}
    ],
    "pagination": {
      "count_per_page": 20,
      "total_count": 59055,
      "current_page": 1,
      "total_pages": 2953,
      "_links": {
        "next": {
          "href": "/v2/animals?type=dog&page=2"
        }
      }
    }
 },
  
  


curl -O  'test.txt' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjA5YzcyZTAxYjI3NDdhMWE1MjEwMmViZThkZWI4NDRkMjI3ZThlYmFiMDVhN2RhNjMzMWI5NzU3YWNkMDJjYTEzYTVhYmEyZDg3ZWFkZDkxIiwiaWF0IjoxNTk1Mzc5NTM5LCJuYmYiOjE1OTUzNzk1MzksImV4cCI6MTU5NTM4MzEzOSwic3ViIjoiIiwic2NvcGVzIjpbXX0.BK6zdQ7KsOa5NTyHrQxDomqUc8fQ7goik4bZekc9atroXPO7hpMFyThaASzHDBz0id0DXmK24QayNi3sa1HVgeAjwlL68PVr8zEinZUKSRZNNrRsWyGMcvOMsXx9qQEegKwHqSvJGWqI_SBPa-4b0tv61r-gsCT2o7Zib5ewkKk3G93YGGyN3Tutc-Ci67x4-FQLLSVz6_91hkv3GNqBQ9pDIIlr-kF4OkaxEHgC0niVRPMZEb5VB1LyF4V4uQC60nUqnlh0VinflGK31RhSDQS-YC0leevCMBgm7ArEkLX1ZeBEdOB0irQaYO2rlC4gj9hDhvv40cCncL0g8EGTKg"  https://api.petfinder.com/v2/animals?type=dog&page=5


{
    "type": {
        "name": "Dog",
        "coats": [
            "Hairless",
            "Short",
            "Medium",
            "Long",
            "Wire",
            "Curly"
        ],
        "colors": [
            "Apricot / Beige",
            "Bicolor",
            "Black",
            "Brindle",
            "Brown / Chocolate",
            "Golden",
            "Gray / Blue / Silver",
            "Harlequin",
            "Merle (Blue)",
            "Merle (Red)",
            "Red / Chestnut / Orange",
            "Sable",
            "Tricolor (Brown, Black, & White)",
            "White / Cream",
            "Yellow / Tan / Blond / Fawn"
        ],
        "genders": [],
            "published_at": "2020-07-20T14:49:09+0000",
        "_links": {
            "self": {
                "href": "/v2/types/dog"
            },
            "breeds": {
                "href": "/v2/types/dog/breeds"
            }
        },
        "tags": []
        ,
        "photos":[]
        ,
        "status": []
    }
}


