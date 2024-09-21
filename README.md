# Real-Time Data Streaming

This project demonstrates a real-time data streaming pipeline that ingests, processes, and stores user data generated via [RandomUser API](https://randomuser.me). The project uses tools like Airflow, Apache Kafka, Apache Spark, PostgreSQL, Cassandra, and more, for orchestrating tasks, streaming data, and storing it in various databases.

![Realtime Data Streaming drawio](https://github.com/user-attachments/assets/4a723c5e-ba6a-4fb4-868d-9f148543f02f)

## Project Structure

The project consists of the following main components:

### 1. **Airflow DAGs** 
   - `dags/kafka_streams.py`: Airflow DAG responsible for streaming data from the RandomUser API and publishing it to Kafka.

### 2. **Scripts**
   - `scripts/entrypoint.sh`: Entrypoint script for setting up Airflow, initializing the database, and ensuring required packages are installed.

### 3. **Docker Compose**
   - `docker-compose.yml`: Defines services for Kafka, Zookeeper, Schema Registry, Control Center, Spark, Cassandra, PostgreSQL, and Airflow, orchestrating the project components using Docker containers.

### 4. **Spark Streams**
   - `spark_streams.py`: Python script for consuming data from Kafka using Apache Spark, processing it, and storing it in Cassandra.

---

## Tools and Technologies

- **[RandomUser API](https://randomuser.me/)**: Used to generate random user data.
- **[Apache Airflow](https://airflow.apache.org/)**: Orchestrates workflows for streaming data.
- **[Apache Kafka](https://kafka.apache.org/)**: Message broker for real-time streaming of data.
- **[Zookeeper](https://zookeeper.apache.org/)**: Coordinates Kafka brokers.
- **[Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html)**: Manages Avro schemas for Kafka topics.
- **[Confluent Control Center](https://docs.confluent.io/platform/current/control-center/index.html)**: Monitors and manages Kafka clusters.
- **[Apache Spark](https://spark.apache.org/)**: Real-time data processing.
- **[PostgreSQL](https://www.postgresql.org/)**: Relational database for Airflow metadata.
- **[Cassandra](https://cassandra.apache.org/)**: NoSQL database for storing the processed data.

---

## Project Workflow

1. **Data Ingestion (Kafka Producer)**:
   - `Airflow DAG` runs a task that fetches random user data from the RandomUser API and streams it into a Kafka topic (`user_created`).

2. **Data Processing (Spark Streaming)**:
   - Spark consumes data from the `user_created` Kafka topic, processes it by extracting and transforming fields, and then inserts it into a Cassandra table (`created_users`).

3. **Orchestration (Airflow)**:
   - Airflow orchestrates the entire data pipeline, scheduling data ingestion at regular intervals.

---

## Project Setup

### Prerequisites
- Docker
- Docker Compose

### Steps to run the project

1. Clone the repository:
    ```bash
    git clone <repo_url>
    cd <repo_name>
    ```

2. Start the services using Docker Compose:
    ```bash
    docker-compose up -d
    ```

3. Access Airflow Web UI:
   - Airflow is running at `http://localhost:8080`. You can log in using the default credentials:
     - **Username**: `admin`
     - **Password**: `admin`

4. Access Confluent Control Center:
   - Confluent Control Center is running at `http://localhost:9021`.

5. Access Kafka Schema Registry:
   - Schema Registry is available at `http://localhost:8081`.

6. Spark Master UI:
   - Access the Spark Master UI at `http://localhost:9090`.

7. Cassandra:
   - Cassandra is running and accessible at `localhost:9042`.

---

## Airflow DAG

The Airflow DAG `user_automation` consists of the following tasks:
- **stream_data**: This task retrieves random user data from the RandomUser API, formats it, and publishes the data to the Kafka topic `user_created`.
- you can see kafka_streams.py in dags folder for code 


## Docker Compose Services

The docker-compose.yml file defines the following services:

    Zookeeper: Manages Kafka broker metadata.
    Kafka Broker: Streams messages to topics.
    Schema Registry: Ensures proper schema versioning.
    Confluent Control Center: GUI for managing and monitoring Kafka.
    Airflow Webserver: Runs Airflow for orchestration.
    PostgreSQL: Airflow metadata storage.
    Spark Master and Spark Worker: Spark for processing Kafka streams.
    Cassandra: Stores processed user data.

## Docker Compose Command

To start all the services:

```bash
docker-compose up -d
```
## Spark Streaming

The spark_streams.py file processes the user data stream from Kafka and stores the output in Cassandra. The steps are as follows:

    Kafka Stream Consumption: Spark reads messages from the Kafka topic.
    Data Transformation: The streamed data is parsed, transformed, and prepared for insertion into Cassandra.
    Data Insertion into Cassandra: The transformed data is inserted into the created_users table in Cassandra.

