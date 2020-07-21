curl -O '../data/api_dump_2020-07.json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6Ijk5NzAwMTYxOTE1NjBhOGU2NzZkMTQ2NjIyMDE1NmZlN2U1YmZkNzgwYmViMWQ3ZmQ5YzljYWRjOTBiYmVlNzA3ZGE4YTRmZmU0OTMwMGRjIiwiaWF0IjoxNTk1Mjc5NDIwLCJuYmYiOjE1OTUyNzk0MjAsImV4cCI6MTU5NTI4MzAyMCwic3ViIjoiIiwic2NvcGVzIjpbXX0.JxLi3yhHOh_d8aAmQMz5lVxlS4ZDor68H8NEvcYdvgOaJ7s2JsvWrzTQiVv70cmbDxes9vXp0RKOmJK3aIXov72I31uwSieYgOTpx1oVIlLGFz2WORU0gtZ2USNkIXGV8usqArsgl2gCpSzEnN14ZH_5z885XHUBocZarREJwo8PqyfXgybNzbzWHcL-XQiKieuDNBjgH1RaIqbUfWcto_7d3S093gCCkDlnXcrdq8M5LJTUnIhSbTBdyGeRHLTQPLGVxvjQW6IWjYAbCAIgYNOgAKxmlSI0n5aJHDoNle6CAcUwtm9xWKKw4jY6IIFKX1uMlQZ-UcnpB9BiRIcXqg" https://api.petfinder.com/v2/animals?type=dog&page=4

curl -o 'test.txt' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImZmZWIxOTNlM2VlOTViZTFkMzk1NDVlNmFiMDRiNjNhMWQ4OTRiMDI1ZmY2YjJmYTYzZjY3OTI1MWYzOGVhNDA4Mjg0MjgwYjJlNjM2ZTIwIiwiaWF0IjoxNTk1MjgzMzI5LCJuYmYiOjE1OTUyODMzMjksImV4cCI6MTU5NTI4NjkyOSwic3ViIjoiIiwic2NvcGVzIjpbXX0.KdKb_p2xeaO55hkDtrn9TiSjWI6BIuG6IcO-PQ3428e6XqAEvk8froBgLCOhQwnLfAKiTzQNHZx96RnCdqSuYbCa_jNylVSbT7RTXuIfT1YNJ-E3YGkxu8zQgcU6yUOzAJxNndg5RbAjGdlA1hZjd5WjQnNX80lHbfrcS15wcb-KjvF1GkiZ290RsXWUnxlHKlOQRM4yb59B-X1H4WXlCbH-72znC4haWQHlJENKfc372xKX4-knAamawd72VKqoZzZsYJ5fX2-W9v1UosPIUff4sDwAdQMryItgjTrxcT5Fsfgo0-mSesFhfIXzfQX-ybym1AlRiS5x1koY0ZM5lg" https://api.petfinder.com/v2/animals?type=dog&count_per_page=100


curl -o  'test.txt' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjQ3YjgxM2IzYTJhYTVhOGVkNmUzZDdjZmZlZDhiNjE3NWUxZDU4NmI5MjZhOGM3YmM1ODUyOWU4YzUzMDJkYTJmODU0NDBhZjhiODBhM2U2IiwiaWF0IjoxNTk1Mjg3MDMxLCJuYmYiOjE1OTUyODcwMzEsImV4cCI6MTU5NTI5MDYzMSwic3ViIjoiIiwic2NvcGVzIjpbXX0.G-ubKC4bRQ0aOoiuPyNxEz9TONa3u326SuVGhVxhhbiGrIu03lxcqSexTTQrg8gGrxQo3Ej2ZJmt1fKKkjK0cS609ObP__vYaU648DikcHx_AGZm2hpq_X3eBMGyQYxJuYyH5uaQ08J1ss4NzTgnkC7zC1AB7aq98p3w2faE9zMeY9OYZTmKwb1VCHfgqObS6oVkHniQH98POSIYaeo-iSYk-lOrOsD2IFj1YRHyUQhoeDJ9ST59xjShdlh_b4VjwURy58j0QmEgyj_nNB_pip72lpxyy6pmjUmP3VoLTXft9TumSZe52A_mTfktpcVAgpzCZFE1PBqn27tNxU-CVA"  https://api.petfinder.com/v2/animals?type=dog&page=5


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
