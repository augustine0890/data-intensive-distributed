# Basic Kafka Commands

- Start Zookeeper
    - `bin/zookeeper-server-start.sh config/zookeeper.properties`
- Start Kafka Broker
    - `bin/kafka-server-start.sh config/server.properties`

- Create Topic
    ```bash
    bin/kafka-topics.sh \
    --bootstrap-server <host:port> \
    --create \
    --replication-factor 1 \
    --partitions 3 \
    --topic <topic-name>
    ```

- List Topics
    ```
    bin/kafka-topics.sh \
    --bootstrap-server <host:port> \
    --list
    ```

- Topic Details
    ```
    bin/kafka-topics.sh \
    --bootstrap-server <host:port> \
    --describe \
    --topic <topic-name>
    ```

- Start Console Producer
    ```bash
    bin/kafka-console-producer.sh \
    --broker-list <host:port> \
    --topic <topic-name>
    ```

- Start Console Consumer
    ```bash
    bin/kafka-console-consumer.sh \
    --bootstrap-server <host:port> \
    --topic <topic-name>
    ```

- Start Console Consumer and Read Messages from Beginning
    ```bash
    bin/kafka-console-consumer.sh \
    --bootstrap-server <host:port> \
    --topic <topic-name> \
    --from-beginning
    ````

- Start console consumer with specific consumer group
    ```bash
    bin/kafka-console-consumer.sh \
    --bootstrap-server <host:port> \
    --topic <topic-name> \
    --group <group-name> \
    --from-beginning
    ```

- List consumer groups
    ```bash
    bin/kafka-consumer-groups.sh \
    --bootstrap-server <host:port> \
    --list
    ```

- Consumer group details
    ```bash
    bin/kafka-consumer-groups.sh \
    --bootstrap-server <host:port> \
    --group <group-name> \
    --describe
    ```