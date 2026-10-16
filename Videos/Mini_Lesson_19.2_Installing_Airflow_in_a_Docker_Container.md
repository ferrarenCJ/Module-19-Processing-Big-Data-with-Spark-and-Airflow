# Mini-Lesson 19.2: Installing Airflow in a Docker Container

---

# Overview

In this mini-lesson, Apache Airflow is installed using Docker containers.

Airflow is an open-source workflow orchestration platform that allows data engineers to create, schedule, monitor, and manage data pipelines through Directed Acyclic Graphs (DAGs).

This lesson demonstrates:

- Installing Airflow with Docker Compose
- Running Airflow containers
- Accessing the Airflow Web UI
- Understanding Airflow's directory structure
- Logging into the Airflow platform

Upon completion, a fully functioning Airflow environment is available for creating and managing workflows.

---

# Learning Objectives

After completing this lesson, I should be able to:

- Install Apache Airflow using Docker.
- Download and modify Docker Compose configuration files.
- Launch Airflow services in Docker containers.
- Access the Airflow user interface.
- Understand Airflow project folders.
- Log in and navigate the Airflow platform.

---

# Prerequisites

Before beginning:

✅ Docker Desktop installed

✅ Docker Desktop running

✅ Internet connection available

Verify Docker installation:

```bash
docker --version
```

Verify Docker Compose:

```bash
docker compose version
```

---

# Step 1: Create Airflow Project Folder

Create a folder named:

```text
airflow-docker
```

Example:

```bash
mkdir airflow-docker
```

Navigate into the folder:

```bash
cd airflow-docker
```

---

# Step 2: Download docker-compose.yaml

Download the Airflow Docker Compose configuration file.

Command:

```bash
curl "https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml" -o docker-compose.yaml
```

Result:

```text
docker-compose.yaml
```

File downloaded successfully.

---

# Step 3: Configure Airflow

Open:

```text
docker-compose.yaml
```

using Visual Studio Code.

Example:

```bash
code docker-compose.yaml
```

Locate:

```yaml
AIRFLOW__CORE__LOAD_EXAMPLES: 'true'
```

Change to:

```yaml
AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
```

Purpose:

```text
Disable example DAGs
```

Benefits:

- Cleaner environment
- Faster startup
- Easier navigation

Save and close the file.

---

# Step 4: Start Airflow Containers

Inside the:

```text
airflow-docker
```

directory run:

```bash
docker-compose up
```

or

```bash
docker compose up
```

Docker will:

```text
Download Images
Create Networks
Create Volumes
Create Containers
Start Services
```

Expected Airflow Services:

```text
airflow-webserver
airflow-scheduler
airflow-worker
postgres
redis
```

---

# Verify in Docker Desktop

Open Docker Desktop.

All Airflow containers should display:

```text
Running
```

Example:

```text
airflow-webserver
airflow-scheduler
airflow-worker
postgres
redis
```

---

# Step 5: Verify Generated Folders

Open a new terminal.

Navigate back to:

```bash
cd airflow-docker
```

List contents:

```bash
ls
```

or

```cmd
dir
```

New folders should appear:

```text
dags
logs
plugins
```

---

# Purpose of Each Folder

## dags

Stores workflow definitions.

Example:

```text
daily_etl.py
weekly_report.py
```

---

## logs

Stores workflow execution logs.

Examples:

```text
Task Success Logs
Task Failure Logs
Scheduler Logs
```

---

## plugins

Stores custom Airflow extensions.

Examples:

```text
Custom Operators
Custom Hooks
Custom Sensors
```

---

# Step 6: Access Airflow UI

Open a browser.

Navigate to:

```text
http://localhost:8080
```

You should see:

```text
Apache Airflow Login Screen
```

Prompt:

```text
Username
Password
```

---

# Step 7: Sign Into Airflow

Default credentials:

### Username

```text
airflow
```

### Password

```text
airflow
```

Click:

```text
Sign In
```

---

# Airflow Home Page

After signing in successfully, you should see:

```text
Airflow Dashboard
```

Features include:

- DAG Management
- Workflow Monitoring
- Task Monitoring
- Execution History
- Scheduling Controls

---

# Airflow Architecture Overview

Airflow consists of several services working together.

```text
Airflow Web UI
        │
        ▼
Airflow Scheduler
        │
        ▼
Airflow Workers
        │
        ▼
Task Execution
```

Supporting services:

```text
PostgreSQL
Redis
```

---

# What is a DAG?

DAG stands for:

```text
Directed
Acyclic
Graph
```

Example:

```text
Extract Data
      ↓
Transform Data
      ↓
Load Data
      ↓
Send Notification
```

Each step is a task inside the workflow.

---

# Why Airflow Uses DAGs

DAGs provide:

- Task dependency management
- Workflow scheduling
- Retry handling
- Failure monitoring
- Parallel processing

Example:

```text
Task A
  ↓
Task B
  ↓
Task C
```

Airflow ensures:

```text
A completes before B
B completes before C
```

---

# Common Airflow Use Cases

## ETL Pipelines

```text
Extract
Transform
Load
```

---

## Data Warehousing

```text
Operational Systems
        ↓
Airflow
        ↓
Data Warehouse
```

---

## Machine Learning Pipelines

```text
Feature Engineering
      ↓
Model Training
      ↓
Scoring
      ↓
Deployment
```

---

## Spark Job Scheduling

```text
Airflow
      ↓
Submit Spark Job
      ↓
Process Data
      ↓
Store Results
```

---

# Airflow + Spark Workflow

Example:

```text
Airflow Scheduler
        ↓
Launch Spark Job
        ↓
Spark Data Processing
        ↓
Load Results
        ↓
Send Notification
```

Airflow manages the workflow.

Spark performs the computation.

---

# Benefits of Airflow

## Workflow Automation

Eliminates manual execution.

---

## Monitoring

Tracks job success and failure.

---

## Scheduling

Supports:

```text
Hourly
Daily
Weekly
Monthly
```

---

## Scalability

Handles complex enterprise workflows.

---

## Extensibility

Supports:

```text
Python
Spark
AWS
Azure
Google Cloud
Databases
REST APIs
```

---

# Folder Structure After Installation

```text
airflow-docker
│
├── dags
├── logs
├── plugins
└── docker-compose.yaml
```

---

# Command Reference

## Create Project Folder

```bash
mkdir airflow-docker
```

---

## Navigate to Folder

```bash
cd airflow-docker
```

---

## Download Docker Compose File

```bash
curl "https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml" -o docker-compose.yaml
```

---

## Start Containers

```bash
docker compose up
```

or

```bash
docker-compose up
```

---

## View Containers

```bash
docker ps
```

---

## Stop Containers

```bash
docker compose down
```

---

# Key Takeaways

- Apache Airflow is a workflow orchestration platform.
- Airflow can be installed easily using Docker.
- Docker Compose automates deployment of all required Airflow services.
- Airflow stores workflows in the dags directory.
- Airflow uses DAGs to manage and schedule workflows.
- Airflow provides a web interface for monitoring tasks and workflows.
- Airflow is commonly used alongside Spark to automate ETL pipelines.
- Airflow improves reliability, visibility, and automation of data engineering workflows.

---

# Connection to Future Lessons

The Airflow installation completed in this lesson will be used for:

- Creating DAGs
- Building workflows
- Scheduling jobs
- Integrating Airflow with Spark
- Automating ETL pipelines
- Module 19 coding activities

---

# Summary

In this mini-lesson, Apache Airflow was installed using Docker Compose and configured for local development. The Airflow services were launched in Docker containers, supporting directories were generated automatically, and the Airflow web interface was accessed using default credentials. With Airflow successfully running, the environment is now ready for creating DAGs and orchestrating data engineering workflows.