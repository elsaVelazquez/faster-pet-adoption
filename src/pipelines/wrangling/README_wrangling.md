To save time and maintain spirits, I did this in VS Code:


Remove any instances of pagination or animals:
Examples of stuff I removed:

"pagination": {
      "count_per_page": 20,
      "total_count": 7800826,
      "current_page": 1,
      "total_pages": 390042,
      "_links": {
        "next": {
          "href": "/v2/animals?status=adopted&page=2"
        }
      }
    }
  }
]



    "pagination": {
      "count_per_page": 20,
      "total_count": 7807006,
      "current_page": 1,
      "total_pages": 390351,
      "_links": {
        "next": {
          "href": "/v2/animals?status=adopted&page=2"
        }
      }
    }
  },
  {
    "animals": [









This is what the JSON should look like to work in PySpark correctly:

this is what the json looks like to get this schema
first few lines---->
[

      {
        "id": 48549327,
        "organization_id": "CA162",
        "url": "https://www.petfinder.com/dog/snap-48549327/ca/vacaville/solano-county-s-dot-pc-dot-a-ca162/?referrer_id=5957d654-0b8d-4a02-bbae-6c7dd49e1074",
        "type": "Dog",
        "species": "Dog",
        "breeds": {
          "primary": "Chihuahua",
          "secondary": "Mixed Breed",
          "mixed": true,
          "unknown": false
        },
        "colors": {
          "primary": null,
          "secondary": null,
          "tertiary": null
        },


##### 
last few lines--->
            "state": "GA",
            "postcode": "30019",
            "country": "US"
          }
        },
        "_links": {
          "self": {
            "href": "/v2/animals/48549284"
          },
          "type": {
            "href": "/v2/types/dog"
          },
          "organization": {
            "href": "/v2/organizations/ga537"
          }
        }
      },
      {
        "id": 48549285,
        "organization_id": "NC807",
        "url": "https://www.petfinder.com/dog/bruno-48549285/nc/raleigh/cause-for-paws-of-nc-nc807/?referrer_id=5957d654-0b8d-4a02-bbae-6c7dd49e1074",
        "type": "Dog",
        "species": "Dog",
        "breeds": {
          "primary": "Terrier",
          "secondary": null,
          "mixed": false,
          "unknown": false
        },
        "colors": {
          "primary": null,
          "secondary": null,
          "tertiary": null
        },
        "age": "Young",
        "gender": "Male",
        "size": "Medium",
        "coat": null,
        "attributes": {
          "spayed_neutered": false,
          "house_trained": false,
          "declawed": null,
          "special_needs": false,
          "shots_current": false
        },
        "environment": {
          "children": null,
          "dogs": null,
          "cats": null
        },
        "tags": [],
        "name": "Bruno",
        "description": "If you are interested in this animal please start by filling out an adoption application at &amp;lt;a href=&amp;#34;&amp;#34;http://www.cfp-nc.org/adopt&amp;#34;&amp;#34;&amp;gt;CFP-NC.org/adopt&amp;lt;/a&amp;gt; and we...",
        "organization_animal_id": "D2020125",
        "photos": [],
        "primary_photo_cropped": null,
        "videos": [],
        "status": "adoptable",
        "status_changed_at": "2020-07-21T10:03:19+0000",
        "published_at": "2020-07-21T10:03:19+0000",
        "distance": null,
        "contact": {
          "email": "careteam@cfp-nc.org",
          "phone": "9196734003",
          "address": {
            "address1": null,
            "address2": null,
            "city": "Raleigh",
            "state": "NC",
            "postcode": "27603",
            "country": "US"
          }
        },
        "_links": {
          "self": {
            "href": "/v2/animals/48549285"
          },
          "type": {
            "href": "/v2/types/dog"
          },
          "organization": {
            "href": "/v2/organizations/nc807"
          }
        }
      }
]



