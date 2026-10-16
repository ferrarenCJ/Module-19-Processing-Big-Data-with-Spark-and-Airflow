# Video 19.5: Loading Flight Data into the Spark Docker Container

**Duration:** 02:49

---

# Overview

In this lesson, Dr. Sanchez demonstrates how to load a dataset from a local machine into a Spark Docker container.

After the data file has been copied into the container, Spark can be launched from the command line and used to perform data processing and analytics operations.

This workflow represents a common data engineering task:

```text
Local Data
      ↓
Docker Container
      ↓
Spark Environment
      ↓
Data Processing
      ↓
Analysis
```

---

# Learning Objectives

After completing this lesson, I should be able to:

- Move files from a local machine into a Docker container.
- Identify Spark container names.
- Use Docker commands to interact with containers.
- Start a PySpark session.
- Prepare data for analysis in Spark.
- Understand common workflows for loading data into distributed processing environments.

---

# Why Load Data into Docker?

Spark is running inside a Docker container.

Because the container is isolated from the host operating system, files stored on the local machine are not automatically available inside Spark.

To process local data, files must first be copied into the running container.

---

# Data Loading Workflow

```text
Download Dataset
        ↓
Save on Local Machine
        ↓
Identify Spark Container
        ↓
Copy File into Container
        ↓
Enter Container
        ↓
Launch PySpark
        ↓
Access Dataset
```

---

# Step 1: Download Flight Dataset

The course provides a flight dataset for Spark analysis.

Example:

```text
FlightData.csv
```

Save the file on the local machine.

---

# Step 2: Verify Spark Containers

Check running containers.

```bash
docker ps
```

Example output:

```text
bitnami_spark_1
bitnami_spark-worker-1
```

The Spark Master container will be used for data loading.

---

# Step 3: Copy Dataset into Spark Container

Use the Docker copy command:

```bash
docker cp FlightData.csv bitnami_spark_1:/FlightData.csv
```

### Command Breakdown

```text
docker cp
```

Copies files between:

- Local Machine
- Docker Container

Source:

```text
FlightData.csv
```

Destination:

```text
bitnami_spark_1:/FlightData.csv
```

Result:

```text
Local File
        ↓
Spark Container
```

---

# Step 4: Verify File Exists

Connect to the Spark container.

Example:

```bash
docker exec -it bitnami_spark_1 bash
```

List files:

```bash
ls
```

Verify:

```text
FlightData.csv
```

appears in the directory listing.

---

# Step 5: Start PySpark

Inside the Spark container:

```bash
/opt/spark/bin/pyspark
```

Expected output:

```text
SparkSession available as 'spark'
```

This indicates Spark is running successfully.

---

# SparkSession

Spark automatically creates:

```python
spark
```

This object serves as the entry point for Spark functionality.

Example:

```python
spark
```

returns:

```text
SparkSession
```

---

# Why SparkSession Matters

SparkSession provides access to:

- DataFrames
- SQL Queries
- File Operations
- Streaming
- Machine Learning

Most Spark workloads begin with:

```python
spark.read
```

or

```python
spark.sql()
```

---

# Flight Data Analysis Workflow

After loading the file:

```text
FlightData.csv
          ↓
spark.read
          ↓
DataFrame
          ↓
Filtering
          ↓
Aggregation
          ↓
Analysis
```

This workflow will be used in upcoming coding activities.

---

# Common Docker Commands

## Display Running Containers

```bash
docker ps
```

---

## Copy File into Container

```bash
docker cp FlightData.csv bitnami_spark_1:/FlightData.csv
```

---

## Open Container Shell

```bash
docker exec -it bitnami_spark_1 bash
```

---

## Launch PySpark

```bash
/opt/spark/bin/pyspark
```

---

# Practical Use Case

Data engineers often load data into Spark environments from:

- CSV files
- Databases
- Data Lakes
- Cloud Storage
- API Exports
- Streaming Sources

Examples:

```text
AWS S3
Azure Data Lake
Google Cloud Storage
Oracle Databases
PostgreSQL
SQL Server
```

The process demonstrated in this lesson is a simplified version of real-world enterprise data ingestion.

---

# Key Takeaways

- Spark runs inside a Docker container.
- Local files must be copied into the container before Spark can use them.
- The `docker cp` command transfers files into containers.
- The `docker exec` command opens a shell inside a running container.
- PySpark is launched using:

```bash
/opt/spark/bin/pyspark
```

- Spark automatically creates a SparkSession object.
- SparkSession is the entry point for Spark processing.
- Data loading is the first step in any analytics workflow.

---

# My Notes

## Connection to Data Engineering

This lesson introduces the ingestion phase of a data pipeline.

General data engineering process:

```text
Source Data
      ↓
Ingestion
      ↓
Storage
      ↓
Transformation
      ↓
Analytics
      ↓
Reporting
```

The Docker copy operation represents the ingestion step.

---

## Preparing for Coding Activity 19.2

This lesson directly supports:

### Coding Activity 19.2

Loading Data into a Spark Docker Container

Key skills needed:

- Docker file management
- Navigating containers
- Starting PySpark
- Verifying datasets
- Preparing DataFrames

These skills will be required for subsequent Spark query exercises and the final module assignment.

---

# Commands Reference

```bash
docker ps
```

```bash
docker cp FlightData.csv bitnami_spark_1:/FlightData.csv
```

```bash
docker exec -it bitnami_spark_1 bash
```

```bash
ls
```

```bash
/opt/spark/bin/pyspark
```

```python
spark
```

---

# Summary

In Video 19.5, Spark data ingestion is introduced using Docker containers. The lesson demonstrates how to copy files from the local machine into the Spark container, verify that the data exists inside the container, and launch a PySpark session. These foundational skills prepare the environment for querying and analyzing flight data in the upcoming coding activities.