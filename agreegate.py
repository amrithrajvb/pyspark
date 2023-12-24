from pyspark.sql import SparkSession

from pyspark.ml.feature import VectorAssembler
spark=SparkSession.builder.appName("practice").getOrCreate()
df=spark.read.csv('test.csv',header=True,inferSchema=True)
df.show()

df.groupBy("name").sum().show()


# //algorithms?

print(df.columns)

featues=VectorAssembler(inputCols=['age','experience'],outputCol='independent_feature')
new=featues.transform(df)
print(new.show())
new.select("salary",'independent_feature').show()



