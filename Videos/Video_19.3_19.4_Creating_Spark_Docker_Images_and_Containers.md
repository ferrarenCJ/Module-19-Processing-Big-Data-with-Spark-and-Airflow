# Creating Spark Docker Images and Containers (Videos 19.3 & 19.4)

## Overview

In these videos, Dr. Sanchez demonstrates how to use Docker to deploy Apache Spark.

Docker provides a lightweight, repeatable, and platform-independent way to run Spark without requiring complex local installation and configuration.

For this module, Spark will be executed inside Docker containers, allowing students to focus on Spark concepts rather than environment setup challenges.

---

# Learning Objectives

After completing these videos, I should be able to:

- Explain the purpose of Docker Images and Containers.
- Identify Spark Docker images available for use.
- Create Spark containers using Docker Compose.
- Start and manage Spark services.
- Verify Spark container status.
- Access Spark services through a web browser.
- Prepare for upcoming Spark coding activities.

---

# Video 19.3: Creating Spark Docker Images

**Duration:** 03:12

---

## Why Use Docker for Spark?

Installing Spark directly on a local machine can be complicated due to:

- Java dependencies
- Version compatibility issues
- Environment variables
- Cluster configuration

Docker solves these problems by packaging Spark into a reusable container image.

Benefits include:

- Consistency across environments
- Faster setup
- Easier deployment
- Simplified maintenance
- Cross-platform compatibility

---

# Docker Concepts

## Docker Image

A Docker Image is a blueprint used to create containers.

It contains:

- Operating System
- Libraries
- Configurations
- Runtime Dependencies
- Spark Installation

Think of an image as:

```text
Class Blueprint
        ↓
Create Instance
        ↓
Docker Container
```

---

## Docker Container

A Docker Container is a running instance of a Docker image.

Containers provide:

- Isolation
- Portability
- Repeatability

For this module, Spark runs inside Docker containers.

---

# Spark Docker Images

At the time the original video was recorded, two Spark images were commonly used.

---

## Big Data Europe Spark Image

Resources:

- Big Data Europe Project
- Big Data Europe Docker Spark Repository

Features:

- Spark Cluster Deployment
- Docker Compose Support
- Multi-Container Architecture

---

## Bitnami Spark Image

Resources:

- Bitnami Containers Library
- Docker Hub Spark Repository

Historically popular due to:

- Ease of configuration
- Enterprise-ready deployment

### Important Note

The Bitnami image used in the original video is no longer the recommended image for this course.

---

# Current Recommendation

For Module 19 activities, use the:

```text
Official Spark Docker Image
```

Docker image:

```text
spark
```

The course materials have been updated accordingly.

---

# General Spark Docker Workflow

```text
Pull Image
     ↓
Create Container
     ↓
Start Services
     ↓
Verify Status
     ↓
Access Spark
     ↓
Load Data
     ↓
Run PySpark
```

This workflow will be used repeatedly throughout the Spark activities.

---

# Video 19.4: Creating Spark Docker Containers

**Duration:** 02:06

---

## Creating Spark Containers

Once a Spark Docker image is available, containers can be created from the image.

Typical workflow:

### Step 1

Download:

```text
docker-compose.yml
```

---

### Step 2

Start Services

```bash
docker compose up
```

Docker performs:

```text
Download Image
        ↓
Build Environment
        ↓
Create Containers
        ↓
Start Services
```

---

### Step 3

Verify Running Containers

```bash
docker ps
```

Example output:

```text
CONTAINER ID
IMAGE
STATUS
PORTS
```

This confirms that Spark services are running correctly.

---

# Monitoring Spark

After containers start successfully, Spark services can be accessed through a browser.

Example:

```text
http://localhost:8080
```

This interface allows users to:

- View Spark status
- Monitor applications
- Review workloads
- Monitor execution

---

# Docker Compose

Docker Compose simplifies multi-container deployments.

Instead of manually starting containers one by one:

```bash
docker run ...
docker run ...
docker run ...
```

Docker Compose allows configuration within:

```text
docker-compose.yml
```

Then execute:

```bash
docker compose up
```

Benefits:

- Simpler deployment
- Reproducible environments
- Easier maintenance
- Version-controlled configuration

---

# Spark Architecture in Docker

```text
                 Docker Host
                       |
         --------------------------------
         |                              |
    Spark Container             Local Files
         |
    PySpark
         |
   Data Processing
```

The container encapsulates the Spark runtime while the host system manages Docker.

---

# Why Docker Matters for Data Engineers

Docker has become a standard technology because it provides:

- Environment consistency
- Easier deployment
- Simplified onboarding
- Infrastructure portability
- Reproducible analytics workflows

Modern data engineering platforms frequently rely on Docker.

Examples include:

- Apache Spark
- Apache Airflow
- Kafka
- Databases
- Machine Learning Platforms

---

# Key Takeaways

- Spark is executed inside Docker containers for this module.
- A Docker Image serves as a template used to create containers.
- A Docker Container is a running instance of an image.
- The course now recommends using the official Spark Docker image.
- Docker Compose simplifies deployment and management.
- Spark services can be monitored through localhost ports.
- Docker improves consistency, portability, and reproducibility.

---

# My Notes

## Why This Matters

As a Data Engineer working with large-scale enterprise datasets, Docker provides a standardized deployment mechanism for:

- Spark
- Airflow
- Databases
- ETL Frameworks
- Analytics Platforms

Instead of spending time configuring environments, teams can share Docker configurations and reproduce environments quickly.

## Connection to Upcoming Activities

These videos prepare us for:

### Coding Activity 19.1

Creating Spark Docker Images and Containers

### Coding Activity 19.2

Loading Data into a Spark Docker Container

### Coding Activity 19.3

Using PySpark to Query Data

The Docker environment created here becomes the foundation for all Spark work in Module 19.
``