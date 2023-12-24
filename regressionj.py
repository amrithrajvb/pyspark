
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
spark=SparkSession.builder.appName("practice").getOrCreate()
df=spark.read.csv('test.csv',header=True,inferSchema=True)
df.show()

featues=VectorAssembler(inputCols=['age','experience'],outputCol='independent_feature')


new=featues.transform(df)
print(new.show())
datas=new.select("salary",'independent_feature')
datas.show()

train_data,test_data=datas.randomSplit([0.75,0.25])
lg=LinearRegression(featuresCol="independent_feature",labelCol="salary")
regression=lg.fit(train_data)
pp=regression.coefficients
print(pp)
pp=regression.intercept
print(pp)
# prediction
pp=regression.evaluate(test_data)
pp.predictions.show()
