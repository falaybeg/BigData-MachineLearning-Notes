'''
RDD Wordcount Sample

RDD is a component which enables us to make computation on data.
It is a old Spark 1.0 API.
'''

# import Pyspark libraries 
import findspark 
findspark.init()
from pyspark.sql import SparkSession 
from pyspark.conf import SparkConf 

# Here is defined Spark begining point
spark = SparkSession.builder.master("local[4]")\
.appName("Wordcount_Rdd")\
.getOrCreate()

# Here is defined SparkContext which uses for accessing to cluster
sc = spark.sparkContext

data = sc.textFile("HanselStory.txt")
# row number is counted from story text
print("Story Row Number: ",data.count())
# 5 row is taken from story text file
print("\n-- Take first 5 row ---\n",data.take(5))

words = data.flatMap(lambda row: row.split(" "))
print("\n\n--- Splitted Words ---\n",     words.take(10))

words_number = words.map(lambda word: (word,1))
print(words_number.take(5))

words = data.flatMap(lambda row: row.split(" "))
print("\n--- Splitted Words ---\n",     words.take(10))

words_number = words.map(lambda word: (word,1))
print("\n--- Word Count (key,value) ---\n",words_number.take(5))

words_number_RBW = words_number.reduceByKey(lambda key,count: key+count)
print("\n--- Word Total Count (key,value) ---\n",words_number_RBW.take(10))

words_number_RBW2 = words_number_RBW.map(lambda key: (key[1], key[0]))
words_number_RBW2.take(5)
print("\n--- Sorted Words ---\n",words_number_RBW2.sortByKey(False).take(20))