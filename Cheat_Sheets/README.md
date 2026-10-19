# Module 19 Cheat Sheets

## Processing Big Data with Spark and Airflow

This folder contains quick-reference materials created during Module 19. These cheat sheets summarize important concepts, commands, examples, and workflows related to Apache Spark, PySpark, Apache Airflow, and Docker.

---

## Purpose

The cheat sheets were created to:

- Summarize key concepts
- Store commonly used commands
- Provide reusable examples
- Support assignments and coding activities
- Create a reference library for future projects

---

## Topics Covered

### Apache Spark

- Spark Architecture
- Spark Core
- Spark Sessions
- DataFrames
- Spark SQL
- Distributed Processing

### PySpark

- Data Loading
- DataFrame Operations
- Query Execution
- Data Analysis

### Apache Airflow

- DAGs
- Tasks
- Operators
- Scheduling
- Monitoring

### Docker

- Container Management
- Docker Compose
- Environment Deployment

---

## Spark Quick Reference

### Import SparkSession

from pyspark.sql import SparkSession

### Create Spark Session

spark = SparkSession.builder \
    .appName("Module19") \
    .getOrCreate()

### Start PySpark

/opt/spark/bin/pyspark

---

## DataFrame Operations

### Load CSV File

Load departuredelays.csv into a Spark DataFrame.

### Display Data

df.show()

### Display Schema

df.printSchema()

### Count Records

df.count()

---

## Spark SQL

### Create Temporary View

df.createOrReplaceTempView("flight_delays")

### Run Query

Query records using Spark SQL against temporary views.

### Common Operations

- Filtering
- Record Counts
- Data Exploration
- Conditional Queries

---

## Sample Queries

### Flights from PHL to DFW with Delays Greater Than 150 Minutes

Filter records by origin, destination, and delay value.

### Flights Less Than 200 Miles

Filter records by distance less than 200.

### Flights Greater Than 600 Miles

Filter records by distance greater than 600.

---

## Airflow Quick Reference

### Core Components

- DAG
- Task
- Operator
- Scheduler
- Webserver

### PythonOperator

Used to execute Python functions inside Airflow workflows.

### Workflow Monitoring

Monitor:

- Success
- Running
- Failed
- Queued
- Skipped

---

## Airflow Login

Default Username:

airflow

Default Password:

airflow

Default URL:

http://localhost:8080

---

## Docker Quick Reference

### Start Containers

docker compose up

### Run in Background

docker compose up -d

### Stop Containers

docker compose down

### View Running Containers

docker ps

### View All Containers

docker ps -a

---

## Spark Concepts

### Spark Session

Entry point into Spark functionality.

### DataFrame

Primary structured data object within Spark.

### Spark SQL

SQL engine used for analytical queries.

### Spark Core

Responsible for scheduling and task execution.

---

## Airflow Concepts

### DAG

Defines workflow structure and execution order.

### Task

Represents a unit of work.

### Operator

Defines task behavior.

### Scheduler

Controls when workflows run.

---

## Spark and Airflow

Spark is responsible for:

- Data Processing
- Transformations
- Analytics

Airflow is responsible for:

- Scheduling
- Workflow Orchestration
- Monitoring

Together they support automated data engineering pipelines.

---

## Skills Reinforced

- Spark Fundamentals
- PySpark Development
- Spark SQL
- Workflow Automation
- DAG Creation
- Docker Administration
- Data Engineering Best Practices

---

## Key Takeaways

- Spark enables distributed data processing.
- PySpark provides Python integration.
- Spark SQL supports large-scale analytics.
- Airflow automates workflows.
- Docker simplifies deployment.
- Spark and Airflow are commonly used together in modern data engineering solutions.

---

## Summary

The cheat sheets provide a quick-reference guide for Apache Spark, PySpark, Apache Airflow, and Docker. They support coursework, assignments, and future data engineering projects by consolidating frequently used concepts and commands in a single location.