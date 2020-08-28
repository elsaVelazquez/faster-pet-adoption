
---

## FASTER PET ADOPTION
### HOW CAN A DOG SHELTER MANAGE DOGS' ONLINE PRESENCES TO GET DOGS ADOPTED OUT FASTER?

### Using a Multinomial Naive Bayes Classification System to Predict on Images and 


A Supervised Learning ML Project by Elsa Velazquez, MEd, Data Scientist, Software Engineer<br>
LinkedIn: <a href="https://www.linkedin.com/in/elsa-velazquez-020bb9175/"> https://www.linkedin.com/in/elsa-velazquez-020bb9175/ </a>



---  


>Ho:  Naive Bayes Image Classifier will have >= 90% accuracy in predicting which dogs 
are adopted.  
Ha: Naive Bayes Image Classifier will 
have < 90% accuracy in predicting which dogs are adopted.  

* ### Spoiler alert for the busy: 

* Using a random state to ensure the model results can be replicated with 25% of data as the test set, the Naive Bayes Image Classifier performed at 63.8% accuracy on image classification, and we therefore reject our null hypothesis.  
* A text description
of the dog appears to be more telling
of the dog's future than its pictures, and we
therefore reject our null hypothesies. 

*Note that the data described here only captures a specific window in time that was deeply affected by the Covid global pandemic and the reissuance of global lockdowns.*<br>
The following figure shows the time series for which this data was taken and the activity that week at dog shelters.  Due to the nature of the PetFinder API, it was not possible to legally scrape for data before this time period and the databases are such that length of stays is overwritten when the dog status changes.
>The dataset includes 527 adopted dogs and 227 adoptable dogs.
<img src="src/readme/capstone_2_readme/dog_adoption_trends_time_series.png" align=center>



<br>

## *Why a multinomial naive bayes:*
<br>
The multinomial Naive Bayes classifier is suitable for classification with discrete features (ex: pre-selected categories, word counts for text classification). 

This result is only a bit better than random chance, 
and the average colored images (shown below) show that
this problem would be a more difficult problem to classify.  Possibly, a more sophisticated ML algorithm could predict with a higher accuracy rate. The images below are a comparison of the average adopted and adoptable dog images.  


|Average Adopted Image <img src="src/readme/capstone_2_readme/average_adopted_dog.png"> | Average Adoptable Image<img src= "src/readme/capstone_2_readme/average_adoptable_dog.png "> |
|-|-|



<br>

# The following are examples of misclassified images:
## False Positive Misclassification
 Naive Bayes predicted adopted when the dog's status was adoptable (it was still avaiable):
 
|<img src ="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48550332_adopted.jpg" width=100><br>|<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48550683_adopted.jpg" width=100><br>|<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48551112_adopted.jpg" width=100><br>|<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48551249_adopted.jpg" width=100>|<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48551520_adopted.jpg" width=100> |<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48554016_adopted.jpg" width=100>|<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48554271_adopted.jpg" width=100>|<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48555413_adopted.jpg" width=100 height=30>|
|-|-|-|-|-|-|-|-|

<br>

## False Negative Misclassifications
Naive Bayes predicted adoptable though the dog was already adopted:
<br>

|<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48550728_adoptable.jpg" width=100>|<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48550922_adoptable.jpg" width=100>|<img src="src/readme/capstone_2_readme/misclassified_naive_bayes_imgs/48554156_adoptable.jpg" width=100>|
|-|-|-|




## PCA 
PCA further supports the decision to abandon a Naive Bayes Image Classification Investigation because it did not help with data analysis, classification, or visualization to simply and interpret the multiviariate data. <br>
> Ho: PCA will provide <= 4 features that will improve classification by increasing prediction accuracy. <br>
>Ha: PCA will not provide <= 4 features that will improve classification by increasing prediction accuracy.  

The following tables shows, in red, the data that would be discarded by applying PCA.
<img src="src/readme/capstone_2_readme/pca_amnt_data_discarded.png">
In the following figure, it is evident there is no gain from reducing dimensionality from 1024 features (a flattened 32*32 pixel  colored image) to 2-dimensional space because there is no clustering as a result.  The same results were found when running PCA on 2, 4, 6 and 10 principal components.  
<img src="src/readme/capstone_2_readme/pca_from_1024_to_2_dimensions.png"><br>
>*note: Column 2, i.e. the third column vector of the flattened images, had the least std deviation 
so was a likely candidate to show the most
average scenario, but otherwise random feature (i.e. column) selection did not appear to have an impact.*

<br>
 We therefore reject our null hypothesis because we did not find <= 4 features to help understand the data. 
<br>

## Logistic Regression
Logistic Regression, Two Tail
<br>
Ho: The slope will be zero.  
Ha: The slope will be < zero <. 

Logistic Regression also shows that there 
is not a best fitting line that could answer 
the classification question using image data. 
This scikit learn module is ideal 
because the labels (adopted=1, adoptable=0)
are discrete.
It appears the data shows all the dogs will be adopted. 
<br>
>The original data is compared side by side with the Logistic Regression of the image data. 

|<img src="src/readme/capstone_2_readme/dog_adoption_status_initial_data_viz.png">|<img src="src/readme/capstone_2_readme/logistic_regression_dog_img_data.png">|
|-|-|


<br>

# Why not an SVM
A preliminary quest to use a random forest model, applied with cross validation and 5 folds, showed to also do no better than random chance. 
<img src="src/readme/capstone_2_readme/ROC_why_NOT_using_SVM.png">

 
# VIF
Due to the continued dead ends in understanding the dog's online presence using image classification, the direction of the investigation lead to a text analysis and VIF was used to determine which features to keep, as they did not have strong multicollinearity.  It was determined that the strongest predictive factor was the manually input description.  <br>
<img src="src/readme/capstone_2_readme/VIF_multicollinearity.png">

<br>

# Text Analysis to Predict Dog's Adopted Status

## Bag of Words Cosine DIstance and TF-IDF
When text was analyzed using Naive Bayes on manually input dog descriptions, the prediction performance improved significantly, but we were still not able to fail to reject our null hypothesis.
>Ho: Naive Bayes Text Classification will predict adoption status of adopted with >= 90% accuracy. <br>
>Ha: Naive Bayes Text Classification will predict adoption status of adopted with < 90% accuracy. 
<br>

We reject the null hypothesis because Naive Bayes text analysis on dog descriptions had an accuracy rate of 70% despite rates of test and training data splits. 


Using TF-IDF and cosine distances failed to provide insight into which words made the dog's adoption status predictable.  The words "playful" and "heartworm" appeared in Word Clouds but did not have an impact when investigated further.  

|Word Cloud of Adopted Dog Descriptions <img src ="src/readme/capstone_2_readme/word_cloud_adopted.png">|Word Cloud of Adoptable Dog Descriptions <img src="src/readme/capstone_2_readme/word_cloud_adoptable.png">|
|-|-|

<br>

## Comparisons of Cosine Distances
There were no differences in cosine distances with any combinations of including and not including the words "playful" or "heartworm."
<br>

Adoptable :<br>
>* Stemming and Lemmitization:<br>
people	peopl	peopl	people<br>
prepare	prepar	prepar	prepare<br>
>* COSINE DISTANCE same for both:  0.922<br>

<br>
Adopted:<br>

>* Stemming and Lemmitization:<br>
probably	probabl	probabl	probably<br>
lbs	lb	lbs	lb<br>
complete	complet	complet	complete<br>
>* COSINE DISTANCE same for both:  0.953<br>

<br>
Entire dataset with and without "playful":<br>

>* Stemming and Lemmitization:<br>
probably	probabl	probabl	probably<br>
lbs	lb	lbs	lb<br>
complete	complet	complet	complete<br>
>* COSINE DISTANCE same for both:  0.954
<br>
<br>
## Comparison of Words in Entire Dataset Vs. Adopted Vs. Adoptable
The following images show the top description words used, collectively, for adopted dogs, and for adoptable dogs.  Note that the word 'None' is a placeholder in the adoptable dogs' descriptions that was left blank in the dog's description.   
<br>
### Word Counts of Dog Descriptions 
Top 25 Words Less Stopwords
|<img src="src/readme/capstone_2_readme/word_counts_entire_dataset.png" >|<img src="src/readme/capstone_2_readme/word_counts_adopted.png" >|<img src="src/readme/capstone_2_readme/word_counts_adoptable.png">|
|-|-|-|
<br>

## NEXT STEPS
## Image Classification as a Predictor of Dog Adoption Status
A CNN will be employed to determine if there is signal to capture. 
## Text As a Predictor of Dog Status
Text analysies will be used to determine if leaving the description blank has a correlation to adoptable status, or if there is a general sentiment that is visible in the adopted dogs' descriptions.





## DATA PIPELINE
The data was acquired using an automated script that ran a curl command to scrape the API using an authentication key (<a href="src/pipelines/data_ingestion/cron/get_api_token.py">get_api_token.py</a>).  Only 1K API calls are allowed per 24 hour period, with a download limit of 50K.  This lead to only being able to access 1K records per ID per day (<a href="src/pipelines/data_ingestion/cron/scrape_by_animal_id.py">scrape_by_animal_id.py</a>).
<br>
From there data was further skimmed down to only include dog data ( <a href="src/pipelines/cleaning/delete_invalid_json_files.py"> delete_invalid_json_files.py</a>). The data were cleaned through string manipulation, as dataframes, and pushed into CSV format for ease of use (<a href="https://raw.githubusercontent.com/elsaVelazquez/faster-pet-adoption/master/data/csv/giant_valid_csv.csv">raw json</a>).  A <a href="test/unit_tests/test_strings_are_lowercase.py">unit test </a>was used to determine if the corpuses for IF-IDF was correctly processing in all lowercase.  <br>
The images were acquired using an automated Beautiful Soup 4 Script.
<br>
The majority of the automated pipeline can be seen in <a href="src/main.py">main.py</a>.
<br>



## Sidenotes regarding this project

* The code is not PEP8 compliant, but it *is* readable by the author, whom is dyslexic and with other visual and cognitive impairments. 
*  All animal species in shelters were represented by the API call JSON responses, 
including cats and mares, but the focus for this project
is on dogs. 
* This is the first pandemic in known history where dogs are not scapegoated as carriers, thanks to advances in science, so are subsequently in high demand. 
* In other countries, people have started renting out their dogs as companions during the Covid pandemic.  
* India has declared the feeding of street dogs, who lost food sources when restaurants and street vendors shut down, an essential service.



---



For a deeper explanation of Naive Bayes Multinomial, please visit <a href="https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Multinomial_na%C3%AFve_Bayes">https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Multinomial_na%C3%AFve_Bayes</a>
<img src="src/readme/capstone_2_readme/Screen Shot 2020-08-28 at 1.49.39 AM.png" align=center>

---
FASTER PET ADOPTION<br>
by Elsa Velazquez, MEd<br>
Data Scientist, Software Engineer<br>
August 28, 2020<br>
LinkedIn: <a href="https://www.linkedin.com/in/elsa-velazquez-020bb9175/"> https://www.linkedin.com/in/elsa-velazquez-020bb9175/ </a>

---