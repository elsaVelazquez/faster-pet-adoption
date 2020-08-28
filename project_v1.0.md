<img src="https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/title_banner.png"  width=800>

<br />
<div class="baron baron__root baron__clipper _MODIFIER">
    <div class="baron__scroller">
        <!-- Your content here --><br>
     <br>
     <br>
     <br>
     <br>
    </div>

    <div class="baron__track">
        <div class="baron__control baron__up">▲</div>
        <div class="baron__free">
            <div class="baron__bar"></div>
        </div>
        <div class="baron__control baron__down">▼</div>
    </div>
</div>


### Are there *really* more female dogs in animal rescue shelters than male dogs?
<br />

![raw counts of male vs female dogs](src/readme/raw_counts.png)

## Data science application: Hypothesis Testing--> 
### Ho : There are 50% female dogs in shelters.  
### Ha : It is not the case that there are 50% female dogs in shelters.  
<br />

### Statistic:  A binomial test using stats.binom.

The goal is to determine if there is a statistically significant difference between female vs male dog populations in animal rescue shelters. 

<br />

### Conclusion: 
Because p != alpha, we fail to reject the null hypothesis and determine there are not 50% female dogs in shelters.  

<br />

<img src = "https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/images/reject_null_hyp.png" align=center>



<br />

### Is this the case for *all* subrgroups of dogs?
|<img src = "https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/imgs/by_age_and_gender.png" width=600 align=right> | <img src = "https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/imgs/dogs_grouped_by_age_and_gender.png" width=200 align=center>| 
|-|-|

### There are more male adult dogs in shelters.
<br />

# Revisit Data Science Application
## Adjusted Project Focus Is On Adult Male Dogs
<img src = "https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/images/fig3_workflow.png" width=500 align=center>

<br /> <br />
## Data Wrangling
### Web Scraping for Data Collection

The data was collected using <a href="https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/json_data_cleaning.py">OS-level Curl command line prompt </a>, written in python, that sped up the collection of 200,000 records from PetFinder's public API to less than 1 minute.

<br />

### Data Ingestion

Due to the API, the scrape returned 5000 JSON files with 20 records each. 
These records were mashed into 1 giant JSON file that revealed a <a href="https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/schemas.txt">multi-level schema</a> when put through a PySpark pipeline.
<br />
| <img src="https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/imgs/initial_eda.png" width=500 align=center> |  <img src="https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/imgs/final_working_json.png" width=500> |
|-|-|


<br /> <br />

### The next question:  Does the adult male dog's picture pose influence how fast it gets adopted from a rescue shelter?
 <br />
 
## Machine Learning

### Image Processing
Using img data from PetFinder.com, I began the process of image classification by finding existing python <a href="https://scikit-learn.org/stable/datasets/index.html">Scikit-Learn</a>, scikit-image libraries for image flattening.  

 <img src="https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/imgs/flatten_image.png" align=center> 

<br /> <br />



## By classifying animal shelter images and arrival and departure dates, a new hypothesis emerges from the data and we can now use science to determine if specific advertising methods can be used to help the adult male dog population.  
The feature selection process involves best methods to classify imgs with male dogs that are:
- ![#9900c5](https://placehold.it/15/9900c5?text=+)Standing
- ![#9900c5](https://placehold.it/15/9900c5?text=+)Sitting
- ![#9900c5](https://placehold.it/15/9900c5?text=+)Laying
- ![#9900c5](https://placehold.it/15/9900c5?text=+)Clothed

<br /> <br />
## Future Work
<br />
Through this dataset, it is possible to determine when and where there will be an influx of male dogs to which rescue shelters, and those shelters can then be informed of the conclusions of this investigation to help them best present the male dogs to help balance the ratio of adult males in animal rescue shelters.   

<br /><br />
## My Motivation
 ![quote the greatness of a nation can be measured by how they treat their pets](/src/readme/imgs/ghandi_quote.png) 
 ![](/data/img_dumps/dl5zpyw5k3jeb.cloudfront-1.jpg) 
*https://www.goodreads.com/quotes/340-the-greatness-of-a-nation-and-its-moral-progress-can*
-Quote by Ghandi

>I am passionate about this project because I am a disabled veteran, and 
>my dog saved my life.  
>Surely more dogs can do more, for more vetearns and more people in general, and 
>we can continue to be proud and grateful to this great nation!

## Latest Project Updates
Please find the latest updates on the project <a href="https://trello.com/b/o8vNQDDg/faster-dog-adoptions">Trello</a> board. 
