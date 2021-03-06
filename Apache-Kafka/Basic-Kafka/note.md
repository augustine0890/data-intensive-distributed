# Basic Kafka
## Examples
- Netflix uses Kafka to apply recommendations in real-time while you're watching TV shows
- Uber uses Kafka to gather user, taxi and trip data in real-time to compute and forecast demand, and compute surge pricing in real-time.
- LinkedIn uses Kafka to prevent spam, collect user interactions to make better connection recommendations in real time.

## Kafka Theory
- Topics: a particular stream of data
- Topics are split in partitions
    - Each partition is ordered
    - Each message within a partition gets an incremental id, called offset
- Brokers
    - A Kafka cluster is composed of multiple brokers (servers)
    - Each broker is identified with its ID (integer)
    - Each broker contains certain topic partitions
    - After connecting to any broker (called a bootstrap broker), broker will be connected to the entire cluster.
- Topic replication factor
    - Topics should have a replication factor > 1 (usually between 2 and 3)
    - At anytime only ONE broker can be a leader for a given partition
    - Only that leader can receive and serve data for a partition
    - The other brokers will synchronize the data
    - Each partition has one leader and multiple ISR (in-sync replica)
- Producers
    - Write data to topics (which is made of partitions)
    - Automatically know to which broker and partition to write to
- Message keys
    - Producers can choose to send a key with the message (string, number, etc..)
    - If key=null, data is sent round robin (broker 101 then 102 and then 103 ...)
- Consumers
    - Read data from a topic (identified by name)
    - Consumers know which broker to read from
    - In case of broker failures, consumers know how to recover
    - Data is read in order within each partitions
- Consumer Groups
    - Each consumer within a group reads from exclusive partitions
    - If you have more consumers than partitions, some consumers will be inactive
- Consumer Offsets
    - Kafka stores the offsets at which a consumer group has been reading
    - The offsets committed live in a Kafka __topic__ named `__consumer_offsets`
    - When a consumer in a group has processed data received from Kafka, it should be committing the offsets
    - If a consumer dies, it will be able to read back from where it left off
- Delivery semantics for consumers
    - At most one:
        - Offsets are committed as soon as the message is received
        - If the processing goes wrong, the message will be lost
    - At least once;
        - Offsets are committed after the message is processed
        - Make sure the processing is idempotent (processing again the messages won't impact your systems)
    - Exactly once:
        - Can be achieved for Kafka --> Kafka workflows using Kafka Streams API
- Kafka Broker Discovery
    - Every Kafka broker is also called a `bootstrap server`
    - Only need to connect to one broker and it will be connected to the entire cluster
    - Each broker knows about all brokers, topics and partitions (metadata)
- Zookeeper
    - Manages brokers (keeps a list of them)
    - Helps in performing leader election for partitions
    - Sends notifications to Kafka in case of changes (e.g new topic, broker dies, broker comes up, delete topics, etc...)
    - By design operates with an odd number of servers
    - Zookeeper has a leader (handle writes) the rest of the servers are followers (handle reads)
- Kafka Guarantees
    - Messages are appended to a topic-partition in the order they are sent
    - Consumers read messages in the order stored in a topic-partition
    - With a replication factor of N, producers and consumers can tolerate up to N-1 brokers being down
    - Example replication factor of 3
        - Allows for one broker to be taken down for maintenance
        - Allows for another broker to be taken down unexpectedly
    - As long as the number of partitions remains constant for a topic (no new partitions), the same key will always go to the same partition