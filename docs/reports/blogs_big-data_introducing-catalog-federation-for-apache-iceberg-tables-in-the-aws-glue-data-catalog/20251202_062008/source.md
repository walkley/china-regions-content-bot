# Introducing catalog federation for Apache Iceberg tables in the AWS Glue Data Catalog

by Debika D, Pratik Das, and Srividya Parthasarathy on 26 NOV 2025 in Advanced (300), Amazon SageMaker, Announcements, AWS Glue, AWS Lake Formation Permalink  Comments   Share

Apache Iceberg has become the standard choice of open table format for organizations seeking robust and reliable analytics at scale. However, enterprises increasingly find themselves navigating complex multi-vendor landscapes with disparate catalog systems. Managing data across these has become a major challenge for organizations operating in multi-vendor environments. This fragmentation drives significant operational complexity, particularly around access control and governance. Customers using AWS analytics services such as [Amazon Redshift](https://aws.amazon.com/redshift), [Amazon EMR](https://aws.amazon.com/emr/), [Amazon Athena](https://aws.amazon.com/athena), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), and [AWS Glue](https://aws.amazon.com/glue) to analyze Iceberg tables in the [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html) want to get the same price-performance for workloads in remote catalogs. Simply migrating or replacing these remote catalogs isn’t practical, leaving teams to implement and maintain synchronization processes that continuously replicate metadata across systems, creating operational overhead, escalating costs, and risking data inconsistencies.

AWS Glue now supports catalog federation for remote Iceberg tables in the Data Catalog. With catalog federation, you can query remote Iceberg tables, stored in [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3) and cataloged in remote Iceberg catalogs, using AWS analytics engines and without moving or duplicating tables. After a remote catalog is integrated, AWS Glue always fetch the latest metadata in the background, so you always have access to the Iceberg metadata through your preferred AWS analytics services. This capability supports both coarse-grained access control and fine-grained permissions through [AWS Lake Formation](https://aws.amazon.com/lake-formation/), giving you the flexibility on how and when remote Iceberg tables are shared with data consumers. With integration for Snowflake Polaris Catalog, Databricks Unity Catalog, and other custom catalogs supporting Iceberg REST specifications, you can federate to remote catalogs, discover databases and tables, configure access permissions, and begin querying remote Iceberg data.

In this post, we discuss how to get started with catalog federation for Iceberg tables in the Data Catalog.

## Solution overview

Catalog federation uses the Data Catalog to communicate with remote catalog systems to discover catalog objects and Lake Formation to authorize access to their data in Amazon S3. When you query a remote Iceberg table, the Data Catalog discovers the latest table information in the remote catalog at query runtime, getting the table’s S3 location, current schema, and partition information. Your analytics engine (Athena, Amazon EMR, or Amazon Redshift) Your analytics engine (Athena, EMR, or Redshift) then uses this information to access Iceberg data files directly from Amazon S3. And Lake Formation manages access to the table by vending scoped credentials to the table data stored in Amazon S3, allowing the engines to apply fine-grained permissions to the federated table. This approach avoids metadata and data duplication while providing real-time access to remote Iceberg tables through your preferred AWS analytics engines.

The Data Catalog facilitates connectivity to remote catalog systems that support Apache Iceberg by establishing an AWS Glue connection with the remote catalog endpoint. You can connect the Data Catalog to remote Iceberg REST catalogs using OAuth2 or custom authentication mechanisms using an access token. During integration, administrators configure a principal (service account or identity) with the appropriate permissions to access resources in the remote catalog. The AWS Glue connection object uses this configured principal’s credentials to authenticate and access metadata in the remote catalog server. You can also connect the Data Catalog to remote catalogs that use a private link or proxy for isolating and restricting network access. After it’s connected, this integration uses the standardized Iceberg REST API specification to retrieve the most current table metadata information from these remote catalogs. AWS Glue onboards these remote catalogs as federated catalogs within its own catalog infrastructure, enabling unified metadata access across multiple catalog systems.

Lake Formation serves as the centralized authorization layer for managing user access to federated catalog resources. When users attempt to access tables and databases in federated catalogs, Lake Formation evaluates their permissions and enforces fine-grained access control policies.

Beyond metadata authorization, the catalog federation also manages secure access to the actual underlying data files. It accomplishes this through credential vending mechanisms that issue temporary, scope-limited credentials. AWS Glue federated catalogs work with your preferred AWS analytics engines and query services, enabling consistent metadata access and unified data governance across your analytics workloads.

In the following sections, we walk through the steps to integrate the Data Catalog with your remote catalog server:

1. Set up an integration principal in the remote catalog and provide required access on catalog resources to this principal. Enable OAuth based authentication for the integration principal.
2. Create a federated catalog in the Data Catalog using the AWS Glue connection. Create an AWS Glue connection that uses the credentials of the integration principal (in Step1) to connect to the Iceberg REST endpoint of the remote catalog. Configure an [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) role with permission to S3 locations where the remote table data resides. In a cross-account scenario, make sure the bucket policy grants required access to this IAM role. This federated catalog mirrors the catalog object in your remote catalog server.
3. Discover Iceberg tables in federated catalogs using Lake Formation or AWS Glue APIs. Query Iceberg tables using AWS analytics engines. During query operations, Lake Formation manages fine-grained permission on federated resources and credential vending to underlying data for the end-users.

### Prerequisites

Before you begin, verify you have the following setup in AWS:

- An [AWS account](https://aws.amazon.com/account/).
- The [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI) version 2.31.38 or later installed and configured.
- An IAM admin role or user with appropriate permissions to the following services:
- IAM
- AWS Glue Data Catalog
- Amazon S3
- AWS Lake Formation
- AWS Secrets manager
- Amazon Athena
- Create a data lake admin. For instructions, see [Create a data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin).

#### Set up authentication credentials in remote Iceberg catalog

Catalog federation to a remote Iceberg catalog uses the OAuth2 credentials of the principal configured with metadata access. This authentication mechanism allows the AWS Glue Data Catalog to access the metadata of various objects (such as databases, and tables) within the remote catalogs, based on the privileges associated with the principal. To support proper functionality, you must grant the principal with the necessary permissions to read the metadata of these objects. Generate the `CLIENT_ID` and `CLIENT_SECRET` to enable OAuth based authentication for the integration principal.

#### Create AWS Glue catalog federation using connection to remote Iceberg catalog

Create a federated catalog in the Data Catalog that mirrors a catalog object in the remote Iceberg catalog server and is used by the AWS Glue service to federate metadata queries such as `ListDatabases`, `ListTables`, and `GetTable` to the remote catalog. As data lake administrator, you can create a federated catalog in the Data Catalog using an AWS Glue connection object that is registered with AWS Lake Formation.

**Configure data source connection for AWS Glue connection**

Catalog federation uses an AWS Glue connection for metadata access when you provide authentication and Iceberg REST API endpoint configurations in the remote catalog. The AWS Glue connection supports OAuth2 or custom as the authentication method.

**Connect using OAuth2 authentication**

For the OAuth2 authentication method, you can provide a client secret either directly as input or stored in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) and used by the AWS Glue connection object during authentication. AWS Glue internally manages the token refresh upon expiration. To store the client secret in Secrets manager, complete the following steps:

1. On the Secrets Manager console, choose **Secrets** in the navigation pane.
2. Choose **Store a new secret**.
3. Choose **Other type of secret**, provide the key name as `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET`, and enter the client secret value.
4. Choose **Next** and provide a name for the secret.
5. Choose **Next** and choose **Store** to save the secret.

**Connect using custom authentication**

For custom authentication, use Secrets Manager to store and retrieve the access token. This access token is created, refreshed, and managed by the customer’s application or system, providing proper control and management over the authentication process. To store the access token in Secrets Manager, complete the following steps:

1. On the Secrets Manager console, choose **Secrets** in the navigation pane.
2. Choose **Store a new secret**.
3. Choose **Other type of secret** and provide the key name as `BEARER_TOKEN` with the value noted as the access token of the integration principal.
4. Choose **Next** and provide a name for the secret.
5. Choose **Next** and choose **Store** to save the secret.

**Register AWS Glue connection with Lake Formation**

Create an IAM role that Lake Formation can use to vend credentials and attach permission on S3 bucket prefixes where the Iceberg tables are stored. Optionally, if you’re using Secrets Manager to store the client secret or are using a network configuration, you can add permissions for those services to this role. For instruction, refer to [Catalog federation to remote Iceberg catalogs](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation.html).

Complete the following steps to register the connection:

1. On the Lake Formation console, choose **Catalogs** in the navigation pane.
2. Choose **Create catalog** and select the data source.
3. Provide the federated catalog details:
1. Name of the federated catalog.
2. Catalog name in the remote catalog server and this needs to match the exact catalog name in remote catalog.
4. Provide AWS Glue connection details. To reuse an existing connection, choose **Select existing connection** and choose the connection to reuse. For a first-time setup, choose **Input new connection configuration** and provide the following information:
1. Provide the AWS Glue connection name.
2. Provide the remote catalog Iceberg REST API endpoint.
3. Specify the catalog object casing type. The connection can support uppercase objects through the object hierarchy or lowercase objects.
4. Configure authentication parameters:
1. For OAuth2: Provide the client ID and client secret directly or choose the secret where the client secret is stored, token authorization URL, and scope mapped to the credential.
2. For custom: Provide the secret managed by Secrets Manager where the access token is stored.
3. Network configuration: If you have a network and/or proxy setup, you can provide this information. Otherwise, leave this section as default.
5. Register the connection with Lake Formation using the IAM role with access to the bucket where the remote table metadata and data is stored.
6. Verify the connection by choosing **Run test**.
7. After the test is successful, create the catalog.

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/BDB-5682/catalogdemo.mp4?_=1)

You can now discover remote objects under the federated catalog. You can onboard other remote catalogs by reusing the existing connection configured to the same external catalog instance.

#### Query the federated catalog objects using AWS analytical engines

As the data lake administrator, you can now manage access control on databases and tables in a federated catalog using AWS Lake Formation. You can also use tag-based access control to scale your permission model by tagging the resource based on the access control mechanism.

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/BDB-5682/allgrants.mp4?_=2)

After permissions are granted, an IAM principal or an IAM user can access the federated tables using AWS analytical services including Athena, Amazon Redshift, Amazon EMR, and Amazon SageMaker. Query the federated Iceberg table using Athena as shown in the following example.

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/BDB-5682/athena.mp4?_=3)

## Clean up

To avoid incurring ongoing charges, complete the following steps to clean up the resources created during this walkthrough:

1. Delete the federated catalog in the Data Catalog:

```
aws glue delete-catalog \
--name <your-federated-catalog-name>
```
2. Deregister the AWS Glue connection from Lake Formation:

```
aws lakeformation deregister-resource \
--resource-arn <your-glue-connector-arn>
```
3. Revoke Lake Formation permissions (if any were granted):

```
# List existing permissions first
aws lakeformation list-permissions \
--catalog-id <your-account-id> \
--resource '{
"Catalog": {}
}'

# Revoke permissions as needed
aws lakeformation revoke-permissions \
--principal '{
"DataLakePrincipalIdentifier": "<principal-arn>"
}' \
--resource '{
"Database": {
"CatalogId": "<catalog-id>",
"Name": "<database-name>"
}
}' \
--permissions ["SELECT", "DESCRIBE"]
```
4. Delete the AWS Glue connection:

```
aws glue delete-connection \
--connection-name <your-glue-connection-to-snowflake-account>
```
5. Delete IAM roles and policies associated with Lake Formation and the AWS Glue connection:

```
# Detach policies from the role
aws iam detach-role-policy \
--role-name <your-lakeformation-role-name> \
--policy-arn <your-lakeformation-policy-arn>

# Delete the custom policy
aws iam delete-policy \
--policy-arn <your-lakeformation-policy-arn>

# Delete the role
aws iam delete-role \
--role-name <your-lakeformation-role-name>
# Detach policies from the role
aws iam detach-role-policy \
--role-name <your-glue-connection-role-name> \
--policy-arn <your-glue-connection-policy-arn>

# Delete the custom policy
aws iam delete-policy \
--policy-arn <your-glue-connection-policy-arn>

# Delete the role
aws iam delete-role \
--role-name <your-glue-connection-role-name>
```
6. Delete the Secrets Manager secret:

```
# Schedule secret for deletion (7-30 days)
aws secretsmanager delete-secret \
--secret-id <your-snowflake-secret>
```

This teardown guide doesn’t affect the actual metadata in the remote catalog server nor the data in S3 buckets. It only affects the federation configurations in the Data Catalog and Lake Formation. Any corresponding service principals or configurations in the remote catalog server must be addressed separately.

Make sure you follow the teardown steps in the specified order to avoid dependency conflicts. For example, an AWS Glue connection object can’t be deleted if an AWS Glue catalog object is associated with it.

Additionally, make sure you have the necessary permissions to delete these resources.

## Conclusion

In this post, we explored how catalog federation addresses the growing challenge of managing Iceberg tables across multi-vendor catalog environments. We walked through the architecture, demonstrating how the Data Catalog communicates with remote catalog systems, including Snowflake Polaris Catalog, Databricks Unity Catalog, and custom Iceberg REST-compliant catalogs, with centralized authorization and credential vending for secure data access. We covered the setup process, including configuring authentication principals, creating federated catalogs using AWS Glue connections, to implementing fine-grained access controls and querying remote Iceberg tables directly from AWS analytics engines.

Catalog federation offers several advantages:

- Query your Iceberg data where it lives while maintaining security, governance, and price-performance benefits of AWS analytics services
- Remove operational overheads and costs to maintain synchronization processes
- Avoid data duplication and inconsistencies
- Get real-time access to up-to-date table schemas without migrating or replacing existing catalogs.

To learn more, refer to [Catalog federation to remote Iceberg catalogs](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation.html).

---

### About the authors

![Debika D](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/26/ddebika.jpg)

### Debika D

[Debika](https://www.linkedin.com/in/debikad/) is a Senior Product Marketing Manager with Amazon SageMaker, specializing in messaging and go-to-market strategy for lakehouse architecture. She is passionate about all things data and AI.

![Srividya Parthasarathy](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/26/srivipar.jpg)

### Srividya Parthasarathy

[Srividya](https://www.linkedin.com/in/srividya-parthasarathy-8b71bb32/) is a Senior Big Data Architect on the AWS Lake Formation team. She works with the product team and customers to build robust features and solutions for their analytical data platform. She enjoys building data mesh solutions and sharing them with the community.

![Pratik Das](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2025/11/26/pratdas.jpeg)

### Pratik Das

[Pratik](https://www.linkedin.com/in/das-pratik/) is a Senior Product Manager with AWS Lake Formation. He is passionate about all things data and works with customers to understand their requirements and build delightful experiences. He has a background in building data-driven solutions and machine learning systems.