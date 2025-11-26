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

# Access data in Amazon S3 Tables using PyIceberg through the AWS Glue Iceberg REST endpoint

by Srividya Parthasarathy, Dylan Qu, Kalyan Kumar Neelampudi, and Aritra Gupta on 17 FEB 2025 in [Amazon Athena](https://aws.amazon.com/blogs/storage/category/analytics/amazon-athena/ "View all posts in Amazon Athena"), [Amazon QuickSight](https://aws.amazon.com/blogs/storage/category/analytics/amazon-quicksight/ "View all posts in Amazon QuickSight"), [Amazon Redshift](https://aws.amazon.com/blogs/storage/category/analytics/amazon-redshift-analytics/ "View all posts in Amazon Redshift"), [Amazon S3 Tables](https://aws.amazon.com/blogs/storage/category/storage/amazon-s3-tables/ "View all posts in Amazon S3 Tables"), [Amazon Simple Storage Service (S3)](https://aws.amazon.com/blogs/storage/category/storage/amazon-simple-storage-services-s3/ "View all posts in Amazon Simple Storage Service (S3)"), [Analytics](https://aws.amazon.com/blogs/storage/category/analytics/ "View all posts in Analytics"), [AWS Glue](https://aws.amazon.com/blogs/storage/category/analytics/aws-glue/ "View all posts in AWS Glue"), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/storage/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [AWS Lake Formation](https://aws.amazon.com/blogs/storage/category/analytics/aws-lake-formation/ "View all posts in AWS Lake Formation"), [Intermediate (200)](https://aws.amazon.com/blogs/storage/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Storage](https://aws.amazon.com/blogs/storage/category/storage/ "View all posts in Storage"), [Technical How-to](https://aws.amazon.com/blogs/storage/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/storage/access-data-in-amazon-s3-tables-using-pyiceberg-through-the-aws-glue-iceberg-rest-endpoint/)  [Comments](https://aws.amazon.com/blogs/storage/access-data-in-amazon-s3-tables-using-pyiceberg-through-the-aws-glue-iceberg-rest-endpoint/#Comments)  Share

Modern data lakes integrate with multiple engines to meet a wide range of analytics needs, from SQL querying to stream processing. A key enabler of this approach is the adoption of Apache Iceberg as the open table format for building transactional data lakes. However, as the Iceberg ecosystem expands, the growing variety of engines and languages has introduced significant integration challenges. Each engine needs its own client to connect to catalogs, which are the components responsible for tracking table metadata and evolution. This fragmented approach forces developers to manage multiple catalog integrations, thereby increasing pipeline complexity. The lack of a standardized solution often leads to data silos, inconsistent features across engines, and slower progress in analytics modernization efforts.

The [AWS Glue Iceberg REST endpoint](https://docs.aws.amazon.com/glue/latest/dg/access_catalog.html) addresses these challenges by providing a standardized interface for interacting with Iceberg tables. Fully aligned with the [Iceberg REST Catalog Open API specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml), the Glue Iceberg REST endpoint streamlines interoperability. This enables users to interact with Iceberg tables through a single, unified standard set of REST APIs across various engines, languages, and platforms. This, in conjunction with the enhanced performance of [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/), automated table maintenance, and streamlined security features, provides a strong foundation for users to build and scale data lakes on AWS.

In this post, we demonstrate how to access Iceberg tables stored in S3 Tables using [PyIceberg](https://py.iceberg.apache.org/) through the Glue Iceberg REST endpoint with [AWS Lake Formation](https://aws.amazon.com/lake-formation/) managing storage credential vending. PyIceberg is the official Python client of the Iceberg project, which provides a lightweight solution for discovering and querying Iceberg tables with your preferred Python tools. The same data consumption flow can also be applied to other compute engines that support the Iceberg REST catalog specification, providing a consistent and efficient experience across platforms.

## Solution overview

![Solution overview diagram](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/pyIcebergBlog-3.png)

This post references an example of a user using a local PyIceberg client to perform some basic data transformations, such as table creation, data ingestion, updates, and time travel. This workflow showcases a common development pattern where developers use local environments to prototype and iterate on data transformation pipelines before deploying them at scale.

We begin by creating a table bucket to store Iceberg tables. Then, we configure the PyIceberg client to interact with the Iceberg table through the AWS Glue Iceberg REST endpoint. All permissions are centrally managed using Lake Formation.

## Prerequisites

To follow along, you need the following setup:

1. You need access to an [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that is a Lake Formation data lake administrator in the Data Catalog account. For instructions, go to [Create a data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin).

2. Verify that you have Python version 3.7 or later installed. Check if pip3 version is 22.2.2 or higher is installed.

3. Install or update to the latest [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli). For instructions, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Run the AWS configure command using the AWS CLI to point to your AWS account.

## Walkthrough

The following steps walk you through this solution.

### Step 1: Create a table bucket and enable Glue Data Catalog integration for S3 Tables:

1.1. Log in to the [Amazon S3 console](https://console.aws.amazon.com/s3) using Admin role and choose **Table Buckets** from the navigation panel, as shown in the following figure.

![Table buckets](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/image002.jpg)

1.2. Choose **Enable integration**. When the integration is successfully integrated, you should see it enabled for your table buckets, as shown in the following figure.

![Integration with AWS analytics services](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/image003-scaled.jpg)

1.3. From the left pane of Amazon S3, choose **Table buckets**. Choose **Create table bucket.**

1.4. Under **Properties**, enter the Table bucket name as `pyiceberg-blog-bucket` and choose **Create table bucket.**

### Step 2: Create IAM role for the local PyIceberg environment

You need to create an IAM role for the PyIceberg script to access Glue and Lake Formation APIs. To do this you create the following policy and role:

2.1. Create the policy and name it `irc-glue-lf-policy`. Here are some steps to do it through the [AWS Management Console](https://aws.amazon.com/console/):

a. Sign in to the console.

b. Open the IAM console.

c. In the navigation pane of the console, choose **Policies** and choose the **Create Policy** option.

d. In the policy editor choose **JSON** and paste the following policies.

i. Replace `<region>`, `<account-id>`, `<s3_table_bucket_name>`, and `<database_name>` in the following policy as per your [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), AWS account ID, S3 table bucket name, and database name respectively. We use `myblognamespace` as the database name in the rest of this post.

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
                "glue:GetTables",
                "glue:CreateTable",
                "glue:UpdateTable"
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

2.2. Create a role named `pyiceberg-etl-role` by following these steps in the IAM console.

a. In the navigation pane of the console, choose **Roles** and choose the **Create role**option.

b. Choose **Custom trust policy** and paste the following policy.

i. Replace `<account-id>` and `<Admin_role>` in the following policy as per your data lake admin ARN.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<accountid>:role/<Admin_role>"
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
        }
    ]
}
```

c. Choose **Next** and choose the policy you previously created in Step 2a, named `irc-glue-lf-policy`.

d. Choose **Next** and enter `pyiceberg-etl-role` as the role name.

e. Choose **Create role**.

When you create the role, you need to define access to this role using Lake Formation.

### Step 3: Define access control using Lake Formation

3.1. Application integration setup:

a. In Lake Formation, enable full table access for external engines to access data. This allows third-party applications to get the Lake Formation temporary credential using an IAM role(s) that has full permissions (ALL) on the requested table.

i. Sign in as an admin user and go to [Lake Formation](https://us-east-1.console.aws.amazon.com/lakeformation/home).

ii. On the Left Pane, expand the **Administration** section.

iii. Choose **Application integration settings** and choose **Allow external engines to access data in Amazon S3 locations with full table access**.

iv. Choose **Save,** as shown in the following figure.

![Application integration settings](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/image004-1.jpg)

3.2. Create a database:

a. In the Lake Formation console navigation pane, choose **Databases** under **Data Catalog.**

b. Choose **Create database**, and provide the name `myblognamespace`.

c. Choose the Data Catalog created in Step 1 (`<accountid>:s3tablescatalog/pyiceberg-blog-bucket`) from the drop-down.

d. Choose **Create database.**

e. Refresh the browser if the database does not show up.

After you create the database, you need to set up Lake Formation grants for the role used by the PyIceberg client to create and manage tables under this database. To do this you need to provide database and table level permissions to the `pyiceberg-etl-role`.

3.3. Set up database level permissions:

Grant the following permissions to the `pyiceberg-etl-role` role on the resources as shown in the following table.

a. In the Lake Formation console navigation pane, choose **Data permissions**, then choose **Grant**.

b. In the **Principals** section, choose the radio button **IAM users and roles**, and from the drop-down choose `pyiceberg-etl-role`.

c. In the **LF-Tags** or **catalog resources** section, choose **Named Data Catalog** resources:

i. Choose `<accountid>:s3tablescatalog/pyiceberg-blog-bucket` for Catalogs.

ii. Choose `mynamespace` for Databases.

d. Choose **CREATE TABLE, DESCRIBE** for database permissions.

e. Choose **Grant**.

3.4. Set up table level permissions:

a. In the Lake Formation console navigation pane, choose **Data permissions**, then choose **Grant**.

b. In the **Principals** section, choose the radio button **IAM users and roles**, and from the drop-down choose `pyiceberg-etl-role`.

c. In the **LF-Tags** or **catalog resources** section, choose **Named Data Catalog** resources:

i. Choose `<accountid>:s3tablescatalog/pyiceberg-blog-bucket` for Catalogs.

ii. Choose **mynamespace** for Databases.

iii. Choose **ALL\_TABLES** for Tables.

d. Choose **SUPER** for table permissions.

e. Choose **Grant**.

Now that the permissions are set up, you can set up a local PyIceberg environment to use S3 Tables.

### Step 4: Set up local PyIceberg environment

4.1. Install Python along with the following packages:

```
pip install "pyiceberg[pandas,pyarrow]"

pip install boto3

pip install tabulate
```

4.2. [Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) to log in as the Admin user on your local machine and assume the `spark-etl-role` with the following command:

```
aws sts assume-role --role-arn "arn:aws:iam::<accountid>:role/pyiceberg-etl-role" --role-session-name pyiceberg-etl-role
```

4.3. Copy the credentials and replace the following placeholders to configure environment variables.

```
export AWS_ACCESS_KEY_ID='<AccessKeyId>'
export AWS_SECRET_ACCESS_KEY='<SecretAccessKey>'
export AWS_SESSION_TOKEN='<SessionToken>'
export AWS_DEFAULT_REGION='<region>'
```

Next, use a PyIceberg setup locally to create a table and load data, and perform basic queries.

### Step 5: Run PyIceberg script

In this post, we highlight the key steps incrementally. You can [download the entire Python script](https://aws-bigdata-blog.s3.us-east-1.amazonaws.com/artifacts/s3tables-pyiceberg/blogcode_pyiceberg.py) and run `python blogcode_pyiceberg.py --table customer`.

First, we import some libraries and initialize constants that we use throughout our script.

```
#!/usr/bin/env python3
from pyiceberg.catalog import load_catalog
import os
import pyarrow as pa
import pandas as pd
from pyiceberg.expressions import EqualTo
import boto3
import json
import argparse
from botocore.exceptions import ProfileNotFound
from datetime import datetime
from tabulate import tabulate

# Constants
REGION = 'us-east-2'
CATALOG = 's3tablescatalog'
DATABASE = 'myblognamespace'
TABLE_BUCKET = 'pyiceberg-blog-bucket'
```

We initialize catalog using the Glue Iceberg REST endpoint.

```
rest_catalog = load_catalog(
        $CATALOG,
        **{
            "type": "rest",
            "warehouse": f"{account_id}:s3tablescatalog/$TABLE_BUCKET",
            "uri": f"https://glue.{region}.amazonaws.com/iceberg",
            "rest.sigv4-enabled": "true",
            "rest.signing-name": "glue",
            "rest.signing-region": region
        }
    )
```

We define a table schema.

```
def create_customer_schema() -> pa.Schema:
    """
    Create and return the PyArrow schema for customer table.
    """
    return pa.schema([
        pa.field('c_salutation', pa.string()),
        pa.field('c_preferred_cust_flag', pa.string()),
        pa.field('c_first_sales_date_sk', pa.int32()),
        pa.field('c_customer_sk', pa.int32()),
        pa.field('c_first_name', pa.string()),
        pa.field('c_email_address', pa.string())
    ])
```

Then, we create a table with the following schema.

```
my_schema = create_customer_schema()
# Check if table exists before creating
        try:
            rest_catalog.create_table(
                identifier=f"{database_name}.{table_name}",
                schema=my_schema
            )
            print("Table created successfully")
        except Exception as e:
            print(f"Table creation note: {str(e)}")
```

We load a sample customer data to the table.

```
def get_sample_customer_data() -> dict:
    return {
        "c_salutation": "Ms",
        "c_preferred_cust_flag": "NULL",
        "c_first_sales_date_sk": 2452736,
        "c_customer_sk": 1234,
        "c_first_name": "Mickey",
        "c_email_address": "mickey@email.com"
    }
sample_data = get_sample_customer_data()
        df = pa.Table.from_pylist([sample_data], schema=my_schema)
        table.append(df)
```

We query the table.

```
tabledata = table.scan(
row_filter=EqualTo("c_first_name", "Mickey"),
limit=10
).to_pandas()
```

![update the value of the “c_preferred_cust_flag” column and display the change](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/image005.png)

Then, we update the value of the `c_preferred_cust_flag` column and display the change.

```
condition = tabledata['c_preferred_cust_flag'] == 'NULL'
        tabledata.loc[condition, 'c_preferred_cust_flag'] = 'N'
        df2 = pa.Table.from_pandas(tabledata, schema=my_schema)
        table.overwrite(df2)
```

![display the snapshot history](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/image006-1.png)

Finally, we display the snapshot history.

```
print("\n⏰ Performing Time Travel Operations...")
        customer_snapshots = table.snapshots()
        print_snapshot_info(customer_snapshots)
```

![Snapshot history](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/image007-1.png)

## Cleaning up

To clean up your resources, complete the following steps:

1. [Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html) the **Amazon S3 table.**
2. [Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-delete.html) the **namespace.**
3. [Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-delete.html) the **S3** **table bucket.**

## Conclusion

In this post, we’ve showcased an example of how you can use PyIceberg to create, load, and query data in S3 Tables using the AWS Glue Iceberg REST endpoint. Integrating your table buckets with the AWS Glue Data Catalog (in preview) allows you to query and visualize data using AWS Analytics services such as [Amazon Athena](https://aws.amazon.com/athena/), [Amazon Redshift](https://aws.amazon.com/redshift/), and [Amazon QuickSight](https://aws.amazon.com/quicksight/), and open source clients such as PyIceberg.

TAGS: [Amazon Athena](https://aws.amazon.com/blogs/storage/tag/amazon-athena/), [Amazon Quicksight](https://aws.amazon.com/blogs/storage/tag/amazon-quicksight/), [Amazon Redshift](https://aws.amazon.com/blogs/storage/tag/amazon-redshift/), [Amazon S3](https://aws.amazon.com/blogs/storage/tag/amazon-s3/), [AWS Glue](https://aws.amazon.com/blogs/storage/tag/aws-glue/), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/storage/tag/aws-identity-and-access-management-iam/)

![Srividya Parthasarathy](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/srivipar.jpg)

### Srividya Parthasarathy

Srividya Parthasarathy is a Senior Big Data Architect on the AWS Lake Formation team. She works with product team and customer to build robust features and solutions for their analytical data platform. She enjoys building data mesh solutions and sharing them with the community.

![Dylan Qu](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2020/09/16/Dylan-Qu.jpg)

### Dylan Qu

Dylan Qu is a Specialist Solutions Architect focused on Big Data & Analytics with AWS. He helps customers architect and build highly scalable, performant, and secure cloud-based solutions on AWS.

![Kalyan Kumar Neelampudi](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/14/kalyan.jpg)

### Kalyan Kumar Neelampudi

Kalyan Kumar Neelampudi (KK) is a Specialist Partner Solutions Architect at AWS, focusing on Data Analytics and Generative AI from Austin, Texas. As a technical advisor to AWS partners, KK helps architect and implement cutting-edge data analytics and AI/ML solutions, driving innovation in cloud technologies. When he's not architecting cloud solutions, KK maintains an active lifestyle, enjoying competitive sports like badminton and pickleball.

![Aritra Gupta](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2024/12/02/14.png)

### Aritra Gupta

Aritra Gupta is a Senior Technical Product Manager on the Amazon S3 team at AWS. He helps customers build and scale multi-region architectures on Amazon S3. Based in Seattle, he likes to play chess and badminton in his spare time.

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