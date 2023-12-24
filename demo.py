import pyspark
import os
import findspark
findspark.init()
import pandas as pd
from pyspark.sql import SQLContext, SparkSession
from pyspark.sql.functions import lit, when
# os.environ['PYSPARK_SUBMIT_ARGS'] =PYSPARK_SUBMIT_ARGS="--master local[2] pyspark-shell"
# dd=pd.read_csv('test.csv')
# print(dd)

# spark = (
#     SparkSession.builder
#         .getOrCreate()
# )
# print(spark)

import os

# file_path = 'C:\\path\\to\\your\\file.txt'
#
# if os.path.exists(file_path):
#     # Proceed to open and work with the file
#     with open(file_path, 'r') as file:
#          # Your file operations here
# else:
#     print("The file '{file_path}' does not exist.")

# /spark session
spark=SparkSession.builder.appName("NewApp").getOrCreate()
print(spark.sparkContext.appName)

# read data from file
df=spark.read.csv('test.csv',header=True,inferSchema=True)

# structure
df.printSchema()
df.show()

# adding column
df.withColumn('salary',lit(3500)).show()
# condition based column
df.withColumn("grade", \
   when((df.salary < 4000), lit("A")) \
     .when((df.salary >= 4000) & (df.salary <= 5000), lit("B")) \
     .otherwise(lit("C")) \
  ).show()

# creating table
df.createOrReplaceTempView("emp")
spark.sql("select name from emp").show()
print(type(df))

print("---------------------------")
#
# # first 3 row of record
# mm=df.head(3)
# print(mm)
#
# # show columns
#
# cc=df.columns
# print(cc)
#
# # select particular columns
#
# df.select("name","age").show()
#
# # renaming
# df.withColumnRenamed("name","Name").show()
# # drop column
# df.drop("name").show()
# df.show()
# # drop null value column
# df.na.drop().show()
# # //set up how =all row having null value any=anyofthem
#
# df.na.drop(how="any").show()
#  # threshold-atleaset 2 non null values should be there
# df.na.drop(how="any",thresh=2).show()
#
# # need to delete particular column null value will delete entire row of records
#
# df.na.drop(how="any",subset=['age']).show()

# /fill will missing value
# df.na.fill('missing').show()
# print("---------------------")
# filter function
df.filter("salary<=2000").show()

df.filter("salary>=2000").select(['name','age']).show()


