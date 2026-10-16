# Required Coding Activity 19.2: Loading Data into a Spark Docker Container

## Module 19: Processing Big Data with Spark and Airflow

---

# Activity Information

| Item | Details |
|--------|--------|
| Activity | Required Coding Activity 19.2 |
| Title | Loading Data into a Spark Docker Container |
| Points | 20 |
| Due Date | October 22, 2026 |
| Submission Type | Word Document (.docx) |
| Estimated Time | 45 Minutes |
| Learning Outcome | Use Docker to create and manipulate Spark images and containers |

---

# Objective

The purpose of this activity is to:

- Load data into a Spark Docker container
- Create a SparkSession
- Load CSV data into a Spark DataFrame
- Execute SQL queries using Spark SQL
- Analyze flight departure delays

By the end of this activity, a Spark environment will be configured, data will be loaded into Spark, and multiple analytical queries will be executed successfully.

---

# Technologies Used

- Apache Spark 3.5.1
- PySpark
- Docker
- Docker Desktop
- Spark SQL
- CSV Data Source

---

# Dataset

Dataset Used:

```text
departuredelays.csv
```

Location:

```text
Coding_Activity_19.2_Loading_Data_Into_Spark\data
```

File Size:

```text
33.4 MB
```

---

# Step 1: Create Data Folder and Download Dataset

## Objective

Create a directory to store the flight delay dataset and download the CSV file.

## Actions

Created:

```text
data
```

Downloaded:

```text
departuredelays.csv
```

Directory Structure:

```text
Coding_Activity_19.2_Loading_Data_Into_Spark
│
└── data
    └── departuredelays.csv
```

### Screenshot

```text
Step01_Data_Folder_And_DepartureDelays_File.png
```

### Result

Successfully created the data folder and downloaded the dataset.

---

# Step 2: Verify Spark Containers Are Running

## Objective

Confirm that the Spark Docker environment from Activity 19.1 is operational.

## Verification

Docker Desktop displayed:

```text
bitnami_spark_1
Running
```

```text
bitnami_spark-worker-1
Running
```

### Screenshot

```text
Step02_Spark_Containers_Running.png
```

### Result

Both Spark containers were running successfully.

---

# Step 3: Copy CSV File into Spark Container

## Objective

Transfer the dataset from the local computer into the Spark container.

## Command Executed

```bash
docker cp departuredelays.csv bitnami_spark_1:/departuredelays.csv
```

## Result

```text
Successfully copied 33.4MB
```

### Screenshot

```text
Step03_Copy_CSV_To_Spark_Container.png
```

### Outcome

The CSV file was copied successfully into the Spark container.

---

# Step 4: Verify File Exists in Container

## Objective

Confirm that the dataset exists inside the Spark container.

## Commands Executed

```bash
docker exec -it bitnami_spark_1 bash
```

```bash
ls /
```

## Verification

File found:

```text
departuredelays.csv
```

### Screenshot

```text
Step04_Verify_CSV_In_Container.png
```

### Outcome

Verified that the file was successfully copied into the container root folder.

---

# Step 5: Start PySpark

## Objective

Launch the PySpark interactive environment.

## Command Executed

```bash
/opt/spark/bin/pyspark
```

## Verification

Output:

```text
SparkSession available as 'spark'
```

### Screenshot

```text
Step05_Start_PySpark.png
```

### Outcome

PySpark launched successfully.

---

# Step 6: Create Spark Session

## Objective

Create a SparkSession for data processing.

## Commands Executed

```python
from pyspark.sql import SparkSession
```

```python
spark = SparkSession.builder.appName("DepartureDelays").getOrCreate()
```

## Verification

Output:

```text
Using an existing Spark session
```

### Screenshot

```text
Step06_Create_Spark_Session.png
```

### Outcome

SparkSession initialized successfully.

---

# Step 7: Load CSV into DataFrame

## Objective

Load flight delay data into a Spark DataFrame.

## Commands Executed

```python
csv_file = "/departuredelays.csv"

df = spark.read.format("csv") \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .load(csv_file)

df.createOrReplaceTempView("delays_table")
```

### Screenshot

```text
Step07_Load_CSV_Into_DataFrame.png
```

### Outcome

Successfully loaded the dataset and created the temporary SQL view:

```text
delays_table
```

---

# Step 8: Flights Over 1,000 Miles

## Objective

Retrieve flights with distances greater than 1,000 miles.

## Query Executed

```sql
SELECT
    distance,
    origin,
    destination
FROM delays_table
WHERE distance > 1000
ORDER BY distance DESC
```

## Sample Results

```text
distance origin destination
4330     HNL    JFK
```

### Screenshot

```text
Step08_Query_Distance_Greater_Than_1000.png
```

### Outcome

Displayed distance, origin, and destination for flights over 1,000 miles.

---

# Step 9: SFO to ORD Delays Greater Than 120 Minutes

## Objective

Identify significantly delayed flights from SFO to ORD.

## Query Executed

```sql
SELECT *
FROM delays_table
WHERE delay > 120
  AND origin = 'SFO'
  AND destination = 'ORD'
ORDER BY delay DESC
```

## Sample Results

```text
delay = 1638
delay = 396
delay = 326
```

### Screenshot

```text
Step09_Query_SFO_ORD_Delays.png
```

### Outcome

Successfully retrieved flights with delays greater than 120 minutes.

---

# Step 10: Categorize Delays

## Objective

Classify flights based on delay duration.

## Query Executed

```sql
SELECT
    delay,
    origin,
    destination,
    CASE
        WHEN delay > 360 THEN 'Very Long Delays'
        WHEN delay BETWEEN 120 AND 360 THEN 'Long Delays'
        WHEN delay BETWEEN 60 AND 120 THEN 'Short Delays'
        WHEN delay BETWEEN 0 AND 60 THEN 'Tolerable Delays'
        WHEN delay = 0 THEN 'No Delays'
        ELSE 'Early'
    END AS delay_length
FROM delays_table
```

## Categories

| Delay Range | Category |
|------------|------------|
| > 360 | Very Long Delays |
| 120 - 360 | Long Delays |
| 60 - 120 | Short Delays |
| 0 - 60 | Tolerable Delays |
| 0 | No Delays |
| < 0 | Early |

### Screenshot

```text
Step10_Categorize_Delay_Lengths.png
```

### Outcome

Successfully categorized flight delays.

---

# Step 11: Determine Maximum Delay

## Objective

Find the largest delay in the dataset.

## Query Executed

```sql
SELECT MAX(delay) AS max_delay
FROM delays_table
```

## Result

```text
1642
```

### Screenshot

```text
Step11_Maximum_Delay_Query.png
```

### Outcome

Maximum delay identified:

```text
1642 minutes
```

---

# Step 12: Determine Minimum Delay

## Objective

Find the smallest delay in the dataset.

## Query Executed

```sql
SELECT MIN(delay) AS min_delay
FROM delays_table
```

## Result

```text
-112
```

### Screenshot

```text
Step12_Minimum_Delay_Query.png
```

### Outcome

Minimum delay identified:

```text
-112 minutes
```

---

# Final Results Summary

| Metric | Value |
|----------|----------|
| Maximum Delay | 1642 Minutes |
| Minimum Delay | -112 Minutes |
| Spark Version | 3.5.1 |
| Dataset | departuredelays.csv |
| Data Loaded Successfully | Yes |
| SQL Queries Executed Successfully | Yes |

---

# What I Learned

Through this activity I learned how to:

- Use Docker to manage Spark containers
- Copy data into a Spark container
- Start PySpark
- Create SparkSessions
- Load CSV files into DataFrames
- Create temporary SQL views
- Query data using Spark SQL
- Categorize data using SQL CASE statements
- Calculate aggregate metrics such as MAX and MIN

---

# Conclusion

The flight delay dataset was successfully loaded into the Spark Docker container and processed using PySpark. Spark SQL queries were executed to analyze flight distances, delayed flights, delay categories, and summary statistics. This activity demonstrated how PySpark combines Python and SQL to analyze large datasets efficiently within a distributed computing framework.

---

# Submission Checklist

- [x] Step 01 – Data Folder and CSV Downloaded
- [x] Step 02 – Spark Containers Running
- [x] Step 03 – CSV Copied to Container
- [x] Step 04 – CSV Verified in Container
- [x] Step 05 – PySpark Started
- [x] Step 06 – Spark Session Created
- [x] Step 07 – DataFrame Loaded
- [x] Step 08 – Distance Query Executed
- [x] Step 09 – SFO to ORD Delay Query Executed
- [x] Step 10 – Delay Categories Created
- [x] Step 11 – Maximum Delay Calculated
- [x] Step 12 – Minimum Delay Calculated

✅ Activity Completed Successfully