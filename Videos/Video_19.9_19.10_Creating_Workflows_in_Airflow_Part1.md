# Creating Workflows in Airflow (Videos 19.9 and 19.10)

## Module 19: Processing Big Data with Spark and Airflow

---

# Overview

These two videos demonstrate how to create workflows in Apache Airflow using Directed Acyclic Graphs (DAGs).

The lessons progress from:

1. A simple **Hello World** workflow
2. A more realistic **Loan Review Workflow**

Together, these examples illustrate how Airflow automates task execution and manages dependencies between tasks in a workflow.

---

# Learning Objectives

After completing these videos, I should be able to:

- Create Airflow DAGs.
- Deploy DAGs into Airflow.
- Execute workflows from the Airflow UI.
- Define task dependencies.
- Use PythonOperator in Airflow.
- Build multi-step workflows.
- Understand real-world workflow automation use cases.

---

# Video 19.9: Creating a "Hello World" Workflow

**Duration:** 07:44

---

# Purpose

This video demonstrates the complete lifecycle of creating a simple Airflow workflow:

```text
Write DAG
     ↓
Deploy DAG
     ↓
View DAG in Airflow
     ↓
Execute DAG
     ↓
Review Results
```

The workflow contains a single task that outputs a simple message.

---

# Workflow Objective

Print:

```text
Hello World
```

or a similar message to demonstrate that Airflow can successfully execute a task.

---

# Airflow DAG Structure

Every workflow requires:

```python
from airflow import DAG
```

and at least one task.

---

# Typical Workflow Components

## Imports

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
```

---

## Default Arguments

```python
default_args = {
    'owner': 'airflow'
}
```

---

## DAG Definition

```python
dag = DAG(
    dag_id='hello_world',
    schedule_interval='@daily'
)
```

---

## Task Definition

```python
hello_task
```

---

## Task Execution

```text
Print Message
```

---

# PythonOperator

The workflow uses:

```python
PythonOperator
```

to execute a Python function.

Example:

```python
def hello():
    print("Hello World")
```

---

# Workflow Execution

Once the DAG file is placed inside:

```text
dags/
```

Airflow automatically detects the workflow.

Process:

```text
DAG Created
      ↓
Placed in dags Folder
      ↓
Airflow Detects DAG
      ↓
Visible in Web UI
      ↓
DAG Executed
```

---

# Airflow User Interface

After deployment the DAG appears inside the Airflow dashboard.

Users can:

- Enable DAGs
- Trigger DAG runs
- View logs
- Monitor completion

---

# Monitoring Execution

Airflow displays task status:

```text
Success
Running
Failed
Queued
```

The Hello World workflow demonstrates the complete development lifecycle using a very simple example.

---

# Key Lesson From Video 19.9

Even the simplest workflow follows the same pattern used by complex enterprise workflows.

Structure:

```text
DAG
   ↓
Task
   ↓
Execution
   ↓
Monitoring
```

---

# Video 19.10: Creating a Loan Review Workflow

**Duration:** 07:18

---

# Purpose

The second video demonstrates a more realistic workflow used in financial services.

The workflow processes loan applications through several review and validation steps.

This example introduces:

- Multiple tasks
- Task dependencies
- Workflow sequencing
- Business process automation

---

# Loan Review Workflow

Example:

```text
Receive Application
          ↓
Validate Application
          ↓
Review Loan Data
          ↓
Approve or Reject
          ↓
Notify Applicant
```

This workflow contains multiple tasks instead of a single task.

---

# Business Scenario

Suppose a bank receives thousands of loan applications.

Manual processing introduces:

- Delays
- Human error
- Inconsistent decisions

Airflow can automate the workflow by ensuring every application passes through the required review steps.

---

# Workflow Tasks

Example tasks may include:

### Task 1

```text
Receive Loan Application
```

---

### Task 2

```text
Validate Applicant Information
```

---

### Task 3

```text
Perform Loan Review
```

---

### Task 4

```text
Determine Approval Status
```

---

### Task 5

```text
Notify Customer
```

---

# Dependency Management

Dependencies enforce workflow order.

Example:

```python
application >> validation >> review >> approval >> notification
```

Workflow:

```text
Application
      ↓
Validation
      ↓
Review
      ↓
Approval
      ↓
Notification
```

---

# Why Dependencies Matter

Without dependencies:

```text
Tasks may run in the wrong order
```

Example:

```text
Notification sent before approval
```

which would be incorrect.

Dependencies guarantee:

```text
Proper workflow execution
```

---

# DAG Visualization

Airflow displays workflows graphically.

Example:

```text
Application
      ↓
Validation
      ↓
Review
      ↓
Approval
      ↓
Notification
```

Benefits:

- Easy monitoring
- Easier troubleshooting
- Clear dependencies

---

# Workflow Monitoring

Airflow tracks:

```text
Task Status
Execution Time
Failures
Retries
Logs
```

This allows operators to quickly identify workflow issues.

---

# Example Workflow Lifecycle

```text
Loan Application Arrives
          ↓
Airflow Scheduler Starts DAG
          ↓
Validation Task Runs
          ↓
Review Task Runs
          ↓
Decision Task Runs
          ↓
Notification Task Runs
          ↓
Workflow Completes
```

---

# Comparing the Two Workflows

## Hello World Workflow

```text
Single Task
```

Purpose:

```text
Learn Airflow Basics
```

Complexity:

```text
Low
```

---

## Loan Review Workflow

```text
Multiple Tasks
```

Purpose:

```text
Business Process Automation
```

Complexity:

```text
Moderate
```

---

# Airflow Concepts Demonstrated

Both workflows demonstrate:

## DAG Creation

```python
DAG()
```

---

## Task Definition

```python
PythonOperator()
```

---

## Dependencies

```python
task1 >> task2
```

---

## Execution

```text
Trigger Workflow
```

---

## Monitoring

```text
View Logs
Track Status
```

---

# Real-World Applications

The same concepts can be used for:

- ETL Pipelines
- Data Warehouse Loading
- Financial Processing
- Claims Processing
- Customer Onboarding
- Utility Asset Data Processing
- Spark Job Orchestration
- Machine Learning Pipelines

---

# Utility Industry Example

A gas utility workflow could look like:

```text
Extract Leak Survey Data
            ↓
Validate Records
            ↓
Run Asset Risk Analysis
            ↓
Create Reports
            ↓
Refresh Dashboard
```

Airflow automates the workflow while Spark performs the analytics.

---

# Spark and Airflow Together

A common architecture:

```text
Airflow DAG
      ↓
Launch Spark Job
      ↓
Spark Processes Data
      ↓
Store Results
      ↓
Send Notification
```

Responsibilities:

### Airflow

```text
Scheduling
Monitoring
Dependencies
Workflow Management
```

### Spark

```text
Processing
Analytics
Machine Learning
```

---

# Key Takeaways

- Airflow workflows are defined using DAGs.
- DAGs contain tasks and dependencies.
- A Hello World workflow demonstrates the basic Airflow lifecycle.
- More advanced workflows may contain many interconnected tasks.
- Dependencies ensure tasks execute in the proper order.
- Airflow provides graphical workflow visualization.
- Airflow tracks execution status and logs.
- Workflow automation improves reliability and consistency.
- Airflow is commonly used to orchestrate Spark jobs and ETL pipelines.

---

# My Notes

## Progression of Learning

### Video 19.9

Introduced:

```text
Single DAG
Single Task
Simple Execution
```

### Video 19.10

Expanded to:

```text
Multiple Tasks
Dependencies
Business Process Automation
```

---

## Main Concept

Airflow workflows become increasingly powerful as tasks are combined into larger DAGs.

The pattern remains:

```text
Define Tasks
      ↓
Define Dependencies
      ↓
Deploy DAG
      ↓
Run Workflow
      ↓
Monitor Results
```

---

# Summary

Videos 19.9 and 19.10 demonstrate how Apache Airflow workflows are created, deployed, and executed through Directed Acyclic Graphs (DAGs). The Hello World example introduces the foundational workflow concepts, while the Loan Review example illustrates how Airflow can automate real business processes using multiple tasks and dependencies. Together, these examples show how Airflow serves as a powerful workflow orchestration platform for data engineering and business automation.