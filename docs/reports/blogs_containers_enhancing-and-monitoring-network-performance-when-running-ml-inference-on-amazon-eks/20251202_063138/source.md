# Enhancing and monitoring network performance when running ML Inference on Amazon EKS

by Chiedu Eluehike and Frank Fan on 26 NOV 2025 in Amazon Elastic Kubernetes Service, Amazon Machine Learning, Technical How-to Permalink  Share

[Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/) has become a popular choice for customers looking to run their workloads in the Amazon Web Services (AWS) Cloud with customers increasingly choosing to run their AI and Machine Learning (AI/ML) workloads on Amazon EKS. Customers can use Amazon EKS to customize configuration to match their workload requirements. Furthermore, Platform teams can use it to transfer their existing container orchestration model and expertise when deploying new workloads and standardize on Amazon EKS. Kubernetes also provides access to a rich environment of popular open source AI/ML frameworks, tools, and inference engines such as Ray, vLLM, Triton, PyTorch. Lastly, they can use Kubernetes’ tested capability to auto-scale, deploy and manage containerized workloads at scale, and implement the [full cluster automation](https://aws.amazon.com/eks/auto-mode/) capabilities of EKS.

Some use cases of AI/ML workloads deployed on Amazon EKS include generative AI Model training for Large Language Models (LLMs), real-time and batch ML inference, and Retrieval Augmented Generation (RAG) Pipelines. ML inference is the process where a trained model generates predictions on a user’s input prompt or query. Inference has become an important part of modern applications and powers applications such as content generation, intelligent assistants, recommendation engines.

Over the years AWS has released a suite of resources and artifacts to accelerate and streamline customers’ usage of Amazon EKS as their service of choice for running AI/ML workloads. These include [AI on EKS](https://awslabs.github.io/ai-on-eks/), [Best Practices for Running AI/ML workloads](https://docs.aws.amazon.com/eks/latest/best-practices/aiml.html), [Amazon EKS-optimized accelerated AMIs for GPU Instances](https://docs.aws.amazon.com/eks/latest/userguide/ml-eks-optimized-ami.html), and [AWS Deep Learning Containers](https://github.com/aws/deep-learning-containers).

Recently AWS announced [Container Network Observability in Amazon EKS](https://aws.amazon.com/blogs/aws/monitor-network-performance-and-traffic-across-your-eks-clusters-with-container-network-observability), a set of Amazon EKS network observability features that customers can use to observe, visualize, and enhance their Amazon EKS network environment. In this post we explore the feature sets, deep dive into how it works, and explore an ML inference workload scenario where we use it to monitor and enhance its network performance.

## Current challenges with network observability for ML inference workloads

ML inference workloads need efficient access to model artifacts such as Model Weights, model configuration files, and tokenizers (for LLMs). The Model Weights, which are the learned parameters from the model training process, are responsible for converting the user’s prompt into predicted output. They are typically the largest artifact, often being many GBs in size and needing to be loaded into the [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instance’s GPU memory at runtime. Therefore, the pattern of coupling—either choosing to embed the weights and other model artifacts in the container image or keep it separate in an AWS storage service—and the choice of storage solution are very important decisions to consider when reducing image pull time, pod, and application start-up time. Likewise, this is important in reducing inference latency, which users care about because it determines how long they wait for their response. We recommend not embedding the artifacts in container images and instead storing them in the appropriate AWS storage service for the workload requirement. Amazon EKS supports various Container Storage Interface (CSI) drivers to reduce the management overhead of pod volume mount. For more information on storage design and considerations for optimizing ML inference latency, refer to our guidance in the Amazon EKS Best Practices and this [Amazon EKS container start up time guidance](https://awslabs.github.io/ai-on-eks/docs/guidance/container-startup-time).

ML platform teams encounter situations where they need to troubleshoot network connectivity issues related to their workload affecting inference. For example, a pod might fail to respond to requests and they must quickly determine if this is an application issue, network issue, or something else. It gets more complex when the ML inference workloads depend on cluster external AWS services such as [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/). Furthermore, the view into the AWS network path is important, and users might have issues with high inference latency, in which case the team would want to quickly identify the bottleneck to optimize. Moreover, they might also get users encountering issues with intermittent timeouts or disconnects. Therefore, the platform teams need to have an end-to-end view of the path from client request to inference pod to cluster external dependencies and back that is Kubernetes-enriched. Today teams with their choice of observability stack or AWS network monitoring feature often struggle with this. Container Network Observability in Amazon EKS addresses this, where network optimization and troubleshooting becomes data driven. This leads to improvements in system metrics such as Mean Time to Detect (MTTD), Mean Time to Recover (MTTR), and [inference metrics](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-observability.html) such as Time to First Token (TTFT), end-to-end latency, and output tokens per second.

## Deep-dive into Container Network Observability in Amazon EKS

Container Network Observability in Amazon EKS is enabled by [Amazon CloudWatch Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html). It operates a Network Flow Monitor agent running as a DaemonSet on all worker nodes in the Amazon EKS Cluster and is installed using the Amazon EKS Network Flow Monitor Agent add-on. When it is running, it collects network observability metrics from all pods and worker nodes and exposes them in the Open Metrics Format for scrapping by your platform team’s observability stack. Therefore, they can continue to use their existing stack, and it provides a visualization from the Amazon EKS console through the **Network** tab of your cluster’s Observability Dashboard and the CloudWatch Network Monitoring Flow Monitor Console.

Container Network Observability in Amazon EKS has three features:

- Service map: You can use this to visualize communication between pods and services in your ML inference workload.
- Flow table: This provides detailed flow level metrics across your ML inference workload, segmenting the data by views. An important one for ML inference workloads is the “AWS service view,” which provides information on pod traffic to AWS services (such as Amazon S3 and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)). Some of the metrics include TCP Retransmissions and Data Transferred.
- Performance metrics: This feature allows pod and worker nodes’ system metrics to be scraped and observed from your observability stack. Some of the metrics include Ingress and Egress Flow, and Bandwidth In and Out Allowance Exceeded. For a full list, refer to the Amazon [EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html).

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-1.png)

*Figure 1: Architecture of Container Network Flow Monitor Agent and integration with observability stacks*

## ML inference workload scenario

To demonstrate how to use the Container Network Observability feature in Amazon EKS, we deploy a sample ML inference workload running on Amazon EKS and use the feature to enhance and monitor network performance across a range of use cases.

The ML inference workload is Image Generation using the popular [Stable Diffusion](https://aws.amazon.com/what-is/stable-diffusion/) (SD) model that generates photorealistic images from text and image prompts. The workload is deployed using the [Guidance for Asynchronous Image Generation with Stable Diffusion on AWS](https://aws.amazon.com/solutions/guidance/asynchronous-image-generation-with-stable-diffusion-on-aws/) from the [AWS Solutions Library](https://aws.amazon.com/solutions/), as shown in the following figure.

When a user submits an image generation prompt, the request arrives at an [Amazon API Gateway](https://aws.amazon.com/api-gateway/) frontend, which forwards it to an [AWS Lambda](https://aws.amazon.com/lambda/) function for validation. The Lambda function publishes validated requests to an [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) topic, which subsequently delivers them to an [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) queue. [Kubernetes Event Driven Auto-Scaler (KEDA)](https://keda.sh/) launches new pods in response to the SQS queue to process the prompt request. [Karpenter](https://karpenter.sh/), an open source node lifecycle management project, provisions GPU EC2 instances such as g5 and p4 to schedule the pods. The pods run an SD Runtime container image, and when they reach the Running state they load the SDXL-Turbo Model Weights (stored in safetensor format) from an S3 bucket using the [Mountpoint for Amazon S3 CSI Driver](https://github.com/awslabs/mountpoint-s3-csi-driver). The generated images are stored in another S3 bucket.

This architecture uses the pattern discussed previously of decoupling storing the Model Weights from the container image. This leads to faster pod and application start time, more efficient memory usage, and scaling of the ML workload.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-2.png)

*Figure 2: Image generation with SD on AWS Solution Reference architecture*

### Setting up

The following prerequisites are needed to get started:

- An AWS account with access to EC2 G5 instances. Request a [quota increase](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) if needed.
- [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), to deploy and manage AWS resources.
- [kubectl](https://kubernetes.io/docs/tasks/tools/), to access and deploy Kubernetes Resources.
- [eksctl,](https://eksctl.io/installation/) to access the EKS cluster.
- Your development environment or setup.

#### Step 1: Clone the solutions GitHub repository

```
git clone https://github.com/aws-solutions-library-samples/guidance-for-asynchronous-inference-with-stable-diffusion-on-aws.git
```

#### Step 2: Deploy the solution

```
cd guidance-for-asynchronous-inference-with-stable-diffusion-on-aws/deploy

# Install prerequisite tools
./install-tools.sh

# Deploy the Solution
./deploy.sh
```

This takes about 1 hour to complete, the solution uses AWS Cloud Development Kit (AWS [CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html)) to deploy the necessary AWS services and all resources. You can monitor its creation in the console and through [AWS CloudFormation](https://aws.amazon.com/cloudformation/).

```
# Once ready confirm that all the components have been deployed in the cluster
kubectl get all -A
```

#### Step 3: Enable Container Network Observability on the EKS cluster

To enable Container Network Observability on the EKS cluster, navigate to the EKS cluster and choose **Monitor cluster**, as shown in the following figure. This takes you to the Observability Dashboard of the cluster, where you choose **Network**. Choose **Edit container network observability,** choose **Enable network monitoring**, and choose a Pod Identity [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) role that the Network Flow Monitor Agent uses when installed on the cluster. Then, choose **Save changes**.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-3.png)

*Figure 3: Amazon EKS console showing Container Network Observability*

Confirm that the Network Flow Monitor Agent is installed by checking the installed add-ons in the Amazon EKS console, or by running the following command.

```
# check if network flow monitor agent is running
kubectl get pods -l name=aws-network-flow-monitor-agent

NAME                                   READY   STATUS    RESTARTS   AGE
aws-network-flow-monitor-agent-b67jr   1/1     Running   0          22h
aws-network-flow-monitor-agent-dfjdc   1/1     Running   0          22h
```

#### Step 4: Configure observability stack to collect and visualize metrics

MLOps and platform teams often standardize on an observability stack to track metrics and to alert if they’re breaching defined thresholds. In this scenario we use [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) to ingest the metrics and [Amazon Managed Grafana](https://aws.amazon.com/grafana/) to visualize them in a dashboard. We’d deploy an [Amazon Managed Service for Prometheus managed collector](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html) to scrape the metrics exposed by the Network Flow Monitor Agent on its port 9101 and on path /metrics.

To create an Amazon Managed Service for Prometheus workspace for the EKS cluster, follow the steps in the [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-create-workspace.html) and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/getting-started-with-AMG.html#AMG-getting-started-workspace-create) documentation.

Create an Amazon Managed Service for Prometheus workspace:

```
export AWS_REGION=us-east-1 #Replace this with your AWS Region

aws amp create-workspace sdoneks-amp-workspace --region ${AWS_REGION}
```

This [Containers post](https://aws.amazon.com/blogs/containers/monitoring-network-performance-on-amazon-eks-using-aws-managed-open-source-services/) also goes into the details of setting it up for Container Network Observability.

When the workspaces are created, configure a scraper to scrape the metrics from the Network Flow Monitor Agent. We use [Amazon Managed Service for Prometheus Managed Collector](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html). To do this, navigate to the **Observability** section of the EKS cluster, and under **Scrapers** choose **Add,** as shown in the following figure.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-4.png)

*Figure 4: Amazon EKS console showing Amazon Managed Service for Prometheus Managed collector*

Choose the existing workspace and choose the Amazon Managed Service for Prometheus workspace that you configured previously. Under the Scraper configuration, append the following scraper job to the end. This is the job that scrapes Network Flow Monitor metrics from the Agent and forwards them to Amazon Managed Service for Prometheus.

```
- job_name: 'eks-nfm-sdoneks'
kubernetes_sd_configs:
- role: pod
metrics_path: /metrics
relabel_configs:
- source_labels:
- __meta_kubernetes_namespace
- __meta_kubernetes_pod_label_name
action: keep
regex: amazon-network-flow-monitor;aws-network-flow-monitor-agent
- target_label: __address__
replacement: ${1}:9101
source_labels:
- __meta_kubernetes_pod_ip
```

#### Step 5: Deploy user and generate image

```
cd test/
./run.sh

# Below is an example of the output and the S3 bucket location the image is stored in

API Endpoint is https://1abcde2f3g.execute-api.us-east-1.amazonaws.com/dev/
Generating test text-to-image request...
{"id": "test-t2i", "runtime": "sdruntime", "output_location": "s3://sdoneksstack-outputs3bucket123456789abcd/output/test-t2i"}
Generating test image-to-image request...
{"id": "test-i2i", "runtime": "sdruntime", "output_location": "s3://sdoneksstack-outputs3bucket123456789abcd/output/test-i2i"}
Generating image upscaling request...
{"id": "test-extra", "runtime": "sdruntime", "output_location": "s3://sdoneksstack-outputs3bucket123456789abcd/output/test-extra"}

# Confirm that the pods have launched

kc get pods -n sdruntime
NAME                                                 READY   STATUS    RESTARTS   AGE
sdruntime-sd-on-eks-inference-api-6468cbcc64-dznvd   3/3     Running   0          125m

# Confirm that the pods have launched on GPU-Backed instances

kubectl get pod sdruntime-sd-on-eks-inference-api-6468cbcc64-dznvd -n sdruntime -o custom-columns=POD:.metadata.name,NODE:.spec.nodeName --no-headers | whileread pod node; do echo "Pod: $pod | Node: $node | Instance Type: $(kubectl get node $node -o jsonpath='{.metadata.labels.node\.kubernetes\.io/instance-type}')"; done
Pod: sdruntime-sd-on-eks-inference-api-6468cbcc64-dznvd | Node: ip-10-0-159-241.ec2.internal | Instance Type: g5.2xlarge
```

Create a UI deployment and SD Runtime service. You can use these to send traffic from the UI to the SD Runtime Deployment and visualize it.

```
cat << 'EOF' > ui-deployment.yaml
apiVersion: v1
kind: Namespace
metadata:
name: ui
---
apiVersion: apps/v1
kind: Deployment
metadata:
name: client-ui
namespace: ui
labels:
app.kubernetes.io/type: app
spec:
replicas: 3
selector:
matchLabels:
app.kubernetes.io/name: ui
template:
metadata:
labels:
app.kubernetes.io/name: ui
spec:
containers:
- name: ui
image: amazonlinux:latest
command: ["/bin/bash"]
args: ["-c", "while true; do sleep 30; done;"]
resources:
requests:
memory: "64Mi"
cpu: "250m"
---
apiVersion: v1
kind: Service
metadata:
name: sdruntime-service
namespace: sdruntime
labels:
app: inference-api
app.kubernetes.io/name: sd-on-eks
app.kubernetes.io/instance: sdruntime
spec:
selector:
app: inference-api
app.kubernetes.io/name: sd-on-eks
app.kubernetes.io/instance: sdruntime
ports:
- name: inference-api
protocol: TCP
port: 8080
targetPort: 8080
type: ClusterIP

EOF

kubectl apply -f ui-deployment.yaml
```

Generate an image of a dog or your choice of image by sending the following image generation prompt:

```
export POD_1=$(kubectl -n ui get pods -o jsonpath='{.items[0].metadata.name}')

kubectl exec --stdin $POD_1 -n ui -- curl -vko /dev/null -X POST http://sdruntime-service.sdruntime.svc.cluster.local:8080/sdapi/v1/txt2img -H "Content-Type: application/json"   -d '{
"task": {
"metadata": {
"id": "test-t2i",
"runtime": "sdruntime",
"tasktype": "text-to-image",
"prefix": "output",
"context": ""
},
"content": {
"alwayson_scripts": {},
"prompt": "A dog",
"steps": 16,
"width": 512,
"height": 512
}
}
}'

# Repeat above prompt from the other 2 pods and then Confirm the Stable Diffusion Image Generation Process

kubectl logs sdruntime-sd-on-eks-inference-api-6468cbcc64-dznvd -n sdruntime --tail=100 -f

API 2025-11-23 05:48:48.933274 200 http/1.1 POST /sdapi/v1/txt2img 10.0.135.71 6.8513
INFO:     10.0.135.71:57196 - "POST /sdapi/v1/txt2img HTTP/1.1" 200 OK
2025-11-23 05:48:49 INFO [modules.shared_state] Starting job scripts_txt2img
Warning: field infotext in API payload not found in <modules.processing.StableDiffusionProcessingTxt2Img object at 0x7f4dd87e8340>.

Total progress:   0%|          | 0/16 [00:00<?, ?it/s]
Total progress:  12%|█▎        | 2/16 [00:00<00:00, 15.41it/s]
................
Total progress:  94%|█████████▍| 15/16 [00:01<00:00,  7.62it/s]
100%|██████████| 16/16 [00:02<00:00,  7.61it/s]
Total progress: 100%|██████████| 16/16 [00:01<00:00,  7.61it/s]
2025-11-23 05:48:52 INFO [modules.shared_state] Ending job scripts_txt2img (2.35 seconds)

# To view how long it took the SD Runtime pod to load the SD XL Turbo Model Weights from the S3 bucket through its S3 CSI Driver

kc logs sdruntime-sd-on-eks-inference-api-6468cbcc64-bmq27 -n sdruntime | grep loaded
Defaulted container "inference-api" out of: inference-api, queue-agent, xray-daemon
Model loaded in 33.7s (load weights from disk: 27.1s, create model: 0.5s, apply weights to model: 5.1s, apply half(): 0.1s, calculate empty prompt: 0.5s).
```

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-5.png)

*Figure 5: Image of a dog generated from the SD Runtime Pod (stored in the S3 bucket output)*

## Container Network Observability use cases for ML inference workload

This section walks through the container network observability use cases for ML inference workload.

### Visualize and confirm intercommunication between services for troubleshooting

Using the Service Map feature we visualize the intercommunication between the pod and services in our workload. This is a quick way to view and understand the workload and confirm whether or not services are communicating with each other. In the following figure we can observe and confirm that the UI and SD Runtime Deployments are communicating. This is a quick and visual way to rule out issues such as security misconfiguration (NetworkPolicy, Security Groups, Network Access Control Lists).

We can also filter for the namespaces we’re interested in to streamline the view.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-6.png)

*Figure 6: Container Network Observability console in Amazon EKS showing Service map view*

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-7.png)

*Figure 7: Container Network Observability console in Amazon EKS showing Pod view*

### Analyze Availability Zone (AZ) traffic pattern between deployments

Using the Flow table feature and CloudWatch Network Monitoring Flow Monitor we can analyze the AZ traffic pattern for inter-AZ and intra-AZ traffic. This is useful if we’re optimizing for a very low latency ML inference and decide that pods communicating between services should only communicate intra-AZ.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-8.png)

*Figure 8: Container Network Observability console in Amazon EKS showing Flow table view*

In Kubernetes you can use a feature such as [Topology Aware Routing](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/) to implement this, and confirm it is working using Container Network Observability. In our example we observe that UI Pods are communicating with the SD Runtime pods inter-AZ (az4 ↔ az6).

### Network Health Indicator

We can investigate if an AWS Network Issue has occurred using [Network Health Indicator (NHI)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html), as shown in the following figure. The Network Flow Monitor generates an NHI value of 0 (signifying healthy) or 1 (signifying an AWS network issue). This is important when troubleshooting ML inference for high latency. You want to quickly confirm if there was an AWS Network issue or not and then focus your investigation.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-9.png)

*Figure 9: CloudWatch Network Monitoring Flow Monitor console showing NHI healthy*

### Investigating ML inference Latency using performance metrics in Amazon Manged Grafana

We can use performance metrics to identify ML inference optimization opportunities. The key metrics include the following:

- TTFT
- End-to-end latency
- Output tokens per second (throughput)

Common root causes of increased ML inference latency include the following:

- Pod and application startup time
- Model loading duration

To visualize the performance metrics collected by our Network Flow Monitor Agent in Amazon Managed Grafana, we can use this already built [dashboard](https://raw.githubusercontent.com/aws-observability/aws-observability-accelerator/refs/heads/main/artifacts/grafana-dashboards/eks/network/nperf-dashboard.json) that provides detailed network monitoring. Import it by going to your Amazon Managed Grafana Workspace URL. Then, navigate to **Dashboard**, choose **New**, choose **Import,** and upload the JSON copied.

Next, generate lots of image generation requests.

```
# command to generate Image Generation requests to the SD Runtime deployment every 2 seconds

while true; do sleep 2; ./run.sh; done

# confirm that multiple pods have been launched
kc get pods -n sdruntime -w
NAME READY STATUS RESTARTS AGE
sdruntime-sd-on-eks-inference-api-6468cbcc64-bgvr9 3/3 Running 0 2m41s
sdruntime-sd-on-eks-inference-api-6468cbcc64-bmq27 3/3 Running 0 3m57s
sdruntime-sd-on-eks-inference-api-6468cbcc64-mhthj 3/3 Running 0 42m
sdruntime-sd-on-eks-inference-api-6468cbcc64-ztrdd 3/3 Running 0 3m26s

```

We notice something when isolating the Metrics for Ingress Bytes and Bandwidth In Allowance Exceeded (a metric that represents packets that are queued or dropped due to inbound bandwidth limit). At the time when the pod is launched, running, and beginning to download the SDXL-Turbo Model Weights from the S3 buckets, there are noticeable events of the underlying g5.2xlarge EC2 instance getting its packets queued or dropped. g5.2xlarge has a Network Bandwidth of up to [10 Gbps](https://aws.amazon.com/ec2/instance-types/g5/), and this is being breached. We also correlate this in our CloudWatch Network Monitoring Flow Monitor were we observe at the same time a large spike in Retransmissions, which occurs when receipt of a data segment isn’t confirmed by the receiver. In this case the pod isn’t confirming receipt of data segments of the Model Weights sent by Amazon S3 because the maximum bandwidth of the underlying g5.2xlarge instance was breached. Therefore, Amazon S3 is re-transmitting that segment until the pod acknowledges. This can contribute to ML inference time and poor user experience.

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-10.png)

*Figure 10: Amazon Managed Grafana dashboard showing performance metrics*

In this case, choosing to use an instance type with a larger maximum bandwidth (for example g5.4xlarge has a Network Bandwidth up to 25 Gbps) would be appropriate, or you could use other [optimization techniques](https://awslabs.github.io/ai-on-eks/docs/guidance/container-startup-time/reduce-container-image-size/decoupling-model-artifacts).

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-11.png)

*Figure 11: CloudWatch Network Monitoring Flow Monitor console showing Retransmissions spike*

## Cleaning up

After concluding, delete and clean up all resources deployed. This prevents you incurring other costs. To delete the solution, navigate to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home), choose the **sdoneks** Stack, and choose **Delete.**

Furthermore, navigate to your Amazon Managed Service for Prometheus and Amazon Managed Grafana console to delete the workspaces. Finally navigate to Amazon S3 and delete the two S3 buckets for Model Storage and for Image Output Storage.

## Conclusion

This post explored the importance of Container Network Observability for ML inference workloads, emphasizing the critical need for low inference latency. We examined the networking challenges that teams encounter when optimizing and troubleshooting these workloads. The newly launched Container Network Observability in Amazon EKS offers a solution through the Service Map, Flow Table, and Performance Metrics features. These capabilities provide Kubernetes-enriched data for both internal cluster traffic and communications with external AWS services. Furthermore, platform teams have the flexibility to integrate these insights with their existing observability stack.

We used a sample image generation ML inference workload to explore various network enhancement and troubleshooting use cases addressed by the feature.

For more information on this feature, please check out the following resources:

[Container Network Observability in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html)

[Container Network Observability in Amazon EKS Launch Blog](https://aws.amazon.com/blogs/aws/monitor-network-performance-and-traffic-across-your-eks-clusters-with-container-network-observability/)

[Amazon CloudWatch Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html)

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-12.png) **Chiedu Eluehike** is a Senior Solutions Architect at AWS based in Sydney, Australia. In his role he works with Large Enterprise customers and helps them translate business problems to technology solutions using the Cloud. He specializes in Application Modernization using container technologies and the intersection with Networking. Outside of work he enjoys playing soccer and basketball, reading books, and spending time with friends and family. He is CCIE #48238 (Emeritus).

![](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2025/11/26/CONTAINERS-132-13.png)**Frank Fan** is a Sr. Container Solutions Architect at AWS Australia. As a passionate advocate for application modernization, Frank specializes in containerization and overseeing large-scale migration and modernization initiatives. Frank is a frequent speaker at prominent tech events including AWS re:Invent, AWS Summit, and Kubernetes Community Day. You can get in touch with Frank through his [LinkedIn page](https://www.linkedin.com/in/frankfan7/), and his presentations are available on his [YouTube channel](https://www.youtube.com/@gettocloud5719).