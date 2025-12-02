# How Letta builds production-ready AI agents with Amazon Aurora PostgreSQL

by Sarah Wooders and Steve Dille on 26 NOV 2025 in Advanced (300), Amazon Aurora, Customer Solutions, PostgreSQL compatible Permalink  Comments   Share

AI agents require persistent memory to maintain context, learn from past interactions, and provide consistent responses over time. Consider a customer service AI agent deployed at a large ecommerce company. Without long-term memory, the agent would need to ask customers to repeat their order numbers, shipping preferences, and past issues in every conversation. This creates a frustrating experience where customers feel unrecognized and need to constantly provide context. With long-term memory, the agent can recall previous interactions, understand customer preferences, and maintain context across multiple support sessions, even when conversations span several days or weeks.

With the [Letta Developer Platform](https://www.letta.com/), you can create stateful agents with built-in context management (compaction, context rewriting, and context offloading) and persistence. Using the Letta API, you can create agents that are long-lived or achieve complex tasks without worrying about context overflow or model lock-in. You can self-host the Letta API in your own virtual private cloud (VPC) and persist agent state in [Amazon Aurora PostgreSQL-Compatible Edition](https://aws.amazon.com/rds/aurora/postgresql-features/). Letta persists all state, including memories, tools, and messages, in normalized tables, so you can query data across agents and port state across different model providers.

In this post, we guide you through setting up [Amazon Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/) as a scalable, highly available PostgreSQL database repository for storing Letta long-term memory. We show how to create an Aurora cluster in the cloud, configure Letta to connect to it, and deploy agents that persist their memory to Aurora. We also explore how to query the database directly to view agent state.

## Solution overview

Letta runs in a Docker™ container on your local machine and connects to Aurora PostgreSQL over the internet. Aurora stores agent configuration, memory, and conversation history in PostgreSQL tables. The connection uses standard PostgreSQL [wire protocol](https://www.postgresql.org/docs/current/protocol.html) on port 5432.

The following diagram illustrates this architecture.

![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/11/26/DBBLOG-5201-1.png)

### Aurora PostgreSQL

The integration of Aurora PostgreSQL brings several capabilities needed for production-ready AI agent memory systems. Aurora PostgreSQL supports the [pgvector extension](https://github.com/pgvector/pgvector), enabling efficient similarity searches across millions of vector embeddings, which are the numerical representation of past conversations. This allows AI agents to quickly retrieve contextually relevant information.

Aurora PostgreSQL delivers sub-second query latency for memory lookups and supports up to 15 read replicas to scale memory retrieval operations efficiently. This means your AI agents can access their memory rapidly, even under heavy loads. The database’s storage capacity extends up to 256 TB, providing ample space for extensive memory archives and long-term conversation history.

Aurora provides reliability through its comprehensive [durability features](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Reliability.html). The database maintains six-way replication across three Availability Zones, reducing the risk of data loss. Your agents’ memories are further protected by [point-in-time recovery](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-pitr.html) capabilities with up to 35 days of backup retention. The self-healing storage system continuously performs data integrity checks, maintaining the consistency of your agents’ memory states.

For cost optimization, Aurora Serverless automatically scales based on workload, handling thousands of concurrent agent connections. Storage scaling is also dynamic, growing from 10 GiB to 256 TB with no downtime, so your agents don’t run out of memory space as they learn and interact.

### Letta

[Letta treats agents as persistent services](https://docs.letta.com/core-concepts), maintaining state server-side and enabling agents to run independently, communicate with each other, and continue processing when clients are offline. For production workloads, [Letta supports horizontal scaling using Kubernetes](https://docs.letta.com/guides/selfhosting/performance), with configurable worker processes and database connection pooling. The [background execution mode](https://docs.letta.com/guides/agents/long-running) enables resumable streams that survive disconnects and allow load balancing by picking up streams started by other instances.

Production deployments support multi-tenancy with unlimited agents on [Pro and Enterprise plans](https://docs.letta.com/guides/cloud/plans), making Letta suitable for large-scale customer service and multi-user applications. The platform includes [enterprise features](https://docs.letta.com/guides/cloud/rbac) like SAML/OIDC SSO, role-based access control, and tool sandboxing, with [telemetry and performance monitoring](https://docs.letta.com/guides/server/otel) for tracking system metrics. Although this post demonstrates a local setup, production deployments typically use [cloud platforms](https://docs.letta.com/guides/server/remote) with HTTPS access and [security controls](https://docs.letta.com/guides/selfhosting).

### Walkthrough overview

In the following sections, we walk through the steps to build the following resources:

- An Aurora serverless cluster with the [pgvector](https://github.com/pgvector/pgvector) extension for embedding storage
- A security group configuration that allows your IP address to connect on port 5432
- A Letta Docker container configured with `LETTA_PG_URI` pointing to Aurora
- Working AI agents that persist all state to Aurora instead

Our solution uses Aurora Serverless with minimal capacity settings suitable for development and testing environments.

Although we’re using an internet-exposed database for this post for simplicity, the best practice in production is to place it in a private subnet with a security group that only allows connections from your application.

## Prerequisites

Before we begin, make sure you have the following:

- An [AWS account](https://aws.amazon.com/free/) with permissions to create Aurora clusters and modify [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
- [Docker](https://www.docker.com/get-started/) installed on your local machine
- An [OpenAI API key](https://openai.com/) for Letta’s language model integration
- [PostgreSQL client tools](https://www.postgresql.org/download/) installed locally (psql version 12 or higher recommended)
- Python 3.8+ with pip, or Node.js 16+ with npm

## Set up Aurora Serverless

In this section, we demonstrate how to create an Aurora PostgreSQL cluster configured for external access from your local machine.

### Create the Aurora cluster

To create the Aurora cluster, complete the following steps:

1. On the Amazon RDS console, in the navigation pane, choose **Databases**.
2. Choose **Create database**.

![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/11/26/DBBLOG-5201-2.png)
3. For **Engine options**, select **Aurora (PostgreSQL Compatible)**.
4. For **Engine version**, select **Aurora PostgreSQL (Compatible with PostgreSQL 17.4)**.

This is the default for major version 17, or you can choose your preferred version.
5. Under **Templates**, select **Dev/Test** to optimize for lower costs.
6. Under **Settings**, configure the following:
1. For **DB cluster identifier**, enter a name, such as `letta-aurora-cluster`.
2. For **Master username**, keep the default (`postgres`).
3. For **Credentials management**, choose **Self managed**.
4. For **Master password**, enter an alphanumeric password.
7. Under **Instance configuration**, select **Serverless v2**.
8. For **Capacity range**, set the following:
1. **Minimum capacity (ACUs)**: 0.5
2. **Maximum capacity (ACUs)**: 1

[Aurora Capacity Units (ACUs)](https://aws.amazon.com/rds/aurora/pricing/) are the measurement unit for database compute capacity in Aurora Serverless. Each ACU is a combination of approximately 2 GiB of memory, corresponding CPU, and networking capabilities. For example, 0.5 ACUs provides 1 GiB of memory, whereas 32 ACUs provides 64 GiB of memory with proportional compute resources. Your Aurora [database charges](https://aws.amazon.com/rds/aurora/pricing/) are based on the ACU usage per second. For development and testing, starting with 0.5–1 ACU is sufficient. Production workloads typically require higher ACU ranges based on your application’s memory and processing needs. Aurora Serverless automatically adjusts capacity within your specified ACU range based on actual database load. Aurora can scale to a minimum capacity of zero ACUs, which avoids compute charges in periods where your cluster is not being used.
9. Under **Connectivity**, configure the following:
1. For **Public access**, choose **Yes**.
2. For **VPC security group (firewall)**, select **Create new**.
3. For **New VPC security group name**, enter a name, such as `letta-aurora-sg`.
10. Choose **Create database**.

While Aurora creates the cluster, you can proceed to configure the security group.

### Configure security group access

Aurora clusters require security group configuration to allow external connections. By default, the security group blocks all incoming traffic. This solution creates an [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2) (Amazon EC2) security group.

To configure the security group, complete the following steps:

1. On the Amazon EC2 console, in the navigation pane, under **Network & Security**, choose **Security Groups**.
2. On the **Inbound rules** tab, select the security group attached to your Aurora cluster (`letta-aurora-sg`).
3. Choose **Edit inbound rules**.

![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/11/26/DBBLOG-5201-3.png)
4. Choose **Add rule** and configure the following:
1. For **Type**, choose **PostgreSQL**.
2. For **Protocol**, keep at default (TCP).
3. For **Port range**, keep at default (5432).
4. For **Source**, choose one of the following options:
1. **My IP**: Automatically detects and allows your current IP address (recommended for testing).
2. **Custom**: Enter a specific IP address with `/32` suffix for single IP access.
5. Choose **Save rules**.

![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/11/26/DBBLOG-5201-4.png)

Your security configuration now allows PostgreSQL connections from your IP address to the Aurora cluster.

### Retrieve cluster endpoint

After the cluster status shows as **Available**, retrieve the connection endpoint:

1. On the Amazon RDS console, choose **Databases** in the navigation pane.
2. Choose your cluster.

![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/11/26/DBBLOG-5201-5.png)
3. On the **Connectivity & security** tab, go to the **Endpoints** section.
4. Copy the writer instance endpoint. It looks similar to `letta-aurora-cluster.cluster-abc123def456.us-east-1.rds.amazonaws.com`. You will use this endpoint to construct the PostgreSQL connection string.

![](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/11/26/DBBLOG-5201-6.png)

### Install pgvector extension

Letta uses the pgvector extension to store vector embeddings for agent memory. You must manually enable this extension before connecting Letta.

To install pgvector, complete the following steps:

1. Connect to Aurora using the psql command line tool:

```
psql -h letta-aurora-cluster.cluster-abc123def456.us-east-1.rds.amazonaws.com \
-U postgres \
-d postgres
```
2. When prompted, enter the primary password you configured during cluster creation.

After successful connection, you will see the PostgreSQL prompt:

```
postgres=>
```
3. Create the pgvector extension:

```
CREATE EXTENSION vector;
```
4. Verify the installation:

```
SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';
--The output should look like the following (version number might vary):
extname | extversion
---------+------------
vector  | 0.8.0

```
5. Exit psql:

```
\q
```

Your Aurora cluster is now ready for Letta connections.

## Connect Letta to Aurora

With Aurora configured, you can now run Letta and connect it to your cluster using the `LETTA_PG_URI` environment variable. Letta’s Docker image automatically detects the external PostgreSQL connection and runs database migrations on startup.

### Construct connection string

The `LETTA_PG_URI` follows the standard PostgreSQL connection string format:

```
postgresql://USERNAME:PASSWORD@ENDPOINT:PORT/DATABASE
```

Using the values from your Aurora cluster, construct the string as follows:

```
postgresql://postgres:TestPassword2025@letta-aurora-cluster.cluster-abc123def456.us-east-1.rds.amazonaws.com:5432/postgres
```

Replace the endpoint and password with your actual cluster endpoint and password.

### Run Letta with Docker

To start Letta connected to Aurora, run the Docker container with your Aurora connection string and OpenAI API key:

```
docker run -p 8283:8283 \
-e LETTA_PG_URI='postgresql://postgres:YOUR_PASSWORD@YOUR_CLUSTER_ENDPOINT:5432/postgres' \
-e OPENAI_API_KEY='your-openai-api-key' \
letta/letta:latest
```

Provide your Aurora primary password, your cluster endpoint, and your OpenAI key.

Watch for the migration output. You should see the following:

```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 9a505cc7eca9, Create a baseline migrations
```

This confirms Letta detected the PostgreSQL connection and created the necessary database schema.

When you see the following output, the server is ready:

```
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8283
```

Letta is now running and connected to Aurora. Agent data will persist to your Aurora cluster instead of local storage.

### Create and test an agent

To verify the connection works, create an agent and send it a message. Choose either Python or TypeScript based on your preferred language.

#### Using Python

With Python, complete the following steps:

1. In a new terminal, create a Python virtual environment and install the Letta Python client:

```
python -m venv venv
source venv/bin/activate
# On Windows: venv/Scripts/activate
pip install letta-client
```
2. Create a Python script called `test_aurora_agent.py`:

```
from letta_client import Letta

# Connect to Letta server with extended timeout
client = Letta(base_url="http://localhost:8283", timeout=600)

# Create a new agent
agent = client.agents.create(
name="aurora_test_agent",
memory_blocks=[
{
"label": "human",
"value": "Name: Test User"
},
{
"label": "persona",
"value": "I am a helpful AI assistant with persistent memory stored in Aurora."
}
],
model="openai/gpt-4o-mini",
embedding="openai/text-embedding-3-small"
)

print(f"Created agent: {agent.id}")

# Send a message to the agent
response = client.agents.messages.create(
agent_id=agent.id,
messages=[{
"role": "user",
"content": "Hello! Can you remember that my favorite color is blue?"
}]
)

# Extract and display the assistant's response
for message in response.messages:
if message.message_type == "assistant_message":
content = message.content
if isinstance(content, str):
print(f"\nAgent: {content}")
elif isinstance(content, list):
for item in content:
if item.get("type") == "text":
print(f"\nAgent: {item.get('text', '')}")

```
3. Run the script:

```
python test_aurora_agent.py
```

You should see output similar to the following code:

```
Created agent: agent-abc123

Agent: Of course! I've made a note that your favorite color is blue. I'll remember that for our future conversations.
```

#### Using TypeScript

With TypeScript, complete the following steps:

1. Initialize a Node.js project and install dependencies:

```
npm init -y
npm install @letta-ai/letta-client tsx
npm install --save-dev @types/node
```
2. Update your package.json to use ES modules by adding the following:

```
{
"type": "module"
}
```
3. Create a TypeScript script called `test_aurora_agent.ts`:

```
import { Letta } from '@letta-ai/letta-client';

async function main() {
// Connect to Letta server
const client = new Letta({
baseURL: 'http://localhost:8283',
});

// Create an agent
const agent = await client.agents.create({
name: 'aurora_test_agent',
model: 'openai/gpt-4o-mini',
embedding: 'openai/text-embedding-3-small',
memory_blocks: [
{
label: 'persona',
value: 'I am a helpful AI assistant with persistent memory stored in Aurora.',
},
{
label: 'human',
value: 'Name: Test User',
},
],
});

console.log(`Created agent: ${agent.id}`);

// Send a message with extended timeout
const response = await client.agents.messages.create(
agent.id,
{
messages: [
{ role: 'user', content: 'Hello! Can you remember that my favorite color is blue?' }
],
},
{
timeout: 600000, // 10 minutes
}
);

// Extract and print assistant's response
for (const message of response.messages) {
if (message.message_type === 'assistant_message') {
console.log(`\nAgent: ${(message as any).content}`);
}
}
}

main().catch(console.error);

```

You might see validation warnings about `tool_return_message` when running this script. These are internal SDK type validation messages. The warnings don’t affect functionality. To suppress these warnings, `redirect stderr: npx tsx test_aurora_agent.ts 2>/dev/null`.
4. Run the script:

```
npx tsx test_aurora_agent.ts
--Or to suppress validation warnings:
npx tsx test_aurora_agent.ts 2>/dev/null
```

You should see output similar to the following code:

```
Created agent: agent-abc123

Agent: Of course! I've made a note that your favorite color is blue. I'll remember that for our future conversations.
```

The agent response confirms that Letta successfully created an agent and processed your message. This data is now stored in Aurora.

## View agent state in Aurora

Now that you have agents running and storing data in Aurora, you can connect directly to the database to inspect how Letta organizes agent state, memory, and conversations.

### Connect to Aurora

Using the same psql connection from earlier, connect to Aurora:

```
psql -h letta-aurora-cluster.cluster-abc123def456.us-east-1.rds.amazonaws.com \
-U postgres \
-d postgres
```

### Explore the database schema

Letta creates 42 tables to manage agents, memory, messages, and associated metadata. To view all tables, use the following command:

```
\dt
```

You should see output showing tables including agents, messages, organizations, users, block, sources, and other details:

```
List of relations
Schema |             Name              | Type  |  Owner
--------+-------------------------------+-------+----------
public | agents                        	| table | postgres
public | block                         	| table | postgres
public | messages                     | table | postgres
public | organizations              | table | postgres
public | users                         	| table | postgres
...
(42 rows)
```

The key tables for understanding agent state are:

- **agents** – Stores agent configuration and metadata
- **messages** – Contains all conversation messages with full content as JSON
- **organizations and users** – Manages multi-tenant access control
- **block and block\_history** – Stores memory blocks and their revision history
- **sources and source\_passages** – Contains data sources and their embeddings for retrieval

### View agent information

To see all agents in your database, use the following code:

```
SELECT id, name, created_at FROM agents;
--Output example:
id                     |       name        |          created_at
--------------------------------------------+-------------------+-------------------------------
agent-29cdd087-44a7-4dd4-b34e-d38dd5ef2935 | aurora_test_agent | 2025-10-27 06:30:56.078296+00
(1 row)
```

### View agent messages

To see the conversation history for a specific agent, use the `content` column, which stores messages as JSON (the `text` column is empty in current Letta versions):

```
SELECT id, role, content::text, created_at
FROM messages
WHERE agent_id = 'agent-29cdd087-44a7-4dd4-b34e-d38dd5ef2935'
ORDER BY created_at
LIMIT 5;
```

The following is an example of the output:

```
id                      |   role    |                              content                              |          created_at
----------------------------------------------+-----------+-------------------------------------------------------------------+-------------------------------
message-9beba3d8-61e3-4eb9-a0b9-94d5745b9431 | system    | [{"type": "text", "text": "<base_instructions>\nYou are Letta...  | 2025-10-27 06:31:02.505196+00
message-64be4f18-ccaa-461c-af21-502372f9a081 | assistant | [{"type": "text", "text": "Bootup sequence complete. Persona...   | 2025-10-27 06:31:02.515623+00
message-f68f492e-c126-477d-a78a-f015036e07a0 | tool      | [{"type": "text", "text": "{\n  \"status\": \"OK\",\n  \"message\... | 2025-10-27 06:31:02.516277+00
message-b9720ed1-6a1f-4827-ad11-60a7dd62e032 | user      | [{"type": "text", "text": "{\n  \"type\": \"login\",\n  \"last_... | 2025-10-27 06:31:02.516304+00
message-4cc57dc7-1952-4e24-a202-f93dfb23004c | user      | [{"type": "text", "text": "Hello! Can you remember that my...     | 2025-10-27 06:31:45.689208+00
(5 rows)
```

The `messages` table stores the complete conversation flow as JSON, so you can trace exactly how agents process and respond to user input.

### Examine message content structure

Letta stores message content as JSON. To view the detailed structure of an assistant message, use the following code:

```
SELECT content::text
FROM messages
WHERE agent_id = 'agent-29cdd087-44a7-4dd4-b34e-d38dd5ef2935'
AND role = 'assistant'
LIMIT 1;
```

The following is an example of the output:

```
content
--------------------------------------------------------------------------------------------------------------------------------
[{"type": "text", "text": "Bootup sequence complete. Persona activated. Testing messaging functionality.", "signature": null}]
(1 row)
```

This shows the JSON structure of assistant messages. Each message is stored as an array of content objects with type, text, and optional signature fields. System messages contain the full agent instructions including memory blocks, and assistant and user messages contain the conversation content.

### Understanding the schema for embeddings and data sources

Letta uses the pgvector extension to store embedding vectors for semantic memory search and Retrieval Augmented Generation (RAG). The database includes tables specifically designed for vector storage:

```
-- Check archival passages (populated when agents use archival memory)
SELECT COUNT(*) FROM archival_passages;

-- Check source passages (populated when you attach data sources to agents)
SELECT COUNT(*) FROM source_passages;
```

For a newly created agent with basic conversation history, both tables will show 0 records. These tables are populated when you take the following actions:

- Attach documents or files to an agent as data sources
- Use archival memory features for long-term storage
- Implement RAG workflows

The `source_passages` table stores embeddings for external data sources, and `archival_passages` stores embeddings for the agent’s archival memory system. Both use pgvector’s vector data type for efficient similarity search.

## Clean up

When you’ve finished exploring the integration, delete the Aurora cluster and associated resources to avoid ongoing charges.

### Delete the Aurora cluster

To delete your Aurora cluster, complete the following steps:

1. On the Amazon RDS console, in the navigation pane, choose **Databases**.
2. Select your database within the cluster (such as `letta-aurora-cluster-instance-1`).
3. Choose **Actions**, then choose **Delete**.
4. Enter `delete me` in the confirmation field.
5. After the instance is deleted, you can delete the cluster.
6. For **Create final snapshot**, choose **No** (this is a test environment).
7. Enter `delete me`in the confirmation field.
8. Choose **Delete**.

The deletion process takes several minutes.

### Delete the security group

After the cluster is deleted, complete the following steps to delete the security group:

1. On the Amazon EC2 console, in the navigation pane, choose **Security Groups**.
2. Select the security group you created (such as `letta-aurora-sg`).
3. Choose **Actions**, then choose **Delete security groups**.
4. Choose **Delete**.

## Conclusion

In this post, you configured Letta to use Aurora PostgreSQL as a managed database backend. You created an Aurora Serverless cluster, configured security group access, installed the pgvector extension, and connected Letta using the `LETTA_PG_URI` environment variable. You then created AI agents that persist their state to Aurora and queried the database to view agent conversations and memory.

This integration enables production deployments of Letta with the scalability, durability, and high availability that Aurora provides. For production use, consider implementing additional security measures such as [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) [database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html), encryption at rest, and restricting security group access to specific IP ranges or VPC configurations.

To learn more about Letta, refer to the [Letta documentation guides](https://docs.letta.com/). For more information about Aurora PostgreSQL, see [Working with Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html).

---

### About the authors

![Dr. Sarah Wooders](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/11/26/DBBLOG-5201-7.png)

### Dr. Sarah Wooders

[Sarah](https://www.linkedin.com/in/wooders/) is the Co-Founder & CTO of Letta, where she leads engineering and systems strategy to build stateful AI agents that remember, reason, and grow smarter over time. Previously, she earned her PhD in Computer Science at University of California Berkeley, focused on systems for machine learning and cloud data infrastructure. She also holds an undergraduate degree in Computer Science & Mathematics from Massachusetts Institute of Technology. Her prior startup, Glisten.ai (YC W20), harnessed AI for ecommerce product data, and her academic work includes high-impact systems research (such as MemGPT and Skyplane), which underpins Letta’s memory-first platform.

![Steve Dille](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2025/11/26/DBBLOG-5201-8.jpeg)

### Steve Dille

[Steve](https://www.linkedin.com/in/stevedille/) is a Senior Product Manager for Amazon Aurora, where he drives generative AI strategy and product innovation across Amazon Aurora databases and Amazon Bedrock. Since joining AWS in 2020, he has led Aurora performance and benchmarking efforts, and launched the Amazon RDS Data API for Amazon Aurora Serverless, Aurora pgvector 0.8.0, Aurora quick create for Amazon Bedrock Knowledge Bases, and numerous Aurora zero-ETL features. Before AWS, Steve held engineering and product leadership roles at NCR, HP, Morgan Stanley, and Sybase (SAP), and served as VP of Product and CMO at multiple companies, leading to successful public offerings or acquisition. He holds a Master’s in Information and Data Science from UC Berkeley, an MBA from Chicago Booth, and a BS in Computer Science and Mathematics from the University of Pittsburgh.