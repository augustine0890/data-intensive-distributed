# Apache-Kafka
## Installation
- [Download](https://www.apache.org/dyn/closer.cgi?path=/kafka/) the Kafka and extract:
    - `tar -xzf kafka.tgz`
    - `cd kafka`
## Start the kafka environment
- Start the Zookeeper service
    - `bin/zookeeper-server-start.sh config/zookeeper.properties`
- Start the kafka broker service
    - `bin/kafka-server-start.sh config/server.properties`
