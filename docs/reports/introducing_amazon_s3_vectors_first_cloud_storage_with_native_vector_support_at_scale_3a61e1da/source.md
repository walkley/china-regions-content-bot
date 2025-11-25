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

## [AWS News Blog](https://aws.amazon.com/blogs/aws/)

# Introducing Amazon S3 Vectors: First cloud storage with native vector support at scale (preview)

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 15 JUL 2025 in [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-knowledge-bases/ "View all posts in Amazon Bedrock Knowledge Bases"), [Amazon OpenSearch Service](https://aws.amazon.com/blogs/aws/category/analytics/amazon-elasticsearch-service/ "View all posts in Amazon OpenSearch Service"), [Amazon SageMaker Unified Studio](https://aws.amazon.com/blogs/aws/category/analytics/amazon-sagemaker-unified-studio/ "View all posts in Amazon SageMaker Unified Studio"), [Amazon Simple Storage Service (S3)](https://aws.amazon.com/blogs/aws/category/storage/amazon-simple-storage-services-s3/ "View all posts in Amazon Simple Storage Service (S3)"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Summit New York](https://aws.amazon.com/blogs/aws/category/events/aws-summit-new-york/ "View all posts in AWS Summit New York"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Storage](https://aws.amazon.com/blogs/aws/category/storage/ "View all posts in Storage") [Permalink](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-vectors-first-cloud-storage-with-native-vector-support-at-scale/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-vectors-first-cloud-storage-with-native-vector-support-at-scale/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing the preview of [Amazon S3 Vectors,](https://aws.amazon.com/s3/features/vectors/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) a purpose-built durable vector storage solution that can reduce the total cost of uploading, storing, and querying vectors by up to 90 percent. Amazon S3 Vectors is the first cloud object store with native support to store large vector datasets and provide subsecond query performance that makes it affordable for businesses to store AI-ready data at massive scale.

Vector search is an emerging technique used in [generative AI](https://aws.amazon.com/generative-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) applications to find similar data points to given data by comparing their vector representations using distance or similarity metrics. Vectors are numerical representation of unstructured data created from [embedding models](https://aws.amazon.com/what-is/embeddings-in-machine-learning/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). You use embedding models to generate vector embeddings of your data and store them in S3 Vectors to perform semantic searches.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/16/2025-s3-vector-1-vector-overview-1.png)

S3 Vectors introduces vector buckets, a new bucket type with a dedicated set of APIs to store, access, and query vector data without provisioning any infrastructure. When you create an S3 vector bucket, you organize your vector data within vector indexes, making it simple for running similarity search queries against your dataset. Each vector bucket can have up to 10,000 vector indexes, and each vector index can hold tens of millions of vectors.

After creating a vector index, when adding vector data to the index, you can also attach metadata as key-value pairs to each vector to filter future queries based on a set of conditions, for example, dates, categories, or user preferences. As you write, update, and delete vectors over time, S3 Vectors automatically optimizes the vector data to achieve the best possible price-performance for vector storage, even as the datasets scale and evolve.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/14/2025-s3-vector-1-overview-1.png)

S3 Vectors is also natively integrated with [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), including within [Amazon SageMaker Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), for building cost-effective [Retrieval-Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) applications. Through its integration with [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), you can lower storage costs by keeping infrequent queried vectors in S3 Vectors and then quickly move them to OpenSearch as demands increase or to support real-time, low-latency search operations.

With S3 Vectors, you can now economically store the vector embeddings that represent massive amounts of unstructured data such as images, videos, documents, and audio files, enabling scalable generative AI applications including semantic and similarity search, RAG, and build agent memory. You can also build applications to support a wide range of industry use cases including personalized recommendations, automated content analysis, and intelligent document processing without the complexity and cost of managing vector databases.

**S3 Vectors in action**

To create a vector bucket, choose **Vector buckets** in the left navigation pane in the [Amazon S3 console](https://console.aws.amazon.com/s3/) and then choose **Create vector bucket**.

Enter a vector bucket name and choose the encryption type. If you don’t specify an encryption type, Amazon S3 applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for new vectors. You can also choose server-side encryption with [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) keys (SSE-KMS). To learn more about managing your vector bucket, visit [S3 Vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-buckets.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the Amazon S3 User Guide.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/15/2025-s3-vector-1-create-vector-bucket.png)

Now, you can create a vector index to store and query your vector data within your created vector bucket.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/15/2025-s3-vector-1-create-vector-index.png)

Enter a vector index name and the dimensionality of the vectors to be inserted in the index. All vectors added to this index must have exactly the same number of values.

For **Distance metric**, you can choose either **Cosine** or **Euclidean**. When creating vector embeddings, select your embedding model’s recommended distance metric for more accurate results.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/15/2025-s3-vector-1-create-vector-index-2-1.png)

Choose **Create vector index** and then you can insert, list, and query vectors.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/10/2025-s3-vector-1-list-vector-bucket-2.png)

To insert your vector embeddings to a vector index, you can use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [AWS SDKs](https://aws.amazon.com/developer/tools/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), or [Amazon S3 REST API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). To generate vector embeddings for your unstructured data, you can use embedding models offered by Amazon Bedrock.

If you’re using the latest AWS Python SDKs, you can generate vector embeddings for your text using Amazon Bedrock using following code example:

```
# Generate and print an embedding with Amazon Titan Text Embeddings V2.
import boto3
import json

# Create a Bedrock Runtime client in the AWS Region of your choice.
bedrock= boto3.client("bedrock-runtime", region_name="us-west-2")

The text strings to convert to embeddings.
texts = [
"Star Wars: A farm boy joins rebels to fight an evil empire in space",
"Jurassic Park: Scientists create dinosaurs in a theme park that goes wrong",
"Finding Nemo: A father fish searches the ocean to find his lost son"]

embeddings=[]
#Generate vector embeddings for the input texts
for text in texts:
        body = json.dumps({
            "inputText": text
        })
        # Call Bedrock's embedding API
        response = bedrock.invoke_model(
        modelId='amazon.titan-embed-text-v2:0',  # Titan embedding model
        body=body)
        # Parse response
        response_body = json.loads(response['body'].read())
        embedding = response_body['embedding']
        embeddings.append(embedding)
```

Now, you can insert vector embeddings into the vector index and query vectors in your vector index using the query embedding:

```
# Create S3Vectors client
s3vectors = boto3.client('s3vectors', region_name='us-west-2')

# Insert vector embedding
s3vectors.put_vectors( vectorBucketName="channy-vector-bucket",
  indexName="channy-vector-index",
  vectors=[
{"key": "v1", "data": {"float32": embeddings[0]}, "metadata": {"id": "key1", "source_text": texts[0], "genre":"scifi"}},
{"key": "v2", "data": {"float32": embeddings[1]}, "metadata": {"id": "key2", "source_text": texts[1], "genre":"scifi"}},
{"key": "v3", "data": {"float32": embeddings[2]}, "metadata": {"id": "key3", "source_text":  texts[2], "genre":"family"}}
],
)

#Create an embedding for your query input text
# The text to convert to an embedding.
input_text = "List the movies about adventures in space"

# Create the JSON request for the model.
request = json.dumps({"inputText": input_text})

# Invoke the model with the request and the model ID, e.g., Titan Text Embeddings V2.
response = bedrock.invoke_model(modelId="amazon.titan-embed-text-v2:0", body=request)

# Decode the model's native response body.
model_response = json.loads(response["body"].read())

# Extract and print the generated embedding and the input text token count.
embedding = model_response["embedding"]

# Performa a similarity query. You can also optionally use a filter in your query
query = s3vectors.query_vectors( vectorBucketName="channy-vector-bucket",
  indexName="channy-vector-index",
  queryVector={"float32":embedding},
  topK=3,
  filter={"genre":"scifi"},
  returnDistance=True,
  returnMetadata=True
  )
results = query["vectors"]
print(results)
```

To learn more about inserting vectors into a vector index, or listing, querying, and deleting vectors, visit [S3 vector buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-vectors.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [S3 vector indexes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-index.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the Amazon S3 User Guide. Additionally, with the S3 Vectors embed command line interface (CLI), you can create vector embeddings for your data using Amazon Bedrock and store and query them in an S3 vector index using single commands. For more information, see the [S3 Vectors Embed CLI GitHub repository](https://github.com/awslabs/s3vectors-embed-cli).

**Integrate S3 Vectors with other AWS services**

S3 Vectors integrates with other AWS services such as Amazon Bedrock, Amazon SageMaker, and Amazon OpenSearch Service to enhance your vector processing capabilities and provide comprehensive solutions for AI workloads.

**Create Amazon Bedrock Knowledge Bases with S3 Vectors**

You can use S3 Vectors in Amazon Bedrock Knowledge Bases to simplify and reduce the cost of vector storage for RAG applications. When creating a knowledge base in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#knowledge-bases?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), you can choose the S3 vector bucket as your vector store option.

In **Step 3**, you can choose the **Vector store creation method** either to create an S3 vector bucket and vector index or choose the existing S3 vector bucket and vector index that you’ve previously created.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/15/2025-s3-vector-2-create-bedrock-kb.png)

For detailed step-by-step instructions, visit [Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the Amazon Bedrock User Guide.

**Using Amazon SageMaker Unified Studio** You can create and manage knowledge bases with S3 Vectors in Amazon SageMaker Unified Studio when you build your generative AI applications through Amazon Bedrock. SageMaker Unified Studio is available in the next generation of Amazon SageMaker and provides a unified development environment for data and AI, including building and texting generative AI applications that use Amazon Bedrock knowledge bases.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/16/2025-s3-vector-3-create-bedrock-kb-sagemaker-unified-studio-1.png)

You can choose **Amazon S3 Vectors** as the **Vector store** when you create a new knowledge bases in the SageMaker Unified Studio. To learn more, visit [Add an Amazon Bedrock Knowledge Base component to a chat agent app](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/creating-a-knowledge-base-component.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the Amazon SageMaker Unified Studio User Guide.

**Export S3 vector data to Amazon OpenSearch Service** You can balance cost and performance by adopting a tiered strategy that stores long-term vector data cost-effectively in Amazon S3 while exporting high priority vectors to OpenSearch for real-time query performance.

This flexibility means your organizations can access OpenSearch’s high performance (high QPS, low latency) for critical, real-time applications, such as product recommendations or fraud detection, while keeping less time-sensitive data in S3 Vectors.

To export your vector index, choose **Advanced search export**, then choose **Export to OpenSearch** in the Amazon S3 console.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/08/2025-s3-vector-1-list-vector-bucket.png)

Then, you will be brought to the [Amazon OpenSearch Service Integration console](https://console.aws.amazon.com/aos/home#opensearch/integrations/s3-vector/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) with a template for S3 vector index export to OpenSearch vector engine. Choose **Export** with pre-selected S3 vector source and a service access role.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/14/2025-s3-vector-3-export-opensearch-1-1.png)

It will start the steps to create a new OpenSearch Serverless collection and migrate data from your S3 vector index into an OpenSearch knn index.

Choose the **Import history** in the left navigation pane. You can see the new import job that was created to make a copy of vector data from your S3 vector index into the OpenSearch Serverless collection.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/14/2025-s3-vector-3-export-opensearch-2-history.png)

Once the status changes to **Complete**, you can [connect to the new OpenSearch serverless collection](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-getting-started.html#serverless-gsg-index?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [query your new OpenSearch knn index](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

To learn more, visit [Creating and managing Amazon OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collections.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the Amazon OpenSearch Service Developer Guide.

**Now available** [Amazon S3 Vectors](https://aws.amazon.com/s3/features/vectors/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), and its integrations with Amazon Bedrock, Amazon OpenSearch Service, and Amazon SageMaker are now in preview in the US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Frankfurt), and Asia Pacific (Sydney) Regions.

Give S3 Vectors a try in the [Amazon S3 console](https://console.aws.amazon.com/s3?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) today and send feedback to [AWS re:Post for Amazon S3](https://repost.aws/tags/TADSTjraA0Q4-a1dxk6eUYaw/amazon-simple-storage-service) or through your usual AWS Support contacts.

— [Channy](https://linkedin.com/in/channy/)

*Updated on July 15, 2025 – Revised the console screenshot of Amazon SageMaker Unified Studio.*

TAGS: [Amazon AI](https://aws.amazon.com/blogs/aws/tag/amazon-ai/), [Homepage Featured](https://aws.amazon.com/blogs/aws/tag/homepage-featured/)

![Channy Yun (윤석찬)](https://d2908q01vomqb2.cloudfront.net/7b52009b64fd0a2a49e6d8a939753077792b0554/2020/06/05/channyun_400x400.jpg)

### [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)")

Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.

Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Top Posts](https://aws.amazon.com/blogs?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Official AWS Podcast](https://aws.amazon.com/podcasts/aws-podcast?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Case Studies](https://aws.amazon.com/solutions/case-studies?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [AWS re:Post](https://repost.aws/ "https://repost.aws/")

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [RSS Feed](https://aws.amazon.com/blogs/aws/feed/)
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