# Module 19 Coding Activities

## Processing Big Data with Spark and Airflow

This folder contains the coding activities completed for Module 19. The activities focused on deploying and using Apache Spark for distributed data processing and Apache Airflow for workflow orchestration.

---

# Learning Objectives

The coding activities were designed to provide hands-on experience with:

- Creating and managing Docker containers
- Deploying Apache Spark
- Using PySpark to process and query data
- Understanding Spark DataFrames
- Executing Spark SQL queries
- Deploying Apache Airflow
- Creating Directed Acyclic Graphs (DAGs)
- Scheduling and monitoring workflows
- Executing Python-based Airflow tasks

---

# Coding Activities Overview

## Coding Activity 19.1

### Spark Docker Environment Setup

This activity introduced the Spark Docker environment using Bitnami containers.

### Skills Practiced

- Downloading Docker Compose files
- Starting Spark containers
- Managing Docker services
- Accessing Spark containers

### Key Commands

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
- Verified Spark services were available
- Connected to the Spark container

---

## Coding Activity 19.2

### Working with PySpark

This activity introduced PySpark and Spark Sessions.

### Skills Practiced

- Launching PySpark
- Creating Spark Sessions
- Loading CSV files
- Working with DataFrames

### Key Commands

```python
from pyspark.sql import SparkSession
```

```python
spark = SparkSession.builder \
    .appName("MyApplication") \
    .getOrCreate()
```

### Outcomes

- Created Spark Sessions
- Loaded structured data
- Worked with Spark DataFrames

---

## Coding Activity 19.3

### Spark SQL Data Analysis

This activity focused on analyzing flight delay data using Spark SQL.

### Dataset

```text
departuredelays.csv
```

### Skills Practiced

- Creating temporary views
- Executing SQL queries
- Filtering records
- Retrieving subsets of data

### Example Commands

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
- Used SQL against Spark DataFrames
- Applied filtering conditions
- Retrieved analytical results

---

## Coding Activity 19.4

### Apache Airflow Fundamentals

This activity introduced workflow orchestration using Airflow.

### Skills Practiced

- Deploying Airflow with Docker
- Accessing the Airflow UI
- Creating DAG files
- Building PythonOperator tasks

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

# Spark Environment

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
    .appName("Module19")
    .getOrCreate()
```

---

# Working with DataFrames

## Load CSV Data

```python
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/departuredelays.csv")
```

---

## View Data

```python
df.show()
```

---

## View First Five Records

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
df.createOrReplaceTempView("flight_delays")
```

---

## Run SQL Query

```python
spark.sql("""
SELECT *
FROM flight_delays
LIMIT 10
""").show()
```

---

## Count Records

```python
spark.sql("""
SELECT COUNT(*)
FROM flight_delays
""").show()
`*`

*--

# Airflow Environment

## Down*oad Configuration

```bash*curl "https://airflow*apache.org/docs/apache-airflow/2.1*1/docker-compose.yaml" -o docker-c*mpose.yaml
```

*--

## Start Airflow

```bash
dock*r compose up
```

---

*# Airflow Login

Default Credentia*s*

```text
Username: airflow
Passwo*d: airflow
```

*--

## Airflow URL

*``text
http://localhost:8080
```

*r

```text*http://localhost:8081
```

*f a custom port mapping is used.

*--

# Basic*Airflow DAG Structure

```python*from airflow import DAG

dag = DAG*
    'example_dag',
    descriptio*='Example Workflow'
)
```

---

# *ythonOperator Example

```*ython
*rom airflow.operators.python_opera*or import PythonOperator
```

```p*thon
def hello():
    print*"Hello World")
```

*``python
task = PythonOperator(
  * task_id='hello',
    python_calla*le=hello,
    dag*dag
)
```

*--

# Workflow Execution

## Trigg*r DAG

Use the Airflow web interfa*e to:

1.*Enable*the DAG
2. Trigger execution
3.*Monitor progress
4. Review logs

-*-

## Success Indicators

Successf*l execution typically shows:

```t*xt
Marking task as SUCCESS
```

*``*ext
Task exited with return code 0*```

*--

# Common Workflow Architecture*
```text
Data Source
      │
     *▼
PySpark Processing
      │
     *▼
Transform Data
      │
      ▼**irflow DAG
      │
      ▼*Schedule and*Monitor
      │
      ▼
Output*Results
```

*--

# Key Concepts Learned

*# Apache Spark

Used for:

- Distr*buted Processing
- Data Transforma*ion
- SQL Analytics
- Large-Scale *omputing

### Advantages

- Speed** Scalability
- Fault*Tolerance
- Multi-Language Support*
---

*# Apache Airflow

Used for:

- Wor*flow Automation
- Scheduling
-*Monitoring
- Dependency Management*
### Advantages

- Workflow Visibi*ity
- Automation
- Reliability
- E*tensibility

---

* Practical Skills Developed

Throu*h these coding activities I learne* how to:

- Deploy Spark using Doc*er
- Launch and manage PySpark ses*ions
- Create Spark DataFrames
- Q*ery data using Spark SQL
- Deploy*Airflow services
- Create DAGs
- I*plement PythonOperator tasks
- Exe*ute workflows
- Review Airflow log*
- Troubles*oot containerized environments

--*

# Real-World Applications

The t*chniques used in these activities *re commonly applied to:

- ETL Pip*lines
- Data Warehousing
- Busines* Intelligence
- Cloud Data Platfor*s
- Machine Learning Pipelines
- S*reaming Data Processing
- Workflow*Automation
- Enterprise Data Engin*ering

---

# Key Takeaways

- Spa*k processes data efficiently acros* distributed systems.
- Airflow or*hestrates workflows and automates *xecution.
- Docker simplifies depl*yment and environment management.
* DataFrames are*the primary abstraction used*in Spark.
- DAG* are the foundation of Airflow wor*flows.
- Spark and Airflow are fre*uently used together in enterprise*data engineering solutions.

---

* Module 19 Summary

The coding act*vities in Module 19 provided hands*on experience with Apache Spark an* Apache Airflow. Spark was used to*process and analyze structured dat* through PySpark and Spark SQL, wh*le Airflow was used to create and *utomate workflows through DAGs and*Operators. Together, these tools d*monstrated how modern data enginee*ing platforms process large volume* of data and automate complex data*pipelines using scalable and maint*inable architectures.