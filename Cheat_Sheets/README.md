# Module 19 Cheat Sheet: Spark and Airflow

## Quick Overview

### Apache Spark

Apache Spark is a distributed computing framework used for large-scale data processing and analytics.

Primary Uses:

- Data Processing
- Data Transformation
- SQL Analytics
- Machine Learning
- Distributed Computing

---

### Apache Airflow

Apache Airflow is a workflow orchestration platform used to automate, schedule, and monitor data pipelines.

Primary Uses:

- Workflow Automation
- Task Scheduling
- Dependency Management
- Pipeline Monitoring

---

# Docker Commands

## List Running Containers

```bash
docker ps
```

---

## List All Containers

```bash
docker ps -a
```

---

## Start Containers

```bash
docker compose up
```

or

```bash
docker-compose up
```

---

## Run Containers in Background

```bash
docker compose up -d
```

---

## Stop Containers

```bash
docker compose down
```

---

## Open Container Terminal

```bash
docker exec -it <container_name> bash
```

Example:

```bash
docker exec -it bitnami_spark_1 bash
```

---

## Copy File Into Container

```bash
docker cp localfile.csv container_name:/path/file.csv
```

Example:

```bash
docker cp Data/departuredelays.csv bitnami_spark_1:/departuredelays.csv
```

---

# Spark Commands

## Start PySpark

```bash
/opt/spark/bin/pyspark
```

---

## Import SparkSession

```python
from pyspark.sql import SparkSession
```

---

## Create Spark Session

```python
spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()
```

---

## Verify Session

```python
spark
```

---

# Working with DataFrames

## Define Dataset Path

```python
data_file = "/departuredelays.csv"
```

---

## Load CSV File

```python
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(data_file)
```

---

## View Data

```python
df.show()
```

---

## View First 5 Records

```python
df.show(5)
```

---

## Display Schema

```python
df.printSchema()
```

---

## Count Records

```python
df.count()
```

---

# Spark SQL

## Create Temporary View

```python
df.createOrReplaceTempView("my_table")
```

---

## Execute SQL Query

```python
spark.sql("""
SELECT *
FROM my_table
""").show()
```

---

## Example Query

```python
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE distance < 200
LIMIT 10
""").show()
```

---

## Count Records Using SQL

```python
spark.sql("""
SELECT COUNT(*)
FROM assignment*9_3_table
""").show()
``*

*--

# SQL Query Patterns

## Filte* Records

```sql
SELECT *
FROM tab*e_name
WHERE condition
```

*--

##*Filter by Multiple Conditions

```*ql
SELECT *
*ROM table_name
WHERE origin*= 'PHL'
  AND destination = 'DFW'
*``

*--

## Return Limited Rows

```sql*SELECT *
FROM table_name
LIMIT 10
*``

*--

## Count Records

```*ql
SELECT COUNT(*)
FROM table_name
```

---

# Spark Flight Delay Queries

## PHL to DFW Delays Greater Than 150

```python
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE origin = 'PHL'
  AND destination = 'DFW'
  AND delay > 150
LIMIT 15
""").show()
```

---

## Distance Less Than 200 Miles

```python
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE distance < 200
LIMIT 10
""").show()
```

---

## Distance Greater Than 600 Miles

```python
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE distance > 600
LIMIT 10
""").show()
```

---

# Airflow Concepts

## DAG

Directed Acyclic Graph

A DAG defines:

- Tasks
- Dependencies
- Schedule
- Workflow Logic

---

## Task

A unit of work inside a DAG.

Examples:

- Run Python Function
- Execute SQL
- Send Email
- Run Spark Job

---

## Dependency

Defines task order.

Example:

```python
task1 >> task2
```

Meaning:

```text
task1 runs before task2
```

---

## PythonOperator

Executes Python code inside a DAG.

Example:

```python
PythonOperator(
    task_id='task_name',
    python_callable=my_function,
    dag=dag
)
```

---

# Airflow Imports

```python
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
```

---

# Airflow Default Arguments

```python
default_args = {
    'owner': 'Ferraren',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['ferrarecliff@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
```

---

# Create a DAG

```python
dag = DAG(
    'python_square_operator',
    description='Squaring a number using Airflow',
    schedule_interval='0 12 * * *',
    start_date=datetime(2017, 3* 20),
   *catchup=False
)
```

*--

# Define a Python Function

``*python
def square(x):
*   return*x * x
```

*--

# Create a PythonOperator Task*
```python
t1 = PythonOperator(
  * task_id*'square',
    python_callable=squa*e,
    op_kwargs={'x': 13},
    da*=dag
)
``*

---

* Airflow Login

Default Credential*:

```text
Username: airflow
Passw*rd: airflow
```

*--

* Airflow Web UI

Default*URL:

```text
http://localhost:8080
```

Port Conflict Example:

```t*xt
http://localhost:8081
*``

*--

#*Airflow Success Indicators

Succes*ful DAG execution typically shows:*
```text
Marking task as SUCCESS
`*`

```*ext
Task exited with return code 0*```

*``text
Done* Returned value was: <value>
``*

Example:

```text*Done. Returned value was: 169
```
**--

# Spark vs Airflow

## Spark

*esponsible For:

```text
Data Proc*ssing
Analytics
Machine*Learning
Distributed Computing
```*
---

## Airflow

Responsible For:*
```text*Workflow Scheduling
Orchestration
*onitoring
Automation
```

---

# A*chitecture Example

```text
Airflo* DAG
      │
      ▼
Spark*Job
      │
      ▼
Transform*Data
      │
      ▼
Store*Results*      │
      ▼
Send Notification
*``

---

#*Module 19 Exam*Notes

Remember*

-*Spark processes data.
- Airflow ma*ages workflows.
- Spark*ession*is required before Spark operation*.
- DataFrames are the primary Spa*k structure.
- Temporary*Views*enable SQL queries*
- DAGs define Airflow workflows.
* PythonOperator executes Python fu*ctions.
- Tasks are*connected through dependencies.
- *ocker simplifies deployment.
- Spa*k*and Airflow are commonly used toge*her in production data pipelines.
*---

# One-Line Summary

```text
*park = Process Data

*irflow*= Manage Workflows

Docker = Deplo* Everything
```
``*