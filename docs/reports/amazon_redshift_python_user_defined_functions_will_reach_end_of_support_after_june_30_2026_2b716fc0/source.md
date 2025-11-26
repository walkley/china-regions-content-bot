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

## [AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/)

# Amazon Redshift Python user-defined functions will reach end of support after June 30, 2026

by Raks Khare, Harshida Patel, Ritesh Sinha, and Yanzhu Ji on 30 JUN 2025 in [Amazon Redshift](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-redshift-analytics/ "View all posts in Amazon Redshift"), [Announcements](https://aws.amazon.com/blogs/big-data/category/post-types/announcements/ "View all posts in Announcements") [Permalink](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/)  [Comments](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/#Comments)  Share

The [Amazon Redshift](http://aws.amazon.com/redshift) integration with [AWS Lambda](http://aws.amazon.com/lambda) provides the capability to create Amazon Redshift Lambda user-defined functions (UDFs). This capability delivers flexibility, enhanced integrations, and security for functions defined in Lambda that can be run through SQL queries. Amazon Redshift Lambda UDFs offer many advantages:

* **Enhanced integration** – You can connect to external services or APIs from within your UDF logic, enabling richer data enrichment and operational workflows.
* **Multiple Python runtimes** – Lambda UDFs benefit from Lambda function support for [multiple Python runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html) depending on specific use cases. In addition, the new versions and security patches are available within a month of their [official release](https://www.python.org/doc/versions/).
* **Independent scaling** – Lambda UDFs use Lambda compute resources, so heavy compute or memory-intensive tasks don’t impact query performance or resource concurrency within Amazon Redshift.
* **Isolation and security** – You can isolate custom code execution in a separate service boundary. This simplifies maintenance, monitoring, budgeting, and permission management.

Because Lambda UDFs provide these significant advantages in integration, flexibility, scalability, and security, we will be ending support for Python UDFs in Amazon Redshift. We recommend that you migrate your existing Python UDFs to Lambda UDFs by June 30, 2026.

* **January 31, 2026** – Creation of new Python UDFs will no longer be supported (existing functions can still be invoked)
* **June 30, 2026** – Execution of existing Python UDFs will be suspended

In this post, we walk you through how to migrate your existing Python UDFs to Lambda UDFs, set up monitoring and cost evaluations, and review key considerations for a smooth transition.

## Solution overview

You can create UDFs for tasks such as [tokenization](https://aws.amazon.com/blogs/apn/data-tokenization-with-amazon-redshift-and-protegrity/), [encryption](https://github.com/aws-samples/amazon-redshift-udfs/tree/master/lambda-udfs/f_kms_encrypt%28varchar%2Cvarchar%29) and [decryption](https://github.com/aws-samples/amazon-redshift-udfs/tree/master/lambda-udfs/f_kms_decrypt%28varchar%29), or data science functionality like the Levenshtein distance calculation. For this post, we provide examples for customers who have Python UDFs in place, demonstrating how to replace them with Lambda UDFs.

The [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance) function, also known as the Levenshtein distance or edit distance, is a string metric used to measure the difference between two sequences of characters. Although this functionality was previously implemented using Python UDFs using the Python library in Amazon Redshift, Lambda provides a more efficient and scalable solution. This post demonstrates how to migrate from Python UDFs to Lambda UDFs for calculating Levenshtein distances.

## Prerequisites

You must have the following:

* [An AWS account](https://aws.amazon.com/resources/create-account/).
* One of the following resources, depending on your use case:
  + A Redshift cluster if you are using [Amazon Redshift Provisioned](https://docs.aws.amazon.com/redshift/latest/mgmt/overview.html). For instructions, refer to [Create a sample Amazon Redshift cluster](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-launch-sample-cluster.html).
  + A Redshift workgroup if you are using [Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html). For instructions, refer to [Create a workgroup with a namespace](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.html).
* An [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) [role](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service.html#authorizing-redshift-service-creating-an-iam-role) that is able to ingest data from [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) to Amazon Redshift. Set the IAM role [as the default](https://docs.aws.amazon.com/redshift/latest/mgmt/default-iam-role.html#managing-iam-role-console) for Amazon Redshift.
* Permissions to create Lambda functions and access [Amazon CloudWatch](http://aws.amazon.com/cloudwatch).

## Prepare the data

To set up our use case, complete the following steps:

1. On the Amazon Redshift console, choose **Query editor v2** under **Explorer** in the navigation pane.
2. Connect to your Redshift data warehouse.
3. Create a table and load data. The following query loads 30,000,000 rows in the `customer` table:

```
DROP TABLE IF EXISTS customer;
CREATE TABLE customer
(
c_customer_sk int4 not null ,
c_customer_id char(16) not null ,
c_current_cdemo_sk int4 ,
c_current_hdemo_sk int4 ,
c_current_addr_sk int4 ,
c_first_shipto_date_sk int4 ,
c_first_sales_date_sk int4 ,
c_salutation char(10) ,
c_first_name char(20) ,
c_last_name char(30) ,
c_preferred_cust_flag char(1) ,
c_birth_day int4 ,
c_birth_month int4 ,
c_birth_year int4 ,
c_birth_country varchar(20) ,
c_login char(13) ,
c_email_address char(50) ,
c_last_review_date_sk int4 ,
primary key (c_customer_sk)
) distkey(c_customer_sk);

COPY customer from 's3://redshift-downloads/TPC-DS/2.13/3TB/customer/'
IAM_ROLE default gzip delimiter '|' EMPTYASNULL REGION 'us-east-1';
```

## Identify existing Python UDFs

Run the following script to list existing Python UDFs:

```
SELECT
    p.proname,
    p.pronargs,
    t.typname,
    n.nspname,
    l.lanname,
    pg_get_functiondef(p.oid)
FROM
    pg_proc p,
    pg_language l,
    pg_type t,
    pg_namespace n
WHERE
    p.prolang = l.oid
    and p.prorettype = t.oid
    and l.lanname = 'plpythonu'
    and p.pronamespace = n.oid
    and nspname not in ('pg_catalog', 'information_schema')
ORDER BY
    proname;
```

The following is our existing Python UDF definition for Levenshtein distance:

```
create or replace function fn_levenshtein_distance(a varchar, b varchar) returns integer as
$$

def levenshtein_distance(a, len_a, b, len_b):
    d = [[0] * (len_b + 1) for i in range(len_a + 1)]

    for i in range(1, len_a + 1):
        d[i][0] = i

    for j in range(1, len_b + 1):
        d[0][j] = j

    for j in range(1, len_b + 1):
        for i in range(1, len_a + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,      # deletion
                          d[i][j - 1] + 1,      # insertion
                          d[i - 1][j - 1] + cost) # substitution

    return d[len_a][len_b]

def distance(a, b):
    len_a, len_b = len(a), len(b)
    if len_a == len_b:
        return 0
    elif len_a == 0:
        return len_b
    elif len_b == 0:
        return len_a
    else:
        return levenshtein_distance(a, len_a, b, len_b)

return distance(a, b)
$$ immutable;
```

## Convert the Python UDF function to a Lambda UDF

You can simplify converting your Python UDF to a Lambda UDF using [Amazon Q Developer](https://aws.amazon.com/q/developer/), a generative AI-powered assistant. It handles code transformation, packaging, and integration logic, accelerating migration and improving scalability. Integrated with popular developer tools like VS Code, JetBrains, and others, Amazon Q streamlines workflows so teams can modernize analytics using serverless architectures with minimal effort.

Amazon Q Developer code suggestions are based on large language models (LLMs) trained on billions of lines of code, including open source and Amazon code. Always review a code suggestion before accepting it, and you might need to edit it to make sure that it does exactly what you intended.

```
Convert @python-udf.py Redshift Python UDF to Redshift Lambda UDF which batch processes data in the arguments array in a loop and returns json dump at the end. Refer to @lambda-context.py for reference and additional guidance on Lambda UDF.
```

## Create a Lambda function

Complete the following steps to create a Lambda function:

1. On the Lambda console, choose **Functions** in the navigation pane.
2. Choose **Create function**.
3. Choose **Author from scratch**.
4. For **Function name**, enter a custom name (for example, `levenshtein_distance_func`).
5. **For Runtime**, choose your code environment. (The examples in this post are compatible with Python 3.12.)
6. For **Architecture**, select your system architecture. (The examples in this post are compatible with x86\_64.)

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/06/27/image-1-6.jpg)

7. For **Execution role**, select **Create a new role with basic Lambda permissions**.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/06/27/image-2-5.jpg)

8. Choose **Create function**.
9. Choose **Code** and add the following code:

```
import json

def lambda_handler(event, context):
    t1 = event['arguments']
    resp = [None]*len(t1)

    for i, x in enumerate(t1):
        if x[0] is not None and x[1] is not None:
            resp[i] = distance(x[0], x[1])

    ret = dict()
    ret['results'] = resp
    return json.dumps(ret)

def levenshtein_distance(a, len_a, b, len_b):
    d = [[0] * (len_b + 1) for i in range(len_a + 1)]

    for i in range(1, len_a + 1):
        d[i][0] = i

    for j in range(1, len_b + 1):
        d[0][j] = j

    for j in range(1, len_b + 1):
        for i in range(1, len_a + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,      # deletion
                          d[i][j - 1] + 1,      # insertion
                          d[i - 1][j - 1] + cost) # substitution

    return d[len_a][len_b]

def distance(a, b):
    len_a, len_b = len(a), len(b)
    if len_a == len_b and a == b:
        return 0
    elif len_a == 0:
        return len_b
    elif len_b == 0:
        return len_a
    else:
        return levenshtein_distance(a, len_a, b, len_b)
```

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/BDB-5212/My+Movie.mp4?_=1)

10. Choose configuration and update **Timeout** to 1 minute.

You can modify memory to optimize performance. To learn more, see [Optimizing Levenshtein User-Defined Function in Amazon Redshift](https://repost.aws/fr/articles/ARA8oXevNjTP6ISHBU526Riw/optimizing-levenshtein-user-defined-function-in-amazon-redshift?sc_ichannel=ha&sc_ilang=en&sc_isite=repost&sc_iplace=hp&sc_icontent=ARA8oXevNjTP6ISHBU526Riw&sc_ipos=13).

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/06/27/image-4-3.jpg)

## Create an Amazon Redshift IAM role

To allow your Amazon Redshift cluster to invoke the Lambda function, you must set up proper IAM permissions. Complete the following steps:

1. Identify the IAM role associated with your Amazon Redshift cluster. If you don’t have one, [create a new IAM role](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html) for Amazon Redshift.
2. Add the following IAM policy to this role, providing your AWS Region and AWS account number:

```
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": "lambda:InvokeFunction",
"Resource": "arn:aws:lambda:<REGION>:<AWS account>:function:levenshtein_distance_func"
}
]
}
```

## Create a Lambda UDF

Run following script to create your Lambda UDF:

```
CREATE or REPLACE EXTERNAL FUNCTION
fn_lambda_levenshtein_distance(a varchar, b varchar) returns int
lambda 'levenshtein_distance_func' IAM_ROLE default
STABLE
;
```

## Test the solution

To test the solution, run the following script using the Python UDF:

```
SELECT c_customer_sk, c_customer_id, fn_levenshtein_distance(c_first_name, c_last_name) as distance
FROM customer
WHERE c_customer_sk in (1,2,3,4,5,31);
```

The following table shows our output.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/06/27/image-5-2.jpg)

Run the same script using the Lambda UDF:

```
SELECT c_customer_sk, c_customer_id, fn_lambda_levenshtein_distance(c_first_name, c_last_name) as distance
FROM customer
WHERE c_customer_sk in (1,2,3,4,5,31);
```

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/06/27/image-6-1.jpg)

The results of both UDFs match.

## Replace the Python UDF with the Lambda UDF

You can use the following steps in preproduction for testing:

1. Revoke access for the Python UDF:

```
REVOKE execute on function fn_levenshtein_distance(varchar, varchar) from <group_name> or <role_name>
```

2. Grant access to the Lambda UDF:

```
grant execute on function fn_lambda_levenshtein_distance(varchar, varchar) to <group_name> or <role_name>
```

3. After full testing of the Lambda UDF has been performed, you can drop the Python UDF.
4. Rename the Lambda UDF `fn_lambda_levenshtein_distance` to `fn_levenshtein_distance` so the end-user and application code doesn’t need to change:

```
ALTER FUNCTION fn_lambda_levenshtein_distance(varchar, varchar)
     RENAME TO fn_levenshtein_distance;
```

5. Validate with the following query:

```
SELECT c_customer_sk, c_customer_id, fn_levenshtein_distance(c_first_name, c_last_name) as distance
FROM customer
WHERE c_customer_sk in (1,2,3,4,5,31);
```

## Cost evaluation

To evaluate the cost of the Lambda UDF, complete the following steps:

1. Run the following script to create a table using a SELECT query, which uses the Lambda UDF:

```
DROP TABLE IF EXISTS customer_lambda;
CREATE TABLE customer_lambda as
SELECT c_customer_sk, c_customer_id, fn_levenshtein_distance(c_first_name, c_last_name) as distance
FROM customer;
```

You can inspect the query logs using [CloudWatch Log Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html).

2. On the CloudWatch console, choose **Logs** in the navigation pane, then choose **Log Insights**.
3. Filter by the Lambda UDF and use the following query to identify the number of Lambda invocations.

```
fields @timestamp, @message, @logStream, @log
| filter @message like /^REPORT/
| sort @timestamp desc
| limit 10000
```

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/06/27/image-7-1.jpg)

4. Use following query to find the cost of the Lambda UDF for the specific duration you selected:

```
parse @message /Duration:\s*(?<@duration_ms>\d+\.\d+)\s*ms\s*Billed\s*Duration:\s*(?<@billed_duration_ms>\d+)\s*ms\s*Memory\s*Size:\s*(?<@memory_size_mb>\d+)\s*MB/
| filter @message like /REPORT RequestId/
| stats sum(@billed_duration_ms * @memory_size_mb * 1.6279296875e-11 + 2.0e-7) as @cost_dollars_total
```

For this example, we used the `us-east-1` Region using ARM-based instances. For more details on Lambda pricing by Region and the Free Tier limit, see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).

5. Choose **Summarize results**.

The cost of this Lambda UDF invocation was $0.02329 for 30 million rows.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/06/27/image-8-1.jpg)

## Monitor Lambda UDFs

Monitoring Lambda UDFs involves tracking both the Lambda function’s performance and the impact on the Redshift query execution. Because UDFs execute externally, a dual approach is necessary.

### CloudWatch metrics and logs for Lambda functions

CloudWatch provides comprehensive monitoring for Lambda functions, such as the following key metrics:

* **Invocations** – Tracks the number of times the Lambda function is called, indicating UDF usage frequency
* **Duration** – Measures execution time, helping identify performance bottlenecks
* **Errors** – Counts failed invocations, which is critical for detecting issues in UDF logic
* **Throttles** – Indicates when Lambda limits invocations due to concurrency caps, which can delay query results
* **Logs** – CloudWatch Logs capture detailed execution output, including errors and custom log messages, aiding in debugging
* **Alarms** – Configures alarms for high error rates (for example, Errors > 0) or excessive duration (for example, Duration > 1 second) to receive proactive notifications

### Redshift query performance

Within Amazon Redshift, system views provide comprehensive insights into Lambda UDF performance and errors:

* **SYS\_QUERY\_HISTORY** – Identifies queries that have called your Lambda UDFs by filtering with the UDF name in the `query_text` column. This helps track usage patterns and execution frequency.
* **SYS\_QUERY\_DETAIL** – Provides granular execution metrics for queries involving Lambda UDFs, helping identify performance bottlenecks at the step level.
* **Performance aggregation** – Generates summary reports of Lambda UDF performance metrics, including execution count, average duration, and maximum duration to track performance trends over time.

The following table summarizes the monitoring tools available.

|  |  |  |
| --- | --- | --- |
| **Monitoring Tool** | **Purpose** | **Key Metrics/Views** |
| CloudWatch Metrics | Track Lambda function performance | Invocations, Duration, Errors, Throttles |
| CloudWatch Logs | Debug Lambda execution issues | Error messages, custom logs |
| SYS\_QUERY\_HISTORY | Track Lambda UDF usage patterns | Query execution times, status, user information, query text |
| SYS\_QUERY\_DETAIL | Analyze Lambda UDF performance | Step-level execution details, resource utilization, query plan information |
| Performance Summary Reports | Track UDF performance trends | Execution count, average/maximum duration, total elapsed time |

### Monitoring approach for Lambda UDFs in Amazon Redshift

For analyzing individual queries, you can use the following code to track how your Lambda UDFs are being used across your organization:

```
SELECT * FROM sys_query_history
WHERE query_text LIKE '%your_lambda_udf_name%'
ORDER BY start_time DESC
LIMIT 20;
```

This helps you do the following:

* Identify frequent users
* Monitor execution patterns
* Track usage trends
* Detect unauthorized access

You can also create comprehensive monitoring by using query history to monitor performance metrics at the user level:

```
SELECT
    usename,
    DATE_TRUNC('day', start_time) as day,
    COUNT(*) as query_count,
    AVG(DATEDIFF(microsecond, start_time, end_time))/1000000.0 as avg_duration_seconds,
    MAX(DATEDIFF(microsecond, start_time, end_time))/1000000.0 as max_duration_seconds
FROM sys_query_history q
JOIN pg_user u ON q.user_id = u.usesysid
WHERE query_text LIKE '%your_lambda_udf_name%'
AND user_id > 1
GROUP BY usename, day
ORDER BY usename, query_count DESC;
```

Additionally, you can generate weekly performance reports using the following aggregation query:

```
SELECT
    'your_lambda_udf_name' AS function_name,
    COUNT(DISTINCT q.query_id) AS execution_count,
    AVG(DATEDIFF(millisecond, q.start_time, q.end_time)) AS avg_duration_ms,
    MAX(DATEDIFF(millisecond, q.start_time, q.end_time)) AS max_duration_ms,
    SUM(q.elapsed_time) / 1000000 AS total_elapsed_time_sec
FROM
    sys_query_history q
WHERE
    q.query_text LIKE '%your_lambda_udf_name%'
GROUP BY
    function_name
ORDER BY
    execution_count DESC;
```

## Considerations

To maximize the benefits of Lambda UDFs, consider the following aspects to optimize performance, provide reliability, secure data, and manage costs. If you have Python UDFs that don’t use Python libraries, consider whether they are candidates to convert to [SQL UDFs](https://docs.aws.amazon.com/redshift/latest/dg/udf-creating-a-scalar-sql-udf.html).

The following are key performance considerations:

* **Batching** – Amazon Redshift batches multiple rows into a single Lambda invocation to reduce call frequency, improving efficiency. Make sure the Lambda function handles batched inputs efficiently. For more details, see [Accessing external components using Amazon Redshift Lambda UDFs](https://aws.amazon.com/blogs/big-data/accessing-external-components-using-amazon-redshift-lambda-udfs/).
* **Parallel invocations** – Redshift cluster slices invoke Lambda functions in parallel, enhancing performance for large datasets. Design functions to support concurrent executions.
* **Cold starts** – Lambda functions might experience cold start delays, particularly if infrequently used. Languages like Python or Node.js typically have faster startup times than Java, reducing latency.
* **Function optimization** – Optimize Lambda code for quick execution, minimizing resource usage and latency. For example, avoid unnecessary computations or external API calls.

Consider the following error handling methods:

* **Robust lambda logic** – Implement comprehensive error handling in the Lambda function to manage exceptions gracefully. Return clear error messages in the JSON response, as specified in the Amazon Redshift-Lambda interface. For more details, see [Scalar Lambda UDFs](https://docs.aws.amazon.com/redshift/latest/dg/udf-creating-a-lambda-sql-udf.html).
* **Error propagation** – Lambda errors can cause Redshift query failures. Monitor `SYS_QUERY_HISTORY` for query-level issues and CloudWatch Logs for detailed Lambda errors.
* **JSON interface** – The Lambda function must return a JSON object with `success`, `error_msg`, `num_records`, and `results` fields. Use proper formatting to avoid query disruptions.

## Clean up

Complete the following steps to clean up your resources:

1. Delete the Redshift provisioned or serverless endpoint.
2. Delete the Lambda function.
3. Delete the IAM roles you created.

## Conclusion

Lambda UDFs unlock a new level of flexibility, performance, and maintainability for extending Amazon Redshift. By decoupling custom logic from the warehouse engine, teams can scale independently, adopt modern runtimes, and integrate external systems.

If you’re currently using Python UDFs in Amazon Redshift, it’s time to explore the benefits of migrating to Lambda UDFs. With the generative AI capabilities of Amazon Q Developer, you can automate much of this transformation and accelerate your modernization journey. To learn more, refer to the [Lambda UDF examples GitHub repo](https://github.com/aws-samples/amazon-redshift-udfs/tree/master/lambda-udfs) and [Data Tokenization with Amazon Redshift and Protegrity](https://aws.amazon.com/blogs/apn/data-tokenization-with-amazon-redshift-and-protegrity/).

---

### About the authors

**![Raks Khare](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2022/05/31/BDB-2083-Raks.jpg)Raks Khare** is a Senior Analytics Specialist Solutions Architect at AWS based out of Pennsylvania. He helps customers across varying industries and regions architect data analytics solutions at scale on the AWS platform. Outside of work, he likes exploring new travel and food destinations and spending quality time with his family.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2024/10/25/ritesh-100-1.png)**Ritesh Kumar Sinha** is an Analytics Specialist Solutions Architect based out of San Francisco. He has helped customers build scalable data warehousing and big data solutions for over 16 years. He loves to design and build efficient end-to-end solutions on AWS. In his spare time, he loves reading, walking, and doing yoga.

**![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2022/07/08/Yanzhu-Ji.png)Yanzhu Ji** is a Product Manager in the Amazon Redshift team. She has experience in product vision and strategy in industry-leading data products and platforms. She has outstanding skill in building substantial software products using web development, system design, database, and distributed programming techniques. In her personal life, Yanzhu likes painting, photography, and playing tennis.

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2022/01/28/hspatel.png)**Harshida Patel** is a Analytics Specialist Principal Solutions Architect, with AWS.

Loading comments…

### Resources

* [Amazon Athena](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-athena?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon EMR](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-emr?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Kinesis](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon MSK](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-managed-streaming-for-apache-kafka/)
* [Amazon QuickSight](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-quicksight?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [Amazon Redshift](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-redshift-analytics?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)
* [AWS Glue](https://aws.amazon.com/blogs/big-data/category/analytics/aws-glue?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=bigdata-social)

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