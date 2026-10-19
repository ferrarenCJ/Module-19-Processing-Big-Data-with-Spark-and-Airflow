# Module 19 Coding Activities

## Processing Big Data with Spark and Airflow

This folder contains the coding activities completed during Module 19. These activities introduced Apache Spark for distributed data processing and Apache Airflow for workflow orchestration and automation.

---

# Learning Objectives

The coding activities focused on developing practical skills in:

- Deploying Spark with Docker
- Using PySpark to process large datasets
- Creating Spark DataFrames
- Querying data with Spark SQL
- Deploying Airflow with Docker
- Creating and running DAGs
- Using PythonOperator tasks
- Monitoring workflow execution through Airflow

---

# Coding Activity 19.1: Spark Docker Environment Setup

## Objective

Deploy a Spark environment using Docker containers.

## Skills Practiced

- Docker Compose
- Container management
- Spark container deployment
- Container accessibility verification

## Key Commands

```bash
docker compose up
```

```bash
docker ps
```

```bash
docker exec -it bitnami_spark_1 bash
```

## Results

- Created Spark Master container
- Created Spark Worker container
- Verified the Spark environment was operational

---

# Coding Activity 19.2: PySpark Fundamentals

## Objective

Learn how to use PySpark within the Spark environment.

## Skills Practiced

- Launching PySpark
- Creating Spark Sessions
- Loading datasets
- Creating DataFrames

## Key Commands

```python
from pyspark.sql import SparkSession
```

```python
spark = SparkSession.builder \
    .appName("Module19") \
    .getOrCreate()
```

## Results

- Successfully launched PySpark
- Created Spark sessions
- Loaded structured datasets
- Created DataFrames for analysis

---

# Coding Activity 19.3: Spark SQL Queries

## Objective

Use Spark SQL to analyze flight delay data.

## Dataset

```text
departuredelays.csv
```

## Skills Practiced

- Creating temporary views
- Writing Spark SQL queries
- Filtering records
- Analyzing structured data

## Create Temporary View

```python
df.createOrReplaceTempView("flight_delays")
```

## Example Query

```python
spark.sql("""
SELECT *
FROM flight_delays
LIMIT 10
""").show()
```

## Results

- Queried large datasets
- Applied SQL filters
- Retrieved analytical results using Spark SQL

---

# Coding Activity 19.4: Apache Airflow Fundamentals

## Objective

Create and execute workflows using Apache Airflow.

## Skills Practiced

- Deploying Airflow with Docker
- Creating DAG files
- Using PythonOperator
- Running DAGs
- Monitoring execution logs

## Components Used

- DAG
- Task
- PythonOperator
- Scheduler
- Webserver

## Results

- Created a working DAG
- Executed workflow tasks
- Reviewed execution logs
- Verified successful task completion

---

# Spark Reference Commands

## Open Spark Container

```bash
docker exec -it bitnami_spark_1 bash
```

## Start PySpark

```bash
/opt/spark/bin/pyspark
```

## Create Spark Session

```python
spark = SparkSession.builder \
    .appName("Module19")
    .getOrCreate()
```

## Load CSV File

```python
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/departuredelays.csv")
```

## Display Records

```python
df.show()
```

## Display Schema

```python
df.printSchema()
```

## Count Records

```python
df.count()
```

---

# Spark SQL Reference

## Create Temporary View

```python
df.createOrReplaceTempView("flight_delays")
```

## Query Data

```python
spark.sql("""
SELECT *
FROM flight_delays
LIMIT 10
""").show()
```

## Count Records

```python
spark.sql("""
SELECT COUNT(*)
FROM flight_delays
""").*how*)
```

---

# Sample Module 19 Que*ies

## Flights*from PHL to DFW with Delays*Greater Than 150 Minutes

```pytho*
spark.sql("""
SELECT *
FROM assig*ment19_3_table
WHERE origin = 'PHL*
  AND*destination = 'DFW'
  AND delay > *50
LIMIT *5
""").show()
```

*# Flights Less Than 200 Miles

```*ython**park.sql("""
SELECT *
FROM assignm*nt*9_3_table
WHERE distance < 200
LIM*T 10
""").show()
```

## Flights G*eater Than 600 Miles

```python
sp*rk.sql("""
SELECT *
FROM assignmen*19_3_table
WHERE distance > 600
LI*IT 10
""").show()
```

---

# Airf*ow Environment

## Download Config*ration

```bash*curl "https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml" -o docker-compose.yaml
`*`

## Start Airflow

```bash
docke* compose up
```

## Login Credenti*ls

```text
Username: airflow
Pass*ord: airflow
```

## Web Interface*
```text
http://localhost:8080
```*
or

```text*http://localhost:8081
```

*f a custom port mapping is configu*ed.

---

# Basic DAG Example

```*ython
from airflow import DAG
from*datetime import datetime

dag = DA*(
    "*xample_dag",
    description="Exam*le Workflow",
    start*date=datetime(2024, 1, 1),
    cat*hup=False
)
```

---

# PythonOper*tor Example

```python*from airflow.operators.python_oper*tor import PythonOperator
```

*``python
*ef hello_world():
    print("Hello*World")
```

```python
task = Pyth*nOperator(
    task_id="hello_worl*",
    python_callable=hello_world*
    dag=dag,
)
```

*--

# Workflow Execution Steps

1.*Enable the DAG.
2. Trigger the DAG*
3. Monitor task execution.
4. Rev*ew logs.
5. Verify successful comp*etion.

---

# Successful Executio* Indicators

```text
Marking task *s SUCCESS
```

```text
Task exited*with return code 0
```

*``text
Done. Returned value was: 1*9
```

---

# Typical Data Enginee*ing Workflow

```text*Source Data
    |
    v
Spark*Processing*    |
    v
Data Transformation
  * |
    v
Airflow Workflow
    |
  * v
Monitoring and Automation
    |*    v*Reporting and Analytics
```

---

* Key Concepts Learned

## Apache S*ark

Used For:

- Distributed comp*ting
- Data transformation
- SQL a*alytics
- Large*scale data processing

### Advanta*es

- High performance
- Scalabili*y
- Fault tolerance
- Multi-langua*e support

---

## Apache Airflow
*Used For:

- Workflow automation
* Scheduling
- Monitoring
- Depende*cy management

### Advantages

- A*tomation
- Workflow visibility
- R*liability
- Extensibility

---

# *ractical Skills Developed

Through*these coding activities I learned *ow to:

- Deploy Spark using Docke*
- Launch and manage PySpark sessi*ns
- Create Spark DataFrames
- Que*y data using Spark SQL
- Deploy Ai*flow services
- Create DAGs
- Impl*ment PythonOperator tasks
- Execut* workflows
- Review Airflow logs
-*Troubleshoot containerized environ*ents

---

# Real-World Applicatio*s

The techniques practiced in thi* module are commonly used in:

- E*L pipelines
- Data warehousing
- B*siness intelligence
- Cloud data p*atforms
- Machine*learning pipelines
- Workflow auto*ation
- Streaming analytics
- Ente*prise data engineering

---

# Key*Takeaways

- Spark provides fast d*stributed data processing.
- PySpa*k enables large-scale analytics us*ng Python.
- Spark*SQL allows SQL queries against Dat*Frames.
- Air*low automates and orchestrates wor*flows.
- Docker simplifies deploym*nt and configuration.
- Spark*and Airflow are commonly used toge*her in modern data engineering arc*itectures.

---

# Module 19 Summa*y

Module 19 provided hands-on exp*rience with Apache Spark and Apach* Airflow. Spark was used to proces* and analyze structured data using*PySpark and Spark SQL. Airflow was*used to create, schedule, execute,*and monitor workflows through DAGs*and Operators. Together, these tec*nologies demonstrated how modern d*ta engineering solutions process l*rge datasets and automate complex *orkflows in scalable environments.*