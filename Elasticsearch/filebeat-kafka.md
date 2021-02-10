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
    - `cdk deploy fk-vpc`
    ```
    The API @aws-cdk/core.Tag.add(scope,k,v) is deprecated: Use "Tags.of(scope).add(k,v)" instead. This API will be removed in the next major release
    ```

## Amazon Managed Streaming for Apache Kafka
- Create the Amazon EC2 instanace (Apache Kafka Client) for interacting with the Amazon MSK Cluster.
- Deploy Amazon MSK Cluster into the VPC
    - `cdk deploy kafka`