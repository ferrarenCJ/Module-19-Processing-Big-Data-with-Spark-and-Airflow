# Required Coding Activity 19.4: Creating a Workflow in Airflow

## Module 19: Processing Big Data with Spark and Airflow

---

# Activity Information

| Item | Details |
|--------|--------|
| Activity | Required Coding Activity 19.4 |
| Title | Creating a Workflow in Airflow |
| Points | 20 |
| Submission Type | File Upload |
| Learning Outcome | Create a workflow in Airflow |
| Estimated Completion Time | 60 Minutes |

---

# Objective

The purpose of this activity is to create, deploy, and execute a workflow in Apache Airflow using Docker.

In this activity, I:

- Installed and configured Airflow using Docker Compose
- Disabled default example DAGs
- Launched Airflow services
- Accessed the Airflow Web UI
- Added a custom DAG to the Airflow environment
- Executed the DAG successfully
- Reviewed execution logs

---

# Technologies Used

- Apache Airflow 2.1.1
- Docker
- Docker Compose
- Python
- Visual Studio Code
- Airflow DAGs
- PythonOperator

---

# Directory Structure

```text
Coding_Activity_19.4_Airflow_Workflows
│
└── airflow
    ├── dags
    │   └── SampleDAG.py
    ├── logs
    ├── plugins
    └── docker-compose.yaml
```

---

# Step 1: Download the Airflow Docker Compose File

## Objective

Create the Airflow working directory and download the Airflow Docker Compose configuration file.

## Commands Executed

```bash
mkdir airflow
```

```bash
cd airflow
```

```bash
curl "https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml" -o docker-compose.yaml
```

## Result

Successfully downloaded:

```text
docker-compose.yaml
```

which contains all required Airflow service definitions.

### Screenshot

```text
Step01_Download_Docker_Compose_File.png
```

### Evidence

Verified successful execution of:

```bash
curl
```

and creation of:

```text
docker-compose.yaml
```

---

# Step 2: Disable Example DAGs

## Objective

Prevent Airflow from loading default example workflows.

## File Modified

```text
docker-compose.yaml
```

## Original Configuration

```yaml
AIRFLOW__CORE__LOAD_EXAMPLES: 'true'
```

## Updated Configuration

```yaml
AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
```

## Result

Airflow will only load custom DAGs added during this activity.

### Screenshot

```text
Step02_Load_Examples_False.png
```

### Evidence

Configuration updated successfully and saved.

---

# Step 3: Start Airflow Services

## Objective

Launch all Airflow services using Docker Compose.

## Command Executed

```bash
docker compose up
```

---

# Port Conflict Resolution

Initially, the Airflow webserver failed because port:

```text
8080
```

was already in use.

The following configuration was updated:

```yaml
ports:
  - 8080:8080
```

changed to:

```yaml
ports:
  - 8081:8080
```

The Airflow environment was then restarted.

---

# Running Services

After restart the following containers were running successfully:

```text
airflow-webserver-1
airflow-scheduler-1
airflow-worker-1
flower-1
redis-1
postgres-1
```

## Result

Airflow services initialized successfully.

### Screenshot

```text
Step03_Airflow_Containers_Running.png
```

---

# Step 4: Log Into Airflow

## Objective

Access the Airflow Web UI.

## URL

```text
http://localhost:8081
```

## Credentials

### Username

```text
airflow
```

### Password

```text
airflow
```

## Result

Successfully authenticated and accessed the Airflow dashboard.

### Screenshot

```text
Step04_Airflow_Login_Successful.png
```

---

# Step 5: Add Sample DAG

## Objective

Deploy a custom DAG to Airflow.

## DAG File

```text
SampleDAG.py
```

## Target Location

```text
airflow/dags/SampleDAG.py
```

## Verification

Confirmed that the file exists inside:

```text
dags
```

directory.

### Screenshot

```text
Step05_SampleDAG_In_Dags_Folder.png
```

### Result

Airflow can now automatically scan and discover the DAG.

---

# Sample DAG Source Code

```python
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world from first Airflow DAG!'

dag = DAG(
    'hello_world',
    description='Hello World DAG',
    schedule_interval='0 12 * * *',
    start_date=datetime(2017, 3, 20),
    catchup=False
)

hello_operator = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag
)

hello_operator
```

---

# Step 6: Verify DAG Discovery

## Objective

Confirm that Airflow successfully loaded the DAG.

## DAG Name

```text
hello_world
```

## Verification

After refreshing Airflow, the DAG appeared in the DAG list.

Displayed details included:

```text
DAG Name: hello_world
Owner: airflow
Schedule: 0 12 * * *
```

### Screenshot

```text
Step06_Hello_World_DAG_Displayed.png
```

### Result

Airflow successfully discovered and loaded the DAG definition.

---

# Step 7: Execute the DAG

## Objective

Run the workflow and review execution logs.

## Workflow

```text
hello_world
```

## Task

```text
hello_task
```

## Action

- Enabled the DAG
- Triggered execution
- Opened Graph View
- Selected task logs

---

# Log Output

The Airflow logs displayed:

```text
Hello world from first Airflow DAG!
```

Airflow also reported:

```text
Marking task as SUCCESS
```

and

```text
Task exited with return code 0
```

### Screenshot

```text
Step07_DAG_Log_Successful.png
```

### Result

The workflow executed successfully.

---

# DAG Architecture

The workflow contains:

```text
hello_world DAG
       │
       ▼
hello_task
       │
       ▼
print_hello()
```

Output:

```text
Hello world from first Airflow DAG!
```

---

# Key Airflow Concepts Demonstrated

## DAG

Directed Acyclic Graph

```text
Workflow Definition
```

---

## PythonOperator

Used to execute:

```python
print_hello()
```

---

## Scheduler

Responsible for:

```text
Detecting DAGs
Scheduling Runs
Managing Execution
```

---

## Worker

Responsible for:

```text
Executing Tasks
```

---

## Web Server

Provides:

```text
Airflow User Interface
```

---

# Screenshot Inventory

```text
Step01_Download_Docker_Compose_File.png
Step02_Load_Examples_False.png
Step03_Airflow_Containers_Running.png
Step04_Airflow_Login_Successful.png
Step05_SampleDAG_In_Dags_Folder.png
Step06_Hello_World_DAG_Displayed.png
Step07_DAG_Log_Successful.png
```

---

# What I Learned

Through this activity I learned how to:

- Install Airflow using Docker Compose
- Configure Airflow settings
- Resolve Docker port conflicts
- Access the Airflow Web UI
- Create and deploy DAGs
- Use PythonOperator
- Run workflows
- Monitor workflow execution
- Review Airflow task logs
- Understand DAG discovery and scheduling

---

# Key Takeaways

- Airflow is an open-source workflow orchestration platform.
- DAGs define workflows in Airflow.
- DAGs are written in Python.
- Airflow automatically scans the `dags` folder for workflow definitions.
- Tasks can be implemented using Operators such as PythonOperator.
- Airflow provides detailed logging and monitoring capabilities.
- Docker simplifies Airflow deployment and environment setup.

---

# Conclusion

This activity demonstrated the complete lifecycle of creating and executing a workflow in Apache Airflow. Airflow was successfully installed using Docker Compose, configured to disable default examples, and accessed through the web interface. A custom DAG was deployed, discovered automatically by Airflow, and executed successfully. The workflow produced the expected output and completed without errors, demonstrating the core concepts of DAG creation, task execution, workflow orchestration, and monitoring.

---

# Submission Checklist

- [x] Download Airflow Docker Compose File
- [x] Disable Example DAGs
- [x] Launch Airflow Containers
- [x] Access Airflow UI
- [x] Add SampleDAG.py
- [x] Verify hello_world DAG Discovery
- [x] Execute DAG Successfully
- [x] Review Task Logs

✅ Activity Completed Successfully