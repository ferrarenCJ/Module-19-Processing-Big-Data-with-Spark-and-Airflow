# Final Assignment 19.1: Processing Big Data with Spark and Airflow

## Module 19: Processing Big Data with Spark and Airflow

---

# Assignment Information

| Item | Details |
|--------|--------|
| Assignment | Final Assignment 19.1 |
| Module | Module 19 |
| Title | Processing Big Data with Spark and Airflow |
| Points | 100 |
| Learning Outcomes | Docker, PySpark, Spark SQL, Airflow DAGs |
| Tools Used | Docker, Apache Spark, PySpark, Apache Airflow, VS Code |

---

# Objective

This assignment demonstrates the ability to:

1. Create and manage Spark Docker containers.
2. Load and query data using PySpark.
3. Execute SQL queries against Spark DataFrames.
4. Create and manage Airflow workflows.
5. Define and execute Airflow DAGs using PythonOperator.

The assignment consisted of two major sections:

- Part 1: PySpark
- Part 2: Airflow

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

# Project Structure

```text
Final_Assignment_19.1_Processing_Big_Data_with_Spark_and_Airflow
│
├── airflow_assignment
│   ├── dags
│   │   └── module19_assignment.py
│   ├── logs
│   ├── plugins
│   └── docker-compose.yaml
│
├── bitnami
│   └── docker-compose.yml
│
├── Code
│   ├── airflow_dag_reference.py
│   └── pyspark_queries.py
│
├── Data
│   └── departuredelays.csv
│
├── Document
│
├── Screenshots
│
└── README.md
```

---

# Part 1: PySpark

---

# Step 1: Download Spark Docker Compose File

Created a Bitnami Spark working directory and downloaded the Docker Compose file required to launch the Spark environment.

## Command

```bash
curl https://raw.githubusercontent.com/emeritus/MO-PCDE-assets/main/module19/Required_Coding_activity_spark_image/starter/docker-compose.yml -o docker-compose.yml
```

### Screenshot

```text
Step01_Download_Docker_Compose.png
```

---

# Step 2: Start Spark Containers

Started the Spark environment using Docker Compose.

## Command

```bash
docker compose up
```

## Containers

```text
bitnami_spark_1
bitnami_spark-worker-1
```

### Screenshot

```text
Step02_Containers_Running.png
```

---

# Step 3: Copy Dataset into Spark Container

Copied the dataset into the Spark container.

## Dataset

```text
departuredelays.csv
```

## Command

```bash
docker cp Data\departuredelays.csv bitnami_spark_1:/departuredelays.csv
```

## Verification

```bash
ls /
```

Output included:

```text
departuredelays.csv
```

### Screenshot

```text
Step03_DepartureDelays_Copied.png
```

---

# Step 4: Open PySpark

Opened the Spark container and launched PySpark.

## Commands

```bash
docker exec -it bitnami_spark_1 bash
```

```bash
/opt/spark/bin/pyspark
```

### Screenshot

```text
Step04_Open_PySpark.png
```

---

# Step 5: Import SparkSession

Imported the SparkSession package.

## Code

```python
from pyspark.sql import SparkSession
```

### Screenshot

```text
Step05_Start_PySpark_Session.png
```

---

# Step 6: Create Spark Session

Created a Spark session named Assignment19.3.

## Code

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

# Step 7: Define Dataset Path

Created a variable containing the dataset path.

## Code

```python
assignment19_3_data = "/departuredelays.csv"
```

### Screenshot

```text
Step07_Define_Data_Variable.png
```

---

# Step 8: Load DataFrame

Loaded the CSV file into a Spark DataFrame.

## Code

```python
df = spark.read.format("csv") \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .load(assignment19_3_data)
```

## Verification

```python
df.show(5)
```

### Screenshot

```text
Step08_Create_DataFrame.png
```

---

# Step 9: Create Temporary View

Created a temporary SQL view for querying.

## Code

```python
df.createOrReplaceTempView("assignment19_3_table")
```

## Verification

```python
spark.sql("""
SELECT COUNT(*)
FROM assignment19_3_table
""").s*ow()
```

### Screenshot

```text
*tep09_Create_Temp_View.png
```

--*

# Step 10: Query Flights from PH* to DFW

Selected the first 15 fli*hts from Philadelphia Internationa* Airport (PHL) to Dallas/Fort Wort* International Airport (DFW) with *elays greater than 150 minutes.

#* Query

```sql
SELECT *
FROM assig*ment19_3_table
WHERE origin = 'PHL*
  AND destination = 'DFW'
  AND d*lay > 150
LIMIT 15
```

### Screen*hot

```text
Step10_PHL_DFW_Delay_*ver_150.png
```

---

# Step 11: Q*ery Flights Less Than 200 Miles

S*lected the first 10 flights with d*stances less than 200 miles.

## Q*ery

```sql
SELECT *
FROM assignme*t19_3_table
WHERE distance < 200
L*MIT 10
```

### Screenshot

```tex*
Step11_Distance_Less_Than_200.png*```

---

# Step 12: Query Flights*Greater Than 600 Miles

Selected t*e first 10 flights with distances *reater than 600 miles.

## Query

*``sql
SELECT *
FROM assignment19_3*table
WHERE distance > 600
LIMIT 1*
```

### Screenshot

```text
Step*2_Distance_Greater_Than_600.png
``*

---

# Part 1 Summary

The Spark*environment was successfully deplo*ed using Docker. The flight delay *ataset was loaded into PySpark, co*verted into a DataFrame, exposed a* a temporary SQL view, and queried*using Spark SQL.

Key skills demon*trated:

- Docker container manage*ent
- Spark session creation
- Dat*Frame creation
- Spark SQL queryin*
- Big data analysis using PySpark*
---

# Part 2: Airflow

---

# St*p 1: Download Airflow Docker Compo*e File

Created the Airflow workin* directory and downloaded the Airf*ow Docker Compose configuration fi*e.

## Command

```bash
curl "https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml" *o docker-compose.yaml
```

### Scr*enshot

```text
Step01_Download_Ai*flow_File.png
```

---

# Step 2: *onfigure Airflow

Modified:

```ya*l
AIRFLOW__CORE__LOAD_EXAMPLES: 'f*lse'
```

and updated the webserve* port:

```yaml
8081:8080
```

to *void a local port conflict.

### S*reenshot

```text
Step02_Load_Exam*les_False.png
```

---

# Step 3: *tart Airflow

Started all Airflow *ervices.

## Command

```bash
dock*r compose up
```

### Running Cont*iners

```text
airflow-webserver-1*airflow-scheduler-1
airflow-worker*1
flower-1
postgres-1
redis-1
```
*### Screenshot

```text
Step03_Air*low_Containers_Running.png
```

--*

# Step 4: Log Into Airflow

Acce*sed:

```text
http://localhost:8081
```

using:

```text
Username: ai*flow
Password: airflow
```

### Sc*eenshot

```text
Step04_Airflow_Lo*in_Successful.png
```

---

# Step*5: Create DAG File

Created:

```t*xt
module19_assignment.py
```

ins*de:

```text
airflow_assignment/da*s
```

### Screenshot

```text
Ste*05_Create_Module19_Assignment_File*png
```

---

# Step 6: Import Req*ired Libraries

## Code

```python*from datetime import timedelta, da*etime
from airflow import DAG
from*airflow.operators.python_operator *mport PythonOperator
from airflow.*tils.dates import days_ago
```

##* Screenshot

```text
Step06_Import*Libraries.png
```

---

# Step 7: *onfigure Default Arguments

## Cod*

```python
default_args = {
    '*wner': 'Ferraren',
    'depends_on*past': False,
    'start_date': da*s_ago(2),
    'email': ['ferrarecliff@gmail.com'],
    'email_on_fail*re': False,
    'email_on_retry': *alse,
    'retries': 1,
}
```

###*Screenshot

```text
Step07_Define_*efault_Args.png
```

---

# Step 8* Create square() Function

## Code*
```python
def square(x):
    retu*n x * x
```

### Screenshot

```te*t
Step08_Define_Square_Function.pn*
```

---

# Step 9: Define DAG

#* Code

```python
dag = DAG(
    'p*thon_square_operator',
    descrip*ion='Squaring a number using Airfl*w',
    schedule_interval='0 12 * * *',
    start_date=datetime(2017,*3, 20),
    catchup=False
)
```

#*# Screenshot

```text
Step09_Defin*_DAG_Object.png
```

---

# Step 1*: Create Task

## Code

```python
*1 = PythonOperator(
    task_id='s*uare',
    python_callable=square,*    op_kwargs={'x': 13},
    dag=d*g,
)

t1
```

### Screenshot

```t*xt
Step10_Define_Task.png
```

---*
# Step 11: Verify DAG

Verified t*at the DAG appeared in the Airflow*user interface.

## DAG Name

```t*xt
python_square_operator
```

###*Screenshot

```text
Step11_DAG_Con*igured.png
```

---

# Step 12: Ex*cute DAG

Executed the workflow an* reviewed the task logs.

## Expec*ed Calculation

```text
13 × 13 = *69
```

## Log Results

```text
Do*e. Returned value was: 169
```

``*text
Marking task as SUCCESS
```

*``text
Task exited with return cod* 0
```

### Screenshot

```text
St*p12_DAG_Log_Successful.png
```

--*

# Airflow DAG Source Code

```py*hon
from datetime import timedelta* datetime
from airflow import DAG
*rom airflow.operators.python_opera*or import PythonOperator
from airf*ow.utils.dates import days_ago

de*ault_args = {
    'owner': 'Ferrar*n',
    'depends_on_past': False,
*   'start_date': days_ago(2),
    *email': ['ferrarecliff@gmail.com']*
    'email_on_failure': False,
  * 'email_on_retry': False,
    'ret*ies': 1,
}

def square(x):
    ret*rn x * x

dag = DAG(
    'python_s*uare_operator',
    description='S*uaring a number using Airflow',
  * schedule_interval='0 12 * * *',
 *  start_date=datetime(2017, 3, 20)*
    catchup=False
)

t1 = PythonO*erator(
    task_id='square',
    *ython_callable=square,
    op_kwar*s={'x': 13},
    dag=dag,
)

t1
``*

---

# Lessons Learned

Through *his assignment I learned how to:

* Deploy Spark using Docker contain*rs
- Work with PySpark DataFrames
* Query large datasets using Spark *QL
- Create temporary SQL views
- *nalyze flight delay data
- Deploy *irflow using Docker Compose
- Crea*e DAGs using Python
- Use Airflow Operators
- Automate workflows
- Execute and monitor DAGs
- Review workflow execution logs

---

# Key Takeaways

- Spark provides scalable distributed data processing.
- PySpark enables SQL-based analysis on large datasets.
- Airflow provides workflow orchestration through DAGs.
- Docker simplifies deployment and environment management.
- Airflow and Spark complement each other in modern data engineering architectures.
- Workflow automation improves reliability, scalability, and maintainability.

---

# Conclusion

This assignment successfully demonstrated the deployment and use of Apache Spark and Apache Airflow using Docker. Spark was used to load, process, and query flight delay data through PySpark and Spark SQL. Airflow was used to build and execute a custom workflow using a DAG and PythonOperator. Together, these platforms illustrate how modern data engineering systems process large datasets and automate complex workflows in scalable and reliable environments.

---

# Assignment Completion Checklist

## Part 1: PySpark

- [x] Download Docker Compose File
- [x] Start Spark Containers
- [x] Copy Dataset
- [x] Open PySpark
- [x] Create Spark Session
- [x] Create DataFrame
- [x] Create SQL View
- [x] Execute All Required Queries

## Part 2: Airflow

- [x] Download Airflow Configuration
- [x] Configure Airflow
- [x] Launch Containers
- [x] Login to Airflow
- [x] Create DAG File
- [x] Configure DAG
- [x] Create Task
- [x] Execute Workflow
- [x] Review Logs

✅ Final Assignment 19.1 Completed Successfully