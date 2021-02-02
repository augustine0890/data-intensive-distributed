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
