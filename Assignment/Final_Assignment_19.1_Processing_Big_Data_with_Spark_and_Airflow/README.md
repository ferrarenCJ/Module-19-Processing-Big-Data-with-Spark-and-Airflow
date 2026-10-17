# Final*Assignment 19.1: Processing Big Da*a with Spark and Airflow

## Modul* 19: Processing Big Data with Spar* and Airflow

---

# Objective

Th*s assignment demonstrates the abil*ty to:

- Use Docker to create and*manage Spark containers
- Load and*query data using PySpark
- Execute*SQL queries against Spark DataFram*s
- Create and execute Airflow wor*flows
- Build and run DAGs using P*thonOperator

The assignment consi*ts of two major sections:

1. Part*1: PySpark
2. Part 2: Airflow

---*
# Technologies Used

## Big Data *rocessing

- Apache Spark
- PySpar*

## Workflow Orchestration

- Apa*he Airflow

## Containerization

-*Docker
- Docker Compose

## Develo*ment Environment

- Visual Studio *ode
- Windows Command Prompt

---
*# Project Structure

```text
Final*Assignment_19.1_Processing_Big_Dat*_with_Spark_and_Airflow
│
├── airf*ow_assignment
│   ├── dags
│   │  *└── module19_assignment.py
│   ├──*logs
│   ├── plugins
│   └── docke*-compose.yaml
│
├── bitnami
│   └─* docker-compose.yml
│
├── Code
│  *├── airflow_dag_reference.py
│   └*─ pyspark_queries.py
│
├── Data
│ * └── departuredelays.csv
│
├── Doc*ment
├── Screenshots
└── README.md*```

---

# Part 1: PySpark

## St*p 1: Download Spark Docker Compose*File

Downloaded the Bitnami Spark*Docker Compose configuration file.*
### Screenshot

```text
Step01_Do*nload_Docker_Compose.png
```

---
*## Step 2: Start Spark Containers
*Started the Spark environment usin* Docker Compose.

### Containers

*``text
bitnami_spark_1
bitnami_spa*k-worker-1
```

### Screenshot

``*text
Step02_Containers_Running.png*```

---

## Step 3: Copy Dataset *nto Spark Container

Copied the fl*ght delay dataset into the Spark c*ntainer.

### Dataset

```text
dep*rturedelays.csv
```

### Screensho*

```text
Step03_DepartureDelays_C*pied.png
```

---

## Step 4: Open*PySpark

Opened the Spark containe* and launched PySpark.

### Screen*hot

```text
Step04_Open_PySpark.p*g
```

---

## Step 5: Import Spar*Session

Imported SparkSession.

#*# Code

```python
from pyspark.sql*import SparkSession
```

### Scree*shot

```text
Step05_Start_PySpark*Session.png
```

---

## Step 6: C*eate Spark Session

Created a Spar* session named Assignment19.3.

##* Code

```python
spark = SparkSess*on.builder \
    .appName("Assignm*nt19.3") \
    .getOrCreate()
```
*### Screenshot

```text
Step06_Cre*te_Spark_Session.png
```

---

## *tep 7: Define Data Variable

Creat*d a variable that stores the CSV f*le path.

### Code

```python
assi*nment19_3_data = "/departuredelays*csv"
```

### Screenshot

```text
*tep07_Define_Data_Variable.png
```*
---

## Step 8: Create DataFrame
*Loaded the CSV file into a Spark D*taFrame.

### Code

```python
df =*spark.read.format("csv") \
    .op*ion("inferSchema", "true") \
    .*ption("header", "true") \
    .loa*(assignment19_3_data)
```

### Scr*enshot

```text
Step08_Create_Data*rame.png
```

---

## Step 9: Crea*e Temporary View

Created a tempor*ry SQL view from the DataFrame.

#*# Code

```python
df.createOrRepla*eTempView("assignment19_3_table")
*``

### Screenshot

```text
Step09*Create_Temp_View.png
```

---

## *tep 10: Query Flights from PHL to *FW

Retrieved the first 15 flights*from PHL to DFW with delays greate* than 150 minutes.

### Query

```*ql
SELECT *
FROM assignment19_3_ta*le
WHERE origin = 'PHL'
  AND dest*nation = 'DFW'
  AND delay > 150
L*MIT 15
```

### Screenshot

```tex*
Step10_PHL_DFW_Delay_Over_150.png*```

---

## Step 11: Query Flight* Less Than 200 Miles

Retrieved th* first 10 flights with a distance *ess than 200 miles.

### Query

``*sql
SELECT *
FROM assignment19_3_t*ble
WHERE distance < 200
LIMIT 10
*``

### Screenshot

```text
Step11*Distance_Less_Than_200.png
```

--*

## Step 12: Query Flights Greate* Than 600 Miles

Retrieved the fir*t 10 flights with a distance great*r than 600 miles.

### Query

```s*l
SELECT *
FROM assignment19_3_tab*e
WHERE distance > 600
LIMIT 10
``*

### Screenshot

```text
Step12_D*stance_Greater_Than_600.png
```

-*-

# Part 1 Summary

The Spark env*ronment was successfully deployed *sing Docker. The flight delay data*et was loaded into PySpark, conver*ed into a DataFrame, exposed as a *emporary SQL view, and queried usi*g Spark SQL.

Skills demonstrated:*
- Docker container management
- S*ark session creation
- DataFrame c*eation
- Temporary SQL views
- Spa*k SQL queries
- Big data analysis
*---

# Part 2: Airflow

## Step 1:*Download Airflow Docker Compose Fi*e

Downloaded the Airflow Docker C*mpose configuration file.

### Scr*enshot

```text
Step01_Download_Ai*flow_File.png
```

---

## Step 2:*Configure Airflow

Modified:

```y*ml
AIRFLOW__CORE__LOAD_EXAMPLES: '*alse'
```

and updated the webserv*r port to:

```yaml
8081:8080
```
*### Screenshot

```text
Step02_Loa*_Examples_False.png
```

---

## S*ep 3: Start Airflow

Started the A*rflow environment using Docker Com*ose.

### Screenshot

```text
Step*3_Airflow_Containers_Running.png
`*`

---

## Step 4: Log Into Airflo*

Successfully logged into Airflow*

### URL

```text
http://localhos*:8081
```

### Screenshot

```text*Step04_Airflow_Login_Successful.pn*
```

---

## Step 5: Create DAG F*le

Created:

```text
module19_ass*gnment.py
```

inside the Airflow *AG folder.

### Screenshot

```tex*
Step05_Create_Module19_Assignment*File.png
```

---

## Step 6: Impo*t Required Libraries

### Code

``*python
from datetime import timede*ta, datetime
from airflow import D*G
from airflow.operators.python_op*rator import PythonOperator
from a*rflow.utils.dates import days_ago
*``

### Screenshot

```text
Step06*Import_Libraries.png
```

---

## *tep 7: Define Default Arguments

#*# Code

```python
default_args = {*    'owner': 'Ferraren',
    'depe*ds_on_past': False,
    'start_dat*': days_ago(2),
    'email': ['fer*arecliff@gmail.com'],
    'email_o*_failure': False,
    'email_on_re*ry': False,
    'retries': 1,
}
``*

### Screenshot

```text
Step07_D*fine_Default_Args.png
```

---

##*Step 8: Define square Function

##* Code

```python
def square(x):
  * return x * x
```

### Screenshot
*```text
Step08_Define_Square_Funct*on.png
```

---

## Step 9: Define*DAG Object

### Code

```python
da* = DAG(
    'python_square_operato*',
    description='Squaring a num*er using Airflow',
    schedule_in*erval='0 12 * * *',
    start_date*datetime(2017, 3, 20),
    catchup*False
)
```

### Screenshot

```te*t
Step09_Define_DAG_Object.png
```*
---

## Step 10: Define Task

###*Code

```python
t1 = PythonOperato*(
    task_id='square',
    python*callable=square,
    op_kwargs={'x*: 13},
    dag=dag,
)

t1
```

###*Screenshot

```text
Step10_Define_*ask.png
```

---

## Step 11: Veri*y DAG Configuration

Verified that*the DAG appeared in the Airflow in*erface.

### DAG Name

```text
pyt*on_square_operator
```

### Screen*hot

```text
Step11_DAG_Configured*png
```

---

## Step 12: Execute *he DAG

Executed the workflow and *eviewed the logs.

### Expected Ca*culation

```text
13 × 13 = 169
``*

### Successful Log Messages

```*ext
Done. Returned value was: 169
*``

```text
Marking task as SUCCES*
```

```text
Task exited with ret*rn code 0
```

### Screenshot

```*ext
Step12_DAG_Log_Successful.png
```

---

# Key Skills Demonstrated

- Docker container deployment
- Apache Spark configuration
- PySpark DataFrames
- Spark SQL querying
- Apache Airflow configuration
- DAG creation
- PythonOperator implementation
- Workflow orchestration
- Workflow monitoring and logging

---

# Key Takeaways

- Spark provides scalable distributed data processing.
- PySpark enables SQL-based big data analysis.
- Airflow provides workflow automation and orchestration.
- Docker simplifies environment setup and deployment.
- Spark and Airflow work together to support modern data engineering pipelines.

---

# Conclusion

This assignment successfully demonstrated both large-scale data processing with Apache Spark and workflow orchestration with Apache Airflow. Flight delay data was analyzed using PySpark and Spark SQL, while a custom Airflow DAG was created, deployed, and executed successfully. Together, these activities reinforced key concepts in modern data engineering, including distributed processing, workflow automation, containerization, and monitoring.

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