# Video 19.8: Creating a Workflow in Airflow: Directed Acyclic Graphs (DAGs)

**Duration:** 03:56

---

# Overview

In this lesson, Dr. Sanchez demonstrates how to create a workflow in Apache Airflow using a **Directed Acyclic Graph (DAG)**.

DAGs are the foundation of Airflow and define:

- Tasks
- Task dependencies
- Execution order
- Scheduling behavior

Every Airflow workflow is represented as a DAG.

The lesson demonstrates how Airflow uses Python code to define workflows and how tasks are connected together to create automated data pipelines.

---

# Learning Objectives

After completing this lesson, I should be able to:

- Explain what a DAG is.
- Understand how Airflow workflows are defined.
- Create a simple DAG.
- Define task dependencies.
- Understand workflow execution order.
- Recognize the role of DAGs in data engineering pipelines.

---

# What is a DAG?

DAG stands for:

```text
Directed
Acyclic
Graph
```

A DAG is Airflow's workflow definition structure.

---

# Directed

Tasks have a specific execution path.

Example:

```text
Task A
   ↓
Task B
   ↓
Task C
```

Each task points to the next task in the pipeline.

---

# Acyclic

The workflow cannot contain loops.

Valid:

```text
A → B → C
```

Invalid:

```text
A → B → C → A
```

Airflow requires workflows to move forward without repetition.

---

# Graph

Tasks are represented as nodes.

Dependencies between tasks are represented as edges.

Example:

```text
Extract Data
      ↓
Transform Data
      ↓
Load Data
```

This creates a graph structure.

---

# Why DAGs Matter

DAGs help Airflow determine:

```text
What tasks exist
When tasks run
Which tasks run first
Which tasks depend on others
```

Without DAGs:

```text
Execution order is unclear
Dependencies are unmanaged
Automation becomes difficult
```

---

# Basic Airflow Workflow

Example ETL pipeline:

```text
Extract
    ↓
Transform
    ↓
Load
```

Airflow executes each task in sequence according to the DAG definition.

---

# DAG Components

A typical DAG consists of:

## DAG Definition

Defines the workflow.

---

## Tasks

Units of work.

Examples:

```text
Read File
Query Database
Run Spark Job
Send Email
```

---

## Dependencies

Control task execution order.

Example:

```text
Task A >> Task B
```

Task A must finish before Task B starts.

---

# Creating a DAG

Airflow DAGs are defined using Python.

Example:

```python
from airflow import DAG
```

The DAG object represents the workflow.

---

# Defining Default Arguments

Example:

```python
default_args = {
    "owner": "airflow"
}
```

Default arguments provide workflow configuration.

Common settings include:

```text
Owner
Retries
Retry Delay
Start Date
```

---

# Creating the DAG Object

Example:

```python
dag = DAG(
    dag_id="example_workflow",
    schedule_interval="@daily"
)
```

Key properties:

### dag_id

Unique workflow identifier.

Example:

```python
example_workflow
```

---

### schedule_interval

Workflow frequency.

Examples:

```python
@hourly
@daily
@weekly
@monthly
```

---

# Defining Tasks

Tasks perform specific work.

Example:

```python
task_1
task_2
task_3
```

Workflow:

```text
Task 1
   ↓
Task 2
   ↓
Task 3
```

---

# Creating Dependencies

Dependencies tell Airflow the order of execution.

Example:

```python
task_1 >> task_2 >> task_3
```

Meaning:

```text
Task 1 executes first
Task 2 executes second
Task 3 executes third
```

---

# Visualizing a DAG

Airflow provides a visual representation of workflows.

Example:

```text
Task_A
   ↓
Task_B
   ↓
Task_C
```

Benefits:

- Easier troubleshooting
- Better workflow understanding
- Dependency visibility

---

# Example Data Pipeline

A simple pipeline could perform:

```text
Download File
      ↓
Validate Data
      ↓
Transform Data
      ↓
Load Database
      ↓
Generate Report
```

Each step becomes a task inside the DAG.

---

# Airflow Scheduler

The scheduler monitors DAGs and determines:

```text
When a DAG should run
Which tasks should execute
Whether dependencies are met
```

---

# Airflow Execution Process

```text
DAG Defined
      ↓
Scheduler Detects DAG
      ↓
Tasks Queued
      ↓
Tasks Executed
      ↓
Workflow Completed
```

---

# Monitoring DAGs

The Airflow UI allows users to:

- View DAGs
- Monitor task status
- Retrigger workflows
- Examine execution logs
- Troubleshoot failures

Task statuses include:

```text
Success
Running
Queued
Failed
Skipped
```

---

# Example Utility Industry Workflow

For a gas utility company:

```text
Extract Leak Survey Data
            ↓
Validate Data Quality
            ↓
Run Risk Analysis
            ↓
Generate Asset Scores
            ↓
Update Dashboard
```

Airflow can automate and orchestrate this entire process.

---

# Spark and Airflow Integration

One of the most common Airflow use cases is orchestrating Spark jobs.

Workflow example:

```text
Airflow DAG
      ↓
Launch Spark Job
      ↓
Process Large Dataset
      ↓
Store Results
      ↓
Send Notification
```

Responsibilities:

### Airflow

```text
Scheduling
Workflow Management
Monitoring
```

### Spark

```text
Data Processing
Analytics
Machine Learning
```

---

# Benefits of DAGs

## Clear Workflow Design

Visual representation of tasks.

---

## Dependency Management

Ensures tasks run in the correct order.

---

## Reliability

Prevents accidental execution errors.

---

## Automation

Supports scheduled workflows.

---

## Scalability

Works with small and enterprise-scale pipelines.

---

# Key Takeaways

- Airflow workflows are defined as Directed Acyclic Graphs (DAGs).
- DAGs describe task execution order and dependencies.
- DAGs are written in Python.
- Tasks represent units of work within a workflow.
- Dependencies determine which tasks run before others.
- Airflow provides a visual interface for monitoring DAGs.
- DAGs are commonly used to orchestrate ETL pipelines.
- Airflow and Spark work together to automate large-scale data processing workflows.

---

# Connection to Previous Lessons

## Spark

Responsible for:

```text
Processing Data
Executing Analytics
Machine Learning
```

---

## Airflow

Responsible for:

```text
Orchestration
Scheduling
Workflow Management
Monitoring
```

Combined workflow:

```text
Airflow
   ↓
Spark Job
   ↓
Processed Data
   ↓
Analytics
```

---

# Real-World Applications

Airflow DAGs are frequently used for:

- ETL Pipelines
- Data Warehouses
- Data Lakes
- Reporting Pipelines
- Machine Learning Workflows
- Cloud Data Processing
- Utility Asset Analytics
- IoT Data Pipelines

---

# My Notes

## Core Concept

A DAG is essentially a blueprint for a workflow.

It defines:

```text
Tasks
Dependencies
Execution Order
Schedule
```

without actually performing the data processing itself.

## Simple Mental Model

```text
Spark = Worker

Airflow = Project Manager
```

Airflow decides:

```text
What runs
When it runs
What runs next
```

Spark performs the computational work.

---

# Summary

In Video 19.8, the concept of Directed Acyclic Graphs (DAGs) is introduced as the foundation of Apache Airflow workflows. DAGs define tasks, dependencies, and execution order, allowing Airflow to automate and manage complex data engineering pipelines. By combining DAG orchestration with Spark processing, organizations can build scalable, reliable, and automated analytics platforms.