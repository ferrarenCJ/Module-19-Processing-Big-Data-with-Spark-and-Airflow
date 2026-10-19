# Module 19 Knowledge Checks

## Processing Big Data with Spark and Airflow

This folder contains notes and summaries from the knowledge checks completed throughout Module 19. The knowledge checks reinforced key concepts related to Apache Spark, PySpark, Apache Airflow, Docker, distributed computing, and workflow orchestration.

---

# Purpose

The purpose of the knowledge checks was to:

- Verify understanding of module concepts
- Reinforce key terminology
- Assess comprehension of Spark and Airflow architecture
- Prepare for coding activities and assignments
- Support long-term retention of data engineering concepts

---

# Topics Covered

## Big Data Processing

Knowledge checks introduced the challenges associated with processing large volumes of data and the importance of distributed computing.

### Key Concepts

- Big Data
- Distributed Computing
- Parallel Processing
- Scalability
- Fault Tolerance

### Key Takeaway

Large datasets require distributed processing frameworks capable of dividing workloads across multiple computing resources.

---

# Apache Spark

Knowledge checks focused on understanding Spark as a distributed data processing platform.

### Topics Covered

- Spark Architecture
- Spark Core
- Spark Session
- DataFrames
- Spark SQL
- Cluster Computing

### Key Takeaways

- Spark is designed for large-scale data processing.
- Spark supports parallel execution.
- Spark provides high-performance analytics.
- Spark supports multiple programming languages.

---

# Spark Session

Knowledge checks reinforced the importance of Spark Sessions.

### Definition

A Spark Session is the entry point for all Spark functionality.

### Example

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Module19") \
    .getOrCreate()
```

### Key Takeaway

A Spark Session must be created before working with DataFrames or Spark SQL.

---

# DataFrames

Knowledge checks covered DataFrames as Spark's primary structured data object.

### Common Operations

```python
df.show()
```

```python
df.printSchema()
```

```python
df.count()
```

### Key Takeaways

- DataFrames organize structured data.
- DataFrames support analytical operations.
- DataFrames integrate directly with Spark SQL.

---

# Spark SQL

Knowledge checks evaluated understanding of querying data using Spark SQL.

### Example

```python
spark.sql("""
SELECT *
FROM flight_delays
LIMIT 10
""").show()
```

### Key Takeaways

- Spark SQL allows SQL queries against DataFrames.
- Temporary views enable SQL-based analysis.
- SQL remains a valuable skill within Spark environments.

---

# PySpark

Knowledge checks reinforced how Python is used with Spark.

### Topics Covered

- SparkSession
- DataFrames
- SQL Queries
- Data Processing

### Key Takeaway

PySpark enables distributed analytics using familiar Python syntax.

---

# Apache Airflow

Knowledge checks introduced Airflow as a workflow orchestration platform.

### Topics Covered

- DAGs
- Tasks
- Operators
- Scheduling
- Monitoring

### Key Takeaways

- Airflow automates workflows.
- Airflow manages task dependencies.
- Airflow simplifies scheduling and monitoring.

---

# Directed Acyclic Graphs (DAGs)

Knowledge checks reinforced DAG fundamentals.

### Definition

A Directed Acyclic Graph (DAG) defines a workflow in Airflow.

### Responsibilities

- Define tasks
- Define dependencies
- Define execution order
- Define schedules

### Key Takeaway

Every Airflow workflow is built around a DAG.

---

# Tasks and Operators

Knowledge checks covered the relationship between tasks and operators.

## Task

A task represents a single unit of work.

Examples include:

- Execute Python code
- Run SQL queries
- Send notifications
- Trigger processing jobs

## Operator

An operator defines how a task is executed.

Examples include:

- PythonOperator
- BashOperator
- EmailOperator

### Key Takeaway

Operators define behavior while tasks represent the work being performed.

---

# PythonOperator

Knowledge checks reinforced the use of PythonOperator within Airflow workflows.

### Example

```python
def square(x):
    return x * x
```

```python
task = PythonOperator(
    task_id="square",
    python_callable=square,
    op_kwargs={"x": 13},
    dag=dag
)
```

### Key Takeaway

PythonOperator allows Python functions to be integrated directly into Airflow workflows.

---

# Workflow Scheduling

Knowledge checks covered scheduling concepts in Airflow.

### Concepts

- Scheduled execution
- Recurring workflows
- CRON expressions
- Task timing

### Example

```python
schedule_interval="0 12 * * *"
```

### Key Takeaway

Airflow uses scheduling mechanisms to automate workflow execution.

---

# Docker Concepts

Knowledge checks reinforced Docker fundamentals used throughout the module.

### Topics Covered

- Containers
- Docker Compose
- Container Management
- Environment Deployment

### Key Takeaways

- Docker simplifies deployment.
- Containers provide consistent environments.
- Docker improves reproducibility.

---

# Relationship Between Spark and Airflow

## Apache Spark

Responsible for:

- Processing data
- Transforming data
- Performing analytics

## Apache Airflow

Responsible for:

- Scheduling workflows
- Managing dependencies
- Monitoring workflow execution

### Key Takeaway

Spark processes data while Airflow manages and automates the workflow surrounding that processing.

---

# Common Knowledge Check Themes

Recurring themes throughout the module included:

- Scalability
- Automation
- Workflow orchestration
- Distributed processing
- Data transformation
- Parallel execution
- Containerization

---

# Practical Skills Reinforced

The knowledge checks helped reinforce the ability to:

- Identify Spark components
- Understand distributed computing concepts
- Explain Spark Sessions and DataFrames
- Write and interpret Spark SQL queries
- Understand DAG structures
- Identify Airflow tasks and operators
- Explain workflow orchestration
- Understand Docker deployment concepts

---

# Exam Preparation Notes

Important concepts to remember:

- Spark is a distributed computing framework.
- PySpark is the Python interface for Spark.
- Spark Session is required before Spark operations.
- DataFrames are Spark's primary structured data object.
- Spark SQL enables SQL-based analytics.
- Airflow automates workflows.
- DAGs define workflow structure.
- Tasks perform individual units of work.
- Operators determine task behavior.
- Docker provides containerized environments.

---

# Key Takeaways

- Apache Spark enables scalable data processing.
- PySpark supports Python-based analytics.
- Spark SQL combines SQL with distributed computing.
- Apache Airflow automates workflow execution.
- DAGs are the foundation of Airflow workflows.
- Docker simplifies deployment and environment management.
- Spark and Airflow are commonly used together in modern data engineering environments.

---

# Summary

The Module 19 knowledge checks reinforced the fundamental concepts of Apache Spark and Apache Airflow through short assessments and concept reviews. These exercises strengthened understanding of distributed computing, workflow automation, Spark SQL, DataFrames, DAGs, Operators, and Docker while helping prepare for the hands-on coding activities and final assignment.