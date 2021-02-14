# Filebeat-Kafka
## Bootstrap CDK
- Install CDK
    - `npm install -g aws-cdk`
    - `cdk --version`
- Create project directory
    - `mkdir filebeat-kafka && cd filebeat-kafka`
- Create new Python CDK project
    - `cdk init --language python`
- Activating the Virtualenv
    - `source .venv/bin/activate`
- Install required python modules
    - `pip install -r requirements.txt`
- Run `cdk-deploy-to.sh`
    - `chmod +x cdk-deploy-to.sh`
    - `./cdk-deploy-to.sh`
- Create the CDK configuration
    - `cdk bootstrap aws://youraccount/yourregion`

## Amazon Virutal Private Cloud
- The filebeat-kafka stack will be deployed into this VPC
- Deploy the vpc stack
    - `cdk deploy filebeat-kafka-vpc`
    ```
    The API @aws-cdk/core.Tag.add(scope,k,v) is deprecated: Use "Tags.of(scope).add(k,v)" instead. This API will be removed in the next major release
    ```

## Amazon Managed Streaming for Apache Kafka
- Create the Amazon EC2 instanace (Apache Kafka Client) for interacting with the Amazon MSK Cluster.
- Deploy Amazon MSK Cluster into the VPC
    - `cdk deploy kafka`
- Amazon EC2 instance will be deployed to interact with the Amazon MSK Cluster.
- Kafka topics: `topic`, `apachelog`, `appevent`
- Connect to the Kafka client Amazon EC2 instance
    - Get the EC2 instance public dns
        ```bash
        kafka_client_dns=`aws ec2 describe-instances --filter file://filebeat-kafka/kafka/kafka_filter.json --output text --query "Reservations[*].Instances[*].{Instance:PublicDnsName}[0].Instance"` && echo $kafka_client_dns
        ```
    - Connect to the amazon EC2 instance
        - `ssh -i "~/.ssh/key_pairs.pem" ec2-user@$kafka_client_dns`
- Create the Kafka producer session on the `topic` Kafka topic
    - Get the cluster ARN
        - `kafka_arn=`aws kafka list-clusters --output text --query 'ClusterInfoList[*].ClusterArn'` && echo $kafka_arn`
    - Get the bootstrap brokers
        - `kafka_brokers=`aws kafka get-bootstrap-brokers --cluster-arn $kafka_arn --output text --query '*'` && echo $kafka_brokers`
    - Connect to the cluster as a `producer` on the Kafka topic `topic`
        - `/opt/kafka_2.12-2.4.0/bin/kafka-console-producer.sh --broker-list $kafka_brokers --topic topic`
- Create the Kafka consumer session:
    - Connect to the Kafka client EC2 instance
        - `kafka_client_dns=`aws ec2 describe-instances --filter file://filebeat-kafka/kafka/kafka_filter.json --output text --query "Reservations[*].Instances[*].{Instance:PublicDnsName}[0].Instance"` && echo $kafka_client_dns`
        - `ssh -i "~/.ssh/key_pairs.pem" ec2-user@$kafka_client_dns`
    - Get the cluster ARN
        - `kafka_arn=`aws kafka list-clusters --output text --query 'ClusterInfoList[*].ClusterArn'` && echo $kafka_arn`
    - Get the bootstrap brokers
        - `kafka_brokers=`aws kafka get-bootstrap-brokers --cluster-arn $kafka_arn --output text --query '*'` && echo $kafka_brokers`
    - Connect to the cluster as a consumer
        - `/opt/kafka_2.12-2.4.0/bin/kafka-console-consumer.sh --bootstrap-server $kafka_brokers --topic topic --from-beginning`

