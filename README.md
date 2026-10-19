# Module 19: Processing Big Data with Spark and Airflow

## Overview

Module 19 introduced two foundational technologies used in modern data engineering:

- Apache Spark for distributed data processing and analytics
- Apache Airflow for workflow orchestration and automation

Through a combination of hands-on activities, discussions, self-study, and a comprehensive final assignment, this module provided practical experience deploying, configuring, and using Spark and Airflow in containerized environments.

---

# Learning Objectives

By completing Module 19, I was able to:

- Understand the fundamentals of distributed data processing
- Deploy and manage Apache Spark using Docker
- Use PySpark to process structured datasets
- Create and manipulate Spark DataFrames
- Execute Spark SQL queries
- Understand Airflow architecture and workflow orchestration concepts
- Create Directed Acyclic Graphs (DAGs)
- Implement PythonOperator tasks
- Execute and monitor Airflow workflows
- Analyze workflow logs and troubleshoot execution issues

---

# Module Components

## Discussions

### Self-Study Discussion 19.1

**Topic:** Thinking Like a Data Scientist: Processing Big Data with Spark and Airflow

Key Contributions:

- Shared official Spark documentation resources
- Shared official Airflow documentation resources
- Discussed Docker troubleshooting tips
- Reflected on strengths and improvement opportunities for the module

---

### Discussion 19.3

**Topic:** Big Data Processing and Workflow Automation

Topics Explored:

- Distributed computing concepts
- Spark processing capabilities
- Workflow orchestration
- Enterprise data engineering use cases

---

## Coding Activities

### Coding Activity 19.1

**Spark Docker Environment Setup**

Topics Covered:

- Docker Compose
- Spark containers
- Environment setup
- Container management

Skills Developed:

- Starting Spark services
- Verifying container health
- Connecting to Spark containers

---

### Coding Activity 19.2

**PySpark Fundamentals**

Topics Covered:

- SparkSession
- PySpark
- DataFrames

Skills Developed:

- Creating Spark sessions
- Loading structured datasets
- Working with DataFrames

---

### Coding Activity 19.3

**Spark SQL Data Analysis**

Topics Covered:

- Temporary views
- Spark SQL
- Query execution
- Data exploration

Skills Developed:

- Using SQL against DataFrames
- Filtering records
- Retrieving analytical results

---

### Coding Activity 19.4

**Apache Airflow Fundamentals**

Topics Covered:

- Airflow deployment
- DAG creation
- Task scheduling
- Workflow execution

Skills Developed:

- Creating DAGs
- Building PythonOperator tasks
- Monitoring workflow execution
- Reviewing task logs

---

# Final Assignment 19.1

## Part 1: Apache Spark

The first portion of the assignment focused on loading and analyzing flight delay data using PySpark.

### Activities Completed

- Deployed Spark using Docker
- Copied dataset into the Spark container
- Launched PySpark
- Created a Spark session
- Loaded a CSV file into a DataFrame
- Created a temporary SQL view
- Executed Spark SQL queries

### Dataset

```text
departuredelays.csv
```

### Queries Performed

#### Flights from PHL to DFW with Delays Greater Than 150 Minutes

```sql
SELECT *
FROM assignment19_3_table
WHERE origin = 'PHL'
  AND destination = 'DFW'
  AND delay > 150
LIMIT 15
```

#### Flights with Distance Less Than 200 Miles

```sql
SELECT *
FROM assignment19_3_table
WHERE distance < 200
LIMIT 10
```

#### Flights with Distance Greater Than 600 Miles

```sql
SELECT *
FROM assignment19_3_table
WHERE distance > 600
LIMIT 10
```

---

## Part 2: Apache Airflow

The second portion of the assignment focused on workflow creation and execution using Airflow.

### Activities Completed

- Downloaded Airflow Docker Compose configuration
- Disabled example DAGs
- Deployed Airflow services
- Accessed the Airflow user interface
- Created a custom DAG
- Configured a PythonOperator task
- Executed the workflow successfully
- Reviewed execution logs

### Custom DAG

```python
def square(x):
    return x * x
```

### Workflow Task

```python
t1 = PythonOperator(
    task_id='square',
    python_callable=square,
    op_kwargs={'x': 13},
    dag=dag
)
```

### Expected Result

```text
13 × 13 = 169
```

### Workflow Result

```text
Done. Returned value was: 169
```

---

# Technologies Used

## Apache Spark

Used For:

- Distributed computing
- Data transformation
- Data analysis
- SQL processing

Primary Components:

- Spark Core
- Spark SQL
- SparkSession
- DataFrames
- PySpark

---

## Apache Airflow

Used For:

- Workflow orchestration
- Scheduling
- Automation
- Monitoring

Primary Components:

- DAGs
- Tasks
- Operators
- Scheduler
- Webserver

---

## Docker

Used For:

- Environment deployment
- Container management
- Platform consistency
- Service isolation

---

# Key Concepts Learned

## Apache Spark

Apache Spark is an open-source distributed computing framework that enables high-speed data processing and analytics across large datasets.

### Key Benefits

- Scalability
- Parallel processing
- Fault tolerance
- Multi-language support

---

## PySpark

PySpark provides a Python interface for Apache Spark and allows developers to work with distributed datasets using Python.

### Common Tasks

- Create Spark sessions
- Load datasets
- Build DataFrames
- Execute SQL queries

---

## Spark SQL

Spark SQL enables SQL-based analysis of structured data stored within Spark DataFrames.

### Common Uses

- Record filtering
- Aggregations
- Joins
- Data exploration

---

## Apache Airflow

Apache Airflow is a workflow orchestration platform used to automate and monitor recurring data processing workflows.

### Common Uses

- ETL orchestration
- Scheduling jobs
- Dependency management
- Monitoring task execution

---

## Directed Acyclic Graph (DAG)

A DAG defines:

- Workflow structure
- Task relationships
- Execution order
- Scheduling behavior

---

# Practical Skills Developed

Throughout Module 19, I learned how to:

- Deploy Spark using Docker
- Manage containerized environments
- Launch and use PySpark
- Create Spark sessions
- Build Spark DataFrames
- Query data using Spark SQL
- Deploy Airflow services
- Create and configure DAGs
- Implement PythonOperator tasks
- Execute workflows
- Review Airflow logs
- Troubleshoot deployment and execution issues

---

# Real-World Applications

The technologies and concepts covered in this module are commonly used in:

- ETL pipelines
- Data warehousing
- Business intelligence
- Enterprise analytics
- Cloud data platforms
- Workflow automation
- Machine learning pipelines
- Streaming data processing
- Enterprise data engineering

---

# Key Takeaways

- Apache Spark provides scalable distributed data processing.
- PySpark enables distributed analytics using Python.
- Spark SQL allows SQL-based access to DataFrames.
- Apache Airflow automates and orchestrates workflows.
- Docker simplifies deployment and environment management.
- Spark and Airflow are commonly used together in production data engineering environments.
- Workflow automation improves repeatability, reliability, and operational efficiency.

---

# Module Reflection

This module was particularly effective because it combined theory with extensive hands-on practice. The Docker-based labs provided practical experience deploying enterprise-grade technologies while the assignments reinforced concepts through real-world scenarios. Working directly with Spark and Airflow helped bridge the gap between conceptual learning and practical implementation.

The most valuable takeaway from this module was understanding how Spark and Airflow complement each other within modern data engineering architectures. Spark provides scalable data processing capabilities, while Airflow orchestrates and automates the execution of those processing tasks within larger workflows.

---

# Conclusion

Module 19 provided a comprehensive introduction to big data processing and workflow orchestration using Apache Spark and Apache Airflow. Through discussions, coding activities, and a capstone assignment, I gained practical experience working with distributed computing and automated workflows in containerized environments. The skills acquired in this module form a strong foundation for building scalable and maintainable data engineering solutions.

---

# Module Completion Checklist

## Discussions

- [x] Self-Study Discussion 19.1
- [x] Discussion 19.3

## Coding Activities

- [x] Coding Activity 19.1
- [x] Coding Activity 19.2
- [x] Coding Activity 19.3
- [x] Coding Activity 19.4

## Final Assignment

- [x] Part 1 - PySpark
- [x] Part 2 - Airflow

## Documentation

- [x] Glossary
- [x] Cheat Sheet
- [x] Coding Activities README
- [x] Module README

✅ **Module 19 Successfully Completed**