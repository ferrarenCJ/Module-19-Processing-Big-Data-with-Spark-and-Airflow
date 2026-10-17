# Module 19: Glossary

## Airflow

Airflow is a platform that allows you to manipulate big data by using workflows to automate processing steps that are performed repeatedly.

---

## Cache

A cache is a special storage space for temporary files that makes a device or browser run faster and more efficiently. Caching is the action of keeping data accessible for improved speed.

---

## CRON Cycle

A CRON cycle is the collection of all of the scheduled tasks performed by a program.

---

## DAG Arguments

DAG arguments are configuration parameters that define how a DAG will behave. They are defined as dictionary keys inside the Python script that defines the DAG.

---

## DAG States

A DAG state determines the status of a DAG and manages the Airflow schedules for the operations within a workflow.

---

## Dependencies

In a DAG, dependencies specify the relationships between tasks.

---

## Directed Acyclic Graph (DAG)

Mathematically, a DAG is a directed graph without any cycles.

In Airflow, Directed Acyclic Graphs (DAGs) are used to define a workflow or data pipeline.

---

## Directed Graph

A directed graph is any graph in which the vertices and edges have order or direction associated with them.

---

## Operator (Airflow)

In Airflow, an Operator is a template for a predefined task that can be defined declaratively inside a DAG. An Operator requires dependencies to define the DAG structure.

---

## PySpark

PySpark is a commonly used tool that enables Python applications to run with Spark.

---

## Spark

Spark is an open-source analytical engine optimized to process data in parallel. Key benefits include:

- High performance
- Parallel processing
- Multi-language support
- Advanced analytics capabilities

---

## Spark Core

Spark Core is the foundation of the Spark project. It is responsible for distributing, dispatching, and scheduling tasks.

---

## Spark SQL

Spark SQL is a Spark module for structured data processing that allows the execution of SQL queries.

---

## Spark Session

A Spark Session is the entry point for all functionality in Spark. A Spark Session must be created before performing Spark operations.

Example:

```python
spark = SparkSession.builder \
    .appName("Assignment19.3") \
    .getOrCreate()
```

---

## Spark Stack

The Spark Stack is the collection of all engines and applications within Spark.

Examples include:

- Spark SQL
- MLlib
- GraphX
- SparkR

---

## Task (Airflow)

In an Airflow DAG, a task represents an individual unit of work and describes the action being performed. Tasks are organized using dependencies.

---

## Thread

A thread is the execution of a sequence of programmed instructions.

---

## Workflow

In Airflow, a workflow defines the pipeline of actions that contains the steps required to process data.

Example:

```text
Extract Data
      ↓
Transform Data
      ↓
Load Data
      ↓
Generate Reports
```

---

# Key Terms Summary

| Term | Purpose |
|--------|--------|
| Airflow | Workflow orchestration platform |
| DAG | Defines workflow structure |
| Task | Individual unit of work in a DAG |
| Operator | Template used to create tasks |
| Spark | Distributed data processing engine |
| PySpark | Python interface for Spark |
| Spark SQL | SQL processing engine for Spark |
| Spark Session | Entry point into Spark |
| Dependencies | Control task execution order |
| Workflow | End-to-end data processing pipeline |

---

# Module 19 Focus Areas

This module focused on two major technologies:

## Apache Spark

Used for:

- Distributed computing
- Big data processing
- SQL analytics
- Data transformation

## Apache Airflow

Used for:

- Workflow orchestration
- Task scheduling
- Dependency management
- Workflow monitoring
- Automation

Together, Spark and Airflow provide a powerful framework for building scalable and automated data engineering pipelines.