Workflow:
Data Ingestion
had to figure out how to get out the data i wanted using their whack API
    ended up making a Python Flask version of a  cron job

Clean the Data
    Data Structures Conversions-- turned all the JSON into csv with a python function


EDA
compare ratio of male and female dogs in shelters to ratios of adopted genders

compare by age groups


do a time series to see if there is any truth to covid driven adoption spikes- trends and seasons?
Can I predict when more dogs will be adopted?
When more will go to shelters?





find 1-3 features to really look into now that I have the data on adopted dogs

Regression - Lasso and Elastic Net-- predicting a quantity of dogs

Clustering-- because number of categories is known, < 10K samples so can use KMeans (could have also bootstrapped)