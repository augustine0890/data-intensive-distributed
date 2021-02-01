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