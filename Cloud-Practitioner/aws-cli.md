# AWS Command Line
- For the latest version
    - `curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"`
    - `sudo installer -pkg AWSCLIV2.pkg -target /`
    - `aws --version`
- Configuration
    ```bash
    aws configure
    AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
    AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    Default region name [None]: us-west-2
    Default output format [None]: json
    ```
- List configuration data
    -  `aws configure list`
- List all of users
    - `aws iam list-users`
- Command structure
    - `aws <command> <subcommand> [options and parameters]`

[Reference](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

# AWS Cloud Development Kit (AWS CDK)
- Bootstrapping is the deployment of a AWS CloudFormation template to a specific AWS enviroment (account and region)
- Use the `cdk bootstrap`
    - `cdk bootstrap aws://ACCOUNT-NUMBER-1/REGION-1 aws://ACCOUNT-NUMBER-2/REGION-2 ...`
    ```
    cdk bootstrap aws://123456789012/us-east-1
    cdk bootstrap 123456789012/us-east-1 123456789012/us-west-1
    ```