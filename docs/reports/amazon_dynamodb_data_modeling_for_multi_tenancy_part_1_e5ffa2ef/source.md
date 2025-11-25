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

## [AWS Database Blog](https://aws.amazon.com/blogs/database/)

# Amazon DynamoDB data modeling for Multi-Tenancy – Part 1

by Dave Roberts, Josh Hart, and Samaneh Utter on 16 MAY 2025 in [Amazon DynamoDB](https://aws.amazon.com/blogs/database/category/database/amazon-dynamodb/ "View all posts in Amazon DynamoDB"), [Best Practices](https://aws.amazon.com/blogs/database/category/post-types/best-practices/ "View all posts in Best Practices"), [Intermediate (200)](https://aws.amazon.com/blogs/database/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [SaaS](https://aws.amazon.com/blogs/database/category/saas/ "View all posts in SaaS") [Permalink](https://aws.amazon.com/blogs/database/amazon-dynamodb-data-modeling-for-multi-tenancy-part-1/)  [Comments](https://aws.amazon.com/blogs/database/amazon-dynamodb-data-modeling-for-multi-tenancy-part-1/#Comments)  Share

One reason that customers choose [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is because it provides single-digit millisecond performance on any scale. However, this performance depends on an [effective data model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-general-nosql-design.html) that supports the application’s access patterns and concurrency requirements. Multi-tenant applications (such as Software-as-a-Service or SaaS applications) introduce additional complexity with unique considerations around performance, scalability, and isolation.

In this series of posts, we walk through the process of creating a DynamoDB data model using an example multi-tenant application, a customer issue tracking service. The goal of this series is to explore areas that are important for decision-making and provide insights into the influences to help you plan your data model for a multi-tenant application.

In this post, we define the access patterns and decide on the table design. In [Part 2](https://aws.amazon.com/blogs/database/amazon-dynamodb-data-modeling-for-multi-tenancy-part-2/), we select a partition key design and create the data schema by iterating across the access patterns. Finally, in [Part 3](https://aws.amazon.com/blogs/database/amazon-dynamodb-data-modeling-for-multi-tenancy-part-3/), we validate the data model and explore how to extend the model as new access patterns emerge.

## Considerations when designing a data model for multi-tenancy

The primary goal when designing a data model is to make queries as efficient as possible whilst maintaining [tenant isolation](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/tenant-isolation.html). An efficient data model optimizes cost, reduces waste, and ensures queries are performant. This helps your application scale as your tenants grow without causing significant costs or performance issues.

The [data partitioning](https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/multitenancy-on-dynamodb.html) and tenant isolation approaches you use, heavily influence your data model design. Depending on the [deployment model](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-pool-and-bridge-models.html) you use, how you partition data and implement tenant isolation may differ. A silo model may not need a specific data partitioning approach, because the table belongs to the tenant. Similarly, you can implement [tenant isolation at the table resource level](https://aws.amazon.com/blogs/apn/partitioning-pooled-multi-tenant-saas-data-with-amazon-dynamodb/) using AWS Identity and Access Management (IAM).

The pool model introduces more complexity because multiple tenants share the same DynamoDB table. You can partition data using a unique tenant identifier (`tenantId`) in the table’s partition key to associate the item with the tenant it belongs to. However, this introduces the constraint that your data model must include `tenantId` in all partition keys, which may exclude potential data patterns.

This constraint has greater weight because you can also use `tenantId` as a data point to enforce tenant isolation. For example, you can implement [fine-grained access control](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html) with [IAM and attribute-based access control](https://aws.amazon.com/blogs/security/how-to-implement-saas-tenant-isolation-with-abac-and-aws-iam/), using the `dynamodb:LeadingKeys` condition key to restrict permissions to only the items whose partition key matches the tenant’s identifier as passed in a session tag.

Another consideration is whether you need to support multiple deployment models. It’s common to have silo and pool models within a multi-tenant solution. Besides different access patterns and tenant isolation mechanisms, supporting mechanisms (such as backup, metrics, metering, and tenant portability) may vary by model, increasing operational complexity.

When using multiple partitioning strategies, it’s important to maintain a consistent data model*.* For example, when deploying silo tenants, you may use `tenantId` in the prefix to align with your pool model, even if this isn’t strictly required for isolation. A consistent data model across service tiers simplifies the application architecture, offers standardized [data migration](https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/data-migration.html) within and across tiers, and increases operational efficiencies by enabling single processes for operational activities like metrics gathering, scaling, and cost allocation.

Regardless of the partitioning model, you need to implement operational monitoring to help maintain a consistent tenant experience as your application scales. For more details, see [Monitoring Amazon DynamoDB for operational awareness](https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/).

For this application, we have selected a pool deployment model. This means there is a single table for all tenant data and we implement isolation using IAM policies. This is important because to implement this, all the partition keys for the base table and global secondary indexes (GSIs) require `tenantId` as a prefix to use the [LeadingKeys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html#FGAC_DDB.ConditionKeys) condition key. This is shown in Part 2.

**For multi-tenant applications,** [on-demand capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html) **is recommended as the default approach.** This mode automatically handles varying workloads across multiple tenants without requiring capacity planning, and ensures that one tenant’s activity doesn’t impact others. [Provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html) should be considered as an optimization for predictable workloads.

## Defining access pattern entities

[Identifying your data access patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step3.html) is key to designing a successful data model. We start by defining the entities and attributes in our data model, then document our access patterns.

In our example multi-tenant issue tracking application, we have the following entities and attributes:

Ticket

* **TenantId** – This is the customer (buyer) of our application. There are multiple tenants.
* **TicketId** – This is an auto-generated unique identifier for each ticket.
* **Status** – The current status of the ticket.
* **Created Date** – The date the ticket was created.
* **Resolver** – The current assigned resolver of the ticket.
* **Title** – The title of the ticket
* **Created By** – The user who raised the ticket

Comment

* **CommentId** – This is an auto-generated unique identifier for each comment.
* **Created Date** – The date the comment was created
* **Created By** – The user who added the comment

The following figure shows this as a traditional entity-relationship diagram (ERD).

[![Entity relationship diagram](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/05/07/1_erd.png)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/05/07/1_erd.png)

## Documenting access patterns

Now that you have modeled the entities, it’s time to document the access patterns. For simplicity, there are two personas in the application: a regular tenant user and a tenant admin user. Not all personas and access patterns may be known at this point.

The following are the access patterns for our example application:

* “As a user, I want to get a single ticket and all comments.”
* “As a user, I want to view a single ticket summary.”
* “As a user, I want to get all open tickets.”
* “As a user, I want to view all open tickets for a given resolver.”
* “As a user, I want to change the status of multiple tickets atomically.”
* “As a tenant admin, I want to view an aggregate of the tickets by status in my tenant.”

With the access patterns documented, to design the right data model, requirements such as frequency, requests per second, SLA, and consistency need to be collected for each access pattern. We document these requirements for the issue tracking application in the following table.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Access Pattern** | **Peak Throughput (requests per second)** | **Frequency** | **Priority** | **Consistency Requirement** | **Persona** |
| As a user, I want to get a single ticket and all comments. | 50 | Hourly | High | Eventual | User |
| As a user, I want to view a single ticket summary. | 100 | Hourly | High | Eventual | User |
| As a user, I want to get all open tickets. | 25 | Hourly | Medium | Eventual | User |
| As a user, I want to view all open tickets for a given resolver. | 25 | Hourly | High | Strong | User |
| As a user, I want to change the status of multiple tickets atomically. | 5 | Hourly | High | Strong | User |
| As a tenant admin, I want to view an aggregate of the tickets by status in my tenant. | 10 | Daily | Low | Eventual | Tenant Admin |

## Table design for multi-tenant applications

Choosing a table design is a non-trivial decision and should be carefully considered. Our goal is to create an efficient data model for cost and performance. With multi-tenancy, any ***wastage scales*** with the number of tenants, so efficiency becomes a priority.

When choosing a table design, it’s important to work backwards from your access patterns and choose the best data model for your use case. Considerations for table design are covered in [Data Modeling foundations in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling-foundations.html).

If your access patterns lead you to a single-table design, then you should consider whether the cost and performance efficiencies of a single-table design outweigh the simplicity of a multi-table one. Single-table design is an advanced pattern and should not necessarily be the default approach.

## Conclusion

Designing a performant DynamoDB data model for multi-tenant applications requires careful planning and analysis. By starting with the core entities and access patterns of your application, you can make informed decisions about partitioning, isolation strategies, and table structure. Defining these requirements per access pattern ahead of time helps make sure the table can scale as the application grows.

To summarize the takeaways:

* Start by defining the entities and entity relationships inside your data model
* Document your access patterns
* Maintain a consistent data model across different tenant partitioning models
* Evaluate table design based on your application requirements

In this post, we discussed the requirements for building a multi-tenant DynamoDB table. In [Part 2](https://aws.amazon.com/blogs/database/amazon-dynamodb-data-modeling-for-multi-tenancy-part-2/), you will learn about data modeling and implementing the access patterns defined in this post. In [Part 3](https://aws.amazon.com/blogs/database/amazon-dynamodb-data-modeling-for-multi-tenancy-part-3/), you’ll validate your data model and explore how to extend the model as new access patterns emerge.

---

### About the Authors

**[![Dave Roberts](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/05/07/profile_dave.jpg)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/05/07/profile_dave.jpg)Dave Roberts** is a Senior Solutions Architect in the AWS SaaS Factory team where he helps software vendors to build SaaS and modernize their software delivery. Originally from Aotearoa, he now lives in Germany with a loving wife and two kids. Outside of SaaS, he enjoys hearing the birds sing and hiding Easter eggs in technical content.

**[![Josh "Hitman" Hart](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/05/07/profile_josh.jpg)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/05/07/profile_josh.jpg)Josh Hart** is a Principal Solutions Architect at Amazon Web Services. He works with ISV customers in the UK to help them build and modernize their SaaS applications on AWS.

**[![Samaneh Utter](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/05/07/profile_samaneh.jpg)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/05/07/profile_samaneh.jpg)Samaneh Utter** is an Amazon DynamoDB Specialist Solutions Architect based in Göteborg, Sweden.

Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=database-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=database-resources)

---

### Blog Topics

* [Amazon Aurora](https://aws.amazon.com/blogs/database/category/database/amazon-aurora/)
* [Amazon DocumentDB](https://aws.amazon.com/blogs/database/category/database/amazon-document-db/)
* [Amazon DynamoDB](https://aws.amazon.com/blogs/database/category/database/amazon-dynamodb/)
* [Amazon ElastiCache](https://aws.amazon.com/blogs/database/category/database/amazon-elasticache/)
* [Amazon Keyspaces (for Apache Cassandra)](https://aws.amazon.com/blogs/database/category/database/amazon-managed-apache-cassandra-service/)
* [Amazon Managed Blockchain](https://aws.amazon.com/blogs/database/category/blockchain/amazon-managed-blockchain/)
* [Amazon MemoryDB for Redis](https://aws.amazon.com/blogs/database/category/database/amazon-memorydb-for-redis/)
* [Amazon Neptune](https://aws.amazon.com/blogs/database/category/database/amazon-neptune/)
* [Amazon Quantum Ledger Database (Amazon QLDB)](https://aws.amazon.com/blogs/database/category/database/amazon-quantum-ledger-database/)
* [Amazon RDS](https://aws.amazon.com/blogs/database/category/database/amazon-rds/)
* [Amazon Timestream](https://aws.amazon.com/blogs/database/category/database/amazon-timestream/)
* [AWS Database Migration Service](https://aws.amazon.com/blogs/database/category/database/aws-database-migration-service/)
* [AWS Schema Conversion Tool](https://aws.amazon.com/blogs/database/category/database/aws-schema-conversion-tool/)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=database-social)

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