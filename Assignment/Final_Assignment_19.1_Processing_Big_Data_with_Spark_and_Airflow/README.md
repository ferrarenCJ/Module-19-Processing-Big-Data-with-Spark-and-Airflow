# Final Assignment 19.1: Processing Big Data with Spark and Airflow

## Module 19: Processing Big Data with Spark and Airflow

---

# Objective

This assignment demonstrates the ability to:

- Use Docker to create and manage Spark containers
- Load and query data using PySpark
- Execute SQL queries against Spark DataFrames
- Create and execute Airflow workflows
- Build and run DAGs using PythonOperator

The assignment consists of two major sections:

1. Part 1: PySpark
2. Part 2: Airflow

---

# Technologies Used

## Big Data Processing

- Apache Spark
- PySpark

## Workflow Orchestration

- Apache Airflow

## Containerization

- Docker
- Docker Compose

## Development Environment

- Visual Studio Code
- Windows Command Prompt

---

# Part 1: PySpark

## Step 1: Download Spark Docker Compose File

Downloaded the Bitnami Spark Docker Compose configuration file.

### Screenshot

```text
Step01_Download_Docker_Compose.png
```

---

## Step 2: Start Spark Containers

Started the Spark environment using Docker Compose.

### Containers

```text
bitnami_spark_1
bitnami_spark-worker-1
```

### Screenshot

```text
Step02_Containers_Running.png
```

---

## Step 3: Copy Dataset into Spark Container

Copied the flight delay dataset into the Spark container.

### Dataset

```text
departuredelays.csv
```

### Screenshot

```text
Step03_DepartureDelays_Copied.png
```

---

## Step 4: Open PySpark

Opened the Spark container and launched PySpark.

### Screenshot

```text
Step04_Open_PySpark.png
```

---

## Step 5: Import SparkSession

Imported SparkSession.

### Code

```python
from pyspark.sql import SparkSession
```

### Screenshot

```text
Step05_Start_PySpark_Session.png
```

---

## Step 6: Create Spark Session

Created a Spark session named Assignment19.3.

### Code

```python
spark = SparkSession.builder \
    .appName("Assignment19.3") \
    .getOrCreate()
```

### Screenshot

```text
Step06_Create_Spark_Session.png
```

---

## Step 7: Define Data Variable

Created a variable that stores the CSV file path.

### Code

```python
assignment19_3_data = "/departuredelays.csv"
```

### Screenshot

```text
Step07_Define_Data_Variable.png
```

---

## Step 8: Create DataFrame

Loaded the CSV file into a Spark DataFrame.

### Code

```python
df = spark.read.format("csv") \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .load(assignment19_3_data)
```

### Screenshot

```text
Step08_Create_DataFrame.png
```

---

## Step 9: Create Temporary View

Created a temporary SQL view from the DataFrame.

### Code

```python
df.createOrReplaceTempView("assignment19_3_table")
```

### Screenshot

```text
Step09_Create_Temp_View.png
```

---

## Step 10: Query Flights from PHL to DFW

Retrieved the first 15 flights from PHL to DFW with delays greater than 150 minutes.

### Screenshot

```text
Step10_PHL_DFW_Delay_Over_150.png
```

---

## Step 11: Query Flights Less Than 200 Miles

Retrieved the first 10 flights with a distance less than 200 miles.

### Screenshot

```text
Step11_Distance_Less_Than_200.png
```

---

## Step 12: Query Flights Greater Than 600 Miles

Retrieved the first 10 flights with a distance greater than 600 miles.

### Screenshot

```text
Step12_Distance_Greater_Than_600.png
```

---

# Part 2: Airflow

## Step 1: Download Airflow Docker Compose File

### Screenshot

```text
Step01_Download_Airflow_File.png
```

---

## Step 2: Configure Airflow

Updated:

```yaml
AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
```

and changed:

```yaml
8081:8080
```

to avoid a local port conflict.

### Screenshot

```text
Step02_Load_Examples_False.png
```

---

## Step 3: Start Airflow Containers

### Screenshot

```text
Step03_Airflow_Containers_Running.png
```

---

## Step 4: Log Into Airflow

### Screenshot

```text
Step04_Airflow_Login_Successful.png
```

---

## Step 5: Create DAG File

Created:

```text
module19_assignment.py
```

### Screenshot

```text
Step05_Create_Module19_Assignment_File.png
```

---

## Step 6: Import Required Libraries

### Screenshot

```text
Step06_Import_Libraries.png
```

---

## Step 7: Define Default Arguments

### Screenshot

```text
Step07_Define_Default_Args.png
```

---

## Step 8: Define square Function

### Screenshot

```text
Step08_Define_Square_Function.png
```

---

## Step 9: Define DAG Object

### Screenshot

```text
Step09_Define_DAG_Object.png
```

---

## Step 10: Define Task

### Screenshot

```text
Step10_Define_Task.png
```

---

## Step 11: Verify DAG Configuration

### Screenshot

```text
Step11_DAG_Configured.png
```

---

## Step 12: Execute the DAG

Expected result:

```text
13 × 13 = 169
```

### Screenshot

```text
Step12_DAG_Log_Successful.png
```

---

# Lessons Learned

Through this assignment I learned how to:

- Deploy Spark using Docker
- Work with PySpark DataFrames
- Query large datasets using Spark SQL
- Create temporary SQL views
- Deploy Airflow using Docker Compose
- Create DAGs using Python
- Execute and monitor workflows
- Review Airflow task logs

---

# Key Takeaways

- Apache Spark provides scalable distributed data processing.
- PySpark enables SQL-based analysis of large datasets.
- Apache Airflow orchestrates and automates workflows.
- Docker simplifies deployment and environment management.
- Spark and Airflow work together to support modern data engineering pipelines.

---

# Conclusion

This assignment demonstrated both distributed data processing with Apache Spark and workflow orchestration with Apache Airflow. Flight delay data was analyzed using PySpark and Spark SQL, while a custom Airflow DAG was created, deployed, and executed successfully. Together, these technologies provide a foundation for building scalable and automated data engineering solutions.

---

# Assignment Completion Checklist

## Part 1: PySpark

- [x] Download Docker Compose File
- [x] Start Spark Containers
- [x] Copy Dataset
- [x] Open PySpark
- [x] Create Spark Session
- [x] Create DataFrame
- [x] Create Temporary View
- [x] Execute Required Queries

## Part 2: Airflow

- [x] Download Airflow Configuration
- [x] Configure Airflow
- [x] Start Containers
- [x] Login to Airflow
- [x] Create DAG File
- [x] Configure DAG
- [x] Create Task
- [x] Execute Workflow
- [x] Review Logs

✅ Final Assignment 19.1 Completed Successfully