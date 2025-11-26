[Skip to Main Content](#aws-page-content-main)

* Filter: All

* English
* [Contact us](https://aws.amazon.com/contact-us/?nc2=h_ut_cu)
* [AWS Marketplace](https://aws.amazon.com/marketplace/?nc2=h_utmp)
* Support
* My account

* Search

  Filter: All
* [Sign in to console](https://console.aws.amazon.com/console/home/?nc2=h_si&src=header-signin)
* [Create account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_su&src=header_signup)

AWS Blogs

* [Home](https://aws.amazon.com/blogs/)
* Blogs
* Editions

## [AWS Storage Blog](https://aws.amazon.com/blogs/storage/)

# Archiving relational databases to Amazon S3 Glacier storage classes for cost optimization

by Jean-Sebastien Labonte, Yanko Bolanos, and Sebastien Perreault on 28 JAN 2025 in [Advanced (300)](https://aws.amazon.com/blogs/storage/category/learning-levels/advanced-300/ "View all posts in Advanced (300)"), [Amazon CloudWatch](https://aws.amazon.com/blogs/storage/category/management-tools/amazon-cloudwatch/ "View all posts in Amazon CloudWatch"), [Amazon Elastic Container Registry](https://aws.amazon.com/blogs/storage/category/compute/amazon-elastic-container-registry/ "View all posts in Amazon Elastic Container Registry"), [Amazon EventBridge](https://aws.amazon.com/blogs/storage/category/application-integration/amazon-eventbridge/ "View all posts in Amazon EventBridge"), [Amazon S3 Glacier](https://aws.amazon.com/blogs/storage/category/storage/amazon-glacier/ "View all posts in Amazon S3 Glacier"), [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/blogs/storage/category/messaging/amazon-simple-notification-service-sns/ "View all posts in Amazon Simple Notification Service (SNS)"), [AWS Batch](https://aws.amazon.com/blogs/storage/category/compute/aws-batch/ "View all posts in AWS Batch"), [AWS Fargate](https://aws.amazon.com/blogs/storage/category/compute/aws-fargate/ "View all posts in AWS Fargate"), [AWS Lambda](https://aws.amazon.com/blogs/storage/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [AWS Secrets Manager](https://aws.amazon.com/blogs/storage/category/security-identity-compliance/aws-secrets-manager/ "View all posts in AWS Secrets Manager"), [Storage](https://aws.amazon.com/blogs/storage/category/storage/ "View all posts in Storage"), [Technical How-to](https://aws.amazon.com/blogs/storage/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/storage/archiving-relational-databases-to-amazon-s3-glacier-storage-classes-for-cost-optimization/)  [Comments](https://aws.amazon.com/blogs/storage/archiving-relational-databases-to-amazon-s3-glacier-storage-classes-for-cost-optimization/#Comments)  Share

Many customers are growing their data footprints rapidly, with significantly more data stored in their relational database management systems (RDBMS) than ever before. Additionally, organizations subject to data compliance including the Health Insurance Portability and Accountability Act (HIPAA), the Payment Card Industry Data Security Standard (PCI-DSS) and General Data Protection Regulation (GDPR) are often required to retain records for extended periods, further increasing their substantial data footprint.

As a result, your organization may need to archive RDBMS data from traditional databases backups (“dumps”) over a long period of time, ready to be used by a database engine. To address this requirements while keeping costs under control, you can leverage the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which are purpose-built for data archiving and provide you with the highest performance, most retrieval flexibility and the lowest cost archive storage in the cloud.

In this post, we will demonstrate how to build an automated backup and archiving solution on Amazon S3 Glacier storage classes using [AWS Batch](http://aws.amazon.com/batch), [AWS Lambda](https://aws.amazon.com/lambda/), [AWS Secret Manager](https://aws.amazon.com/secrets-manager/), and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). This solution will leverage tools such as *mysqldump* and *pg\_dump* to take database backups from Amazon RDS and Amazon Aurora instances on a recurrent schedule using [Amazon EventBridge](https://aws.amazon.com/eventbridge/). The backups are archived via automatic transition to S3 Glacier storage classes in an S3 bucket, providing a cost-effective, long-term storage solution.

## Solution overview

This solution leverages database dumps and S3 Glacier storage classes to provide a flexible, cost-effective approach for long-term data archival. The proposed architecture automates backup processes using a combination of EventBridge for scheduling, Lambda for code execution, and Fargate-based container images through AWS Batch to execute the archiving, enabling efficient data transfer to S3 Glacier storage classes.

While this method offers an innovative archival strategy, it is crucial to understand its limitations. Unlike native Amazon RDS snapshots, which enable quick point-in-time database restoration, this approach requires manually reconstructing the database. Restoring from database dumps involves reading entire dump files and executing SQL statements to rebuild database structures and reinsert data—a process that can be significantly time-consuming, potentially taking hours or even days for large databases.

This solution is best suited for long-term archival and should complement, not replace, standard backup and recovery mechanisms provided by Amazon RDS.

![Figure 1 - End-to-end database archival process with the associated AWS services](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Figure-1-End-to-end-database-archival-process-with-the-associated-AWS-services.png)

*Figure 1: End-to-end database archival process with the associated AWS services*

This solution works as follows:

1. Amazon EventBridge triggers an AWS Lambda function which scan Amazon RDS databases to find specific object tags key/value pairs indicating a Database we want archived.
2. AWS Batch launch an [AWS Fargate](https://aws.amazon.com/fargate/) image from [Amazon ECR](https://aws.amazon.com/ecr/). This image contains databases backup tools such as “*pg\_dump*” and “*mysqldump*“.
3. Database credentials are pulled from [AWS Secret Manager](https://aws.amazon.com/secrets-manager/). We then create a backup dump which get archived to S3 Glacier storage classes. A log entry is created in Amazon DynamoDB for reference and governance purposes.
4. In case of problems with the process, AWS Batch forwards the details of the issue through Amazon SNS to an email of your choice.

In the following sections, we walk you through the steps in details to create your resources and deploy the solution.

## Prerequisites

The following are prerequisites to implementing this solution.

### 1. An S3 bucket

This solution stores your archives in the [Amazon S3 Standard](https://aws.amazon.com/s3/storage-classes/) storage class to store newly created objects. You should configure an [Amazon S3 Lifecycle policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to set the destination Amazon S3 storage class to the desired class that correspond to your organization needs for your archives. S3 Lifecycle helps you store objects cost effectively throughout their lifecycle by transitioning them to lower-cost storage classes automatically as they age.

When selecting an Amazon S3 Glacier storage class, consider the following key characteristics:

![Figure 2 - S3 Glacier storage classes characteristics](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Figure-2-S3-Glacier-storage-classes-characteristics.png)

*Figure 2: S3 Glacier storage classes characteristics*

In doubt, you can use the S3 Glacier Instant Retrieval storage class to facilitate retrieval of your objects. In contrast with objects in S3 Glacier Instant Retrieval, Amazon S3 objects that are stored in the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes are not immediately accessible. To access an object in these storage classes, you must restore a temporary copy of the object to its S3 bucket. For additional information on restoring objects in S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive classes, visit the [S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects.html).

### 2. Networking and security components

To facilitate the archival process and communication with AWS Services, you will need to establish a destination subnet. We suggest simply re-using your databases subnet. Make sure communication to AWS services leverages [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html#concepts-vpc-endpoints), which have the advantage of keeping your traffic within the AWS infrastructure.

### 3. A development environment

To build a container image, you will need a development environment with the AWS CLI and Docker binaries installed.

## Solution deployment

To test this solution in your environment you will be required to follow these steps:

1. Create an [Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) repository and push your container image.

2. Prepare the AWS Lambda function and deploy the CloudFormation template.

3. Create credentials and secrets in Secrets Manager for database access.

4. Create a schedule with EventBridge and apply tag on your databases that require archiving.

### 1. Create an ECR repository and push your container image

To utilize AWS Batch for backing up and archiving your data, you must have an Elastic Container Registry (ECR) configured to store the container image.

#### Create an ECR repository:

1. Go to the [Amazon ECR console](https://us-east-1.console.aws.amazon.com/ecr/get-started?region=us-west-1) (this link will take you to the us-east-1 region, make sure this reflects the region your are building this solution in), and choose **Create a Repository**.

2. Select **Private** fromthe **Visibility setting**.

3. Enter a **Repository name**.

4. Select **Create Repository**.

#### Copy the solution files in your development environment

To download a copy of this solution from GitHub that contains the AWS CloudFormation templates, the AWS Lambda function code, and the Dockerfile used to build the container, complete the following steps:

1. Log in to your development environment.

2. Enter the following command:

```
git clone https://github.com/aws-samples/Archiving-RDBMs-for-cost-reduction.git .
```

#### Build the Docker image

To build and push your Docker image to Amazon ECR, complete the following steps:

1. Go to **Amazon ECR** in AWS Console and **choose your repository name.**

2. Select **View push commands.**

![Figure 3 - Location of the View push command button in the console](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Figure-3-Location-of-the-View-push-command-button-in-the-console.png)

*Figure 3: Location of the **View push command** button in the console*

 3. Select and copy each command listed in the **View push commands** above (steps 1 to 4) to your development environment terminal windows in the GitHub project you have just cloned. This will authenticate you and allow our container image to be pushed to your Amazon ECR private repository.

![Figure 4 - Output of the View push commands window in the console](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Figure-4-Output-of-the-View-push-commands-window-in-the-console.png)

*Figure 4: Output of the **View push commands** window in the console*

**Important**: When building Docker images on a macOS computer with an ARM-based processor, ensure compatibility with x86-based systems (like Amazon’s Elastic Container Service) by adding the “–platform linux/amd64” flag to your Docker build command. This modification allows the image to run correctly on different server architectures. For detailed guidance, consult the official Docker [documentation](https://docs.docker.com/build/building/multi-platform/).

4. Finally, go back to the ECR console and record the **URI** of the image you just built and uploaded.

### 2. Prepare the AWS Lambda function and deploy the CloudFormation template

The CloudFormation template deployed in the next step expect the Lambda function code to be zipped and stored in an Amazon S3 bucket. To store the Lambda function, do the following:

1. In the S3 console, choose the Amazon S3 bucket that will contain your archives (see “Prerequisites” above).

2. Zip and upload the file named “*py”* located in the root directory of your cloned copy of this solution repository to your S3 bucket. Make sure the file you are uploading is named “*cold\_archiving\_lambda\_func.zip“* precisely*.*

#### Deploy the CloudFormation stack

To deploy the CloudFormation stack, complete the following steps:

1. Go to the CloudFormation section in the AWS and **Choose Create stack with new resources**.

2. Select **Choose an existing template**, then **Specify a template**, **Upload a template file** and finally select **Choose File**.

3. Use the location of the CloudFormation template you downloaded locally and and select the “*cold\_archiving\_cfn.yaml*“ file.

![Figure 5 - View of the CloudFormation deployment section](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Figure-5-View-of-the-CloudFormation-deployment-section.png)

*Figure 5: View of the CloudFormation deployment section*

#### CloudFormation deployment parameters

To deploy the CloudFormation stack, you will need to provide some deployment parameters.

To enter the required CloudFormation deployment parameters, complete the following steps:

1. Enter a **Stack name.**

2. Enter the docker image URI you previously built in the **EcrImage**

3. Enter an email address in the **EmailAlerts field.** This used as a destination for alerts.

4. Enter a **Subnet** for the Fargate instance, this is the network discussed in the **Prerequisites** section.

5. Enter the destination **VPC**.

6. Leave everything else at their default value and choose **Submit**.

### 3. Create secrets in Secrets Manager for database access.

We are going to use credentials that only have the minimum set of permissions required to backup RDS instances and store them securely.

#### Creating the credentials

The backup process outlined in this blog post utilizes native database management tools, such as “mysqldump,” which require security credentials. By default, an Amazon RDS DB instance has a single administrative account with full privileges. However, it is recommended to create a dedicated user account that only has the necessary privileges to perform backups. For more information on granting least privilege access, you can refer to [this](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html) link.

To create a backup user, complete the following steps:

1. Connect to your Amazon RDS database endpoint from a location with the mysql client installed using the following command:

```
mysql -u admin -h <rds_Endpoint> -p
```

2. Enter the following command substituting your backup username and wanted password to create a user with the minimum set of required privileges to backup your data:

```
CREATE USER 'backup_user_name'@'%' IDENTIFIED BY 'your_password';
GRANT LOCK TABLES, SELECT ON DATABASE_NAME.* TO 'backup_user_name'@'%' IDENTIFIED BY 'your_password';
```

#### Storing a secret in Secrets Manager

Now that you have created a backup user, you need to store it’s credentials in Secrets Manager.

To store a secret in Secrets Manager, complete the following steps:

1. Open the AWS Management Console and choose Secrets manager.

2. Choose **Store a new Secret**.

3. Choose Secret Type, then select **Credential for Amazon RDS database**.

![Figure 6 - Selecting the type of credentials to be stored in Secrets Manager](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Figure-6-Selecting-the-type-of-credentials-to-be-stored-in-Secrets-Manager.png)

*Figure 6: Selecting the type of credentials to be stored in Secrets Manager*

4. Enter the credentials for the backup user created in the **Creating a backup user** step then choose **Next**.

5. Leave encryption selected to use a generated one or select a customer managed one.

6. Go to **Database**, and select the database to which this secret should be associated.

7. Choose **Next** then enter a secret name. It is **imperative** you precede its name with the “cold-archiving/” prefix (eg. cold-archiving/*secret\_name*). This is to ensure the task execution role will be able to access it and create a connection to your database. Take note of the secret name, including its prefix.

![Figure 7 - The Secret name with its associated prefix](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Figure-7-The-Secret-name-with-its-associated-prefix.png)

*Figure 7: The Secret name with its associated prefix*

8. Leave everything else at their default value and store your secret by choosing **Next**.

### 4. Create a schedule with EventBridge and tag your databases

The archival process can (and should), be scheduled to run periodically. You will create a schedule that runs once a month at a time of your choosing using EventBridge.

To create an EventBridge schedule, complete the following steps:

1. Open EventBridge, then under **Scheduler,** choose **Schedules**.

2. Choose **Create Schedule**.

3. Give a name to your schedule, then under **Occurence,** select **Recurring Schedule.**

4. Under Schedule type, select **Cron-based schedule**.

5. Under **Cron expression**, define a schedule. Here is an example showing a Cron based schedule occurring every first day of the month at 1:30 AM (this can be any day and time of your choosing). For more information about the Cron scheduling syntax, you can refer to the information [here](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html?icmpid=docs_console_unmapped#cron-based) and [here](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html).

![Figure 8 - Configuring the Cron based schedule with a cron expression syntax](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Figure-8-Configuring-the-Cron-based-schedule-with-a-cron-expression-syntax.png)

*Figure 8: Configuring the Cron based schedule with a cron expression* syntax

6. Select **fixed time window**, your local time zone, and choose **Next**.

#### Configure the Lambda invocation

You must select with which parameters your Lambda function will be launched by EventBridge.

To select the Lambda function as a target and configure its input parameters, complete the following steps:

1. Continuing from last step, under **Target detail**, select **Templated targets** then **AWS Lambda Invoke.**

2. Scroll down to **Invoke**, Select the cold-archiving Lambda function from the drop down as your **Lambda function**.

3. Under the **Payload** section, input how many days this archive *Retention* fieldshould correspond to in your DynamoDB archiving journal. The valid JSON format is *‘{“RetentionDays”:“number\_of\_days“}’.* Here is an example for 365 days of retention:

![Figure 9 - Entering the Payload information to configure a retention](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Figure-9-Entering-the-Payload-information-to-configure-a-retention.png)

*Figure 9: Entering the Payload information to configure a retention*

4. Choose **Next**, then scroll down to the **Permissions** section.

5. Select **Use an existing role**, then use the role the CloudFormation template created for you (named ***deployment\_name\_taskexec-role****).* In doubt, you can go look at the Cloudformation “*outputs”*section to find the appropriate role that was created for you*.*

6. Under the **Retry policy and dead-letter queue (DLQ)** section, disable retry under **Retry policy**, then under **Dead-letter queue (DLQ)** choose **Select an Amazon SQS queue in my AWS account as a DLQ.** Finally under **SQS queue,** select the **cold-archiving-error-queue.**

7. Scroll down, choose **Next** then **Create schedule**.

#### Tag your resources

The last step is tagging the resources that you want to be archived. These tags will be scanned by a Lambda function periodically which will launch an archive process on the databases that have the “AutomatedArchiving:Active” tag:value present.

To tag your resources, complete the following steps:

1. Open your Amazon RDS instance. Under the **Tags** tab add all the following key values pair:

![Figure 10 - All the available and mandatory key values pairs to be applied to your databases - unsquished](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/28/Figure-10-All-the-available-and-mandatory-key-values-pairs-to-be-applied-to-your-databases-unsquished-1.png)

*Figure 10: All the available and mandatory key:values pairs to be applied to your databases*

## Handling archives deletion

The solution presented in this blog post does not include a built-in file deletion mechanism. The responsibility of managing the deletion of archived files is left to you, to decide based on your specific requirements and policies.

By recording the archiving activities in Amazon DynamoDB, you have the flexibility to build a file deletion process tailored to your organization’s needs. This allows for a more controlled and adaptable approach to managing the lifecycle of the archived data, without relying on a one-size-fits-all solution.

For more information on how to delete Amazon S3 objects programmatically, you can refer to the link provided [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example_s3_DeleteObject_section.html).

## Cleaning up

When you’re finished evaluating this solution, you should delete the Cloudformation stack, any secrets you created, all associated Evenbridge schedules, and any S3 resources to avoid any further charges.

## Conclusion

In this blog post, we introduced an innovative solution for managing the exponential growth of relational database volumes through strategic cloud archiving to S3 Glacier storage classes. By harnessing AWS services like Batch, Lambda, and EventBridge, we have developed an automated approach that addresses critical data retention challenges for organizations operating under strict regulatory frameworks.

Our solution offers a transformative framework that enables organizations to:

* Optimize storage costs
* Maintain compliance with industry regulations
* Preserve data accessibility
* Streamline data lifecycle management

We encourage you to explore this solution by testing it within your own infrastructure. By doing so, you’ll gain firsthand insights into the potential cost savings and operational efficiencies achievable through intelligent, cloud-based data archiving strategies.

TAGS: [Amason S3 Glacier](https://aws.amazon.com/blogs/storage/tag/amason-s3-glacier/), [Amazon Elastic Container Registry (Amazon ECR)](https://aws.amazon.com/blogs/storage/tag/amazon-elastic-container-registry-amazon-ecr/), [Amazon S3 Glacier storage classes](https://aws.amazon.com/blogs/storage/tag/amazon-s3-glacier-storage-classes/), [Amazon S3 Lifecycle](https://aws.amazon.com/blogs/storage/tag/amazon-s3-lifecycle/), [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/blogs/storage/tag/amazon-simple-storage-service-amazon-s3/), [AWS Batch](https://aws.amazon.com/blogs/storage/tag/aws-batch/), [AWS Cloud Storage](https://aws.amazon.com/blogs/storage/tag/aws-cloud-storage/), [AWS Fargate](https://aws.amazon.com/blogs/storage/tag/aws-fargate/), [AWS Lambda](https://aws.amazon.com/blogs/storage/tag/aws-lambda/), [AWS Secrets Manager](https://aws.amazon.com/blogs/storage/tag/aws-secrets-manager/)

![Jean-Sebastien Labonte](https://d2908q01vomqb2.cloudfront.net/fb644351560d8296fe6da332236b1f8d61b2828a/2024/12/06/John-Sebastien-Labonte.jpg)

### Jean-Sebastien Labonte

Jean-Sebastien Labonte is Solutions Architect specializing in Data and Storage Management services at AWS. Jean-Sebastien has over 20 years of experience in designing and building data and infrastructure solutions, solely focused on customer-centric outcomes. Aside helping customers, when not at AWS, Jean-Sebastien enjoys travelling and hiking.

![Yanko Bolanos](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/09/02/Yanko-Bolanos.jpeg)

### Yanko Bolanos

Yanko Bolanos is a Sr. Solutions Architect enabling customers to successfully run production workloads on AWS. With over 19 years of experience in media & entertainment, telco, gaming, and data analytics, he is passionate about driving innovation in cloud and technology solutions. Prior to AWS, Yanko applied his cross-disciplinary tech and media expertise while serving as a director leading R&D Engineering and Ad Engineering teams.

![Sebastien Perreault](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/01/24/Sebastien-Perreault-Bio-Pic.jpg)

### Sebastien Perreault

Sebastien Perreault, a Principal Solutions Architect at Amazon Web Services (AWS), is a cloud storage expert who designs scalable, resilient solutions for global customers. Throughout his 25 years career he made sure to transform data related challenges into innovative solutions.

Loading comments…

### Resources

* [AWS Cloud Storage](https://aws.amazon.com/products/storage?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=storage-resources)
* [Getting Started with AWS Storage](https://aws.amazon.com/getting-started/hands-on/?getting-started-all.sort-by=item.additionalFields.sortOrder&getting-started-all.sort-order=asc&awsf.getting-started-category=category%23storage&awsf.getting-started-level=*all&awsf.getting-started-content-type=*all)
* [What's New with AWS Storage](https://aws.amazon.com/about-aws/whats-new/storage/)
* [Case Studies](https://aws.amazon.com/solutions/case-studies/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=storage-resources&customer-references-cards.sort-by=item.additionalFields.sortDate&customer-references-cards.sort-order=desc&awsf.content-type=*all&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-industry=*all&awsf.customer-references-use-case=*all&awsf.customer-references-tech-category=tech-category%23storage&awsf.customer-references-product=*all)

---

### Follow

* [Twitter](https://twitter.com/AWS_Storage)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [RSS Feed](http://feeds.feedburner.com/AmazonWebServicesBlog)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-social)

[Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc1=f_ct&src=footer_signup)

## Learn

* [What Is AWS?](/what-is-aws/?nc1=f_cc)
* [What Is Cloud Computing?](/what-is-cloud-computing/?nc1=f_cc)
* [What Is Agentic AI?](/what-is/agentic-ai/?nc1=f_cc)
* [Cloud Computing Concepts Hub](/what-is/?nc1=f_cc)
* [AWS Cloud Security](/security/?nc1=f_cc)
* [What's New](/new/?nc1=f_cc)
* [Blogs](/blogs/?nc1=f_cc)
* [Press Releases](https://press.aboutamazon.com/press-releases/aws)

## Resources

* [Getting Started](/getting-started/?nc1=f_cc)
* [Training](/training/?nc1=f_cc)
* [AWS Trust Center](/trust-center/?nc1=f_cc)
* [AWS Solutions Library](/solutions/?nc1=f_cc)
* [Architecture Center](/architecture/?nc1=f_cc)
* [Product and Technical FAQs](/faqs/?nc1=f_dr)
* [Analyst Reports](/resources/analyst-reports/?nc1=f_cc)
* [AWS Partners](/partners/work-with-partners/?nc1=f_dr)

## Developers

* [Builder Center](/developer/?nc1=f_dr)
* [SDKs & Tools](/developer/tools/?nc1=f_dr)
* [.NET on AWS](/developer/language/net/?nc1=f_dr)
* [Python on AWS](/developer/language/python/?nc1=f_dr)
* [Java on AWS](/developer/language/java/?nc1=f_dr)
* [PHP on AWS](/developer/language/php/?nc1=f_cc)
* [JavaScript on AWS](/developer/language/javascript/?nc1=f_dr)

## Help

* [Contact Us](/contact-us/?nc1=f_m)
* [File a Support Ticket](https://console.aws.amazon.com/support/home/?nc1=f_dr)
* [AWS re:Post](https://repost.aws/?nc1=f_dr)
* [Knowledge Center](https://repost.aws/knowledge-center/?nc1=f_dr)
* [AWS Support Overview](/premiumsupport/?nc1=f_dr)
* [Get Expert Help](https://iq.aws.amazon.com/?utm=mkt.foot/?nc1=f_m)
* [AWS Accessibility](/accessibility/?nc1=f_cc)
* [Legal](/legal/?nc1=f_cc)

English

Back to top

Amazon is an Equal Opportunity Employer: Minority / Women / Disability / Veteran / Gender Identity / Sexual Orientation / Age.

[x](https://twitter.com/awscloud) [facebook](https://www.facebook.com/amazonwebservices) [linkedin](https://www.linkedin.com/company/amazon-web-services/) [instagram](https://www.instagram.com/amazonwebservices/) [twitch](https://www.twitch.tv/aws) [youtube](https://www.youtube.com/user/AmazonWebServices/Cloud/) [podcasts](/podcasts/?nc1=f_cc) [email](https://pages.awscloud.com/communication-preferences?trk=homepage)

* [Privacy](/privacy/?nc1=f_pr)
* [Site terms](/terms/?nc1=f_pr)
* Cookie Preferences

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved.