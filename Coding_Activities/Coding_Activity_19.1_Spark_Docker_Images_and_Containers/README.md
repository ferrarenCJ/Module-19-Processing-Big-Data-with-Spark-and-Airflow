# Required Coding Activity 19.1: Creating Spark Docker Images and Containers

## Module 19: Processing Big Data with Spark and Airflow

---

# Activity Information

| Item | Details |
|----------|----------|
| Activity | Required Coding Activity 19.1 |
| Title | Creating Spark Docker Images and Containers |
| Points | 20 |
| Due Date | October 22, 2026 @ 4:29 PM UTC |
| Estimated Completion Time | 45 Minutes |
| Submission Type | Word Document (.docx) |
| Learning Outcome | Use Docker to create and manipulate Spark images and containers |

---

# Objective

Spark is a powerful distributed computing framework used for processing large datasets. Because Spark can be complex to install and configure manually, Docker provides an efficient way to deploy Spark using preconfigured container images.

In this activity, Docker Compose is used to:

- Download Spark Docker images
- Create Spark containers
- Launch Spark services
- Verify Spark is running
- Access the Spark Master Web UI

Upon completion, a fully functional Spark environment will be available for future coding activities and assignments.

---

# Learning Outcome Addressed

## Use Docker to Create and Manipulate Spark Images and Containers

By completing this exercise, students will learn how to:

- Use Docker Compose
- Deploy Spark in containers
- Verify running containers
- Access Spark services through a browser
- Prepare Spark environments for PySpark development

---

# Technologies Used

- Apache Spark
- Docker Desktop
- Docker Compose
- Apache Spark Docker Image
- Windows Command Prompt
- Web Browser

---

# Environment Information

## Docker Image Used

```yaml
image: apache/spark:3.5.1
```

## Containers Created

### Spark Master

```text
bitnami_spark_1
```

### Spark Worker

```text
bitnami_spark-worker-1
```

### Spark Network

```text
bitnami_spark-network
```

---

# Procedure

---

# Step 1: Verify No Running Containers

## Objective

Verify Docker Desktop is running and there are no active containers before beginning the activity.

## Actions Performed

1. Opened Docker Desktop.
2. Navigated to the Containers page.
3. Verified that no containers were currently running.

## Verification

Docker Desktop displayed:

```text
No containers are running
```

## Screenshot

### Step 1 – No Running Containers

Insert Screenshot Here

---

# Step 2: Create the bitnami Folder

## Objective

Create the working directory that will contain all Spark configuration files.

## Command Executed

```cmd
mkdir bitnami
```

## Verification Command

```cmd
dir
```

## Result

The following folder was created:

```text
bitnami
```

## Screenshot

### Step 2 – Created bitnami Folder

Insert Screenshot Here

---

# Step 3: Download docker-compose.yml

## Objective

Download the Docker Compose configuration file provided by the course.

## Navigate to Folder

```cmd
cd bitnami
```

## Download Configuration File

```cmd
curl https://raw.githubusercontent.com/emeritus/MO-PCDE-assets/main/module19/Required_Coding_activity_spark_image/starter/docker-compose.yml -o docker-compose.yml
```

## Result

File downloaded successfully:

```text
docker-compose.yml
```

## Verification

```cmd
dir
```

File size:

```text
1,806 bytes
```

## Screenshot

### Step 3 – Downloaded docker-compose.yml

Insert Screenshot Here

---

# Step 4: Verify docker-compose.yml Contents

## Objective

Inspect the Docker Compose file and verify Spark services have been defined.

## Command Executed

```cmd
type docker-compose.yml
```

## Key Configuration Identified

### Spark Master

```yaml
spark:
  image: apache/spark:3.5.1
```

### Spark Worker

```yaml
spark-worker:
  image: apache/spark:3.5.1
```

### Ports

```yaml
8080:8080
7077:7077
```

## Result

Verified that both Spark Master and Spark Worker services were configured correctly.

## Screenshot

### Step 4 – Verified docker-compose.yml Contents

Insert Screenshot Here

---

# Step 5: Create and Start Spark Containers

## Objective

Launch the Spark environment using Docker Compose.

## Command Executed

```cmd
docker compose up
```

## Result

Docker successfully:

1. Pulled Spark images
2. Created the Spark network
3. Created Spark containers
4. Started services

Output included:

```text
Image apache/spark:3.5.1 Pulled
Container bitnami_spark_1 Created
Container bitnami_spark-worker-1 Created
```

Services Started:

```text
starting org.apache.spark.deploy.master.Master

starting org.apache.spark.deploy.worker.Worker
```

## Screenshot

### Step 5 – Started Spark Containers

Insert Screenshot Here

---

# Step 6: Verify Spark Containers Running

## Objective

Confirm that both Spark containers are running successfully.

## Verification Tool

Docker Desktop

## Running Containers

### Spark Master

```text
bitnami_spark_1
```

### Spark Worker

```text
bitnami_spark-worker-1
```

## Status

```text
Running
```

## Result

Both Spark services were active and communicating successfully.

## Screenshot

### Step 6 – Verified Running Spark Containers

Insert Screenshot Here

---

# Step 7: Access Spark Web UI

## Objective

Verify that the Spark Master service is accessible through a browser.

## URL

```text
http://localhost:8080
```

## Result

Successfully accessed:

```text
Spark Master at spark://spark:7077
```

Information displayed:

### Spark Cluster Status

```text
Alive Workers: 1
Status: ALIVE
```

### Worker Information

```text
Cores: 1
Memory: 1024 MiB
```

## Verification

The Spark Master and Worker were both functioning correctly.

## Screenshot

### Step 7 – Spark Web Interface

Insert Screenshot Here

---

# Results

The Spark Docker environment was deployed successfully.

## Components Running

| Component | Status |
|------------|------------|
| Docker Desktop | Running |
| Spark Master | Running |
| Spark Worker | Running |
| Spark Network | Running |
| Spark Web UI | Accessible |

---

# What I Learned

Through this activity I learned how to:

- Deploy Spark using Docker
- Use Docker Compose
- Manage Docker containers
- Verify containerized services
- Access Spark administrative interfaces
- Prepare a Spark environment for PySpark development

---

# Future Activities

This environment will be used in:

## Coding Activity 19.2

Loading Data into a Spark Docker Container

## Coding Activity 19.3

Using PySpark to Query Data

## Final Assignment 19.1

Processing Big Data with Spark and Airflow

---

# Conclusion

The Spark Docker environment was installed and configured successfully using Docker Compose. Both the Spark Master and Spark Worker containers launched correctly, and the Spark Web UI was accessible through localhost. The environment is now ready for data loading, PySpark queries, and the remaining Spark exercises in Module 19.

---

# Submission Checklist

- [x] Screenshot 1 – No Running Containers
- [x] Screenshot 2 – bitnami Folder Created
- [x] Screenshot 3 – docker-compose.yml Downloaded
- [x] Screenshot 4 – docker-compose.yml Verified
- [x] Screenshot 5 – docker compose up Executed
- [x] Screenshot 6 – Spark Containers Running
- [x] Screenshot 7 – Spark Web UI Accessible
- [x] Word Document Prepared
- [x] Ready for Submission