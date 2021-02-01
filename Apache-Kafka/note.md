# Apache-Kafka
## Installation
- [Download](https://www.apache.org/dyn/closer.cgi?path=/kafka/) the Kafka and extract:
    - `tar -xzf kafka.tgz`
    - `cd kafka`
## Start the kafka environment
- Start the Zookeeper service
    - `bin/zookeeper-server-start.sh config/zookeeper.properties`
- Start the Kafka broker service
    - `bin/kafka-server-start.sh config/server.properties`
    - Check logs file: `logs/server.log`

## Create Kafka topic
**Kafka Cluster**

    - Zookeeper: `localhost:2181`
    - Kafka server (broker): `localhost:9092`

- Create topic
    - `bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic <topic-name>`
- List the topics
    - `bin/kafka-topics.sh --list --zookeeper localhost:2181`
- Describe detail the topic
    - `bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic <topic-name>`

## Consume and Produce Messages
- Producer: connect to broker
    - `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic <topic-name>`
- Consumer
    - `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic-name>`
    - `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic-name> --from-beginning`
- Kafka cluster stores messages even if they were already consumed by one of the consumers. Same messages may be read muiltiple times by different consumers.
- Multiple consumers and multiple producers could exchange messages via single centralized storage point - kafka cluster.
- Producers send messages to the Kafka cluster.
- Consumers receive messages form the Kafka cluster.
- Every message inside of the topic has unique number called `offset`. First message in each topic has offset 0.
- Consumners start reading messages starting from specific offset.