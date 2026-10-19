# Module 19 Wrap-Up

## Processing Big Data with Spark and Airflow

Module 19 focused on two essential technologies used in modern data engineering:

- Apache Spark
- Apache Airflow

Throughout this module, I gained both theoretical knowledge and practical experience working with distributed data processing and workflow orchestration. Through discussions, coding activities, self-study exercises, and the final assignment, I learned how these technologies work independently and together to support scalable data engineering solutions.

---

# Module Objectives

By the end of this module, I was able to:

- Understand distributed computing concepts
- Deploy Apache Spark using Docker
- Work with PySpark and Spark Sessions
- Create and analyze Spark DataFrames
- Execute SQL queries using Spark SQL
- Understand Apache Airflow architecture
- Create and configure Directed Acyclic Graphs (DAGs)
- Implement PythonOperator tasks
- Execute and monitor workflows
- Review workflow execution logs

---

# Topics Covered

## Big Data Processing

The module introduced the challenges associated with processing large datasets and demonstrated how distributed computing frameworks help overcome these limitations.

Key topics included:

- Distributed processing
- Parallel execution
- Scalability
- Fault tolerance
- Performance optimization

---

## Apache Spark

Apache Spark was introduced as a distributed analytics engine designed for large-scale data processing.

### Spark Concepts Studied

- Spark Architecture
- Spark Core
- Spark Sessions
- DataFrames
- Spark SQL
- Distributed Execution

### Practical Activities

- Creating Spark Sessions
- Loading CSV files
- Creating DataFrames
- Running Spark SQL queries
- Analyzing flight delay data

---

## PySpark

PySpark provided the ability to use Python with Spark.

### Topics Covered

- SparkSession
- Data Loading
- DataFrames
- Data Exploration
- Spark SQL Integration

### Sample Tasks

```python
from pyspark.sql import SparkSession
```

```python
spark = SparkSession.builder \
    .appName("Module19") \
    .getOrCreate()
```

---

## Spark SQL

Spark SQL allowed SQL queries to be executed against DataFrames.

### Benefits

- Familiar SQL syntax
- Structured data analysis
- Scalable query execution

### Sample Query

```sql
SELECT *
FROM assignment19_3_table
WHERE distance > 600
LIMIT 10
```

---

## Apache Airflow

Apache Airflow was introduced as a workflow orchestration platform.

### Topics Covered

- DAGs
- Tasks
- Operators
- Scheduling
- Workflow Monitoring

### Benefits

- Workflow automation
- Dependency management
- Scheduling
- Monitoring

---

## Directed Acyclic Graphs (DAGs)

DAGs form the foundation of Airflow workflows.

A DAG defines:

- Workflow structure
- Task dependencies
- Execution order
- Scheduling behavior

### Example

```python
dag = DAG(
    "python_square_operator",
    description="Squaring a number using Airflow"
)
```

---

## PythonOperator

The PythonOperator enables Python code execution within Airflow workflows.

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

---

# Module Activities Completed

## Discussions

Completed:

- Self-Study Discussion 19.1
- Discussion 19.3

Topics included:

- Spark learning resources
- Airflow learning resources
- Big data processing
- Workflow automation
- Data engineering best practices

---

## Coding Activities

Completed:

- Coding Activity 19.1
- Coding Activity 19.2
- Coding Activity 19.3
- Coding Activity 19.4

Skills developed:

- Docker deployment
- Spark setup
- PySpark analysis
- Spark SQL
- Airflow deployment
- DAG creation

---

## Final Assignment

Successfully completed Final Assignment 19.1.

### Part 1: Apache Spark

Activities included:

- Deploying Spark containers
- Loading flight delay data
- Creating DataFrames
- Building temporary views
- Executing Spark SQL queries

### Queries Performed

```sql
SELECT *
FROM assignment19_3_table
WHERE origin = 'PHL'
  AND destination = 'DFW'
  AND delay > 150
LIMIT 15
```

```sql
SELECT *
FROM assignment19_3_table
WHERE distance < 200
LIMIT 10
```

```sql
SELECT *
FROM assignment19_3_table
WHERE distance > 600
LIMIT 10
```

---

### Part 2: Apache Airflow

Activities included:

- Deploying Airflow containers
- Creating a custom DAG
- Configuring a PythonOperator
- Executing workflow tasks
- Reviewing Airflow logs

### Workflow Result

```text
13 × 13 = 169
```

Log Output:

```text
Done. Returned value was: 169
```

```text
Marking task as SUCCESS
```

---

# Key Concepts Learned

## Apache Spark

Learned how Spark provides:

- Distributed computing
- Parallel processing
- Data transformation
- Large-scale analytics

---

## PySpark

Learned how to:

- Create Spark Sessions
- Load structured data
- Create DataFrames
- Execute Spark SQL queries

---

## Apache Airflow

Learned how to:

- Create workflows
- Schedule tasks
- Manage dependencies
- Monitor execution

---

## Docker

Learned how Docker simplifies:

- Application deployment
- Environment consistency
- Container management
- Development workflows

---

# Practical Skills Developed

Through this module I developed practical experience with:

- Apache Spark
- PySpark
- Spark SQL
- Apache Airflow
- Docker
- Workflow automation
- DAG creation
- Distributed computing
- Data analysis
- Containerized environments

---

# Real-World Applications

The technologies introduced in this module are widely used for:

- ETL pipelines
- Data warehousing
- Data lake processing
- Business intelligence
- Cloud analytics
- Machine learning pipelines
- Workflow automation
- Enterprise data platforms

---

# What Made This Module Effective

Several factors made this module particularly effective:

- Strong balance between theory and hands-on practice
- Real-world technologies used in industry
- Docker-based deployment experience
- Practical Spark exercises
- Workflow automation with Airflow
- Comprehensive final assignment

The hands-on activities helped reinforce concepts by allowing direct interaction with Spark and Airflow instead of only learning the theory.

---

# Opportunities for Improvement

Potential improvements could include:

- Additional troubleshooting guides for Docker environments
- More examples of Spark and Airflow working together in complete pipelines
- Additional Airflow debugging examples
- More enterprise-scale case studies

These additions would further strengthen the connection between course activities and real-world data engineering environments.

---

# Key Takeaways

- Apache Spark is a powerful distributed computing platform.
- PySpark provides a Python interface to Spark.
- Spark SQL enables SQL-based analytics at scale.
- Apache Airflow automates workflow execution.
- DAGs define workflow structure and dependencies.
- Docker simplifies deployment and environment management.
- Spark and Airflow complement each other in modern data engineering architectures.

---

# Personal Reflection

This module provided valuable hands-on experience with two of the most widely used tools in modern data engineering. Learning how to deploy, configure, and use Spark and Airflow helped build a stronger understanding of how large-scale data processing and workflow orchestration operate in production environments.

The practical assignments demonstrated how data pipelines can be built, automated, monitored, and maintained using industry-standard technologies.

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

- [x] Part 1: Apache Spark
- [x] Part 2: Apache Airflow

## Supporting Materials

- [x] Glossary
- [x] Cheat Sheet
- [x] Resources
- [x] Sandbox Documentation
- [x] Video Notes

---

# Conclusion

Module 19 provided a comprehensive introduction to processing big data with Apache Spark and automating workflows with Apache Airflow. Through discussions, coding exercises, and project-based learning, I developed practical skills in distributed data processing, workflow orchestration, and containerized deployment. These skills provide a strong foundation for future data engineering projects and support continued learning in cloud and big data technologies.

✅ Module 19 Successfully Completed