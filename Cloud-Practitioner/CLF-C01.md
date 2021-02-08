# Cloud Practitioneer

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