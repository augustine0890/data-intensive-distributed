# Cloud Practitioner

### IT Terminology
- Router: a networking device that forwards data packets between computer networks. They know where to send your packets on the internet.

### Types of Cloud Computing
- Infrastructure as a Service (IaaS)
    - Networking, computers, data storage space
    - Highest level of flexibility
    - Easy parallel with traditional on-premises IT
    - Amazon EC2, GCP, Azure, Rackspace, Digital Ocean
- Platfrom as a Service (PaaS)
    - Focus on the deployment and management of your applications
    - Elastic Beanstalk, Heroku, Google App Engine, Windows Azure
- Software as a Service (SaaS)
    - Completed product that is run and managed by the service provider
    - Rekognition for ML, Dropbox

### AWS Console
- Global Services:
    - Identity and Access Management (IAM)
    - Route 53 (DNS service)
    - CloudFront (Content Delivery Network)
    - WAF (Web Application Firewall)
- Region-scoped:
    - Amazon EC2, Elastic Beanstalk, Lambda, Rekognition

### IAM - Identity and Access Management
- Users are people within your organization, and can be grouped
- Groups contains users only.
- The policies define the permissions of the users, groups or roles's permissions
- Assign permissions to AWS services with IAM Roles
    - Common roles: EC2 instance, Lambda function, CloudFormation
- Don't use the root account except for AWS account setup
- Use Access Keys for Programmatic Access (CLI/SDK)
- Audit: IAM credential reports & IAM access advisor

### EC2 - Elastic Compute & Instance Storage
- Elastic Compute Cloud = Infrastructure as a Service
    - Renting virtual machine
    - Storing data on virtual drives (EBS)
    - Distributing load across machines (ELB)
    - Scaling the services using an auto-scaling group (ASG)
- EC2 Intance Types
    - General purpose: balance between compute, memory, networking
    - Compute Optimized: batch processing workloads, high performance computing
    - Memory Optimized: fast performance for workloads that process large data sets in memory
    - Storage Optimized: storage-intensive tasks that require high, sequential read and write access to large data sets on local storage
- Security Groups
    - Acting as a `firewall` on EC2 instances
    - Access to Ports
    - Authorised IP ranges - IPv4 and IPv6
    - Control of inbound network (from other to the instance)
    - Control of outboud network (from the instance to other)
- Classic Ports
    - SSH (secure shell): 22 - log into a Linux instance
    - FTP (file transport protocol): 21 - upload files into a file share
    - SFTP (secure file transport protocol): 22 - upload file using SSH
    - HTTP: 80 - access unsecured website
    - HTTPs: 443 - access secured website
- SSH
    - It allows you to control a remote machine, using command line
    - `ssh -i "key.pem" ec2-user@ec2-54-167-189-204.compute-1.amazonaws.com`
- An Amazon EC2 Dedicated Host is a physical server with EC2 instance capacity fully dedicated to your use.
 - Shared Responsibility Model for EC2
    - AMZ: infrastructure (global network security), isolation on physical hosts, replacing faulty hardware, compliance validation.
    - User: security groups rules, operating-system patches and updates, software and utilities installed on the EC2 instance, IAM roles assigned to EC2 & IAM user assess management.
- EC2 Instance: AMI (OS) + Instance Size (CPU + RAM) + Storage + Security Groups + EC2 User Data
    - Security Groups: firewall attached to the EC2 instance
    - EC2 User Data: script launched at the first start of an instance
    - SSH: start a terminal into EC2 instance (port 22)
    - EC2 Instance Role: link to IAM roles
### S3
- "infinitely scaling" storage
- Backup and storage, disaster recovery, application hosting, data lakes & big data analytics, static website.
- Amazon S3 allows people to store objects (file) in "buckets" (directories)
- Buckets must have a globally unique name (across all regions all accounts)
- Object (file):
    - Have a Key
    - The Key is the FULL path
    - The Key is composed of _prefix_ + _object name_
    - The Key with very long names that contain slashes (`/`)

### Deploying and Managing Infrastructure at Scale Section
- CloudFormation: declarative way of outlining your AWS Infrastructure.
- CloudFormation template:
    - Want a security group
    - Two EC2 instances using this security group
    - Want an S3 bucket
    - Want a load balancer (ELB) in front of these machines
- CloudFormation will created in the right order, with the exact configuration that you specify

### VPC & Networking
- VPC - Virtual Private Cloud: private network to deploy the resources (regional resource)
- Subnets allow you to partition your network inside the VPC (Availability Zone resource)
- A public subnet is a subnet that is accessible from the internet
- A private subnet is a subnet that is not accessible from the internet
- VPC Diagram

    ```
    AWS Cloud --> Region --> VPC = (Availability Zone 1: public and private subnet, VPC CIDR Range, Availability Zone 2: public and private subnet)
    ```
- Internet Gateways helps VPC instances connect with the internet.
- Public Subnets have a route to the internet gateway.
- NAT Gateways (AWS-managed) & NAT Instances (self-managed) allow your instances in the Private Subnets to access the internet while remaining private