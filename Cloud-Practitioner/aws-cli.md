# AWS Command Line
- For the latest version
    - `curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"`
    - `sudo installer -pkg AWSCLIV2.pkg -target /`
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
- Command structure
    - `aws <command> <subcommand> [options and parameters]`

[Reference](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)