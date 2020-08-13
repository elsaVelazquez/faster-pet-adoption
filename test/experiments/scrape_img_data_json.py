curl -o '../data/img_dumps/api_img_dump_2019-05.txt' -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjExZGVkNWU0NTJkZTA3OTQyZTk5NmMzYmRmMjFjODgxMzNiMTYyMGQ5Y2U3YTQ3OTk1NGJjNmRkYmQyYzIwMTQ3OGE2MjdmNjU0YTMxYTA1IiwiaWF0IjoxNTk0ODc5MjMzLCJuYmYiOjE1OTQ4NzkyMzMsImV4cCI6MTU5NDg4MjgzMywic3ViIjoiIiwic2NvcGVzIjpbXX0.PMkyCVhaTAwYH5yDzVsLd5VUJ99h1WWB47JtjG7qaGV84MPzQYuZ7iKdxfvKh8H6VnmVhfsrhqN1XkNjZPBnJ5G8rdorUwovT1EBJ3ySP14PZdGWHu0ma9Vk9-fT1w4-R9NzpFO2NGvTKwN9fD81td8tRk68MwrcIgkeMTDRebMT9EGpbtAsgsC0WAPYHZIg00YKnJH_nky1nMy0af0vT4a6P0ZPuH_8Tua068vES3bYZ6md70Q2UTlHaJL0WjzeW_mmP6o_kOFz7LhSAHnfFsCOBs3Qjc3aCAYA5tIqGf4yR_YeP7HIIR92hXwqm6aInMiG1XX8Lr4y1mo8w8KAdg" https://api.petfinder.com/v2/animals?type=dog&page=2
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

curl -o 'adopted.csv'  -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImJlODM4MDhlNWE0N2Y5NDJlMTkwYWY1N2ZhZmNlZTdlZjhmNDIwMTU2NzE4MGM3OWRlMDNjN2YwOGU0ZWQzZjg1MzZhODhiNTI1ZTg4Y2Y1IiwiaWF0IjoxNTk1OTg2NjI3LCJuYmYiOjE1OTU5ODY2MjcsImV4cCI6MTU5NTk5MDIyNywic3ViIjoiIiwic2NvcGVzIjpbXX0.W8wDgvl2JKjpCrgqN6yvB5FCVsbHTevOsv9-NLatiEqnWhv_U4VH15wvMxdW5lwXzG8W01ftNTcvF75tPU55R9CoeBnjcGCJ_OX-f89LAOsjmu0GtHNj0ZznrCbHJ-TOcOwr2a-VINLYi9u6ZQVopqMLF8LF5oj3QtZtDZW2BUYvtQnGFARaNOvrALR7DVPZ-VvG8FwK83OJ2wCGCSpUmdTVOaZVuRAw7kfIJqVrWbV3DlYcl8YiZE961jjL5mjm4ThTVU7nmWLtAjKzRKlRIxT6hzLGeAo-DfJgKqa173e_9ogfWxNq8CkKsNgY9LmH6ohK7JUisN6k9j1gUd1OIw" GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog 

>adoptable.csv


curl -o '../data/csv/api_img_dump_2019-05.txt' "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImJlODM4MDhlNWE0N2Y5NDJlMTkwYWY1N2ZhZmNlZTdlZjhmNDIwMTU2NzE4MGM3OWRlMDNjN2YwOGU0ZWQzZjg1MzZhODhiNTI1ZTg4Y2Y1IiwiaWF0IjoxNTk1OTg2NjI3LCJuYmYiOjE1OTU5ODY2MjcsImV4cCI6MTU5NTk5MDIyNywic3ViIjoiIiwic2NvcGVzIjpbXX0.W8wDgvl2JKjpCrgqN6yvB5FCVsbHTevOsv9-NLatiEqnWhv_U4VH15wvMxdW5lwXzG8W01ftNTcvF75tPU55R9CoeBnjcGCJ_OX-f89LAOsjmu0GtHNj0ZznrCbHJ-TOcOwr2a-VINLYi9u6ZQVopqMLF8LF5oj3QtZtDZW2BUYvtQnGFARaNOvrALR7DVPZ-VvG8FwK83OJ2wCGCSpUmdTVOaZVuRAw7kfIJqVrWbV3DlYcl8YiZE961jjL5mjm4ThTVU7nmWLtAjKzRKlRIxT6hzLGeAo-DfJgKqa173e_9ogfWxNq8CkKsNgY9LmH6ohK7JUisN6k9j1gUd1OIw" https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog 


curl -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6ImJlODM4MDhlNWE0N2Y5NDJlMTkwYWY1N2ZhZmNlZTdlZjhmNDIwMTU2NzE4MGM3OWRlMDNjN2YwOGU0ZWQzZjg1MzZhODhiNTI1ZTg4Y2Y1IiwiaWF0IjoxNTk1OTg2NjI3LCJuYmYiOjE1OTU5ODY2MjcsImV4cCI6MTU5NTk5MDIyNywic3ViIjoiIiwic2NvcGVzIjpbXX0.W8wDgvl2JKjpCrgqN6yvB5FCVsbHTevOsv9-NLatiEqnWhv_U4VH15wvMxdW5lwXzG8W01ftNTcvF75tPU55R9CoeBnjcGCJ_OX-f89LAOsjmu0GtHNj0ZznrCbHJ-TOcOwr2a-VINLYi9u6ZQVopqMLF8LF5oj3QtZtDZW2BUYvtQnGFARaNOvrALR7DVPZ-VvG8FwK83OJ2wCGCSpUmdTVOaZVuRAw7kfIJqVrWbV3DlYcl8YiZE961jjL5mjm4ThTVU7nmWLtAjKzRKlRIxT6hzLGeAo-DfJgKqa173e_9ogfWxNq8CkKsNgY9LmH6ohK7JUisN6k9j1gUd1OIw" GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog -O


curl  -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjM2ZTkxODcxMGEwMzMwMzQ3ZTAxMTY4YjhiZjU0Yjg1NDE3Y2U1ZjJmNmMzNGNmYzIyYjVmY2M1MDMyNjgzODQyYmFhMjFmYWViZjg2ZTU2IiwiaWF0IjoxNTk2MzI2MjAyLCJuYmYiOjE1OTYzMjYyMDIsImV4cCI6MTU5NjMyOTgwMiwic3ViIjoiIiwic2NvcGVzIjpbXX0.cYdl5ObfCEk2a6LYbkDYrWqUxSJbsJm_9VCYORzomu0ptflV2kyEY16bduF5oLAcPVDKfF-zwAaWo4SzTxRHVoqSi7sxpVb43IsgCXOXYvt4BqoQtuZ2MxramsnGtX47Tj9pQbLLwUL8BDaRPNoMuD_ehQ_mNM6teKsPQ0SVG7927wQDpNvdL5xRIfPgz4kLPaPLikJi9ThR1MC03zxb4mRAjhRTxb9VrG61yLQeapzLauVduVCFe4KJjl3DmIKJFdqxLqE6Jm5_JLF6LZce12rwsMhKbltMGqA2bmGfLcr73lQgfH8C87eJKOB0Pr80F6IMMHZgb3NY54OeYB3Xpg" GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog&page=2 -O
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
    ],
    "pagination": {
        "count_per_page": 40,
        "total_pages": 100
        }
    }
}



curl  -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjM2ZTkxODcxMGEwMzMwMzQ3ZTAxMTY4YjhiZjU0Yjg1NDE3Y2U1ZjJmNmMzNGNmYzIyYjVmY2M1MDMyNjgzODQyYmFhMjFmYWViZjg2ZTU2IiwiaWF0IjoxNTk2MzI2MjAyLCJuYmYiOjE1OTYzMjYyMDIsImV4cCI6MTU5NjMyOTgwMiwic3ViIjoiIiwic2NvcGVzIjpbXX0.cYdl5ObfCEk2a6LYbkDYrWqUxSJbsJm_9VCYORzomu0ptflV2kyEY16bduF5oLAcPVDKfF-zwAaWo4SzTxRHVoqSi7sxpVb43IsgCXOXYvt4BqoQtuZ2MxramsnGtX47Tj9pQbLLwUL8BDaRPNoMuD_ehQ_mNM6teKsPQ0SVG7927wQDpNvdL5xRIfPgz4kLPaPLikJi9ThR1MC03zxb4mRAjhRTxb9VrG61yLQeapzLauVduVCFe4KJjl3DmIKJFdqxLqE6Jm5_JLF6LZce12rwsMhKbltMGqA2bmGfLcr73lQgfH8C87eJKOB0Pr80F6IMMHZgb3NY54OeYB3Xpg" GET https://api.petfinder.com/v2/animals?status=adopted&animals?type=dog&page=3 -O
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
    ],
    "pagination": {
        "count_per_page": 40,
        "total_pages": 100
        }
    }
}


curl  -H "Authorization: Bearer eyjXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.eyJhdWQiOiIxOHFkRGVOMjJWSXVOUG01WEJFOXVIUnQycWJBckRWN0Y2VEFjRVdZRHlTVUpTNmRnZCIsImp0aSI6IjM2ZTkxODcxMGEwMzMwMzQ3ZTAxMTY4YjhiZjU0Yjg1NDE3Y2U1ZjJmNmMzNGNmYzIyYjVmY2M1MDMyNjgzODQyYmFhMjFmYWViZjg2ZTU2IiwiaWF0IjoxNTk2MzI2MjAyLCJuYmYiOjE1OTYzMjYyMDIsImV4cCI6MTU5NjMyOTgwMiwic3ViIjoiIiwic2NvcGVzIjpbXX0.cYdl5ObfCEk2a6LYbkDYrWqUxSJbsJm_9VCYORzomu0ptflV2kyEY16bduF5oLAcPVDKfF-zwAaWo4SzTxRHVoqSi7sxpVb43IsgCXOXYvt4BqoQtuZ2MxramsnGtX47Tj9pQbLLwUL8BDaRPNoMuD_ehQ_mNM6teKsPQ0SVG7927wQDpNvdL5xRIfPgz4kLPaPLikJi9ThR1MC03zxb4mRAjhRTxb9VrG61yLQeapzLauVduVCFe4KJjl3DmIKJFdqxLqE6Jm5_JLF6LZce12rwsMhKbltMGqA2bmGfLcr73lQgfH8C87eJKOB0Pr80F6IMMHZgb3NY54OeYB3Xpg" GET https://api.petfinder.com/v2/animals?status=adopted&current_page=8 -O
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
    ],
    "pagination": {
        "count_per_page": 40,
        "total_pages": 100
        }
    }
}