curl -o '../data/img_dumps/api_img_dump_2019-05.txt' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjExZGVkNWU0NTJkZTA3OTQyZTk5NmMzYmRmMjFjODgxMzNiMTYyMGQ5Y2U3YTQ3OTk1NGJjNmRkYmQyYzIwMTQ3OGE2MjdmNjU0YTMxYTA1IiwiaWF0IjoxNTk0ODc5MjMzLCJuYmYiOjE1OTQ4NzkyMzMsImV4cCI6MTU5NDg4MjgzMywic3ViIjoiIiwic2NvcGVzIjpbXX0.PMkyCVhaTAwYH5yDzVsLd5VUJ99h1WWB47JtjG7qaGV84MPzQYuZ7iKdxfvKh8H6VnmVhfsrhqN1XkNjZPBnJ5G8rdorUwovT1EBJ3ySP14PZdGWHu0ma9Vk9-fT1w4-R9NzpFO2NGvTKwN9fD81td8tRk68MwrcIgkeMTDRebMT9EGpbtAsgsC0WAPYHZIg00YKnJH_nky1nMy0af0vT4a6P0ZPuH_8Tua068vES3bYZ6md70Q2UTlHaJL0WjzeW_mmP6o_kOFz7LhSAHnfFsCOBs3Qjc3aCAYA5tIqGf4yR_YeP7HIIR92hXwqm6aInMiG1XX8Lr4y1mo8w8KAdg" https://api.petfinder.com/v2/animals?type=dog&page=2
{
    "type": {
        "status": "adopted",
        "name": "Dog",

            "published_at": "2019-05-04T14:49:09+0000",
            "distance": null,

        "photos":[]
        ,
    }
}

curl -o 'adopted.csv'  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImJlODM4MDhlNWE0N2Y5NDJlMTkwYWY1N2ZhZmNlZTdlZjhmNDIwMTU2NzE4MGM3OWRlMDNjN2YwOGU0ZWQzZjg1MzZhODhiNTI1ZTg4Y2Y1IiwiaWF0IjoxNTk1OTg2NjI3LCJuYmYiOjE1OTU5ODY2MjcsImV4cCI6MTU5NTk5MDIyNywic3ViIjoiIiwic2NvcGVzIjpbXX0.W8wDgvl2JKjpCrgqN6yvB5FCVsbHTevOsv9-NLatiEqnWhv_U4VH15wvMxdW5lwXzG8W01ftNTcvF75tPU55R9CoeBnjcGCJ_OX-f89LAOsjmu0GtHNj0ZznrCbHJ-TOcOwr2a-VINLYi9u6ZQVopqMLF8LF5oj3QtZtDZW2BUYvtQnGFARaNOvrALR7DVPZ-VvG8FwK83OJ2wCGCSpUmdTVOaZVuRAw7kfIJqVrWbV3DlYcl8YiZE961jjL5mjm4ThTVU7nmWLtAjKzRKlRIxT6hzLGeAo-DfJgKqa173e_9ogfWxNq8CkKsNgY9LmH6ohK7JUisN6k9j1gUd1OIw" GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog 

>adoptable.csv


curl -o '../data/csv/api_img_dump_2019-05.txt' "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImJlODM4MDhlNWE0N2Y5NDJlMTkwYWY1N2ZhZmNlZTdlZjhmNDIwMTU2NzE4MGM3OWRlMDNjN2YwOGU0ZWQzZjg1MzZhODhiNTI1ZTg4Y2Y1IiwiaWF0IjoxNTk1OTg2NjI3LCJuYmYiOjE1OTU5ODY2MjcsImV4cCI6MTU5NTk5MDIyNywic3ViIjoiIiwic2NvcGVzIjpbXX0.W8wDgvl2JKjpCrgqN6yvB5FCVsbHTevOsv9-NLatiEqnWhv_U4VH15wvMxdW5lwXzG8W01ftNTcvF75tPU55R9CoeBnjcGCJ_OX-f89LAOsjmu0GtHNj0ZznrCbHJ-TOcOwr2a-VINLYi9u6ZQVopqMLF8LF5oj3QtZtDZW2BUYvtQnGFARaNOvrALR7DVPZ-VvG8FwK83OJ2wCGCSpUmdTVOaZVuRAw7kfIJqVrWbV3DlYcl8YiZE961jjL5mjm4ThTVU7nmWLtAjKzRKlRIxT6hzLGeAo-DfJgKqa173e_9ogfWxNq8CkKsNgY9LmH6ohK7JUisN6k9j1gUd1OIw" https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog 


curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImJlODM4MDhlNWE0N2Y5NDJlMTkwYWY1N2ZhZmNlZTdlZjhmNDIwMTU2NzE4MGM3OWRlMDNjN2YwOGU0ZWQzZjg1MzZhODhiNTI1ZTg4Y2Y1IiwiaWF0IjoxNTk1OTg2NjI3LCJuYmYiOjE1OTU5ODY2MjcsImV4cCI6MTU5NTk5MDIyNywic3ViIjoiIiwic2NvcGVzIjpbXX0.W8wDgvl2JKjpCrgqN6yvB5FCVsbHTevOsv9-NLatiEqnWhv_U4VH15wvMxdW5lwXzG8W01ftNTcvF75tPU55R9CoeBnjcGCJ_OX-f89LAOsjmu0GtHNj0ZznrCbHJ-TOcOwr2a-VINLYi9u6ZQVopqMLF8LF5oj3QtZtDZW2BUYvtQnGFARaNOvrALR7DVPZ-VvG8FwK83OJ2wCGCSpUmdTVOaZVuRAw7kfIJqVrWbV3DlYcl8YiZE961jjL5mjm4ThTVU7nmWLtAjKzRKlRIxT6hzLGeAo-DfJgKqa173e_9ogfWxNq8CkKsNgY9LmH6ohK7JUisN6k9j1gUd1OIw" GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog -O


curl  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjRkZWQ1ZmY3ZWM2MDllMzdkNDE1ZDgzMWUyYzY1MzAxOThhM2I3MDM5M2EwMmQ5MWZkYzk4ZDk0MGVkYmEzNWIzNzJjMWVmZmVmNjI4YTk5IiwiaWF0IjoxNTk2MjQ4NzcwLCJuYmYiOjE1OTYyNDg3NzAsImV4cCI6MTU5NjI1MjM3MCwic3ViIjoiIiwic2NvcGVzIjpbXX0.lB3nuF-2CljpcLY5dfYKhYgJ90r9LbfA_6Px-ZxTagKCro5MIOfz2X_q3a8IshFNzryB4E9ZOr1D1kfdbB8wkTkX1Abh7FflJsaM8tCaq0QcrDrNIIGephg9h_ybaRBkgjpsj-WsV1hzPsskfx56ocAsjcqZ2pbOmMqESHWUuF4jciEWQzHCjxaJ27nQMQWfoOZkLFHvGfuTbCJG620-52zLFUVXxNkX42WzXkzSPR3weUcVsIV9tix68HgbK4FKa_jDoDbD_H5YKlgDVFRRZUy0rx_jylBY3oTOUnofiBKRSuycPIn2MxOjqGzhe8Fy0Ouxk9XamPQZ2SoA52Nyyw" GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog -O
{
    "animals": [
        {
            
            "species": "Dog",
            "breeds": [],
            "age": [],
            "gender": [],
            "size": "Medium",
            "coat": null,
            "tags": [
                "Cute",
                "Intelligent",
                "Large",
                "Playful",
                "Happy",
                "Affectionate"
            ],
            "name": "",
            "description": "",
            "photos": [],
            "status": "adopted",
            "published_at": "",
        }
    ]
    }
}
>a_latest_adoptable.JSON
