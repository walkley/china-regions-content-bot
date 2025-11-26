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

# Connect Snowflake to S3 Tables using the SageMaker Lakehouse Iceberg REST endpoint

by Aritra Gupta, Jeemin Sim, Deepmala Agarwal, Frank Dallezotte, and Srividya Parthasarathy on 14 MAR 2025 in [Amazon Athena](https://aws.amazon.com/blogs/storage/category/analytics/amazon-athena/ "View all posts in Amazon Athena"), [Amazon S3 Tables](https://aws.amazon.com/blogs/storage/category/storage/amazon-s3-tables/ "View all posts in Amazon S3 Tables"), [Amazon SageMaker Lakehouse](https://aws.amazon.com/blogs/storage/category/analytics/amazon-sagemaker-lakehouse/ "View all posts in Amazon SageMaker Lakehouse"), [Amazon Simple Storage Service (S3)](https://aws.amazon.com/blogs/storage/category/storage/amazon-simple-storage-services-s3/ "View all posts in Amazon Simple Storage Service (S3)"), [AWS Glue](https://aws.amazon.com/blogs/storage/category/analytics/aws-glue/ "View all posts in AWS Glue"), [AWS Lake Formation](https://aws.amazon.com/blogs/storage/category/analytics/aws-lake-formation/ "View all posts in AWS Lake Formation"), [AWS Partner Network](https://aws.amazon.com/blogs/storage/category/aws-partner-network/ "View all posts in AWS Partner Network"), [Intermediate (200)](https://aws.amazon.com/blogs/storage/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Partner solutions](https://aws.amazon.com/blogs/storage/category/post-types/partner-solutions/ "View all posts in Partner solutions"), [Technical How-to](https://aws.amazon.com/blogs/storage/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/storage/connect-snowflake-to-s3-tables-using-the-sagemaker-lakehouse-iceberg-rest-endpoint/)  [Comments](https://aws.amazon.com/blogs/storage/connect-snowflake-to-s3-tables-using-the-sagemaker-lakehouse-iceberg-rest-endpoint/#Comments)  Share

Organizations today seek data analytics solutions that provide maximum flexibility and accessibility. Customers need their data to be readily available using their preferred query engines, and break down barriers across different computing environments. At the same time, they want a single copy of data to be used across these solutions, to track lineage, be cost effective, and scale better. The rich ecosystem of tools available to query tabular data at scale has quickly made [Apache Iceberg](https://aws.amazon.com/what-is/apache-iceberg/) a popular choice among organizations.

[Snowflake](https://www.snowflake.com/en/) makes enterprise AI easy, connected and trusted. Thousands of companies around the globe, including hundreds of the world’s largest, use Snowflake’s AI Data Cloud to share data, build applications, and power their business with AI. In June 2024, Snowflake announced [general availability for Iceberg tables](https://www.snowflake.com/en/blog/storage-iceberg-tables-now-generally-available/), bringing the platform’s performance and simplicity to the open table format.

The recent developments from Snowflake and [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/) with built-in Iceberg support provide organizations with a powerful new approach to data lake management. In Snowflake, you can leverage the platform’s elastic and performant compute, use query semantics of typical Snowflake tables, and interact with a single copy of data in S3 Tables that is interoperable across computing environments. At the storage layer, S3 Tables introduce purpose-built optimizations for Iceberg that deliver improved performance, simplified security controls, and automatic table maintenance right out of the box. This approach gives organizations a more streamlined method to leverage open data standards, combining the strengths of Snowflake’s data processing capabilities with S3 Tables.

In this post, we will walk through setting up Snowflake to access S3 Tables using the [Amazon SageMaker Lakehouse Iceberg REST endpoint](https://docs.aws.amazon.com/glue/latest/dg/access_catalog.html) with [AWS Lake Formation](https://aws.amazon.com/lake-formation/) managing storage credential vending. We start by using [Amazon Athena](https://aws.amazon.com/athena/) to create and add data into the table, and Lake Formation for access control. Next, we will walk through setting up Snowflake to register an external catalog and query the table.

**Note:** At the time of publishing this blog post, the credential vending feature offered by Snowflake is in preview. Additionally, external catalogs are offered in a read-only mode by Snowflake. The scope of these features are subject to change in the future.

## Solution Overview

![1_architecture diagram](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/1_architecture-diagram.png)

This post will use the [catalog integration](https://docs.snowflake.com/en/user-guide/tables-iceberg-configure-catalog-integration-rest#sigv4-glue) for the SageMaker Lakehouse Iceberg REST endpoint with [Signature Version 4 (SigV4)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) authentication in Snowflake.

## Prerequisites

* A [Snowflake account](https://signup.snowflake.com/).
* An S3 table bucket with the AWS analytics integration enabled. For this post, we’ve named our bucket, “s3tables-snowflake-integration”.
* An [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) role that is a Lake Formation data lake administrator in the Data Catalog account. For instructions, go to **Create a data lake administrator**.

## Solution walkthrough

### Part 1. Setup a namespace, table, and load data

**Step 1:** Log in to the [Amazon S3 console](https://console.aws.amazon.com/s3) and choose **Table buckets** from the navigation panel. Select the “s3tables-snowflake-integration” bucket.

**Step 2:** Select **Create table with Athena**.

![2_s3tables-snowflake-integration](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/2_s3tables-snowflake-integration.jpg)

**Step 3:** Create a namespace called “testnamespace”.

![3_create-table-athena](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/3_create-table-athena.jpg)

**Step 4:** On namespace creation, you should see this screen. Select **Create table with Athena**.

![4_create-table](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/4_create-table.jpg)

**Step 5:** Create a table “daily\_sales” through Athena.

```
CREATE TABLE `testnamespace`.daily_sales (
sale_date date,
product_category string,
sales_amount double)
PARTITIONED BY (month(sale_date))
TBLPROPERTIES (‘table_type’ = ‘iceberg’)
```

![6_query-editor](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/6_query-editor.jpg)

**Step 6:** Insert sample rows into the “daily\_sales” table using Athena.

```
INSERT INTO daily_sales
VALUES
(DATE '2024-01-15', 'Laptop', 900.00),
(DATE '2024-01-15', 'Monitor', 250.00),
(DATE '2024-01-16', 'Laptop', 1350.00),
(DATE '2024-02-01', 'Monitor', 300.00),
(DATE '2024-02-01', 'Keyboard', 60.00),
(DATE '2024-02-02', 'Mouse', 25.00),
(DATE '2024-02-02', 'Laptop', 1050.00),
(DATE '2024-02-03', 'Laptop', 1200.00),
(DATE '2024-02-03', 'Monitor', 375.00);
```

![7_query editor 2](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/7_query-editor-2.jpg)

Next, we walk through the configuration needed for Snowflake to access this table.

### Part 2. Setup IAM role for Snowflake to access S3 Tables through AWS Lake Formation

First, we create an IAM role that Snowflake will assume to access [AWS Glue](https://aws.amazon.com/glue/) and Lake Formation APIs. To do this we create the following policy and role:

**Step 1:** Create the policy and name it “irc-glue-lf-policy”. Here are some steps to do it through the [AWS Management Console](https://aws.amazon.com/console/):

1.1. Open the IAM console.

1.2. In the navigation pane of the console, choose **Policies**, and choose the **Create Policy** option.

1.3. In the policy editor choose **JSON** and paste the following policies.

1.3.1. Replace `<region>`, `<account-id>`, `<s3_table_bucket_name>`, and `<database_name>` in the following policy with your values. We use “myblognamespace” as the database name in the rest of this post.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "glue:GetCatalog",
                "glue:GetDatabase",
                "glue:GetDatabases",
                "glue:GetTable",
                "glue:GetTables"
            ],
            "Resource": [
                "arn:aws:glue:<region>:<account-id>:catalog",
                "arn:aws:glue:<region>:<account-id>:catalog/s3tablescatalog",
                "arn:aws:glue:<region>:<account-id>:catalog/s3tablescatalog/<s3_table_bucket_name>",
                "arn:aws:glue:<region>:<account-id>:table/s3tablescatalog/<s3_table_bucket_name>/<database_name>/*",
                "arn:aws:glue:<region>:<account-id>:database/s3tablescatalog/<s3_table_bucket_name>/<database_name>"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "lakeformation:GetDataAccess"
            ],
            "Resource": "*"
        }
    ]
}
```

**Step 2:** Create a role named “snowflake\_access\_role” by following these steps in the IAM console.

2.1. In the navigation pane of the console, choose **Roles** and choose the **Create role** option.

2.2. Choose AWS account.

2.3. Choose **Next** and choose the policy you previously created in Step 1, named “irc-glue-lf-policy”.

2.4. Choose **Next** and enter “snowflake\_access\_role” as the role name.

2.5. Choose **Create role**.

2.6. The trust relationship for this role will be updated later. Once you created the role, you need to define access to this role using Lake Formation.

**Note:** If you use encryption for AWS Glue, you must modify the policy to add AWS Key Management Service (AWS KMS) permissions. For more information, see [Setting up encryption in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/set-up-encryption.html).

### Part 3. Define access control using Lake Formation

**Step 1:** We first start with the Application integration setup, which allows third-party engines to access S3 tables. From the Lake Formation console, enable full table access for external engines to access data.

1.1. Sign in as an data lake admin user and go to AWS Lake Formation.

1.2. On the left pane, expand the **Administration** section

1.3. Choose **Application integration settings** and select **Allow external engines to access data in Amazon S3 locations with full table access**.

1.4. Click **Save**.

![8_app integration](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/8_app-integration.jpg)

**Step 2:** Next, we grant the following permissions to the snowflake\_access\_role on the resources as shown in the following table.

2.1 In the Lake Formation console navigation pane, choose **Data permissions**, and then select **Grant**.

2.2. In the Principals section, select the radio button **IAM users and roles**, also from the drop down select **snowflake\_access\_role**.

2.3. In the LF-Tags or catalog resources section, select Named Data Catalog resources:

2.3.1. Select `<accountid>:s3tablescatalog/s3tables-snowflake-integration` for Catalogs.

2.3.2. Select **testnamespace** for Databases.

2.3.3. Select **daily\_sales** for Tables.

2.4. Select **SUPER** for Table permissions.

2.5. Choose **Grant**.

The permission configurations through Lake Formation and IAM are now complete. Next, we look at the Snowflake setup.

### Part 4. Set up SageMaker Lakehouse Iceberg REST integration in Snowflake

**Step 1:** Login to Snowflake as admin user who has permission to create database and create catalog integration.

**Step 2:** Navigate to worksheet and run the following command to create database and catalog integration by providing following parameters.

* S3 table namespace for `CATALOG_NAMESPACE`
* SageMaker Lakehouse Iceberg REST endpoint for `CATALOG_URI`
* `AWSAccountID:s3tablescatalog/table-bucket-name` as `WAREHOUSE`
* IAM role created for snowflake to `SIGV4_IAM_ROLE`
* Configure `ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS` for the catalog integration to use the Lake Formation vended temporary credential for data set access. Replace `<account-id>` and `<region>` with the values for your AWS environment.

```
create database rest_catalog_db;
CREATE CATALOG INTEGRATION glue_rest_catalog_int
  CATALOG_SOURCE = ICEBERG_REST
  TABLE_FORMAT = ICEBERG
  CATALOG_NAMESPACE = 'testnamespace'
  REST_CONFIG = (
    CATALOG_URI = 'https://glue.<region>.amazonaws.com/iceberg'
    CATALOG_API_TYPE = AWS_GLUE
    WAREHOUSE = '<account-id>:s3tablescatalog/s3tables-snowflake-integration'
    ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS
  )
  REST_AUTHENTICATION = (
    TYPE = SIGV4
    SIGV4_IAM_ROLE = 'arn:aws:iam::<account-id>:role/snowflake_access_role'
    SIGV4_SIGNING_REGION = '<region>'
  )
  REFRESH_INTERVAL_SECONDS = 120
  ENABLED = TRUE;
```

**Step 3:** Follow [these steps](https://docs.snowflake.com/en/user-guide/tables-iceberg-configure-catalog-integration-rest-api-gateway#label-tables-iceberg-rest-catalog-integration-trust-relationship-sigv4) to get details to update the trust relationship of the role created to access table buckets through Snowflake (“snowflake\_access\_role”).

**Step 4:** Verify the catalog integration using the command below.

```
SELECT SYSTEM$VERIFY_CATALOG_INTEGRATION('glue_rest_catalog_int');
```

![9_verify catalog](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/9_verify-catalog.jpg)

**Step 5:** Run the below command to mount the S3 table as a Snowflake table.

```
  create iceberg table s3tables_dailysales
  CATALOG='glue_rest_catalog_int'
  CATALOG_TABLE_NAME="daily_sales"
  AUTO_REFRESH = TRUE;
```

### **Part 5. Access S3 Tables through Snowflake**

**Step 1:** Login to Snowflake as admin user who has permission to use catalog integration created.

**Step 2:** Run the following command to query the table “s3tables\_dailysales” on the “S3tables” bucket.

![10_s3 tables bucket](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/10_s3-tables-bucket.png)

## Cleaning up

To clean up your resources, complete the following steps:

1. [Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html) the S3 table.
2. [Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-delete.html) the namespace.
3. [Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-delete.html) the S3 table bucket.
4. You can also drop the [Iceberg table](https://docs.snowflake.com/en/sql-reference/sql/drop-iceberg-table), [catalog integration](https://docs.snowflake.com/en/sql-reference/sql/drop-catalog-integration), and [database](https://docs.snowflake.com/en/sql-reference/sql/drop-database) in Snowflake with the following commands:

```
DROP ICEBERG TABLE s3tables_dailysales;
DROP CATALOG INTEGRATION glue_rest_catalog_int;
DROP DATABASE rest_catalog_db;
```

## Conclusion

In this post, we’ve looked at connecting your Snowflake environment to query S3 Tables, using the SageMaker Lakehouse Iceberg REST endpoint. Combining Snowflake and AWS gives you multiple options to build out a transactional data lake for analytical and other use cases such as data sharing and collaboration.

TAGS: [Amazon Athena](https://aws.amazon.com/blogs/storage/tag/amazon-athena/), [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/blogs/storage/tag/amazon-simple-storage-service-amazon-s3/), [AWS Cloud Storage](https://aws.amazon.com/blogs/storage/tag/aws-cloud-storage/), [AWS Glue](https://aws.amazon.com/blogs/storage/tag/aws-glue/)

![Aritra Gupta](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2023/08/16/Aritra-Gupta.jpg)

### Aritra Gupta

Aritra Gupta is a Senior Technical Product Manager on the Amazon S3 team at Amazon Web Services. He helps customers build and scale data lakes. Based in Seattle, he likes to play chess and badminton in his spare time.

![Jeemin Sim](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/03/14/Jeemin_headshot.jpg)

### Jeemin Sim

Jeemin Sim is a Product Manager at Snowflake, focused on simplifying data architecture and helping organizations unlock the full potential of open formats with Snowflake. Jeemin also enjoys eating delicious food and spending time with her orange cat, Leo.

![Deepmala Agarwal](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2024/12/02/12.png)

### Deepmala Agarwal

Deepmala Agarwal works as an AWS Data Specialist Solutions Architect. She is passionate about helping customers build out scalable, distributed, and data-driven solutions on AWS. When not at work, Deepmala likes spending time with family, walking, listening to music, watching movies, and cooking!

![Frank Dallezotte](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2024/04/05/Frank.jpg)

### Frank Dallezotte

Frank Dallezotte is a Senior Solutions Architect at AWS and is passionate about working with independent software vendors to design and build scalable applications on AWS. He has experience creating software, implementing build pipelines, and deploying these solutions in the cloud.

![Srividya Parthasarathy](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/srivipar.jpg)

### Srividya Parthasarathy

Srividya Parthasarathy is a Senior Big Data Architect on the AWS Lake Formation team. She works with product team and customer to build robust features and solutions for their analytical data platform. She enjoys building data mesh solutions and sharing them with the community.

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