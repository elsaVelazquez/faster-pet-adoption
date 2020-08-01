curl -O '../data/api_dump_2020-07.json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6Ijk5NzAwMTYxOTE1NjBhOGU2NzZkMTQ2NjIyMDE1NmZlN2U1YmZkNzgwYmViMWQ3ZmQ5YzljYWRjOTBiYmVlNzA3ZGE4YTRmZmU0OTMwMGRjIiwiaWF0IjoxNTk1Mjc5NDIwLCJuYmYiOjE1OTUyNzk0MjAsImV4cCI6MTU5NTI4MzAyMCwic3ViIjoiIiwic2NvcGVzIjpbXX0.JxLi3yhHOh_d8aAmQMz5lVxlS4ZDor68H8NEvcYdvgOaJ7s2JsvWrzTQiVv70cmbDxes9vXp0RKOmJK3aIXov72I31uwSieYgOTpx1oVIlLGFz2WORU0gtZ2USNkIXGV8usqArsgl2gCpSzEnN14ZH_5z885XHUBocZarREJwo8PqyfXgybNzbzWHcL-XQiKieuDNBjgH1RaIqbUfWcto_7d3S093gCCkDlnXcrdq8M5LJTUnIhSbTBdyGeRHLTQPLGVxvjQW6IWjYAbCAIgYNOgAKxmlSI0n5aJHDoNle6CAcUwtm9xWKKw4jY6IIFKX1uMlQZ-UcnpB9BiRIcXqg" https://api.petfinder.com/v2/animals?type=dog&page=4

curl -o 'test_no_header.txt' "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImNlNjE2OWIzNmEwYzg1NmQ4NTEyMzI1YWUzMWQzNTk5ZjJkOWY4MGExMTJmZmYxZWFhYzMyZTBiMDQ2MTVmYjI1MWU5Yzg5MDcxMTEyOGYxIiwiaWF0IjoxNTk1MzM0ODUwLCJuYmYiOjE1OTUzMzQ4NTAsImV4cCI6MTU5NTMzODQ1MCwic3ViIjoiIiwic2NvcGVzIjpbXX0.HDEDV_UoHpHsHNZ7uDdexAY672XCwzhUBLFn02Dazjx6RlFPSmjD0FLWAreKP8I0ARcfHD9MLTfSedyRA3IA7UKYammBXE0lHnufWsnJufJmUhqcO5dTGNQw_XtrDIdQH1jkuPdbdUTgsYtrM47IMhWQDlxrSDHePrFpOiCvV1YnL2N2gdGYAtopeYtGCMY-56iGAbl_McgR6MbHlPY3uIkc9JHDS0M-cwiN39uZ6tI7i6_erQL0lS2bV45Wy51ZHmZpANUzTSTHiRzMteCbJ743n3gASAzGJS2ArhlMYFqoWj3oI2Lo6jgL2NyxN0tTZB6RBIetwIR3UBNCJFrYnw" https://api.petfinder.com/v2/animals?type=dog&count_per_page=100


curl -O  '../data/test.txt' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjQ2MTBlNGU0M2I3YWJmNTEwYzFhZjFlMGQ3OTk1Nzc2N2ExZWUzYmVlMTA3ZmNkNDdkYjY4YzY4NWRkYjk0MGE0Yzc4NzI5OWFkMzAzOGE5IiwiaWF0IjoxNTk1NzMwODU0LCJuYmYiOjE1OTU3MzA4NTQsImV4cCI6MTU5NTczNDQ1NCwic3ViIjoiIiwic2NvcGVzIjpbXX0.mFJFYzIhflJ-na2TfKsoWzGzuEfVbN_2ASdiPdVk8hS0ZdGwoYxhP_Rn_fIQvzpxkouheqHoqGG-bOi2wo0QDSNxj71uRujJ6lqhKakLLA-qrg-liTIC4Pej5f6unye2Pm_cRRqVwNHU1VO5ci745D7RPxSBaMhqAmnVboTukF7FEQFDvuneNsQ-51GNHKzRdjztICoUVjklM4fIj4VOX6o07mapouEWsyVlxk8lEkmBYqxBdlB3LJRvwEbCoMBt-K51wMPth-xTx56YLGVtiNd-nVSmDB0W0VGG8nYBzdX6nW95y0hD7kunT9ixQhZ5QpjPCNptdZihxZfy00VVWw"  https://api.petfinder.com/v2/animals?type=dog&page=5


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
        "status": [
            "adoptable", 
            "adopted"
        ]
    }
} >test.txt
