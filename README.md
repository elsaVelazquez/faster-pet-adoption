# Dogs In Shelters

|Are there *really* more male dogs in animal rescue shelters than female dogs?|<img src="https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/imgs/Screen%20Shot%202020-07-16%20at%202.47.09%20AM.png" width=300 align=right>|
|-|-|

## Data science application: Hypothesis Testing--> 
### Ho : There are 50% male dogs in shelters.  
### Ha : It is not the case that there are 50% male dogs in shelters.  

### Statistic:  A normal distribution, 2-tail test using <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html">scipy.stats.ttest_ind</a>

We see that there are, by the numbers, more male than female dogs, but our goal is to ascertain whethere there is a statistically significant difference in male vs female dog populations in animal rescue shelters. 
![raw counts of male vs female dogs](src/readme/raw_counts.png)


#### Conclusion:
If p < alpha, we fail to reject the null hypothesis and determine there are not 50% male dogs in shelters, and our sample does not come from a noraml distribution.  




## Web Scraping for Data Collection
The data was collected using OS-level Curl command line prompts, written in python, that sped up the collection of 200,000 records from PetFinder's public API to less than 1 minute.




## Data Pipeline for EDA
The scraped data was gathered in JSON form, with nested layers of dictionaries.  The data of interest was the 4th layer in. To be more manageable with PySpark, the 5,000 JSON files with 20 records each went through the following flow:





### Data Visualization
The following plots were generated using OOP for plotting. 




<img src = "https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/imgs/Screen%20Shot%202020-07-16%20at%202.47.09%20AM.png" width=600 align=right>

It is also evident in our JSON files that we are able to determine an animal's length of stay.

The length of stay is the key feature in this analysis, barring potential bias given the age of the animal.  The suspected age of the animal is also a included in the data set.  It is accounted for by grouping using age categories, as deemed necessary.  

We can use the IDs given by PetFinder as unique identifiers in the data set to track the animals.  As is seen in this JSON file, the URL is associated with said pet ID. 


# Data Access
The data is gathered using a curl command in the command terminal, using an API issued by PetFinders.

<img src="https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/imgs/Screen%20Shot%202020-07-16%20at%204.41.03%20AM.png" width=600 align=center>



## Next steps --> IMG Classification Using ML <a href="https://scikit-learn.org/stable/datasets/index.html>Scikit-Learn</a>
  
#### The next question:  Is an animal's online presence a predictor of its adoptability? 

Does the pose of a dog influence how fast it gets adopted from a rescue shelter?

By classifying animal shelter data using image processing and tracing an animal's dates of arrival and departure from a shelter, it can be decided if we should fail to reject the null hypothesis and determine that pets are too adorable to be left, no matter how they pose for the cameera.  
In the following image, it is clear to see the image classification categories, as pets are either:
- ![#9900c5](https://placehold.it/15/9900c5?text=+)Standing
- ![#9900c5](https://placehold.it/15/9900c5?text=+)Sitting
- ![#9900c5](https://placehold.it/15/9900c5?text=+)Laying
- ![#9900c5](https://placehold.it/15/9900c5?text=+)Clothed

## My Motivation
| ![Ghandi Image](src/readme/imgs/5810891.jpg)Ghandi | ![quote the greatness of a nation can be measured by how they treat their pets](/src/readme/imgs/Screen%20Shot%202020-07-16%20at%203.51.18%20AM.png) | <img src="https://github.com/elsaVelazquez/faster-pet-adoption/blob/master/src/readme/imgs/dl5zpyw5k3jeb.cloudfront-1.jpg" width=600 align=center> |
*https://www.goodreads.com/quotes/340-the-greatness-of-a-nation-and-its-moral-progress-can*

|-|-|-|
>I am passionate about this project because I am a disabled veteran, and 
>my dog saved my life.  
>Surely more dogs can do more, for more vetearns and more people in general, and 
>we can continue to be proud and grateful to this great nation!

## Latest Project Updates
Please find the latest updates on the project <a href="https://trello.com/b/o8vNQDDg/faster-dog-adoptions">Trello</a> board. 
