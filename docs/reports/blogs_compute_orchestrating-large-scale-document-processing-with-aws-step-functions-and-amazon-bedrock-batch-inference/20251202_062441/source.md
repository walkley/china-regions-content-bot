# Orchestrating large-scale document processing with AWS Step Functions and Amazon Bedrock batch inference

by Brian Zambrano and Dan Ford on 26 NOV 2025 in Amazon Bedrock, Amazon Bedrock Knowledge Bases, Amazon Nova, Amazon Textract, AWS Step Functions Permalink  Share

Organizations often have large volumes of documents containing valuable information that remains locked away and unsearchable. This solution addresses the need for a **scalable, automated text extraction and knowledge base pipeline** that transforms static document collections into intelligent, searchable repositories for generative AI applications.

Organizations can automate the extraction of both content and structured metadata to build comprehensive knowledge bases that power retrieval-augmented generation (RAG) solutions while significantly reducing manual processing costs and time-to-value. The architecture not only demonstrates the processing of 500 research papers automatically, but also scales to handle enterprise document volumes cost-effectively through the [Amazon Bedrock](https://aws.amazon.com/bedrock/) batch inference pricing model.

## Overview

[Amazon Bedrock batch inference](https://aws.amazon.com/blogs/machine-learning/automate-amazon-bedrock-batch-inference-building-a-scalable-and-efficient-pipeline/) is a feature of Amazon Bedrock that offers a 50% discount on inference requests. Although Amazon Bedrock schedules and runs the batch job (needing a minimum of 100 inference requests) as capacity becomes available, the inference won’t be real-time. For use cases where you can accommodate minutes to hours of latency, Amazon Bedrock batch inference is a good option.

This post demonstrates how to build an automated, serverless pipeline using [AWS Step Functions](https://aws.amazon.com/step-functions/), [Amazon Textract](https://aws.amazon.com/textract/), Amazon Bedrock batch inference, and [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) to extract text, create metadata, and load it into a knowledge base at scale. The example solution processes 500 research papers in PDF format from [Amazon Science](https://www.amazon.science/), extracts text using Amazon Textract, generated structured metadata with Amazon Bedrock batch inference and the [Amazon Nova Pro](https://aws.amazon.com/ai/generative-ai/nova/) model, and loads the final output, including Amazon Bedrock Knowledge Base filter, into an Amazon Bedrock Knowledge Base.

## Architecture

This solution uses Step Functions with parallel Amazon Textract job processing through child workflows run by [Distributed Map](https://docs.aws.amazon.com/step-functions/latest/dg/state-map-distributed.html). You can use the concurrency controls offered by Distributed Map to process documents as quickly as possible within your Amazon Textract quotas. Increasing processing speed necessitates adjusting your Amazon Textract quota and updating the Distributed Map configuration. Amazon Bedrock batch inference handles concurrency, scaling, and throttling. This means that you can create the job without managing these complexities.

In this example implementation, the solution processes research papers to extract metadata such as:

- Code availability and repository locations
- Dataset availability and access methods
- Research methodology types
- Reproducibility indicators
- Other relevant research attributes

The high-level parts of this solution include:

- Extracting text from PDF documents with Amazon Textract in parallel, through Step Functions Distributed Map.
- Analyzing extracted text using Amazon Bedrock batch inference to extract structured metadata.
- Loading extract text and metadata into a searchable knowledge base using Amazon Bedrock Knowledge Bases with [Amazon OpenSearch Serverless](https://aws.amazon.com/opensearch-service/features/serverless/).

[![Complete architecture diagram](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/26/computeblog-2442-1.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/26/computeblog-2442-1.png)

Figure 1. Complete architecture diagram

## Prerequisites

The following prerequisites are necessary to complete this solution:

- Access to an [AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) through the [AWS Management Console](https://aws.amazon.com/console/) and the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli). The [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) user that you use must have permissions to make the necessary AWS service calls and manage AWS resources mentioned in this post. While providing permissions to the IAM user, follow the [principle of least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. If you are using long-term credentials such as access keys, then follow [manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) and [secure access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/securing_access-keys.html) for best practices.
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- Python 3.13+ installed.
- Node and npm installed.
- [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) installed.

## Running the solution

The complete solution uses AWS CDK to implement two [AWS CloudFormation](https://aws.amazon.com/cloudformation/) stacks:

1. BedrockKnowledgeBaseStack: Creates the knowledge base infrastructure
2. SFNBatchInferenceStack: Implements the main processing workflow

First, clone the GitHub repository into your local development environment and install the requirements:

`git clone https://github.com/aws-samples/sample-step-functions-batch-inference.git .`

`cd sample-step-functions-batch-inference`

`npm install`

Next, deploy the solution using AWS CDK:

`cdk deploy --all`

After deploying the cdk stacks, upload your data sources (PDF files) into the AWS CDK-created [Amazon S3](https://aws.amazon.com/s3/) input bucket. In this example, I uploaded 500 Amazon Science papers. The input bucket name is included in the AWS CDK outputs:

Outputs:

`SFNBatchInference.BatchInputBucketName = sfnbatchinference-batchinputbucket11aaa222-nrjki8tewwww`

### Parallel text extraction

The process begins when you upload a manifest.json file to the input bucket. The manifest file lists the files for processing, which already exist in the input bucket. The filenames listed in manifest.json define what constitutes a single processing job run. To create another run, you would create a different manifest.json and upload it to the same S3 bucket.

```
[
{
"filename": "flexecontrol-flexible-and-efficient-multimodal-control-for-text-to-image-generation.pdf"
},
{
"filename": "adaptive-global-local-context-fusion-for-multi-turn-spoken-language-understanding.pdf"
}
]

```

The AWS CDK definition for the input bucket includes [Amazon EventBridge](https://aws.amazon.com/eventbridge/) notifications and creates a rule that triggers the Step Functions workflow whenever a manifest.json file is uploaded.

```
private createS3Buckets() {
const batchBucket = new s3.Bucket(this, "BatchInputBucket", {
removalPolicy: cdk.RemovalPolicy.DESTROY,
autoDeleteObjects: true,
})
batchBucket.enableEventBridgeNotification()

new cdk.CfnOutput(this, "BatchInputBucketName", {
value: batchBucket.bucketName,
description: "Name of input bucket to send PDF documents that Textract will read.",
})

const manifestFileCreatedRule = new eventBridge.Rule(this, "ManifestFileCreatedRule", {
eventPattern: {
source: ["aws.s3"],
detailType: ["Object Created"],
detail: {
bucket: {
name: [batchBucket.bucketName],
},
object: {
key: ["manifest.json"],
},
},
},
})

return { batchBucket, manifestFileCreatedRule }
}

```

The first step in the Step Functions workflow is a Distributed Map run that performs the following actions for each PDF in the manifest file:

1. Starts an Amazon Textract job, providing an [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) topic for completion notification.
2. Writes the Step Functions task token to [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), pausing the individual child workflow.
3. Processes the Amazon SNS message when the Amazon Textract job completes, triggering an [AWS Lambda](https://aws.amazon.com/lambda/) function.
4. Uses a Lambda function to retrieve the task token from DynamoDB using the Amazon Textract JobId.
5. Fetches the raw results from Amazon Textract, organizes the text for readability, and writes results to an S3 bucket

[![First step in the Step Functions workflow](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/26/computeblog-2442-2.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/26/computeblog-2442-2.png)

A key component of this architecture is the callback pattern that Amazon Textract supports using the NotificationChannel option, as shown in the preceding figure. The AWS CDK definition the Step Functions state that starts the Amazon Textract job is shown in the following.

```
const startTextractStep = new tasks.CallAwsService(this, "StartTextractJob", {
service: "textract",
action: "startDocumentAnalysis",
resultPath: "$.textractOutput",
parameters: {
DocumentLocation: {
S3Object: {
Bucket: sourceBucket.bucketName,
Name: sfn.JsonPath.stringAt("$.filename"),
},
},
FeatureTypes: ["LAYOUT"],
NotificationChannel: {
RoleArn: textractRoleArn,
SnsTopicArn: snsTopicArn,
},
},
iamResources: ["*"],
})

```

The Lambda function that handles task tokens extracts the Amazon Textract JobId from the Amazon SNS message, fetches the TaskToken from DynamoDB, and resumes the Step Functions Workflow by sending the TaskToken:

```
from aws_lambda_powertools.utilities.data_classes import SNSEvent, event_source

@event_source(data_class=SNSEvent)
def handle_textract_task_complete(event, context):
# Multiple records can be delivered in a single event
for record in event.records:
sns_message = json.loads(record.sns.message)
textract_job_id = sns_message["JobId"]

# Get both task token and original file from DynamoDB
ddb_item = _get_item_from_ddb(textract_job_id)

# Send both the job ID and original file name in the response
_send_task_success(
ddb_item["TaskToken"],
{
"TextractJobId": textract_job_id,
"OriginalFile": ddb_item["OriginalFile"],
},
)
# Delete the task token from DynamoDB after use
_delete_item_from_ddb(textract_job_id)

def _send_task_success(task_token: str, output: None | dict = None) -> None:
"""Sends task success to Step Functions with the provided output"""
sfn = boto3.client("stepfunctions")
sfn.send_task_success(taskToken=task_token, output=json.dumps(output or {}))

```

The Distributed Map runs up to 10 child workflows concurrently, controlled by the maxConcurrency setting. Although Step Functions supports running up to 10,000 child workflow executions, the practical concurrency for this solution is constrained by Amazon Textract quotas. The startDocumentAnalysis API has a default quota of 10 requests per second (RPS), which means you must consider this limit when scaling your document processing workloads and potentially request quota increases for higher throughput requirements.

```
const distributedMap = new sfn.DistributedMap(this, "DistributedMap", {
mapExecutionType: sfn.StateMachineType.STANDARD,
maxConcurrency: 10,
itemReader: new sfn.S3JsonItemReader({
bucket: sourceBucket,
key: "manifest.json",
}),
resultPath: "$.files",
}

```

### Running Amazon Bedrock batch inference

When all of the Amazon Textract jobs finish, the Distributed Map state creates an Amazon Bedrock batch inference input file, launches the Amazon Bedrock inference job, and waits for it to complete.

6. A Lambda function collects text results from Amazon S3 and creates an Amazon Bedrock batch inference input file with custom prompts.
7. The workflow starts the Amazon Bedrock batch inference job by calling createModelInvocationJob and sending the batch inference input file as input.
8. The workflow pauses and stores the task token in DynamoDB.
9. An EventBridge rule matches completed Amazon Bedrock batch inference events, and upon job completion and triggers a Lambda function. The Lambda function retrieves the task token and resumes the workflow, as shown in the following figure.

[![Lambda function retrieves the task token and resumes the workflow](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/26/computeblog-2442-3.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/26/computeblog-2442-3.png)

A batch inference input is a single jsonl file with multiple entries such as the following example. The prompt in each inference request instructs the large language model (LLM) to analyze the paper and extract metadata. Read the full [prompt template in the GitHub repository](https://github.com/aws-samples/sample-step-functions-batch-inference/blob/956b5fc645c7de5f43d650d21ef9df011db67170/src/bedrock-batcher/handler.py#L41-L81).

```
{
"recordId": "c1b8a3b2086141f963",
"modelInput": {
"messages": [
{
"role": "user",
"content": [
{
"text": "Analyze the following research paper transcript and extract metadata about code and dataset availability. Extract the following metadata from this research paper transcript:\n\n1. **has_code**: Does the paper mention or link to source code? (true/false) ...... Return only valid JSON matching the schema above. Do not include any text outside of the JSON structure."
}
]
}
],
"inferenceConfig": { "maxTokens": 4096 }
}
}

```

### Populating the Amazon Bedrock Knowledge Base

After the batch inference completes, the workflow does the following:

10. Extracts inference results and creates metadata files based on the Amazon Bedrock inference results (example metadata shown in the following figure).
11. Starts an Amazon Bedrock Knowledge Base ingestion job.
12. Monitors the ingestion job status using Step Functions Wait and Choice states.
13. Sends a completion notification through Amazon SNS.

[![Populating the Amazon Bedrock Knowledge Base](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/26/computeblog-2442-4.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/26/computeblog-2442-4.png)

The following shows the example metadata format:

```
{
"metadataAttributes": {
"has_code": true,
"has_dataset": false,
"code_availability": "publicly_available",
"dataset_availability": "not_available",
"research_type": "methodology",
"is_reproducible": true,
"code_repository_url": "https://github.com/amazon-science/PIXELS"
}
}

```

## Testing the knowledge base

After the workflow completes successfully, you can test the knowledge base to verify that the documents and metadata have been properly ingested and are searchable. There are two practical methods for testing an Amazon Bedrock Knowledge Base:

1. Using the Console
2. Using the AWS SDK to run a query

## Testing through the Console

The Console provides an intuitive interface for testing your knowledge base queries with metadata filters:

1. Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/).
2. In the left navigation pane, choose **Knowledge Bases** under the **Build** section.
3. Choose the knowledge base created by the AWS CDK deployment (the name will be output by the AWS CDK stack).
4. Choose the **Test** button in the upper right corner.
5. In the test interface, choose your preferred foundation model (FM) (such as Amazon Nova Pro).
6. Expand the **Configurations** column, then navigate to the **Filters** section.
7. Configure filters based on the extracted metadata, as shown in the following figure.

[![Configure filters based on the extracted metadata](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/25/computeblog-2442-5.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/25/computeblog-2442-5.png)

Enter a natural language query related to your documents, for example: “Recent research on retrieval augmented generation?”

The console displays the generated response along with source attributions showing which documents were retrieved and used to formulate the answer, filtered by your specified metadata attributes, as shown in the following figure.

[![A chat example](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/25/compute-2442-6.png)](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2025/11/25/compute-2442-6.png)

## Testing via API

For programmatic testing and integration into applications, use the AWS SDK with metadata filtering. The following is a Python example using boto3:

```
model_arn = "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-pro-v1:0"

# Query for papers with publicly available code
response = bedrock_agent_runtime.retrieve_and_generate(
input={'text': "What recent research has been done on RAG?"},
retrieveAndGenerateConfiguration={
'type': 'KNOWLEDGE_BASE',
'knowledgeBaseConfiguration': {
'knowledgeBaseId': knowledge_base_id,
'modelArn': model_arn,
'retrievalConfiguration': {
'vectorSearchConfiguration': {
'numberOfResults': 5,
'filter': {"equals": {"key": "has_code", "value": True}},
}
},
},
},
)

# Display results
print(f"Response: {response['output']['text']}\n")
print("Source Documents:")

for citation in response.get('citations', []):
for reference in citation.get('retrievedReferences', []):
metadata = reference.get('metadata', {})
print(f" Document: {reference['location']['s3Location']['uri']}\n")

```

The following is the test script output:

```
Response: Recent research on Retrieval-Augmented Generation (RAG) has focused on enhancing the system's ability to dynamically retrieve and utilize relevant information from a Vector Database (VDB) to improve decision-making and performance. Key innovations include:

1. **Dynamic Retrieval and Utilization**: The system is designed to query the VDB for contextually relevant past experiences, which significantly improves decision quality and accelerates performance by leveraging a growing repository of relevant experiences.

2. **Teacher-Student Instructional Tuning**: A novel mechanism where a Teacher agent refines a Student agent's core policy through direct interaction. The Teacher generates a modified SYSTEM prompt based on the Student's actions, creating a meta-learning loop that enhances the Student's reasoning policy over time.

```

## Conclusion

This solution demonstrates how to combine multiple AWS AI and serverless services to build a scalable document processing pipeline. Organizations can use AWS Step Functions for orchestration, Amazon Textract for document processing, Amazon Bedrock batch inference for intelligent content analysis, and Amazon Bedrock Knowledge Bases for searchable storage. In turn, they can automate the extraction of insights from large document collections while optimizing costs.

Following this solution, you can build a solid foundation for production-scale document processing pipelines that maintain the flexibility to adapt to your specific requirements while making sure of reliability, scalability, and operational excellence. Follow this link to learn more about [serverless architectures](https://serverlessland.com/).