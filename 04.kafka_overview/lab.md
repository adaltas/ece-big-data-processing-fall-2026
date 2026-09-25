# Kafka Demo and labs

This lab is a quick demonstration of a simple Kafka producer/topic/consumer combo using the confluent_kafka python library.  

## Prerequisites

- Docker 
- python and a new python environment

## Ojectives

- An understanding of Kafka is obtained by completing the demo.
- A new producer/topic/consumer combo is created and run.

## Environment Setup

1. Start a new python environment in a new project directory.
2. Install confluent-python in the environment.
3. Copy the admin.py, producer.py, and consumer.py files to the new project directory. 

## Start the Docker Containers

The Docker image is pulled and started.  

```bash
# Get the Docker image
docker pull apache/kafka-native:4.1.1
# Start the Kafka Docker container
docker run -p 9092:9092 apache/kafka-native:4.1.1
```

## Demo

1. Open a terminal and run the admin.py file from the command line.

```bash
python admin.py
```

2. From the same terminal run the producer.py file from the command line.

```bash
python producer.py
```

3. Open a new terminal and run the consumer.py file from the command line and observe the output.

```bash
python consumer.py
```

**Note** ensure that your python environment is started in each open terminal before running the commands. Also note that in some environments the `python` command may have to be replaced with `python3`.  

## Lab

1. Examine the three .py files as examples.
2. Create a new topic by adjusting or creating a new admin.py file.
3. Download any book from [Project Gutenberg](https://www.gutenberg.org/).
4. Create a new producer.py that will read the downloaded book line by line and send each line to the topic created in step 2.
5. Adjust the consumer.py so that it reads from the new topic created in step 2.
6. Using the text cleaning steps from the word count lab as inspiration, do some basic text cleaning and parsing for the incoming messages and output them to a new file.
