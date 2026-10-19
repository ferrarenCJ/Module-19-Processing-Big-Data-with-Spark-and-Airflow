# Module 19 Coding Activities

## Processing Big Data with Spark and Airflow

This folder contains the coding activities completed for Module 19. The activities focused on deploying and using Apache Spark for distributed data processing and Apache Airflow for workflow orchestration.

---

# Learning Objectives

The coding activities provided hands-on experience with:

- Creating and managing Docker containers
- Deploying Apache Spark
- Using PySpark to process and query data
- Working with Spark DataFrames
- Executing Spark SQL queries
- Deploying Apache Airflow
- Creating Directed Acyclic Graphs (DAGs)
- Scheduling and monitoring workflows
- Executing Python-based Airflow tasks

---

# Coding Activity Overview

## Coding Activity 19.1: Spark Docker Environment Setup

### Purpose

Introduce the Spark Docker environment using Bitnami containers.

### Skills Practiced

- Downloading Docker Compose files
- Starting Spark containers
- Managing Docker services
- Accessing Spark containers
- Verifying container health

### Commands Used

```bash
docker compose up
```

```bash
docker ps
```

```bash
docker exec -it bitnami_spark_1 bash
```

### Outcomes

- Successfully deployed a Spark environment
- Verified Spark services were running
- Connected to the Spark container

---

## Coding Activity 19.2: Working with PySpark

### Purpose

Learn how to start and use PySpark.

### Skills Practiced

- Launching PySpark
- Creating Spark sessions
- Loading CSV files
- Creating DataFrames
- Displaying data

### Commands Used

```python
from pyspark.sql import SparkSession
```

```python
spark = SparkSession.builder \
    .appName("Module19") \
    .getOrCreate()
```

### Outcomes

- Created Spark sessions
- Loaded structured data
- Worked with Spark DataFrames

---

## Coding Activity 19.3: Spark SQL Data Analysis

### Purpose

Analyze flight delay data with Spark SQL.

### Dataset

```text
departuredelays.csv
```

### Skills Practiced

- Creating temporary views
- Executing SQL queries
- Filtering records
- Retrieving subsets of data

### Commands Used

```python
df.createOrReplaceTempView("flight_delays")
```

```python
spark.sql("""
SELECT *
FROM flight_delays
LIMIT 10
""").show()
```

### Outcomes

- Queried large datasets
- Used SQL with Spark DataFrames
- Applied filtering conditions
- Retrieved analytical results

---

## Coding Activity 19.4: Apache Airflow Fundamentals

### Purpose

Learn workflow orchestration using Apache Airflow.

### Skills Practiced

- Deploying Airflow with Docker
- Accessing the Airflow UI
- Creating DAG files
- Building PythonOperator tasks
- Monitoring workflow execution

### Core Components

- DAG
- Task
- PythonOperator
- Scheduler
- Webserver

### Outcomes

- Built a working DAG
- Executed workflows
- Viewed logs
- Monitored execution status

---

# Spark Environment Commands

## Start Spark

```bash
docker compose up
```

---

## Open Spark Container

```bash
docker exec -it bitnami_spark_1 bash
```

---

## Launch PySpark

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
    .appName("Module19") \
    .getOrCreate()
```

---

# Working with DataFrames

## Define Data Path

```python
data_file = "/departuredelays.csv"
```

---

## Load CSV Data

```python
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(data_file)
```

---

## Display Data

```python
df.show()
```

---

## Display First Five Records

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

# Spark SQL Commands

## Create Temporary View

```python
df.createOrReplaceTempView("flight_delays")
```

---

## Run a SQL Query

```python
spark.sql("""
SELECT *
FROM flight_delays
LIMIT 10
""").show()
```

---

## Count Records Using SQL

```python
spark.sql("""
SELECT COUNT(*)
FROM flight_delays
""").*how()
```

*--

# Sample Queries

## Flights*from PHL to DFW with Delays Greate* Than 150 Minutes

```python*spark.sql("""
SELECT *
FROM assign*ent*9_3_table
WHERE origin*= 'PHL'
* AND destination = 'DFW'
  AND del*y > 150
LIMIT 15
""").show()
```

*--

## Flights with Distance Less *han 200 Miles

```python*spark.sql("""
SELECT *
FROM assign*ent19_3_table
WHERE distance < 200*LIMIT 10
""").show()
```

*--

## Flights*with Distance Greater Than 600 Mil*s

```python
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE d*stance > 600
LIMIT 10
*"").show()
```

*--

# Airflow Environment

## Down*oad Airflow Configuration

```bash*curl "https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml" -o docker-compose.yaml
`*`

---

## Start Airflow

```bash
*ocker compose up
```

---

## Airf*ow Login Credentials

```text
*sername: airflow
Password: airflow*```

---

## Airflow URL

```text
*ttp://localhost:8080
```

or

```t*xt*http://localhost:8081
```

for cus*om port mappings.

---

# Basic Ai*flow DAG Example

```python
from a*rflow import DAG
from datetime imp*rt datetime

dag = DAG(
    'examp*e_dag',
    description='Example W*rkflow',
    start*date=datetime(2024* 1, 1),
*   catchup=False
)
```

*--

# PythonOperator Example

```p*thon
from airflow.operators.python*operator import PythonOperator
```*
```python
def hello_world():
    *rint("Hello World")
```

```python*task = PythonOperator(
    task_id*'hello_world',
    python*callable=hello_world,
    dag=dag
*
```

---

# Airflow Workflow Exec*tion

## Steps*
1.*Enable the DAG*
2.*Trigger the DAG.
3. Monitor task e*ecution.
4. Review logs.
5. Verify*successful completion.

---

* Successful Execution Indicators

*``text
Marking task as SUCCESS
``*

```text
Task exited with return *ode 0
```

*``text*Done. Returned value was: 169
```
*---

# Typical Data Engineering Wo*kflow

```text
Source Data
    *│
     ▼
Spark*Processing
     │
    *▼
Data Transformation
     │
*    ▼
Air*low Workflow
     │
     ▼
Monitor*ng and Automation
     │
    *▼
Reporting and*Analytics*```

---

# Key Concepts Learned

*# Apache Spark

Primary Uses*

* Distributed computing
- Data tran*formation
- Large-scale analytics
* SQL processing

### Advantages

-*High performance
-*Scal*bility
- Fault tolerance
- Multi-l*nguage support

---

## Apache Air*low

Primary Uses:

- Workflow aut*mation
- Scheduling
- Monitoring
-*Dependency management

### Advanta*es

- Workflow visibility
- Automa*ion
- Reliability
- Extensibility
*---

# Practical Skills Developed
*During these coding activities I l*arned how to:

- Deploy Spark usin* Docker
- Launch and manage PySpar* sessions
- Create Spark DataFrame*
- Query data using Spark SQL
- De*loy Airflow services
- Create DAGs*- Implement PythonOperator tasks
-*Execute workflows
- Review Airflow*logs
- Troubleshoot containerized *nvironments

---

# Real-World App*ications

The skills practiced in *hese activities are commonly used *n:

- ETL pipelines
- Data warehou*ing
- Business intelligence
- Clou* data platforms
- Machine learning*pipelines
- Streaming analytics
- *orkflow automation
- Enterprise da*a engineering

---

# Key Takeaway*

- Spark processes large volumes *f data efficiently using distribut*d computing.
- Airflow orchestrate* and automates workflow execution.*- Docker simplifies deployment and*environment management.
- DataFram*s are the primary Spark data struc*ure.
- DAGs are the foundation of *irflow workflows.
- Spark and Airf*ow are commonly used together in p*oduction data pipelines.

---

# M*dule 19 Summary

The coding activi*ies in Module 19 provided hands-on*experience with Apache Spark and A*ache Airflow. Spark was used to pr*cess and analyze structured data u*ing PySpark and Spark SQL, while A*rflow was used to create, automate* and monitor workflows through DAG* and Operators. Together, these te*hnologies demonstrate how modern d*ta engineering platforms process l*rge datasets and automate complex *ata pipelines in scalable environm*nts.