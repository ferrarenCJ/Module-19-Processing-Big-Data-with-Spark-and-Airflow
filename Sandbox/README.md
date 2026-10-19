# Module 19 Sandbox

## Purpose

This Sandbox folder contains reference code, experiments, notes, and supporting files created while working through Module 19: Processing Big Data with Spark and Airflow.

The sandbox environment serves as a safe workspace for testing concepts, validating code examples, and preserving useful reference materials outside of the formal coding activities and assignments.

---

# Folder Structure

```text
Sandbox
│
├── Airflow
├── Code
│   ├── airflow_dag_reference.py
│   └── pyspark_queries.py
│
├── Docker
├── PySpark
├── Spark
└── README.md
```

---

# Contents

## Airflow

Contains materials related to Apache Airflow, including:

- DAG examples
- Operator references
- Workflow examples
- Scheduling notes
- Airflow experimentation files

---

## Docker

Contains Docker-related resources used throughout the module.

Examples include:

- Docker commands
- Docker Compose examples
- Container management notes
- Environment setup references

---

## PySpark

Contains PySpark reference material and sample code.

Topics include:

- SparkSession creation
- DataFrame operations
- Data loading
- Query execution
- Data exploration

---

## Spark

Contains general Apache Spark notes and examples.

Topics include:

- Spark architecture
- Spark Core
- Spark SQL
- Spark Sessions
- Distributed processing concepts

---

## Code

The Code directory contains reusable reference scripts created during Module 19.

### airflow_dag_reference.py

Purpose:

Provide a reusable Airflow DAG example demonstrating:

- DAG creation
- Task definition
- PythonOperator usage
- Workflow execution

Key Concepts:

- Directed Acyclic Graphs (DAGs)
- Tasks
- Operators
- Scheduling
- Workflow orchestration

Example Topics:

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
```

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

---

### pyspark_queries.py

Purpose:

Provide reusable Spark SQL and PySpark query examples used throughout the module.

Key Concepts:

- Spark Sessions
- DataFrames
- Temporary Views
- Spark SQL Queries

Example Topics:

```python
from pyspark.sql import SparkSession
```

```python
spark = SparkSession.builder \
    .appName("Module19") \
    .getOrCreate()
```

```python
df.createOrReplaceTempView("assignment19_3_table")
```

Example Queries:

```python
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE distance < 200
LIMIT 10
""").show()
```

```python
spark.sql("""
SELECT *
FROM assignment19_3_table
WHERE distance > 600
LIMIT 10
""").show()
```

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

# Skills Practiced

The sandbox was used to reinforce the following concepts:

## Apache Spark

- SparkSession creation
- DataFrame creation
- CSV file ingestion
- Temporary views
- Spark SQL
- Data analysis

## Apache Airflow

- DAG creation
- Task configuration
- PythonOperator implementation
- Workflow execution
- Log analysis

## Docker

- Container deployment
- Container administration
- Networking
- Service management

---

# Practical Uses

The sandbox serves as a reusable reference library for future projects involving:

- Apache Spark
- PySpark
- Apache Airflow
- Docker
- Workflow orchestration
- ETL development
- Data engineering

By preserving working examples and tested code, future development efforts can be accelerated while reducing troubleshooting and setup time.

---

# Key Takeaways

- Keep reusable code examples organized.
- Preserve working Spark and Airflow configurations.
- Use sandbox environments to experiment safely.
- Store frequently used commands and templates for future reference.
- Build a personal knowledge repository to support continued learning and project development.

---

# Related Module 19 Artifacts

This sandbox supports the following Module 19 deliverables:

- Self-Study Discussion 19.1
- Discussion 19.3
- Coding Activity 19.1
- Coding Activity 19.2
- Coding Activity 19.3
- Coding Activity 19.4
- Final Assignment 19.1
- Module 19 Cheat Sheet
- Module 19 Glossary

---

# Summary

The Sandbox folder serves as a personal development and experimentation environment for Module 19. It contains reference implementations, reusable Spark and Airflow examples, Docker resources, and supporting notes that can be leveraged in future coursework and real-world data engineering projects.