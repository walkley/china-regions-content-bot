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

## [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Protect sensitive data in RAG applications with Amazon Bedrock

by Praveen Chamarthi, Brandon Rooks, Dhawalkumar Patel, Srikanth Reddy, Vikash Garg, and Vivek Bhadauria on 23 APR 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-guardrails/ "View all posts in Amazon Bedrock Guardrails"), [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-knowledge-bases/ "View all posts in Amazon Bedrock Knowledge Bases"), [Amazon Machine Learning](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Responsible AI](https://aws.amazon.com/blogs/machine-learning/category/responsible-ai/ "View all posts in Responsible AI"), [Security](https://aws.amazon.com/blogs/machine-learning/category/security-identity-compliance/security/ "View all posts in Security") [Permalink](https://aws.amazon.com/blogs/machine-learning/protect-sensitive-data-in-rag-applications-with-amazon-bedrock/)  [Comments](https://aws.amazon.com/blogs/machine-learning/protect-sensitive-data-in-rag-applications-with-amazon-bedrock/#Comments)  Share

[Retrieval Augmented Generation](https://aws.amazon.com/what-is/retrieval-augmented-generation/) (RAG) applications have become increasingly popular due to their ability to enhance generative AI tasks with contextually relevant information. Implementing RAG-based applications requires careful attention to security, particularly when handling sensitive data. The protection of personally identifiable information (PII), protected health information (PHI), and confidential business data is crucial because this information flows through RAG systems. Failing to address these security considerations can lead to significant risks and potential data breaches. For healthcare organizations, financial institutions, and enterprises handling confidential information, these risks can result in regulatory compliance violations and breach of customer trust. See the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) to learn more about the unique security risks associated with generative AI applications.

Developing a comprehensive [threat model](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_threat_model.html) for your generative AI applications can help you identify potential vulnerabilities related to sensitive data leakage, [prompt injections](https://aws.amazon.com/blogs/security/safeguard-your-generative-ai-workloads-from-prompt-injections/), unauthorized data access, and more. To assist in this effort, AWS provides a range of [generative AI security strategies](https://aws.amazon.com/ai/generative-ai/security/) that you can use to create appropriate threat models, and also an [example threat model](https://awslabs.github.io/threat-composer/workspaces/GenAI%20Chatbot/threatModel) for a generative AI chatbot application.

[Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) is a fully managed capability that simplifies the management of the entire RAG workflow, empowering organizations to give foundation models (FMs) and agents contextual information from your private data sources to deliver more relevant and accurate responses tailored to your specific needs. Additionally, with [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/), you can implement safeguards in your generative AI applications that are customized to your use cases and [responsible AI](https://aws.amazon.com/ai/responsible-ai/) policies. You can redact sensitive information such as [PII to protect privacy](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html) using Amazon Bedrock Guardrails.

## RAG workflow: Converting data to actionable knowledge

RAG consists of two major steps:

* **Ingestion** – Preprocessing unstructured data, which includes converting the data into text documents and splitting the documents into chunks. Document chunks are then encoded with an embedding model to convert them to document embeddings. These encoded document embeddings along with the original document chunks in the text are then stored to a vector store, such as [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/).
* **Augmented retrieval** – At query time, the user’s query is first encoded with the same embedding model to convert the query into a query embedding. The generated query embedding is then used to perform a similarity search on the stored document embeddings to find and retrieve semantically similar document chunks to the query. After the document chunks are retrieved, the user prompt is augmented by passing the retrieved chunks as additional context, so that the text generation model can answer the user query using the retrieved context. If sensitive data isn’t sanitized before ingestion, this might lead to retrieving sensitive data from the vector store and inadvertently leak the sensitive data to unauthorized users as part of the model response.

The following diagram shows the architectural workflow of a RAG system, illustrating how a user’s query is processed through multiple stages to generate an informed response

![Bedrock Knowledge Base Flow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/28/ml-17892-bedrock-kb-flow.png)

## Solution overview

In this post we present two architecture patterns: data redaction at storage level and role-based access, for protecting sensitive data when building RAG-based applications using Amazon Bedrock Knowledge Bases.

**Data redaction at storage level** – Identifying and redacting (or masking) sensitive data before storing them to the vector store (ingestion) using Amazon Bedrock Knowledge Bases. This zero-trust approach to data sensitivity reduces the risk of sensitive information being inadvertently disclosed to unauthorized users.

**Role-based access to sensitive data –** Controlling selective access to sensitive information based on user roles and permissions during retrieval. This approach is best in situations where sensitive data needs to be stored in the vector store, such as in healthcare settings with distinct user roles like administrators (doctors) and non-administrators (nurses or support personnel).

For all data stored in Amazon Bedrock, the AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies.

Let’s dive in to understand how to implement the data redaction at storage level and role-based access architecture patterns effectively.

## Scenario 1: Identify and redact sensitive data before ingesting into the vector store

The ingestion flow implements a four-step process to help protect sensitive data when building RAG applications with Amazon Bedrock:

1. **Source document processing** – An [AWS Lambda](http://aws.amazon.com/lambda) function monitors the incoming text documents landing to a source [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) bucket and triggers an [Amazon Comprehend](https://aws.amazon.com/comprehend/) PII redaction job to identify and redact (or mask) sensitive data in the documents. An [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rule triggers the Lambda function every 5 minutes. The document processing pipeline described here only processes text documents. To handle documents containing embedded images, you should implement additional preprocessing steps to extract and analyze images separately before ingestion.
2. **PII identification and redaction** – The Amazon Comprehend PII redaction job analyzes the text content to identify and redact PII entities. For example, the job identifies and redacts sensitive data entities like name, email, address, and other financial PII entities.
3. **Deep security scanning** – After redaction, documents move to another folder where [Amazon Macie](https://aws.amazon.com/macie/) verifies redaction effectiveness and identifies any remaining sensitive data objects. Documents flagged by Macie go to a quarantine bucket for manual review, while cleared documents move to a redacted bucket ready for ingestion. For more details on data ingestion, see [Sync your data with your Amazon Bedrock knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-sync-ingest.html).
4. **Secure knowledge base integration** – Redacted documents are ingested into the knowledge base through a data ingestion job. In case of multi-modal content, for enhanced security, consider implementing:
   * A dedicated image extraction and processing pipeline.
   * Image analysis to detect and redact sensitive visual information.
   * Amazon Bedrock Guardrails to filter inappropriate image content during retrieval.

This multi-layered approach focuses on securing text content while highlighting the importance of implementing additional safeguards for image processing. Organizations should evaluate their multi-modal document requirements and extend the security framework accordingly.

### Ingestion flow

The following illustration demonstrates a secure document processing pipeline for handling sensitive data before ingestion into Amazon Bedrock Knowledge Bases.

![Scenario 1 - Ingestion Flow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/28/ml-17892-s1-ingestion-flow-1.png)

The high-level steps are as follows:

1. The document ingestion flow begins when documents containing sensitive data are uploaded to a monitored `inputs` folder in the source bucket. An EventBridge rule triggers a Lambda function (`ComprehendLambda`).
2. The `ComprehendLambda` function monitors for new files in the `inputs` folder of the source bucket and moves landed files to a `processing` folder. It then launches an asynchronous Amazon Comprehend PII redaction analysis job and records the job ID and status in an [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) `JobTracking` table for monitoring job completion. The Amazon Comprehend PII redaction job automatically redacts and masks sensitive elements such as names, addresses, phone numbers, Social Security numbers, driver’s license IDs, and banking information with the entity type. The job replaces these identified PII entities with placeholder tokens, such as `[NAME]`, `[SSN]` etc. The entities to mask can be configured using [RedactionConfig](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_RedactionConfig.html). For more information, see [Redacting PII entities with asynchronous jobs (API)](https://docs.aws.amazon.com/comprehend/latest/dg/redact-api-pii.html). The `MaskMode` in RedactionConfig is set to `REPLACE_WITH_PII_ENTITY_TYPE` instead of `MASK`; redacting with a `MaskCharacter` would affect the quality of retrieved documents because many documents could contain the same `MaskCharacter`, thereby affecting the retrieval quality. After completion, the redacted files move to the `for_macie_scan` folder for secondary scanning.
3. The secondary verification phase employs Macie for additional sensitive data detection on the redacted files. Another Lambda function (`MacieLambda`) monitors the completion of the Amazon Comprehend PII redaction job. When the job is complete, the function triggers a Macie one-time sensitive data detection job with files in the `for_macie_scan` folder.
4. The final stage integrates with the Amazon Bedrock knowledge base. The findings from Macie determine the next steps: files with high severity ratings (3 or higher) are moved to a `quarantine` folder for human review by authorized personnel with appropriate permissions and access controls, whereas files with low severity ratings are moved to a designated `redacted` bucket, which then triggers a data ingestion job to the Amazon Bedrock knowledge base.

This process helps prevent sensitive details from being exposed when the model generates responses based on retrieved data.

### Augmented retrieval flow

The augmented retrieval flow diagram shows how user queries are processed securely. It illustrates the complete workflow from user authentication through Amazon Cognito to response generation with Amazon Bedrock, including guardrail interventions that help prevent policy violations in both inputs and outputs.

![Scenario 1 - Retrieval Flow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/28/ml-17892-s1-retrieval-flow-2.png)

The high-level steps are as follows:

1. For our [demo](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/security/securing-rag-apps), we use a web application UI built using [Streamlit](https://streamlit.io/). The web application launches with a login form with user name and password fields.
2. The user enters the credentials and logs in. User credentials are authenticated using [Amazon Cognito](https://aws.amazon.com/cognito/) user pools. Amazon Cognito acts as our OpenID connect (OIDC) identity provider (IdP) to provide authentication and authorization services for this application. After authentication, Amazon Cognito generates and returns identity, access and refresh tokens in JSON web token (JWT) format back to the web application. Refer to [Understanding user pool JSON web tokens (JWTs)](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html) for more information.
3. After the user is authenticated, they are logged in to the web application, where an AI assistant UI is presented to the user. The user enters their query (prompt) in the assistant’s text box. The query is then forwarded using a REST API call to an [Amazon API Gateway](https://aws.amazon.com/api-gateway/) endpoint along with the access tokens in the header.
4. API Gateway forwards the payload along with the claims included in the header to a conversation orchestrator Lambda function.
5. The conversation orchestrator Lambda function processes the user prompt and model parameters received from the UI and calls the [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html) API to the Amazon Bedrock knowledge base. Input guardrails are first applied to this request to perform input validation on the user query.
   * The guardrail evaluates and applies predefined responsible AI policies using content filters, denied topic filters and word filters on user input. For more information on creating guardrail filters, see [Create a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html).
   * If the predefined input guardrail policies are triggered on the user input, the guardrails intervene and return a preconfigured message like, “Sorry, your query violates our usage policy.”
   * Requests that don’t trigger a guardrail policy will retrieve the documents from the knowledge base and generate a response using the [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html). Optionally, if users choose to run [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) separately, guardrails can also be applied at this stage. Guardrails during document retrieval can help block sensitive data returned from the vector store.
6. During retrieval, Amazon Bedrock Knowledge Bases encodes the user query using the [Amazon Titan Text v2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) embeddings model to generate a query embedding.
7. Amazon Bedrock Knowledge Bases performs a similarity search with the query embedding against the document embeddings in the OpenSearch Service vector store and retrieves top-k chunks. Optionally, post-retrieval, you can incorporate a reranking model to improve the retrieved results quality from the OpenSearch vector store. Refer to [Improve the relevance of query responses with a reranker model in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html) for more details.
8. Finally, the user prompt is augmented with the retrieved document chunks from the vector store as context and the final prompt is sent to an Amazon Bedrock foundation model (FM) for inference. Output guardrail policies are again applied post-response generation. If the predefined output guardrail policies are triggered, the model generates a predefined response like “Sorry, your query violates our usage policy.” If no policies are triggered, then the large language model (LLM) generated response is sent to the user.

To deploy Scenario 1, find the instructions here on [Github](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/security/securing-rag-apps/scenario_1)

## Scenario 2: Implement role-based access to PII data during retrieval

In this scenario, we demonstrate a comprehensive security approach that combines role-based access control (RBAC) with intelligent PII guardrails for RAG applications. It integrates Amazon Bedrock with AWS identity services to automatically enforce security through different guardrail configurations for admin and non-admin users.

The solution uses the [metadata filtering](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-metadata.html) capabilities of Amazon Bedrock Knowledge Bases to dynamically filter documents during similarity searches using metadata attributes assigned before ingestion. For example, admin and non-admin metadata attributes are created and attached to relevant documents before the ingestion process. During retrieval, the system returns only the documents with metadata matching the user’s security role and permissions and applies the relevant guardrail policies to either mask or block sensitive data detected on the LLM output.

This metadata-driven approach, combined with features like custom guardrails, real-time PII detection, masking, and comprehensive access logging creates a robust framework that maintains the security and utility of the RAG application while enforcing RBAC.

The following diagram illustrates how RBAC works with metadata filtering in the vector database.

![Amazon Bedrock Knowledge Bases metadata filtering](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/28/ml-17892-s2-rag-filters-3.png)

For a detailed understanding of how metadata filtering works, see [Amazon Bedrock Knowledge Bases now supports metadata filtering to improve retrieval accuracy](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-metadata-filtering-to-improve-retrieval-accuracy/).

### Augmented retrieval flow

The augmented retrieval flow diagram shows how user queries are processed securely based on role-based access.

![Scenario 2 - Retrieval flow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/28/ml-17892-s2-retrieval-flow-1.png)

The workflow consists of the following steps:

1. The user is authenticated using an [Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html). It generates a validation token after successful authentication.
2. The user query is sent using an API call along with the authentication token through [Amazon API Gateway](https://aws.amazon.com/api-gateway/).
3. Amazon API Gateway forwards the payload and claims to an integration Lambda function.
4. The Lambda function extracts the claims from the header and checks for user role and determines whether to use an admin guardrail or a non-admin guardrail based on the access level.
5. Next, the Amazon Bedrock Knowledge Bases [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html) API is invoked along with the guardrail applied on the user input.
6. Amazon Bedrock Knowledge Bases embeds the query using the [Amazon Titan Text v2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) embeddings model.
7. Amazon Bedrock Knowledge Bases performs similarity searches on the OpenSearch Service vector database and retrieves relevant chunks (optionally, you can [improve the relevance of query responses using a reranker model](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html) in the knowledge base).
8. The user prompt is augmented with the retrieved context from the previous step and sent to the Amazon Bedrock FM for inference.
9. Based on the user role, the LLM output is evaluated against defined [Responsible AI policies](https://aws.amazon.com/ai/responsible-ai/) using either admin or non-admin guardrails.
10. Based on guardrail evaluation, the system either returns a “Sorry! Cannot Respond” message if the guardrail intervenes, or delivers an appropriate response with no masking on the output for admin users or sensitive data masked for non-admin users.

To deploy Scenario 2, find the instructions here on [Github](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/security/securing-rag-apps/scenario_2)

This security architecture combines Amazon Bedrock guardrails with granular access controls to automatically manage sensitive information exposure based on user permissions. The multi-layered approach makes sure organizations maintain security compliance while fully utilizing their knowledge base, proving security and functionality can coexist.

## Customizing the solution

The solution offers several customization points to enhance its flexibility and adaptability:

* **Integration with external APIs** – You can integrate existing PII detection and redaction solutions with this system. The Lambda function can be modified to use custom APIs for PHI or PII handling before calling the Amazon Bedrock Knowledge Bases API.
* **Multi-modal processing** – Although the current solution focuses on text, it can be extended to handle images containing PII by incorporating image-to-text conversion and caption generation. For more information about using Amazon Bedrock for processing multi-modal content during ingestion, see [Parsing options for your data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html).
* **Custom guardrails** – Organizations can implement additional specialized security measures tailored to their specific use cases.
* **Structured data handling** – For queries involving structured data, the solution can be customized to include [Amazon Redshift](http://aws.amazon.com/redshift) as a structured data store as opposed to OpenSearch Service. Data masking and redaction on Amazon Redshift can be achieved by applying [dynamic data masking](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm.html) (DDM) policies, including fine-grained DDM policies like [role-based access control](https://docs.aws.amazon.com/redshift/latest/dg/t_Roles.html) and column-level policies using [conditional dynamic data masking](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm-conditional.html).
* **Agentic workflow integration** – When incorporating an Amazon Bedrock knowledge base with an agentic workflow, additional safeguards can be implemented to protect sensitive data from external sources, such as API calls, tool use, agent action groups, session state, and long-term agentic memory.
* **Response streaming support** – The current solution uses a REST API Gateway endpoint that doesn’t support streaming. For streaming capabilities, consider WebSocket APIs in API Gateway, [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (ALB), or custom solutions with chunked responses using client-side reassembly or long-polling techniques.

With these customization options, you can tailor the solution to your specific needs, providing a robust and flexible security framework for your RAG applications. This approach not only protects sensitive data but also maintains the utility and efficiency of the knowledge base, allowing users to interact with the system while automatically enforcing role-appropriate information access and PII handling.

## Shared security responsibility: The customer’s role

At AWS, security is our top priority and security in the cloud is a [shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) between AWS and our customers. With AWS, you control your data by using AWS services and tools to determine where your data is stored, how it is secured, and who has access to it. Services such as [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) provide robust mechanisms for securely controlling access to AWS services and resources.

To enhance your security posture further, services like [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and [Amazon Macie](https://aws.amazon.com/macie/) offer advanced compliance, detection, and auditing capabilities. When it comes to encryption, [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) and [AWS Key Management Service](https://aws.amazon.com/kms/) (KMS) enable you to generate and manage encryption keys with confidence.

For organizations seeking to establish governance and maintain data residency controls, [AWS Control Tower](https://aws.amazon.com/controltower/) offers a comprehensive solution. For more information on Data protection and Privacy, refer to [Data Protection and Privacy at AWS](https://aws.amazon.com/compliance/data-protection/).

While our solution demonstrates the use of PII detection and redaction techniques, it does not provide an exhaustive list of all PII types or detection methods. As a customer, you bear the responsibility for implementing the appropriate PII detection types and redaction methods using AWS services, including [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) and other open-source libraries. The regular expressions configured in Bedrock Guardrails within this solution serve as a reference example only and do not cover all possible variations for detecting PII types. For instance, date of birth (DOB) formats can vary widely. Therefore, it falls on you to configure Bedrock Guardrails and policies to accurately detect the PII types relevant to your use case. Amazon Bedrock maintains strict data privacy standards. The service does not store or log your prompts and completions, nor does it use them to train AWS models or share them with third parties. We implement this through our Model Deployment Account architecture – each AWS Region where Amazon Bedrock is available has a dedicated deployment account per model provider, managed exclusively by the Amazon Bedrock service team. Model providers have no access to these accounts. When a model is delivered to AWS, Amazon Bedrock performs a deep copy of the provider’s inference and training software into these controlled accounts for deployment, making sure that model providers cannot access Amazon Bedrock logs or customer prompts and completions.

Ultimately, while we provide the tools and infrastructure, the responsibility for securing your data using AWS services rests with you, the customer. This shared responsibility model makes sure that you have the flexibility and control to implement security measures that align with your unique requirements and compliance needs, while we maintain the security of the underlying cloud infrastructure. For comprehensive information about Amazon Bedrock security, please refer to the Amazon Bedrock Security [documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html).

## Conclusion

In this post, we explored two approaches for securing sensitive data in RAG applications using Amazon Bedrock. The first approach focused on identifying and redacting sensitive data before ingestion into an Amazon Bedrock knowledge base, and the second demonstrated a fine-grained RBAC pattern for managing access to sensitive information during retrieval. These solutions represent just two possible approaches among many for securing sensitive data in generative AI applications.

Security is a multi-layered concern that requires careful consideration across all aspects of your application architecture. Looking ahead, we plan to dive deeper into RBAC for sensitive data within structured data stores when used with Amazon Bedrock Knowledge Bases. This can provide additional granularity and control over data access patterns while maintaining security and compliance requirements. Securing sensitive data in RAG applications requires ongoing attention to evolving security best practices, regular auditing of access patterns, and continuous refinement of your security controls as your applications and requirements grow.

To enhance your understanding of Amazon Bedrock security implementation, explore these additional resources:

* [Implementing least privilege access for Amazon Bedrock](https://aws.amazon.com/blogs/security/implementing-least-privilege-access-for-amazon-bedrock/)
* [Safeguard your generative AI workloads from prompt injections](https://aws.amazon.com/blogs/security/safeguard-your-generative-ai-workloads-from-prompt-injections/)

The complete source code and deployment instructions for these solutions are available in our [GitHub repository](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/security/securing-rag-apps).

We encourage you to explore the repository for detailed implementation guidance and customize the solutions based on your specific requirements using the customization points discussed earlier.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/22/ml-17892-praveen-bio.png)**Praveen Chamarthi** brings exceptional expertise to his role as a Senior AI/ML Specialist at Amazon Web Services, with over two decades in the industry. His passion for Machine Learning and Generative AI, coupled with his specialization in ML inference on Amazon SageMaker and Amazon Bedrock, enables him to empower organizations across the Americas to scale and optimize their ML operations. When he’s not advancing ML workloads, Praveen can be found immersed in books or enjoying science fiction films. Connect with him on [LinkedIn](https://www.linkedin.com/in/praveenchamarthi/) to follow his insights.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/22/ml-17892-srikanth-bio.png)**Srikanth Reddy** is a Senior AI/ML Specialist with Amazon Web Services. He is responsible for providing deep, domain-specific expertise to enterprise customers, helping them use AWS AI and ML capabilities to their fullest potential. You can find him on [LinkedIn](https://www.linkedin.com/in/srikanth-reddy-k/).

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/22/ml-17892-dhawal-bio.png)**Dhawal Patel** is a Principal Machine Learning Architect at AWS. He has worked with organizations ranging from large enterprises to mid-sized startups on problems related to distributed computing and artificial intelligence. He focuses on deep learning, including NLP and computer vision domains. He helps customers achieve high-performance model inference on Amazon SageMaker.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/22/ml-17892-vivek-bio.png)**Vivek Bhadauria** is a Principal Engineer at Amazon Bedrock with almost a decade of experience in building AI/ML services. He now focuses on building generative AI services such as Amazon Bedrock Agents and Amazon Bedrock Guardrails. In his free time, he enjoys biking and hiking.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/28/ml-17892-brandon-bio-1.png)**Brandon Rooks Sr.** is a Cloud Security Professional with 20+ years of experience in the IT and Cybersecurity field. Brandon joined AWS in 2019, where he dedicates himself to helping customers proactively enhance the security of their cloud applications and workloads. Brandon is a lifelong learner, and holds the CISSP, AWS Security Specialty, and AWS Solutions Architect Professional certifications. Outside of work, he cherishes moments with his family, engaging in various activities such as sports, gaming, music, volunteering, and traveling.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/03/22/ml-17892-vikash-bio.png)**Vikash Garg** is a Principal Engineer at Amazon Bedrock with almost 4 years of experience in building AI/ML services. He has a decade of experience in building large-scale systems. He now focuses on building the generative AI service AWS Bedrock Guardrails. In his free time, he enjoys hiking and traveling.

Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=machine-learning-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=machine-learning-resources)

---

### Blog Topics

* [Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/)
* [Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-comprehend/)
* [Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-kendra/)
* [Amazon Lex](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-lex/)
* [Amazon Polly](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-polly/)
* [Amazon Q](https://aws.amazon.com/blogs/machine-learning/category/amazon-q/)
* [Amazon Rekognition](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-rekognition/)
* [Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/sagemaker/)
* [Amazon Textract](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-textract/)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=maching-learning-social)

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