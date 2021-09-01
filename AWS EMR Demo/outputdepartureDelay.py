from pyspark.sql import SparkSession        
spark = (SparkSession
  .builder
  .appName("SparkExample")
  .getOrCreate())
  
spark.sparkContext.setLogLevel('ERROR')

csv_file = "S3 URI of the file"

df = (spark.read.format("csv")
  .option("inferSchema", "true")
  .option("header", "true")
  .load(csv_file))
  
df.show(10)

df.createOrReplaceTempView("us_delay_flights_tbl")

spark.sql("""SELECT delay, origin, destination, 
              CASE
                  WHEN delay > 360 THEN 'Very Long Delays'
                  WHEN delay >= 120 AND delay <= 360 THEN 'Long Delays'
                  WHEN delay >= 60 AND delay < 120 THEN 'Short Delays'
                  WHEN delay > 0 and delay < 60 THEN 'Tolerable Delays'
                  WHEN delay = 0 THEN 'No Delays'
                  ELSE 'Early'
               END AS Flight_Delays
               FROM us_delay_flights_tbl
               ORDER BY origin, delay DESC""").show(10)


df2 = spark.sql("""SELECT delay, origin, destination, 
              CASE
                  WHEN delay > 360 THEN 'Very Long Delays'
                  WHEN delay >= 120 AND delay <= 360 THEN 'Long Delays'
                  WHEN delay >= 60 AND delay < 120 THEN 'Short Delays'
                  WHEN delay > 0 and delay < 60 THEN 'Tolerable Delays'
                  WHEN delay = 0 THEN 'No Delays'
                  ELSE 'Early'
               END AS Flight_Delays
               FROM us_delay_flights_tbl
               ORDER BY origin, delay DESC""")
               

df2.coalesce(1).write.mode("overwrite").csv("s3://rnr-spark-demo/output")