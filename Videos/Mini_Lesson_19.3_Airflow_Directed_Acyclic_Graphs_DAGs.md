# Mini-Lesson 19.3: Airflow Directed Acyclic Graphs (DAGs)

---

# Overview

This mini-lesson introduces **Directed Acyclic Graphs (DAGs)**, the fundamental building blocks of Apache Airflow workflows.

A DAG defines:

- Workflow structure
- Task execution order
- Task dependencies
- Scheduling behavior

Every Airflow workflow is represented as a DAG, making DAGs the core concept behind workflow orchestration in Airflow.

---

# Learning Objectives

After completing this lesson, I should be able to:

- Explain what a directed graph is.
- Differentiate between a directed graph and a directed acyclic graph.
- Understand how DAGs represent workflows in Airflow.
- Define tasks and dependencies within a DAG.
- Understand common Airflow operators.
- Create a simple DAG using Python.
- Define task execution order using dependencies.

---

# What Is a Directed Graph?

A directed graph consists of:

- Vertices (nodes)
- Edges (connections)

where every edge has a direction.

Example:

```text
A → B → C
```

Each arrow indicates the direction of execution or flow.

---

# Components of a Directed Graph

## Nodes

Represent units of work.

Example:

```text
A
B
C
D
```

---

## Edges

Represent relationships between nodes.

Example:

```text
A → B
```

meaning:

```text
A occurs before B
```

---

# What Is a Directed Acyclic Graph (DAG)?

A DAG is a directed graph that contains:

✅ Directions

✅ Relationships

❌ No cycles

---

# What Is a Cycle?

A cycle occurs when a node can eventually return to itself.

Example:

```text
A → B → C → A
```

This creates an infinite loop.

Airflow does not allow cyclic workflows.

---

# Valid DAG Example

```text
A
│
├──► B
│
└──► C
      │
      ▼
      D
      │
      ▼
      E
```

This workflow moves forward and never loops back.

---

# DAG Example in a Data Engineering Pipeline

Consider the following workflow:

```text
Extract API Data
        ↓
Remove IP Addresses
        ↓
Validate Database Tables
        ↓
Check Duplicate Records
        ↓
Load Data
        ↓
Execute SQL Query
```

Each step becomes a task inside an Airflow DAG.

---

# Example Mapping

| Node | Activity |
|--------|--------|
| A | Extract data from an API |
| B | Remove IP addresses |
| C | Validate tables |
| D | Check duplicate records |
| E | Load data into a database |
| F | Execute SQL query |

---

# Tasks in Airflow

An Airflow DAG contains individual pieces of work called:

```text
Tasks
```

Examples:

```text
Run SQL Query
Load Data
Send Email
Execute Python Function
Run Spark Job
```

Each task performs one specific action.

---

# What Are Dependencies?

Dependencies define the execution order of tasks.

Example:

```text
Extract
    ↓
Transform
    ↓
Load
```

Dependencies ensure:

```text
Transform cannot run until Extract finishes.
Load cannot run until Transform finishes.
```

---

# Airflow DAG Structure

A DAG consists of:

```text
Tasks
+
Dependencies
+
Scheduling Rules
```

These elements combine to create an automated workflow.

---

# Airflow Operators

An Operator acts as a template for a task.

Think of an operator as:

```text
Task Blueprint
```

Each operator performs a different type of work.

---

# Common Airflow Operators

## BashOperator

Executes a shell command.

Example:

```bash
ls -l
```

---

## PythonOperator

Executes a Python function.

Example:

```python
def my_function():
    pass
```

---

## EmailOperator

Sends email notifications.

Example:

```text
Send Failure Alert
Send Success Notification
```

---

# Operator Summary

| Operator | Purpose |
|-----------|-----------|
| BashOperator | Execute shell commands |
| PythonOperator | Execute Python functions |
| EmailOperator | Send email messages |

---

# Defining an Airflow DAG

An Airflow DAG is simply:

```text
A Python script
```

that contains:

- DAG definition
- Tasks
- Dependencies

---

# Required Imports

Example:

```python
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
```

---

# Why These Imports Matter

## DAG

Creates workflow objects.

```python
from airflow import DAG
```

---

## PythonOperator

Executes Python functions.

```python
PythonOperator
```

---

## datetime

Supports scheduling.

```python
datetime
```

---

# Defining DAG Arguments

Airflow DAGs typically include configuration settings.

Example:

```python
default_args = {
    'owner': 'student1',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['student1@mit.edu'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
```

---

# Common DAG Arguments

## owner

Workflow owner.

Example:

```python
'owner': 'student1'
```

---

## depends_on_past

Determines whether execution depends on a previous run.

```python
True
False
```

---

## start_date

Workflow start date.

Example:

```python
days_ago(2)
```

---

## email

Notification recipient.

Example:

```python
'email': ['student1@mit.edu']
```

---

## retries

Retry attempts after failure.

Example:

```python
'retries': 1
```

---

# Creating a Python Function

Example:

```python
def my_function(x):
    return x + " is a must have tool for Data Engineers."
```

Input:

```python
Apache Airflow
```

Output:

```text
Apache Airflow is a must have tool for Data Engineers.
```

---

# Creating the DAG Object

Example:

```python
dag = DAG(
    'python_operator_sample',
    description='How to use PythonOperator?',
    schedule_interval='0 12 * * *',
    start_date=datetime(2017, 3, 20),
    catchup=False
)
```

---

# DAG Parameters

## dag_id

Unique workflow name.

```python
python_operator_sample
```

---

## description

Workflow explanation.

```python
How to use PythonOperator?
```

---

## schedule_interval

Execution schedule.

```python
0 12 * * *
```

Meaning:

```text
Every day at noon
```

---

## catchup

Controls execution of missed runs.

```python
False
```

prevents historical backfill.

---

# Creating a Task

Example:

```python
t1 = PythonOperator(
    task_id='print',
    python_callable=my_function,
    op_kwargs={"x": "Apache Airflow"},
    dag=dag,
)
```

---

# Parameter Breakdown

## task_id

Task name.

```python
'print'
```

---

## python_callable

Function executed by task.

```python
my_function
```

---

## op_kwargs

Arguments passed into function.

```python
{"x": "Apache Airflow"}
```

---

## dag

Associated DAG object.

```python
dag = dag
```

---

# Expected Output

The task executes:

```python
my_function("Apache Airflow")
```

Result:

```text
Apache Airflow is a must have tool for Data Engineers.
```

---

# Declaring Dependencies

Airflow uses special operators to define execution order.

---

## Run Task A Before Task B

```python
task_a >> task_b
```

Meaning:

```text
task_a executes first
task_b executes second
```

---

## Run Task C After Tasks D and E

```python
task_c << [task_d, task_e]
```

Meaning:

```text
task_d executes first
task_e executes first
task_c executes afterward
```

---

# Dependency Visualization

Example:

```text
Task A
   ↓
Task B
   ↓
Task C
```

Equivalent code:

```python
task_a >> task_b >> task_c
```

---

# Airflow Execution Flow

```text
DAG Definition
       ↓
Scheduler Detects DAG
       ↓
Tasks Queued
       ↓
Tasks Executed
       ↓
Workflow Completes
```

---

# Airflow UI

The Airflow dashboard provides:

- DAG monitoring
- Task status
- Logs
- Manual execution
- Scheduling controls

Common statuses:

```text
Success
Running
Failed
Queued
Skipped
```

---

# Real-World ETL Example

```text
Extract API Data
        ↓
Validate Data
        ↓
Clean Data
        ↓
Load Database
        ↓
Generate Report
```

Each step becomes an Airflow task.

Dependencies define execution order.

---

# Spark and Airflow Together

Example workflow:

```text
Airflow DAG
       ↓
Trigger Spark Job
       ↓
Process Dataset
       ↓
Load Results
       ↓
Send Notification Email
```

### Airflow

Responsible for:

```text
Scheduling
Dependencies
Monitoring
```

### Spark

Responsible for:

```text
Processing
Analytics
Machine Learning
```

---

# Key Takeaways

- DAG stands for Directed Acyclic Graph.
- DAGs are the foundation of Airflow workflows.
- DAGs consist of tasks and dependencies.
- Airflow DAGs are written in Python.
- Operators define the type of task being executed.
- PythonOperator executes Python functions.
- Dependencies control execution order.
- Airflow prevents cycles in workflow definitions.
- DAGs enable reliable workflow automation.

---

# My Notes

## Mental Model

Think of a DAG as:

```text
Workflow Blueprint
```

and tasks as:

```text
Workflow Steps
```

Airflow reads the blueprint and automatically executes the steps in the correct order.

## Data Engineering Perspective

A typical modern pipeline may look like:

```text
Airflow DAG
      ↓
Extract Data
      ↓
Spark Processing
      ↓
Data Warehouse
      ↓
Reporting Dashboard
```

In this architecture:

```text
Airflow manages the process.
Spark performs the computation.
```

---

# Summary

Airflow Directed Acyclic Graphs (DAGs) define workflows through tasks and dependencies. DAGs are written in Python and use operators such as PythonOperator, BashOperator, and EmailOperator to perform work. Dependencies control the execution order, ensuring that tasks run in a predictable and reliable sequence. DAGs serve as the foundation for 