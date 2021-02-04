# Amazon EC2 Linux Instance
- Launch an [instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)

## Install Docker
- Update the package database
    - `sudo apt-get update`
- Uninstall old versions of Docker (Optional)
    - `sudo apt-get remove docker docker-engine docker.io`
- Install Docker/Docker-Compose on Ubuntu
    - `sudo apt install docker.io`
    - `sudo apt install docker-compose`
- Start and Automate Docker
    - `sudo systemctl start docker`
    - `sudo systemctl enable docker`
- Check Docker version
    - `docker --version`
- Remove all images
    - `sudo docker rmi $(sudo docker images -a -q)`
## Kafka docker-compose
- Default `DOCKER_HOST_IP=127.0.0.1`
- Single Zookeeper/Kafka
    - Zookeeper will be a available at `$DOCKER_HOST_IP:2181`
    - Kafka will be available at `$DOCKER_HOST_IP:9092`
- Run 
    ```
    sudo docker-compose -f single-zk-kafka.yml up
    sudo docker-compose -f single-zk-kafka.yml down
    ```

## Example
### Topic with Multiple Partitions
- __Single__ broker in the cluster
- Topic with multiple partitions and without replication
- Remove kafak log
    - `cd /tmp`
    - `rm -rf kafka-logs zookeeper`
- Create a topic named `animals`:
    ```bash
    sudo docker exec kafka_kafka1_1 kafka-topics \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 3 \
    --topic animals
    ```
- Start console producer
    ```bash
    sudo docker exec -it kafka_kafka1_1 kafka-console-producer \
    --broker-list localhost:9092 \
    --topic animals
    ```
- Start console consumer and read messages (FROM PARTITION 1)
    ```bash
    sudo docker exec kafka_kafka1_1 kafka-console-consumer \
    --bootstrap-server localhost:9092 \
    --partition 1 \
    --topic animals \
    --from-beginning
    ```
- Start console consumer and read messages (STARTING FROM OFFSET)
    ```bash
    sudo docker exec kafka_kafka1_1 kafka-console-consumer \
    --bootstrap-server localhost:9092 \
    --partition 1 \
    --topic animals \
    --offset 0
    ```
- It's not possible to read from specific offset across entire topic. You must specify partition along with offset.
- List Topics
    ```bash
    sudo docker exec kafka_kafka1_1 kafka-topics \
    --bootstrap-server localhost:9092 \
    --list
    ```
- Describe Topic
    ```bash
    sudo docker exec kafka_kafka1_1 kafka-topics \
    --bootstrap-server localhost:9092 \
    --describe \
    --topic animals
    ```
    ```bash
    sudo docker exec kafka_kafka1_1 kafka-topics \
    --bootstrap-server localhost:9092 \
    --describe \
    --topic __consumer_offsets
    ```
### Kafka Cluster with Multiple Brokers
- [Example](https://medium.com/better-programming/your-local-event-driven-environment-using-dockerised-kafka-cluster-6e84af09cd95) and [here](https://medium.com/better-programming/kafka-docker-run-multiple-kafka-brokers-and-zookeeper-services-in-docker-3ab287056fd5)
- Run docker
    - `sudo docker-compose -f single-zk-multi-kafka.yml up`
- Run the zookeeper CLI
    - `bin/zkCli.sh -server localhost:2181` #Make sure Brokers are running
    - From here can explore
        - `ls /brokers/ids` #Gives the list of active brokers
        - `ls /brokers/topics` #Gives the list of topics
        - `get /brokers/ids/1` #Gives more detail information of the brokder id '1'
    - `echo dump | nc localhost 2181 | grep brokers`
----
- Create a topic named `months`:
    ```bash
    sudo docker exec -t kafka_kafka1_1 kafka-topics \
    --bootstrap-server :9092 \
    --create \
    --replication-factor 3 \
    --partitions 7 \
    --topic months
    ```
- Start producer
    ```bash
    sudo docker exec -it kafka_kafka1_1 kafka-console-producer \
    --broker-list localhost:9092 \
    --topic cars
    ```
- Start consumer
    ```bash
    sudo docker exec kafka_kafka1_1 kafka-console-consumer \
    --bootstrap-server localhost:9092 \
    --topic cars \
    --from-beginning
    ```
---
- Get into the `kafka` container
    - `sudo docker exec -it kafka bash`
- Create a topic named `months`
    ```bash
    kafka-topics \
    --create
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094 \
    --replication-factor 3 \
    --partitions 5 \
    --topic months
    ```
- Check the topic
    ```bash
    kafka-topics \
    --list \
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094
    ```
- Check topic detail
    ```bash
    kafka-topics \
    --describe \
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094 \
    --topic months
    ```
- Send messages to topic
    ```bash
    kafka-console-producer \
    --broker-list localhost:9092,localhost:9093,localhost:9094 \
    --topic months \
    --property "parse.key=true" \
    --property "key.separator=:"
    ```
- Consume Messages from topic
    ```bash
    kafka-console-consumer \
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094 \
    --topic months \
    --from-beginning \
    --property "parse.key=true"
    ```
    ```bash
    kafka-console-consumer \
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094 \
    --topic months \
    --partition 0 \
    --from-beginning
    ```
    ```bash
    kafka-console-consumer \
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094 \
    --topic months \
    --partition 0 \
    --offset 1
    ```
- Stop down broker
    - `sudo docker stop kafka-broker2_1`
- Start broker
    - `sudo docker start kafka-broker2_1`

### Kafka Consumer Groups
- Start docker
    -  `sudo docker-compose -f single-zk-kafka.yml up`
- Get into the `kafka` container
    - `sudo docker exec -it kafka bash`
- Create a topic named `numbers`
    ```bash
    kafka-topics \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 5 \
    --topic numbers
    ```
- List the topic
    ```bash
    kafka-topics \
    --list \
    --bootstrap-server localhost:9092
    ```
- Check topic detail
    ```bash
    kafka-topics \
    --describe \
    --bootstrap-server localhost:9092 \
    --topic numbers
    ```
- Start console producer
    ```bash
    kafka-console-producer \
    --broker-list localhost:9092 \
    --topic numbers
    ```
- Start console consumer
    ```bash
    kafka-console-consumer \
    --bootstrap-server localhost:9092 \
    --topic numbers \
    --from-beginning
    ```
- Start console consumer from specific partition
    ```bash
    kafka-console-consumer \
    --bootstrap-server localhost:9092 \
    --topic numbers \
    --partition 4 \
    --from-beginning
    ```
- Start console consumer with specific consumer group
    ```bash
    kafka-console-consumer \
    --bootstrap-server localhost:9092 \
    --topic numbers \
    --group nums \
    --from-beginning
- List consumer group
    ```bash
    kafka-consumer-groups \
    --bootstrap-server localhost:9092 \
    --list
    ```
- Consumer group details
    ```bash
    kafka-consumer-groups \
    --bootstrap-server localhost:9092 \
    --group nums \
    --describe
    ```
