import pyspark as ps    # for the pyspark suite
import json             # for parsing json formatted data
from datetime import datetime
import csv              # for the split_csvstring function from Part 3.2.2
try:                    # Python 3 compatibility
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import os               # for accessing env variables for AWS credentials


import matplotlib
import matplotlib.pyplot as plt
    
    
def explore_data(df):
    # df.count()
    # df.show()
    # df.printSchema()

def is_female(val):
    if val == 'Female':
    return 1
else:
    return 0


def is_male(val):
    if val == 'Male':
        return 1
    else:
        return 0
        
if __name__ == "__main__":
    from pyspark import SparkContext
    sc =SparkContext()
    lst_rdd = sc.parallelize([1, 2, 3])

    file_rdd = sc.textFile('data/cookie_data.txt')
    
    spark = ps.sql.SparkSession.builder \
                .master("local[4]") \
                .appName("sparkSQL exercise") \
                .getOrCreate()

    sc = spark.sparkContext 
    sc.setLogLevel('ERROR')
    
    #data is not yet in an s3 bucket because we do not have access
    # link = ##
    #handle exceptions in columns
    def apply_json(input_lst):
        try:
            return json.loads(input_lst)['animals'][0]
        except:
            return None 

    data_filepath = '../src/big_json.json'
    data = sc.textFile(data_filepath).map(apply_json) #reads in the json file
    print(data)

    df = spark.read.json(data_filepath, multiLine = True)
    
    explore_data(df)

    df_age_gender = df.select('age', 'gender')
    
    df_clean_age_gender = df_age_gender.na.drop()
    
    df_clean_age_gender.createOrReplaceTempView("age_gender_data")
    
    #how to put it in spark context here?
    result = spark.sql('''SELECT gender, 
    COUNT(*) AS Count
                            FROM age_gender_data
                            GROUP BY gender
                            ORDER BY COUNT(*) desc''')
    
    total_dogs = 62378 + 37622
    
    plot_age_gender = result.toPandas()
    plot_age_gender['gender']
    plot_age_gender.dropna(inplace=True)
    
    df = df_clean_age_gender.toPandas()
    
    df['Female']=df['gender'].apply(is_female)  #apply function to column
    df['Male']=df['gender'].apply(is_male)
    
    df['Female']=df['gender'].apply(is_female)  #apply function to column
    df['Male']=df['gender'].apply(is_male)
    
    a = df['Female'].values
    b = df['Male'].values
    

    plt.style.use('ggplot')
    matplotlib.rc('xtick', labelsize=12) 
    matplotlib.rc('ytick', labelsize=12)
    plt.close('all')
    fig, ax = plt.subplots(1, figsize=(10,3))
    ax.bar(x = plot_age_gender['gender'], height=plot_age_gender['Count'], color=['pink', 'blue'])
    ax.set_title("Raw Count of All Male Vs. Female Dogs In Shelters", fontsize=18)

    ax.set_xlabel('Gender', fontsize=16)
    ax.set_ylabel('Number of Dogs', fontsize=16)
    plt.tight_layout()
    plt.show();
    plt.savefig('../src/readme/raw_counts');
    

    plt.style.use('ggplot')
    binomial = stats.binom(n=len(a), p=0.5)
    matplotlib.rc('xtick', labelsize=16) 
    matplotlib.rc('ytick', labelsize=16)
    plt.close('all')


    fig, ax = plt.subplots(1, figsize=(16, 6))
    # _ = ax.set(xlabel='Total Dogs In U.S. Shelters Registered On PetFinder.com', ylabel='Probabilities of Dogs Being Female');
    ax.axvline(x=50000, ymin=0.0, ymax=1, color="red", linestyle='--', alpha=0.5)
    ax.axvline(x=62378, ymin=0.0, ymax=1, color="purple", linestyle='--', alpha=0.5)


    ax.text(42500, 0.0023, r"This $\bar{x}$ would have shown ", fontsize=16, color='r')
    ax.text(42500, 0.0021, r"failure to reject the ${H_o}$.", fontsize=16, color='r')

    ax.text(57250, 0.0013, r"The actual $\bar{x}$ shows", fontsize=16, color='purple')
    ax.text(57250, 0.0011, r"we reject the ${H_o}$.", fontsize=16, color='purple')

    fem_arr= range(len(a))
    _ = ax.plot(fem_arr, [binomial.pmf(i) for i in fem_arr], color="black")
    ax.set_xlim([35000,65000]);

    ax.set_xlabel('Total Dogs In U.S. Shelters Registered On PetFinder.com', fontsize=18)
    ax.set_ylabel('Probabilities of Dogs Being Female', fontsize=18)
    ax.set_title("Evidence For Failure to Reject the Null Hypothesis For the General Dog Population", fontsize=20)

    plt.tight_layout()
    plt.show();
    plt.savefig('../src/readme/reject_null_hyp');