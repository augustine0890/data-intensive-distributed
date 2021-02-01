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

## What is Apache Kafka
- Apache Kafka is distributed pusblish-subsribe messaging system
- __Broker__: receives messages from producers and stores them on disk keyed by unique offset. It allows consumers to fetch messages by topics, partition and offset. Brokers can create a Kafka cluster by sharing information between each other directly or indirectly using Zookeeper.
    - Kafka server (broker): `localhost:9092`
- Broker Cluster: groups of brokers working together 
- __Zookeeper__: 
    - Maintains list of active brokers
    - Manages configuration of the topics and partitions
    - Elects controller
    - Zookeeper: `localhost:2181`
- Zookeepr cluster (ensemble):
    - Minimum number of servers required to run the zookeeper is called quorum.
    - It's recommended to have odd number of servers in the Zookeeper ensemble and quorum set to (n+1)/2 where n i qty of servers.
- __Kafka Cluster__: run a Apache Kafka across multiple datacenters
    - Supports multi-site deployment of synchronous and asynchronous replication between datacenters.
- __Kafka Topic__:
    - Message queues in Kafka, it's category or feed name to which messages are published. Producers write data to topics and consumers read from topics
    - Default lgo retention period is 168 hours (7 days)
- Message structure
    - Timestamp
    - Offset number (unique across partition)
    - Key (optional)
    - Value (sequence of bytes)
- __Partitioned__: topics are partitioned and replicated across multiple nodes.
    - Topic consist of one or more partitions on different brokers in the cluster.
    - Kafka cluster maintains a partitioned logs. 
    - The messages in the partitions are each assigned a sequential id number called the offset that identifies each message within the partition.
    - The producer is responsible for choosing which message to assign to which partition within topic and the consumer need to track what messages that have been consumed.
    - Partition leader is a Kafka Broker. Each partition has one server which acts as the leader and zero or more servers which act as followers.
    - The leader handles all read and write requests for the partition while the followers passively replicate the leader.
- __Controller__: One of the brokers serves as the controller, which is responsible for managing the states of partitions and replicas and replicas and for performing administrative tasks like reassigning partitions.

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
