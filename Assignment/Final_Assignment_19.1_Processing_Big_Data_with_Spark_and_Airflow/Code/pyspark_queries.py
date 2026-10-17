from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Assignment19.3") \
    .getOrCreate()

assignment19_3_data = "/departuredelays.csv"

df = spark.read.format("csv") \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .load(assignment19_3_data)

df.createOrReplaceTempView("assignment19_3_table")

# Query 1
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE delay > 150
  AND origin = 'PHL'
  AND destination = 'DFW'
""").show(15)

# Query 2
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE distance < 200
""").show(10)

# Query 3
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE distance > 600
""").show(10)