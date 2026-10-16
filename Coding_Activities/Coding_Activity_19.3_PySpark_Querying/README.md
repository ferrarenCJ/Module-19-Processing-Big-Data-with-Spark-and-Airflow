# Required Coding Activity 19.3: Using PySpark to Query Data

## Module 19: Processing Big Data with Spark and Airflow

---

# Activity Information

| Item | Details |
|--------|--------|
| Activity | Required Coding Activity 19.3 |
| Title | Using PySpark to Query Data |
| Points | 20 |
| Due Date | October 22, 2026 |
| Submission Type | Word Document (.docx) |
| Estimated Completion Time | 60 Minutes |
| Learning Outcome | Use PySpark to query data |

---

# Objective

The purpose of this activity is to use PySpark and Spark SQL to analyze flight delay data loaded into a Spark Docker container.

By the end of this activity, I successfully:

- Accessed the Spark Docker environment
- Started PySpark
- Created a SparkSession
- Loaded flight delay data into a DataFrame
- Created a temporary SQL view
- Queried flight data using Spark SQL
- Retrieved subsets of flight records based on delay criteria

---

# Technologies Used

- Apache Spark 3.5.1
- PySpark
- Spark SQL
- Docker
- Docker Desktop
- Python
- CSV Data Source

---

# Dataset

## Dataset Name

```text
departuredelays.csv
```

## Source

Flight departure delay dataset used throughout Module 19.

## Location

```text
/departuredelays.csv
```

inside the Spark container.

---

# Step 1: Verify Spark Containers Are Running

## Objective

Confirm that the Spark Docker environment is operational.

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

Both the Spark Master and Worker containers were running successfully.

### Screenshot

```text
Step01_Spark_Containers_Running.png
```

### Result

The Spark Docker environment was available and ready for use.

---

# Step 2: Verify Flight Dataset Exists

## Objective

Confirm that the flight delay dataset is available inside the Spark container.

## Commands Executed

```bash
docker exec -it bitnami_spark_1 bash
```

```bash
ls /
```

## Verification

The root directory contained:

```text
departuredelays.csv
```

### Screenshot

```text
Step02_Verify_CSV_In_Root_Folder.png
```

### Result

Verified that the flight dataset exists in the Spark container.

---

# Step 3: Open PySpark

## Objective

Launch the PySpark interactive shell.

## Command Executed

```bash
/opt/spark/bin/pyspark
```

## Verification

Output included:

```text
SparkSession available as 'spark'
```

and

```text
Spark context available as 'sc'
```

### Screenshot

```text
Step03_Open_PySpark.png
```

### Result

PySpark started successfully.

---

# Step 4: Import SparkSession

## Objective

Import the SparkSession package.

## Command Executed

```python
from pyspark.sql import SparkSession
```

### Screenshot

```text
Step04_Import_SparkSession.png
```

### Result

SparkSession imported successfully.

---

# Step 5: Create Spark Session

## Objective

Create a SparkSession using the application name required by the activity.

## Command Executed

```python
spark = SparkSession.builder.appName("Activity19.3").getOrCreate()
```

## Verification

Spark responded:

```text
Using an existing Spark session
```

which is expected when PySpark has already created a session.

### Screenshot

```text
Step05_Create_Activity19_3_Session.png
```

### Result

SparkSession successfully created.

---

# Step 6: Define Data Path Variable

## Objective

Store the dataset location in a Python variable.

## Command Executed

```python
activity19_3_data = "/departuredelays.csv"
```

### Screenshot

```text
Step06_Define_Activity19_3_Data_Variable.png
```

### Result

The dataset path was stored in the variable:

```python
activity19_3_data
```

---

# Step 7: Create DataFrame

## Objective

Load the dataset into a Spark DataFrame.

## Command Executed

```python
df = spark.read.format("csv") \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .load(activity19_3_data)
```

## Configuration

### Header Row

```python
.option("header", "true")
```

Treats the first row as column names.

### Schema Inference

```python
.option("inferSchema", "true")
```

Automatically determines column data types.

### Screenshot

```text
Step07_Create_DataFrame.png
```

### Result

Successfully loaded the dataset into a DataFrame named:

```python
df
```

---

# Step 8: Create Temporary View

## Objective

Create a temporary SQL view from the DataFrame.

## Command Executed

```python
df.createOrReplaceTempView("activity19_3_table")
```

### Screenshot

```text
Step08_Create_Temp_View.png
```

### Result

Created a temporary SQL view named:

```text
activity19_3_table
```

which can be queried using Spark SQL.

---

# Step 9: Retrieve JFK to SEA Flights Delayed More Than 90 Minutes

## Objective

Display the first 10 flights from:

```text
Origin      = JFK
Destination = SEA
Delay        > 90 Minutes
```

## Query Executed

```sql
SELECT *
FROM activity19_3_table
WHERE delay > 90
  AND origin = 'JFK'
  AND destination = 'SEA'
```

## Spark SQL Command

```python
spark.sql("""
SELECT *
FROM activity19_3_table
WHERE delay > 90
  AND origin = 'JFK'
  AND destination = 'SEA'
""").show(10)
```

## Sample Results

```text
delay = 193
delay = 97
delay = 100
delay = 220
delay = 579
delay = 370
```

### Screenshot

```text
Step09_JFK_To_SEA_Delays_Greater_Than_90.png
```

### Result

Successfully displayed the first 10 JFK-to-SEA flights delayed more than 90 minutes.

---

# Step 10: Retrieve SFO to MIA Flights Delayed Less Than 60 Minutes

## Objective

Display the first 5 flights from:

```text
Origin      = SFO
Destination = MIA
Delay       < 60 Minutes
```

## Query Executed

```sql
SELECT *
FROM activity19_3_table
WHERE delay < 60
  AND origin = 'SFO'
  AND destination = 'MIA'
```

## Spark SQL Command

```python
spark.sql("""
SELECT *
FROM activity19_3_table
WHERE delay < 60
  AND origin = 'SFO'
  AND destination = 'MIA'
""").show(5)
```

## Sample Results

```text
delay = -3
delay = -1
delay = -6
delay = -5
delay = 18
```

### Screenshot

```text
Step10_SFO_To_MIA_Delays_Less_Than_60.png
```

### Result

Successfully displayed the first five SFO-to-MIA flights with delays less than 60 minutes.

---

# Query Summary

## Query 1

### Criteria

```text
Origin: JFK
Destination: SEA
Delay > 90
```

### Records Displayed

```text
10 Rows
```

---

## Query 2

### Criteria

```text
Origin: SFO
Destination: MIA
Delay < 60
```

### Records Displayed

```text
5 Rows
```

---

# Screenshot Inventory

```text
Step01_Spark_Containers_Running.png
Step02_Verify_CSV_In_Root_Folder.png
Step03_Open_PySpark.png
Step04_Import_SparkSession.png
Step05_Create_Activity19_3_Session.png
Step06_Define_Activity19_3_Data_Variable.png
Step07_Create_DataFrame.png
Step08_Create_Temp_View.png
Step09_JFK_To_SEA_Delays_Greater_Than_90.png
Step10_SFO_To_MIA_Delays_Less_Than_60.png
```

---

# What I Learned

Through this activity I learned how to:

- Start and use PySpark
- Create Spark sessions
- Load CSV files into Spark DataFrames
- Create temporary SQL views
- Execute SQL queries within Spark
- Filter flight data by business rules
- Use Spark SQL to analyze transportation datasets
- Combine Python and SQL for distributed analytics

---

# Conclusion

The flight delay dataset was successfully loaded into Spark and exposed as a temporary SQL view. Using Spark SQL, specific flight routes were analyzed based on departure delay criteria. This activity demonstrated how PySpark combines Python and SQL capabilities within a distributed processing framework and reinforced the core concepts of DataFrames, Spark sessions, and Spark SQL querying.

---

# Submission Checklist

- [x] Step 01 – Spark Containers Running
- [x] Step 02 – CSV Verified in Root Folder
- [x] Step 03 – PySpark Started
- [x] Step 04 – SparkSession Imported
- [x] Step 05 – Activity19.3 Spark Session Created
- [x] Step 06 – Data Variable Defined
- [x] Step 07 – DataFrame Created
- [x] Step 08 – Temporary View Created
- [x] Step 09 – JFK to SEA Query Executed
- [x] Step 10 – SFO to MIA Query Executed

✅ Activity Completed Successfully