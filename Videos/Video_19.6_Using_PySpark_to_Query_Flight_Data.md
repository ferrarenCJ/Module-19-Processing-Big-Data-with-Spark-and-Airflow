# Video 19.6: Using PySpark to Query Flight Data

**Duration:** 07:29

---

# Overview

In this lesson, Dr. Sanchez demonstrates how to use PySpark to load and analyze flight delay data.

Spark supports multiple programming languages, including:

- Python
- SQL
- Scala
- Java
- R

Through PySpark, data engineers can combine the power of Python and SQL while leveraging Spark's distributed processing capabilities.

The video uses the **Departure Delays** dataset to demonstrate:

- Loading CSV data into Spark
- Creating DataFrames
- Creating temporary SQL views
- Running SQL queries against flight data
- Performing aggregations and filtering

---

# Learning Objectives

After completing this lesson, I should be able to:

- Create a SparkSession.
- Load CSV data into a Spark DataFrame.
- Create temporary views for SQL access.
- Query data using Spark SQL.
- Filter and analyze flight records.
- Perform aggregations using SQL functions.
- Combine Python and SQL within Spark workflows.

---

# Spark and PySpark

## Apache Spark

Spark is a distributed analytics engine designed for:

- Large-scale analytics
- Distributed processing
- In-memory computation
- Machine learning
- Streaming analytics

---

## PySpark

PySpark is the Python API for Spark.

Benefits:

- Familiar Python syntax
- Distributed execution
- Scalability
- Integration with Spark SQL

Example:

```python
from pyspark.sql import SparkSession
```

---

# Dataset Used

## Departure Delays

The video uses:

```text
departuredelays.csv
```

Dataset contains flight information including:

- Date
- Delay
- Distance
- Origin Airport
- Destination Airport

Example:

```text
date,delay,distance,origin,destination
```

---

# Creating a Spark Session

The first step is creating a SparkSession.

Example:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DepartureDelays") \
    .getOrCreate()
```

---

# Why SparkSession Is Important

SparkSession serves as the main entry point for Spark functionality.

Provides access to:

- DataFrames
- SQL Queries
- Streaming
- Machine Learning
- File Operations

Most Spark programs begin with:

```python
spark
```

---

# Loading CSV Data

Read the CSV file into a DataFrame.

```python
csv_file = "/departuredelays.csv"

df = spark.read.format("csv") \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .load(csv_file)
```

---

# DataFrame Creation

Result:

```python
df
```

returns:

```text
DataFrame
```

The DataFrame becomes Spark's distributed representation of the file.

---

# Creating a Temporary View

To use SQL, create a temporary view:

```python
df.createOrReplaceTempView("delays_table")
```

This allows SQL queries to run against the DataFrame.

Think of this as creating a virtual table:

```text
departuredelays.csv
        ↓
DataFrame
        ↓
delays_table
```

---

# Query Example 1

## Flights Over 1,000 Miles

```python
spark.sql("""
SELECT
    distance,
    origin,
    destination
FROM delays_table
WHERE distance > 1000
ORDER BY distance DESC
""").show(10)
```

---

## Purpose

Retrieve:

- Distance
- Origin Airport
- Destination Airport

For flights:

```text
distance > 1000
```

Sorted by:

```text
distance DESC
```

---

## Example Result

```text
distance origin destination
4330     HNL    JFK
```

---

# Query Example 2

## Long Delays from SFO to ORD

```python
spark.sql("""
SELECT *
FROM delays_table
WHERE delay > 120
  AND origin = 'SFO'
  AND destination = 'ORD'
ORDER BY delay DESC
""").show(10)
```

---

## Purpose

Identify:

- Flights from SFO
- Flights to ORD
- Delays greater than 120 minutes

Sorted by:

```text
delay DESC
```

---

# Example Analysis

Potential use cases:

- Airline performance monitoring
- Route optimization
- Operational reporting
- Delay trend analysis

---

# Query Example 3

## Categorizing Delays

Spark SQL supports CASE expressions.

Example:

```python
spark.sql("""
SELECT
    delay,
    origin,
    destination,
    CASE
        WHEN delay > 360 THEN 'Very Long Delays'
        WHEN delay BETWEEN 120 AND 360 THEN 'Long Delays'
        WHEN delay BETWEEN 60 AND 120 THEN 'Short Delays'
        WHEN delay BETWEEN 0 AND 60 THEN 'Tolerable Delays'
        WHEN delay = 0 THEN 'No Delays'
        ELSE 'Early'
    END AS delay_length
FROM delays_table
""").show(10)
```

---

# Delay Categories

| Delay Range | Category |
|------------|------------|
| > 360 | Very Long Delays |
| 120 - 360 | Long Delays |
| 60 - 120 | Short Delays |
| 0 - 60 | Tolerable Delays |
| 0 | No Delays |
| < 0 | Early |

---

# Business Value

Categorizing delays allows:

- Operational analysis
- Executive reporting
- KPI monitoring
- Flight performance tracking

---

# Aggregate Functions

Spark SQL supports standard SQL aggregations.

---

## Maximum Delay

```python
spark.sql("""
SELECT MAX(delay) AS max_delay
FROM delays_table
""").show()
```

Example:

```text
1642
```

---

## Minimum Delay

```python
spark.sql("""
SELECT MIN(delay) AS min_delay
FROM delays_table
""").show()
```

Example:

```text
-112
```

---

# Why Spark SQL Matters

Spark SQL allows data engineers to:

- Reuse SQL skills
- Work on very large datasets
- Combine SQL with Python
- Build scalable analytics solutions

This makes Spark highly accessible to professionals with database backgrounds.

---

# Spark Processing Workflow

```text
CSV File
    ↓
Spark DataFrame
    ↓
Temporary View
    ↓
SQL Queries
    ↓
Analysis
    ↓
Insights
```

---

# Key Takeaways

- Spark supports both Python and SQL.
- PySpark allows distributed processing using Python syntax.
- Spark DataFrames are distributed collections of structured data.
- Temporary views allow DataFrames to be queried using SQL.
- Spark SQL supports filtering, sorting, aggregations, and CASE statements.
- SQL and Python can be combined to create scalable analytics solutions.
- Spark makes large-scale data analysis easier for data engineers and analysts.

---

# Connection to Coding Activity 19.2

The entire workflow demonstrated in this video matches the steps completed in Coding Activity 19.2:

1. Create SparkSession
2. Load CSV Data
3. Create DataFrame
4. Create Temporary View
5. Execute SQL Queries
6. Analyze Results

---

# Real-World Applications

Spark SQL is commonly used for:

- Data Warehouses
- Data Lakes
- Business Intelligence
- ETL Pipelines
- Cloud Analytics
- Machine Learning Feature Engineering

Platforms include:

- AWS EMR
- Databricks
- Azure Synapse
- Snowflake Integrations
- Hadoop Ecosystems

---

# My Notes

## Connection to Data Engineering

As a Data Engineer, Spark SQL provides a familiar SQL interface while allowing queries to scale across distributed infrastructure.

The workflow is very similar to:

```text
CSV
   ↓
Spark
   ↓
DataFrame
   ↓
SQL View
   ↓
Analytics
```

but can operate against datasets much larger than what traditional databases can efficiently manage.

## Key Concept

One of Spark's greatest strengths is allowing data engineers to combine:

- Python Programming
- SQL Querying
- Distributed Computing

within a single processing framework.