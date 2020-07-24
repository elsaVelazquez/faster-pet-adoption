# from get_file_names import getListOfFiles

# #get all the files
#     # Get the list of all files in directory tree at given path
# listOfFiles = getListOfFiles(dirName)




#start up spark
import pyspark as ps    # for the pyspark suite
from pyspark.sql.types import *
from datetime import datetime
import json

spark = ps.sql.SparkSession.builder \
            .master("local[4]") \
            .appName("sparkSQL exercise") \
            .getOrCreate()

sc = spark.sparkContext 



#handle exceptions in columns
def apply_json(input_lst):
    try:
        return json.loads(input_lst)['animals'][0]                                                  'id']
    except:
        return None 


#read in JSON from files
data_filepath = '../data/json/api_dump_2020-06.json'

data = sc.textFile(data_filepath).map(apply_json) #reads in the json file



df = spark.read.json(data_filepath, multiLine = True)


df.count()


df.printSchema()



df_new = df.select('id', 'age', 'gender', 'primary_photo_cropped', 'status', 'status_changed_at', 'description')


dropped_df = df_new.na.drop()


dropped_df.show()


dropped_df.printSchema()


dropped_df.createOrReplaceTempView("dog_data")


result = spark.sql('''SELECT gender,   
                        COUNT(*) AS Number
                        FROM dog_data
                        GROUP BY gender
                        ORDER BY COUNT(*) desc''')
result.show(20)


result.head()


plot_gender = result.toPandas()
plot_gender['gender']
plot_gender.dropna(inplace=True)



import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, figsize=(10,3))
ax.bar(x = plot_gender['gender'], height=plot_gender['Number'])
ax.set_title("Count of Dogs by Gender")

ax.set_xlabel('Gender')
ax.set_ylabel('Number of Dogs')
plt.tight_layout()
plt.show()




