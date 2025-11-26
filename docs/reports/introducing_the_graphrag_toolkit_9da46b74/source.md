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

# Introducing the GraphRAG Toolkit

by Ian Robinson and Abdellah Ghassel on 27 JAN 2025 in [Amazon Neptune](https://aws.amazon.com/blogs/database/category/database/amazon-neptune/ "View all posts in Amazon Neptune"), [Amazon Neptune Analytics](https://aws.amazon.com/blogs/database/category/database/amazon-neptune-analytics/ "View all posts in Amazon Neptune Analytics"), [Technical How-to](https://aws.amazon.com/blogs/database/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/database/introducing-the-graphrag-toolkit/)  [Comments](https://aws.amazon.com/blogs/database/introducing-the-graphrag-toolkit/#Comments)  Share

[Amazon Neptune](https://aws.amazon.com/neptune/) recently released the [GraphRAG Toolkit](https://github.com/awslabs/graphrag-toolkit), an open source Python library that makes it straightforward to build graph-enhanced Retrieval Augmented Generation (RAG) workflows. The toolkit provides a framework for automating the construction of a graph with vector embeddings from unstructured data, and composing question-answering strategies that query this graph to retrieve structurally relevant information when answering user questions.

In this post, we describe how you can get started with the toolkit. We begin by looking at the benefits of adding a graph to your RAG application. Then we show you how to set up a quick start environment and install the toolkit. Lastly, we discuss some of the design considerations that led to the toolkit’s graph model and its approach to content retrieval.

## Why add a graph to your RAG application?

Consider the following fictitious narrative, assembled from different news articles, press releases, industry publications, and analyst reports over the course of several weeks, and fed, together with many other documents, into a RAG workflow:

* Example Corp, the US-based maker of the popular Widget personal gizmo, has recently extended its worldwide distribution channels by partnering with AnyCompany Logistics, an international shipping, storage, and last-mile distribution provider. Widget is an AI-augmented personal desktop pet whose conversational capabilities are powered by a new breed of generative AI technologies. Developed in the Austin-based Example Corp labs, the toys are manufactured in Taiwan.
* The UK’s Christmas top-10 toy predictions are already in, even though it’s only August, with industry analysts predicting huge demand for Example Corp’s Widget chatty desktop pet. Retailers in London, Manchester, and other major cities have already placed orders for over 1 million units, to the value of $15 million, and those numbers are only set to increase in the months leading up to Christmas.
* AnyCompany Logistics today announced that it is cutting shipping times from Taiwan to the UK from 2 weeks to just 3 days by directing all distribution through the recently opened Fictitious Canal. The Fictitious Canal is set to become one of the most heavily trafficked waterways over the next 5 years as manufacturers and distributors look to move from air to sea to cut energy spend and save costs.
* The Fictitious Canal continues to experience blockages and delays following landslips. Over 5 million tons of rock has now blocked the southern basin, trapping container vessels and disrupting international supply chains. Goods destined for Europe are expected to be delayed for several months, meaning that Christmas inventory for many retailers is under threat.

Imagine you’re a researcher. What do you want to know? How about: What are the sales prospects for Example Corp in the UK?

We asked a leading vector-based RAG application and got the following response:

*Based on the provided context, the sales prospects for Example Corp’s Widget product in the UK appear to be very strong for the upcoming Christmas season. Industry analysts have predicted huge demand for the Widget chatty desktop pet, even ranking it among the top 10 toys for Christmas. Retailers in major UK cities like London and Manchester have already placed orders for over 1 million units worth $15 million, and these order numbers are expected to increase further as Christmas approaches. The context suggests Example Corp can anticipate very high sales volumes and revenues from the UK market for their Widget product during the critical holiday shopping period.*

Then we asked an application built using the GraphRAG Toolkit and got the following response:

*Based on the search results, the sales prospects for Example Corp’s Widget chatty desktop pet in the UK appear to be very promising initially, but there are potential supply chain issues that could hamper sales later on.*

*The search results indicate that retailers in major UK cities like London and Manchester have already placed orders for over 1 million units of the Widget product, anticipating huge demand. Industry analysts are also predicting high demand for this toy.*

*To meet this expected demand, Example Corp has partnered with AnyCompany Logistics to extend its worldwide distribution channels, including in the UK. AnyCompany Logistics had announced plans to significantly cut shipping times from Taiwan to the UK from 2 weeks down to just 3 days by routing shipments through the newly opened Fictitious Canal.*

*However, there are reports of a major blockage in the Fictitious Canal caused by landslips, with over 5 million tons of rock obstructing the southern basin and trapping container vessels. This could potentially disrupt international supply chains and delay goods destined for Europe, including the UK, for several months.*

*So while initial sales prospects for Example Corp’s Widget product in the UK look very promising based on pre-orders and anticipated demand, there is a risk that supply chain issues caused by the Fictitious Canal blockage could hamper the ability to meet that demand in the coming months if the situation is not resolved quickly.*

Why the big difference? What does the graph approach offer that the primarily vector-based one doesn’t?

Vector search can only retrieve information that is *semantically similar*, or close in language, to the question being asked. Information that is dissimilar is structurally unavailable for retrieval. In our example, the fragments concerning AnyCompany Logistics’ use of the Fictitious Canal, and the current blockages troubling the Canal, are sufficiently dissimilar to the question being asked that they don’t get pulled into the context by the vector-based solution—even though they are crucial in formulating a more accurate and complete response.

[![Question: What are the sales prospects for Example Corp in the UK?](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-question.png)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-question.png)

Relevancy can be thought of in terms of *relatedness*: whatever is relevant to the question is somehow related, either directly or indirectly, to the question. Relatedness is a broader concept than similarity. Semantic similarity is just one way in which the things that are of interest to us can be related to one another; we might say, for example, that texts A and B are related because they are semantically similar. But there are lots of other ways in which things can be related: contiguity in time or space, cause and effect, parent-child, part-whole; or social, organizational, legal, taxonomic relations—the list is endless. The ways in which things are related, and the relative importance, strength, and quality of those relationships, will vary from domain to domain, but suffice to say, “is semantically similar to” is just one tool in your RAG retrieval toolbox.

By modeling our domain as a graph and using the edges in the graph to represent the different types of relationships that are important to us, we can provide access to information that is dissimilar to the question but nonetheless structurally relevant for creating an accurate and full response.

Similarity-based retrieval remains an important RAG strategy, and context that is semantically similar to the question will often comprise the foundation of a good answer. However, similarity-based retrieval alone is not always sufficient for generating a nuanced response. In many circumstances it will also be necessary to find and return information that can’t be found using vector similarity search, in order to present a question-answering process with a more differentiated context that it can use to develop comparisons, arguments, and summaries. The relationships in a graph provide a means by which a retrieval process can find this additional, relevant information.

## The GraphRAG Toolkit

Every RAG application is built around two core capabilities: indexing and querying. The GraphRAG Toolkit is an open source Python library that you can use both to index your data into a graph and a vector store, and build question-answering solutions that then retrieve relevant content from this graph.

With the first version of the toolkit, the focus is on building graph-based RAG applications over unstructured and semi-structured textual content (such as webpages, PDFs, and JSON documents). See the Installing the GraphRAG Toolkit section later in this post for details on setting up and running the toolkit.

### Indexing

Indexing content is just a few lines of code:

```
from graphrag_toolkit import LexicalGraphIndex
from graphrag_toolkit.storage import GraphStoreFactory
from graphrag_toolkit.storage import VectorStoreFactory

from llama_index.readers.web import SimpleWebPageReader

import nest_asyncio
nest_asyncio.apply()

doc_urls = [
    'https://docs.aws.amazon.com/neptune/latest/userguide/intro.html',
    'https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html',
    'https://docs.aws.amazon.com/neptune-analytics/latest/userguide/neptune-analytics-features.html',
    'https://docs.aws.amazon.com/neptune-analytics/latest/userguide/neptune-analytics-vs-neptune-database.html'
]

docs = SimpleWebPageReader(
    html_to_text=True,
    metadata_fn=lambda url:{'url': url}
).load_data(doc_urls)

graph_store = GraphStoreFactory.for_graph_store(
    'neptune-db://my-graph.cluster-abcdefghijkl.us-east-1.neptune.amazonaws.com'
)

vector_store = VectorStoreFactory.for_vector_store(
    'aoss://https://abcdefghijkl.us-east-1.aoss.amazonaws.com'
)

graph_index = LexicalGraphIndex(
    graph_store,
    vector_store
)

graph_index.extract_and_build(docs)
```

The `LexicalGraphIndex` is the primary means of indexing content. You can use it, as shown in this example, in a continuous-ingest fashion, whereby content is pipelined through a set of extract and build stages, so that the graph soon starts to be populated with data that can then be queried even while the ingest continues. You can also use it to run separate extract and build stages—something you might do if you have a one-time-only job, or want to build and rebuild a graph multiple times from the same underlying extracted content.

A `LexicalGraphIndex` is configured with a graph store and a vector store. For this example, we’re using a Neptune Database graph store and an [Amazon OpenSearch Serverless](https://aws.amazon.com/opensearch-service/features/serverless/) vector store. At the time of writing, the toolkit supports Neptune Database and Neptune Analytics, OpenSearch Serverless, and [Amazon Bedrock](https://aws.amazon.com/bedrock/) for the foundation models (FMs) used to extract and embed content.

The content that is being indexed in the preceding example comprises several pages of Neptune documentation. We’re using a [LlamaIndex](https://docs.llamaindex.ai/) `[SimpleWebPageReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/)` to parse and load the data into the index. Depending on the type and location of your source data, you can use other LlamaIndex readers, including the `[SimpleDirectoryReader](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/)` and the `[JSONReader](https://llamahub.ai/l/readers/llama-index-readers-json)`, to load data into the index.

### Querying

Querying, or question answering, is as straightforward as indexing:

```
from graphrag_toolkit import LexicalGraphQueryEngine
from graphrag_toolkit.storage import GraphStoreFactory
from graphrag_toolkit.storage import VectorStoreFactory

import nest_asyncio
nest_asyncio.apply()

graph_store = GraphStoreFactory.for_graph_store(
    'neptune-db://my-graph.cluster-abcdefghijkl.us-east-1.neptune.amazonaws.com'
)

vector_store = VectorStoreFactory.for_vector_store(
    'aoss://https://abcdefghijkl.us-east-1.aoss.amazonaws.com'
)

query_engine = LexicalGraphQueryEngine.for_traversal_based_search(
    graph_store,
    vector_store
)

response = query_engine.query('''What are the differences between Neptune Database
                                 and Neptune Analytics?''')

print(response.response)
```

Querying is actually a two-step process. It starts by retrieving relevant information from the underlying storage, and then supplies this information to a large language model (i.e. the FM) for the FM to generate an answer. The `LexicalGraphQueryEngine` performs both steps on your behalf.

Again, we’re configuring the process with a graph store and vector store. At first glance, this looks a little redundant—after all, didn’t we already specify the graph and vector stores in the indexing stage? But remember, indexing and querying are two separate processes. These processes could be running in different environments, on different machines, and at different times. As such, each process needs to be configured with the location of its graph and vector stores.

## Installing the GraphRAG Toolkit

You can get started with the GraphRAG Toolkit using the quick start AWS CloudFormation [template](https://github.com/awslabs/graphrag-toolkit/blob/main/examples/cloudformation-templates/graphrag-toolkit-stack.json) from the project’s GitHub repository. This template creates a Neptune database and OpenSearch Serverless collection, and an [Amazon SageMaker](https://aws.amazon.com/sagemaker/) notebook instance with example code. The examples use FMs in Amazon Bedrock to extract and embed content, and generate responses.

## Prerequisites

Before you run the template, make sure you have enabled access to the appropriate FMs in Amazon Bedrock. The default models are:

* `anthropic.claude-3-sonnet-20240229-v1:0`
* `cohere.embed-english-v3`

You can [configure](https://github.com/awslabs/graphrag-toolkit/blob/main/docs/configuration.md) the toolkit with other models, besides those configured in the quick start examples.

You must run the CloudFormation stack in an AWS Region containing these models, and [enable access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) to the models before running the notebook examples.

## Deploy the CloudFormation stack

The following screenshot shows the stack details for the CloudFormation template.

[![CloudFormation stack details](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-cfn.png)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-cfn.png)

You need to supply a stack name. Most of the parameters have been populated with sensible defaults, but there are a couple you may want to change:

* **ApplicationId** – Use this to specify a unique identifier that will be used to name the resources in the deployment, including the Neptune cluster and instance, and the OpenSearch Serverless collection.
* **IamPolicyArn** – Use this to specify the Amazon Resource Name (ARN) of an additional [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) policy to be attached to the SageMaker notebook instance. This custom policy can contain permissions to additional resources that you want to use, such as specific [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) buckets, or additional Amazon Bedrock FMs.

The template creates the following resources:

* A virtual private cloud (VPC) with three private subnets, one public subnet, and an internet gateway
* A Neptune Database cluster with a single Neptune serverless instance
* An OpenSearch Serverless collection with a public endpoint
* A SageMaker notebook containing the GraphRAG Toolkit sample notebooks

When the stack deployment has completed, you can open the SageMaker sample notebooks (there’s a NeptuneSagemakerNotebook output parameter on the **Outputs** tab of the stack, with a link to the notebook instance), and start indexing and querying your content.

## Run the notebooks

Notebook [01 – Combined-Extract-and-Build](https://github.com/awslabs/graphrag-toolkit/blob/main/examples/notebooks/01-Combined-Extract-and-Build.ipynb) is a good place to start. The first cell in each notebook installs the toolkit from the GitHub repository. You only need to run this install one time per deployment, not for every notebook.

When the install has completed, you can run the second cell, which indexes the example content.

[![Ingest example](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-ingest.png)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-ingest.png)

With the indexing complete, you can start querying the content. Notebook [04 – Querying](https://github.com/awslabs/graphrag-toolkit/blob/main/examples/notebooks/04-Querying.ipynb) allows you to experiment with the different query strategies contained in the toolkit.

[![Query example](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-query.png)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-query.png)

## Clean up

The resources deployed incur costs in your account. Remember to [delete the stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) when you’ve finished with it so that you don’t incur any unnecessary charges (approximately $1.5/hour in the US East (N. Virginia) AWS Region).

## Build your own applications

You don’t need to run the quick start CloudFormation template to use the toolkit. You can install the toolkit in your own environment, and build your own Python applications that compose the toolkit with other libraries and services (you will need to provision the necessary graph and vector store resources, and make sure you have access to the appropriate FMs beforehand).

You can install the toolkit and its dependencies using pip (the toolkit isn’t currently available on PyPi, but we make frequent releases to the project’s GitHub repository). Follow the [installation instructions](https://github.com/awslabs/graphrag-toolkit?tab=readme-ov-file#installation) on the project’s homepage to install the latest version.

The project’s [documentation](https://github.com/awslabs/graphrag-toolkit/tree/main/docs) contains many examples of configuring and running the [indexing](https://github.com/awslabs/graphrag-toolkit/blob/main/docs/indexing.md) and [querying](https://github.com/awslabs/graphrag-toolkit/blob/main/docs/querying.md) processes. You can adapt these examples for use in your own applications. The examples in the documentation are written for running in a notebook environment. If you’re building an application with a main entry point, you should put the application logic inside a method, and add an `if __name__ == '__main__'` block:

```
import os

from graphrag_toolkit import LexicalGraphIndex
from graphrag_toolkit.storage import GraphStoreFactory
from graphrag_toolkit.storage import VectorStoreFactory

from llama_index.readers.web import SimpleWebPageReader

import nest_asyncio
nest_asyncio.apply()

def run_extract_and_build():

    graph_store = GraphStoreFactory.for_graph_store(
        'neptune-db://my-graph.cluster-abcdefghijkl.us-east-1.neptune.amazonaws.com'
    )

    vector_store = VectorStoreFactory.for_vector_store(
        'aoss://https://abcdefghijkl.us-east-1.aoss.amazonaws.com'
    )

    graph_index = LexicalGraphIndex(
        graph_store,
        vector_store
    )

    doc_urls = [
        'https://docs.aws.amazon.com/neptune/latest/userguide/intro.html',
        'https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html',
        'https://docs.aws.amazon.com/neptune-analytics/latest/userguide/neptune-analytics-features.html',
        'https://docs.aws.amazon.com/neptune-analytics/latest/userguide/neptune-analytics-vs-neptune-database.html'
    ]

    docs = SimpleWebPageReader(
        html_to_text=True,
        metadata_fn=lambda url:{'url': url}
    ).load_data(doc_urls)

    graph_index.extract_and_build(docs, show_progress=True)

if __name__ == '__main__':
    run_extract_and_build()
```

## Graph model and query strategy design

When designing a RAG solution, it’s useful to adopt a working backwards approach in order to determine an appropriate set of retrieval and generation strategies, and an underlying indexing and storage scheme, capable of supporting your specific workload needs. What kinds of question-answering or end-user or application data needs is your workflow intended to fulfil? What kinds of data must you therefore retrieve to satisfy those needs? What kinds of retrieval strategies will best furnish the context window with this data? And what kinds of indexing structures or data models will most efficiently facilitate such retrieval?

The GraphRAG Toolkit is designed to support question-answering workflows over unstructured and semi-structured textual content, and in particular workflows that require retrieving relevant information from multiple, potentially unrelated sources, or information that is structurally inaccessible to solely vector-based solutions. We might call these *search-based* workflows, as opposed to *counting*– or *aggregation-based* workflows, which would require computing a numerical result.

To satisfy the needs of a search-based workflow, the system should present the question-answering process—the FM—with pieces of relevant textual content: snippets of text, or lexical units, that the FM can use to generate a response. With this in mind, one of the first design decisions we had to address was, what size lexical unit should form the basis of the context supplied to the FM? For many RAG applications, the primary unit of context is the *chunk*: that is, the context window is formed of one or more chunks retrieved from the corpus. Different chunking strategies produce differently sized chunks—there’s no one-size-fits-all definition of a chunk—but a chunk is typically larger than an individual sentence but smaller than an entire document.

For the GraphRAG Toolkit, the primary unit of context is not the chunk, but the *statement*, which is a standalone assertion or proposition. Source documents are broken into chunks, and from these chunks are extracted statements. Statements are thematically grouped by topic, and supported by facts. At question-answering time, the toolkit retrieves sets of relevant statements grouped by topic, and presents them in the context window to the FM.

This requirement to supply lexical units in the form of statements to the FM led us to design a *lexical graph* model, and an extraction process that targets this model. This lexical graph has three tiers:

* **Lineage** – Sources, chunks, and the relations between them
* **Summarization** – Topics, statements, and the facts that support statements
* **Entity-relationship** – Individual entities and relations extracted from the underlying sources

The following diagram shows the overall lexical graph model.

[![Lexical graph model](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-datamodel.png)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-datamodel.png)

You can read more about this graph model in the toolkit’s [documentation](https://github.com/awslabs/graphrag-toolkit/blob/main/docs/graph-model.md). In this section, we dive deeper into the summarization tier.

When we design a graph model, we often think of this model in terms of its capacity to represent the things we’re interested in. An alternative, though complementary, viewpoint is to consider the role or responsibility of each model element in the context of the application and data needs the model is intended to support. In the context of the search-based workflow needs we’ve identified for the toolkit, the model should support retrieving discrete lexical units that are related directly or indirectly to the question. The way in which the model exhibits and applies this relatedness or connectedness will determine in large part the effectiveness of the retrieval strategies. If it simply links everything to everything else, it makes it difficult to extract relevant units of context from within a sea of irrelevancy. If, on the other hand, the model permits very few links between elements in the graph, it reduces the opportunities for discovering relevant but nonetheless semantically dissimilar information. A well-designed graph strikes a balance: it avoids overwhelming connections that dilute relevance while ensuring enough links to discover contextually important but non-obvious relationships.

The elements in the summarization tier fulfil several different responsibilities. In terms of retrieving lexical units, statements act as the primary unit of context returned to the FM. In terms of connectedness, the summarization tier distinguishes between local and global connectedness. Topics provide local thematic connectivity between statements derived from the same source. Facts provide global connectivity between statements derived from different sources. (Topics and facts also have secondary responsibilities: topics act to group statements; facts act to annotate or furnish statements with more detail.) This division between local and global connectivity responsibilities allows retrieval strategies to control their exploration of the graph: a retriever can choose to stay mostly local, while tentatively exploring more remote opportunities, or start broad, and then narrow in on the most promising topics.

When retrieving content from the graph, retrieval strategies must first find one or more suitable entry points, before then traversing to relevant statements. The vector store plays an important part here in finding entry points. In the current lexical graph implementation, both statements and chunks are embedded. Retrievers can therefore find entry points that are semantically similar to the question, either at the chunk or the statement level, and from there explore neighboring local statements as well as hop to more indirectly connected, remote statements. Retrievers can also perform keyword lookups against entities in the entity-relationship tier, and from there navigate to statements and topics—an approach that tends to yield a broader set of statements.

The toolkit currently contains two different high-level retrievers: a `TraversalBasedRetriever` and a `SemanticGuidedRetriever`. The `TraversalBasedRetriever` uses a combination of top-down search—finding chunks through vector similarity search, and then traversing from these chunks through topics to statements and facts—and bottom-up search, which performs keyword-based lookups of entities, and proceeds through facts to statements and topics. The `SemanticGuidedRetriever` blends vector-based semantic search with structured graph traversal. It identifies entry points through semantic and keyword searches, then intelligently explores the graph through beam search and path analysis, while employing reranking and diversity filtering to achieve quality results. This hybrid approach enables both precise matching and contextual exploration.

## Conclusion

In this post, we discussed how you can get started with the GraphRAG Toolkit. This open source Python library can help you build RAG applications that use a graph to retrieve structurally relevant information.

Try out the [toolkit](https://github.com/awslabs/graphrag-toolkit) for your own use case, and share your feedback in the comments.

---

### About the Authors

[![Ian Robinson](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-ianrob.jpg)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-ianrob.jpg)**Ian Robinson** is a Principal Graph Architect with Amazon Neptune. He is a co-author of ‘Graph Databases’ and ‘REST in Practice’ (both from O’Reilly) and a contributor to ‘REST: From Research to Practice’ (Springer) and ‘Service Design Patterns’ (Addison-Wesley).

[![Abdellah Ghassel](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-abdghsl.jpg)](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/01/14/DBBLOG-4573-abdghsl.jpg)**Abdellah Ghassel** is a Machine Learning Engineer Intern with Amazon Neptune

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