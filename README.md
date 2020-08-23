---
title: Habits
author: John Doe
date: March 22, 2005
output: html_document
---


Workflow:
Data Ingestion
had to figure out how to get out the data i wanted using their whack API
    ended up making a Python  cron job
    
    You will have to open the file creds_temp.txt ('src/pipelines/data_ingestion/cron/creds_temp.txt'), copy and paste your API key, given by PetFinders.com, rename the file as creds.txt and save it in that same directory, for the ingestion pipeline to be automated for you.  

Clean the Data
    Data Structures Conversions-- turned all the JSON into csv with a python function

Data Wrangling/Munging
I used an AWS S3 bucket to store the data and interacted with it using PySpark.
I created a keypair using EC2.



I would have lost about 18% of the data if I had dropped all NaNs.  Because many of the NaNs were simply descriptions that were not filled out, I replaced those rows with the string "DUMMY_TEXT".  



## Initial Schema

root
 |-- _links: struct (nullable = true)
 |    |-- organization: struct (nullable = true)
 |    |    |-- href: string (nullable = true)
 |    |-- self: struct (nullable = true)
 |    |    |-- href: string (nullable = true)
 |    |-- type: struct (nullable = true)
 |    |    |-- href: string (nullable = true)
 |-- age: string (nullable = true)
 |-- attributes: struct (nullable = true)
 |    |-- declawed: boolean (nullable = true)
 |    |-- house_trained: boolean (nullable = true)
 |    |-- shots_current: boolean (nullable = true)
 |    |-- spayed_neutered: boolean (nullable = true)
 |    |-- special_needs: boolean (nullable = true)
 |-- breeds: struct (nullable = true)
 |    |-- mixed: boolean (nullable = true)
 |    |-- primary: string (nullable = true)
 |    |-- secondary: string (nullable = true)
 |    |-- unknown: boolean (nullable = true)
 |-- coat: string (nullable = true)
 |-- colors: struct (nullable = true)
 |    |-- primary: string (nullable = true)
 |    |-- secondary: string (nullable = true)
 |    |-- tertiary: string (nullable = true)
 |-- contact: struct (nullable = true)
 |    |-- address: struct (nullable = true)
 |    |    |-- address1: string (nullable = true)
 |    |    |-- address2: string (nullable = true)
 |    |    |-- city: string (nullable = true)
 |    |    |-- country: string (nullable = true)
 |    |    |-- postcode: string (nullable = true)
 |    |    |-- state: string (nullable = true)
 |    |-- email: string (nullable = true)
 |    |-- phone: string (nullable = true)
 |-- description: string (nullable = true)
 |-- distance: string (nullable = true)
 |-- environment: struct (nullable = true)
 |    |-- cats: boolean (nullable = true)
 |    |-- children: boolean (nullable = true)
 |    |-- dogs: boolean (nullable = true)
 |-- gender: string (nullable = true)
 |-- id: long (nullable = true)
 |-- name: string (nullable = true)
 |-- organization_animal_id: string (nullable = true)
 |-- organization_id: string (nullable = true)
 |-- photos: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- full: string (nullable = true)
 |    |    |-- large: string (nullable = true)
 |    |    |-- medium: string (nullable = true)
 |    |    |-- small: string (nullable = true)
 |-- primary_photo_cropped: struct (nullable = true)
 |    |-- full: string (nullable = true)
 |    |-- large: string (nullable = true)
 |    |-- medium: string (nullable = true)
 |    |-- small: string (nullable = true)
 |-- published_at: string (nullable = true)
 |-- size: string (nullable = true)
 |-- species: string (nullable = true)
 |-- status: string (nullable = true)
 |-- status_changed_at: string (nullable = true)
 |-- tags: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- type: string (nullable = true)
 |-- url: string (nullable = true)
 |-- videos: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- embed: string (nullable = true)



## Reduced Schema
df_breed = df.select('id', 'age', 'gender', 'breeds', 'description', 'status', 'photos', 'status_changed_at')

root
 |-- id: long (nullable = true)
 |-- age: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- breeds: struct (nullable = true)
 |    |-- mixed: boolean (nullable = true)
 |    |-- primary: string (nullable = true)
 |    |-- secondary: string (nullable = true)
 |    |-- unknown: boolean (nullable = true)
 |-- description: string (nullable = true)
 |-- status: string (nullable = true)
 |-- photos: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- full: string (nullable = true)
 |    |    |-- large: string (nullable = true)
 |    |    |-- medium: string (nullable = true)
 |    |    |-- small: string (nullable = true)
 |-- status_changed_at: string (nullable = true)
 |-- species: string (nullable = true)
 
 
 

## After Inserting Dummy Data Certain Fields

+--------+-----+------+--------------------+--------------------+-------+--------------------+--------------------+
|      id|  age|gender|              breeds|         description| status|              photos|   status_changed_at|
+--------+-----+------+--------------------+--------------------+-------+--------------------+--------------------+
|48734452|Adult|  Male|[true, Chihuahua,...|Dexter is a cute ...|adopted|                  []|2020-08-10T03:39:...|
|48734448|Young|  Male|[false, Tabby,, f...|          DUMMY_TEXT|adopted|                  []|2020-08-10T03:38:...|
|48734449|Young|Female|[false, Domestic ...|          DUMMY_TEXT|adopted|                  []|2020-08-10T03:38:...|
|48734431|Young|Female|[false, Great Dan...|You can fill out ...|adopted|[[https://dl5zpyw...|2020-08-10T03:23:...|
|48734430| Baby|  Male|[true, Domestic S...|HUBBLE is a super...|adopted|[[https://dl5zpyw...|2020-08-10T03:22:...|
|48734406|Young|Female|[true, Domestic S...|Hi. I&amp;#39;m M...|adopted|[[https://dl5zpyw...|2020-08-10T03:08:...|
|48734405|Young|  Male|[true, Domestic S...|Ross is a very sw...|adopted|[[https://dl5zpyw...|2020-08-10T03:08:...|
|48734398| Baby|  Male|[true, Shepherd, ...|6 week old male, ...|adopted|[[https://dl5zpyw...|2020-08-10T03:07:...|
|48734397| Baby|  Male|[true, Shepherd, ...|6 week old male, ...|adopted|[[https://dl5zpyw...|2020-08-10T03:07:...|
|48734390| Baby|  Male|[false, Domestic ...|          DUMMY_TEXT|adopted|                  []|2020-08-10T03:06:...|
|48734391| Baby|Female|[false, Domestic ...|          DUMMY_TEXT|adopted|                  []|2020-08-10T03:06:...|
|48734361|Young|  Male|[false, Domestic ...|You can fill out ...|adopted|[[https://dl5zpyw...|2020-08-10T02:54:...|
|48734360|Young|Female|[true, Domestic S...|          DUMMY_TEXT|adopted|                  []|2020-08-10T02:53:...|
|48734359|Young|  Male|[true, Domestic S...|Will looks just l...|adopted|[[https://dl5zpyw...|2020-08-10T02:53:...|
|48734356|Adult|Female|[true, Australian...|          DUMMY_TEXT|adopted|[[https://dl5zpyw...|2020-08-10T02:53:...|
|48734355|Young|Female|[true, Husky, Cat...|Dakota is a lovel...|adopted|[[https://dl5zpyw...|2020-08-10T02:53:...|
|48734309|Young|  Male|[true, Domestic S...|Wendall is just a...|adopted|[[https://dl5zpyw...|2020-08-10T02:38:...|
|48734298|Adult|Female|[true, Chihuahua,...|You can fill out ...|adopted|[[https://dl5zpyw...|2020-08-10T02:35:...|
|48734268| Baby|  Male|[false, Domestic ...|Adopt Butters!
Bu...|adopted|[[https://dl5zpyw...|2020-08-10T02:25:...|
|48734244| Baby|  Male|[true, Hound, Bla...|Steve is a 10 mon...|adopted|[[https://dl5zpyw...|2020-08-10T02:22:...|
+--------+-----+------+--------------------+--------------------+-------+--------------------+--------------------+




EDA
+------+--------------------+-----+-------+-------+------+
|gender|              breeds|  age| status|species|Number|
+------+--------------------+-----+-------+-------+------+
|  Male|[true, Domestic S...| Baby|adopted|    Cat|    37|
|  Male|[true, Terrier, C...|Young|adopted|    Dog|    30|
|  Male|[false, Domestic ...| Baby|adopted|    Cat|    28|
|Female|[true, Domestic S...| Baby|adopted|    Cat|    22|
|  Male|[true, Labrador R...|Young|adopted|    Dog|    20|
|  Male|[false, Domestic ...|Young|adopted|    Cat|    18|
|Female|[true, Chihuahua,...|Young|adopted|    Dog|    17|
|  Male|[true, Domestic S...|Young|adopted|    Cat|    17|
|Female|[false, Domestic ...| Baby|adopted|    Cat|    17|
|Female|[true, Poodle,, f...|Young|adopted|    Dog|    16|
|Female|[true, Shepherd,,...|Young|adopted|    Dog|    15|
|Female|[true, Siamese,, ...| Baby|adopted|    Cat|    15|
|  Male|[true, Siamese,, ...| Baby|adopted|    Cat|    14|
|  Male|[false, Domestic ...|Adult|adopted|    Cat|    13|
|  Male|[true, Pit Bull T...| Baby|adopted|    Dog|    12|
|  Male|[true, German She...| Baby|adopted|    Dog|    11|
|  Male|[true, Yorkshire ...|Young|adopted|    Dog|    10|
|Female|[true, Maltese, P...|Young|adopted|    Dog|    10|
|Female|[false, Husky,, f...|Young|adopted|    Dog|    10|
|Female|[true, Jack Russe...|Adult|adopted|    Dog|     9|
+------+--------------------+-----+-------+-------+------+
compare ratio of male and female dogs in shelters to ratios of adopted genders

compare by age groups


do a time series to see if there is any truth to covid driven adoption spikes- trends and seasons?
Can I predict when more dogs will be adopted?
When more will go to shelters?





find 1-3 features to really look into now that I have the data on adopted dogs

Regression - Lasso and Elastic Net-- predicting a quantity of dogs

Clustering-- because number of categories is known, < 10K samples so can use KMeans (could have also bootstrapped)




https://www.finex.co/how-to-display-html-in-github/
Displaying HTML Files in GitHub
Setting up an HTML page in GitHub is not difficult but it is a bit lengthy. Just follow these steps.

Create the HTML from your RMarkdown document and save to your local directory.
Create a new repo, or go to an existing repo, in your GitHub.
In the repo, create a new file called docs/index.html.
In the index.html file, type this code: <html><body><p>Hello World</p></body></html>
Commit the file.
In the repo, click on the Settings tab.
Scroll down to GitHub Pages Section.
Under “Source”, choose “master branch/docs folder” and save. If that doesn’t work, try the “master branch” and save.
A message will appear that your site is read to be published. Click on the link.
When Git finds the index.html file in a docs/ folder, it creates a web address for the contents. The address takes the form: http://username.github.io/repository
Go to that address. You should see your “Hello World” greeting. That is your index.html file.
Go back to the docs/ folder and open it.
Upload the HTML file you created in RMarkdown and commit.
Return to your github.io site but add the HTML file name to the address: http://username.github.io/repository/filename.html.
You should find your HTML posted there.