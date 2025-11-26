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

# Accelerate safe software releases with new built-in blue/green deployments in Amazon ECS

by [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso") on 17 JUL 2025 in [Amazon Elastic Container Service](https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/ "View all posts in Amazon Elastic Container Service"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Summit New York](https://aws.amazon.com/blogs/aws/category/events/aws-summit-new-york/ "View all posts in AWS Summit New York"), [Compute](https://aws.amazon.com/blogs/aws/category/compute/ "View all posts in Compute"), [Containers](https://aws.amazon.com/blogs/aws/category/containers/ "View all posts in Containers"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/accelerate-safe-software-releases-with-new-built-in-blue-green-deployments-in-amazon-ecs/)  [Comments](https://aws.amazon.com/blogs/aws/accelerate-safe-software-releases-with-new-built-in-blue-green-deployments-in-amazon-ecs/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

While containers have revolutionized how development teams package and deploy applications, these teams have had to carefully monitor releases and build custom tooling to mitigate deployment risks, which slows down shipping velocity. At scale, development teams spend valuable cycles building and maintaining undifferentiated deployment tools instead of innovating for their business.

Starting today, you can use the built-in blue/green deployment capability in [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) to make your application deployments safer and more consistent. This new capability eliminates the need to build custom deployment tooling while giving you the confidence to ship software updates more frequently with rollback capability.

Here’s how you can enable the built-in blue/green deployment capability in the [Amazon ECS](https://console.aws.amazon.com/ecs/v2?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) console.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/29/2025-news-ecsbg-0.png)

You create a new “green” application environment while your existing “blue” environment continues to serve live traffic. After monitoring and testing the green environment thoroughly, you route the live traffic from blue to green. With this capability, Amazon ECS now provides built-in functionality that makes containerized application deployments safer and more reliable.

Below is a diagram illustrating how blue/green deployment works by shifting application traffic from the blue environment to the green environment. You can learn more at the [Amazon ECS blue/green service deployments workflow](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) page.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/10/2025-news-ecsbg-rev-1.png)

Amazon ECS orchestrates this entire workflow while providing event hooks to validate new versions using synthetic traffic before routing production traffic. You can validate new software versions in production environments before exposing them to end users and roll back near-instantaneously if issues arise. Because this functionality is built directly into Amazon ECS, you can add these safeguards by simply updating your configuration without building any custom tooling.

**Getting started**Let me walk you through a demonstration that showcases how to configure and use blue/green deployments for an ECS service. Before that, there are a few setup steps that I need to complete, including configuring [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles, which you can find on the [Required resources for Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-implementation.html?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) Documentation page.

For this demonstration, I want to deploy a new version of my application using the blue/green strategy to minimize risk. First, I need to configure my ECS service to use blue/green deployments. I can do this through the ECS console, [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI), or using infrastructure as code.

Using the Amazon ECS console, I create a new service and configure it as usual:

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/29/2025-news-ecsbg-1.png)

In the Deployment Options section, I choose **ECS** as the **Deployment controller type**, then **Blue/green** as the **Deployment strategy**. **Bake time** is the time after the production traffic has shifted to green, when instant rollback to blue is available. When the bake time expires, blue tasks are removed.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/29/2025-news-ecsbg-2.png)

We’re also introducing deployment lifecycle hooks. These are event-driven mechanisms you can use to augment the deployment workflow. I can select which [AWS Lambda](https://aws.amazon.com/pm/lambda/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) function I’d like to use as a deployment lifecycle hook. The Lambda function can perform the required business logic, but it must return a hook status.

Amazon ECS supports the following lifecycle hooks during blue/green deployments. You can learn more about each stage on the [Deployment lifecycle stages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-how-it-works.html#blue-green-deployment-stages?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) page.

* Pre scale up
* Post scale up
* Production traffic shift
* Test traffic shift
* Post production traffic shift
* Post test traffic shift

For my application, I want to test when the test traffic shift is complete and the green service handles all of the test traffic. Since there’s no end-user traffic, a rollback at this stage will have no impact on users. This makes **Post test traffic shift** suitable for my use case as I can test it first with my Lambda function.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/10/2025-news-ecsbg-rev-2.png)

Switching context for a moment, let’s focus on the Lambda function that I use to validate the deployment before allowing it to proceed. In my Lambda function as a deployment lifecycle hook, I can perform any business logic, such as synthetic testing, calling another API, or querying metrics.

Within the Lambda function, I must return a `hookStatus`. A `hookStatus` can be `SUCCEEDED`, which will move the process to the next step. If the status is `FAILED`, it rolls back to the blue deployment. If it’s `IN_PROGRESS`, then Amazon ECS retries the Lambda function in 30 seconds.

In the following example, I set up my validation with a Lambda function that performs file upload as part of a test suite for my application.

```
import json
import urllib3
import logging
import base64
import os

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Initialize HTTP client
http = urllib3.PoolManager()

def lambda_handler(event, context):
    """
    Validation hook that tests the green environment with file upload
    """
    logger.info(f"Event: {json.dumps(event)}")
    logger.info(f"Context: {context}")

    try:
        # In a real scenario, you would construct the test endpoint URL
        test_endpoint = os.getenv("APP_URL")

        # Create a test file for upload
        test_file_content = "This is a test file for deployment validation"
        test_file_data = test_file_content.encode('utf-8')

        # Prepare multipart form data for file upload
        fields = {
            'file': ('test.txt', test_file_data, 'text/plain'),
            'description': 'Deployment validation test file'
        }

        # Send POST request with file upload to /process endpoint
        response = http.request(
            'POST',
            test_endpoint,
            fields=fields,
            timeout=30
        )

        logger.info(f"POST /process response status: {response.status}")

        # Check if response has OK status code (200-299 range)
        if 200 <= response.status < 300:
            logger.info("File upload test passed - received OK status code")
            return {
                "hookStatus": "SUCCEEDED"
            }
        else:
            logger.error(f"File upload test failed - status code: {response.status}")
            return {
                "hookStatus": "FAILED"
            }

    except Exception as error:
        logger.error(f"File upload test failed: {str(error)}")
        return {
            "hookStatus": "FAILED"
        }
```

When the deployment reaches the lifecycle stage that is associated with the hook, Amazon ECS automatically invokes my Lambda function with deployment context. My validation function can run comprehensive tests against the green revision—checking application health, running integration tests, or validating performance metrics. The function then signals back to ECS whether to proceed or abort the deployment.

As I chose the blue/green deployment strategy, I also need to configure the load balancers and/or Amazon ECS Service Connect. In the **Load balancing** section, I select my **Application Load Balancer**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/29/2025-news-ecsbg-4.png)

In the **Listener** section, I use an existing listener on port 80 and select two **Target groups**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/29/2025-news-ecsbg-5.png)

Happy with this configuration, I create the service and wait for ECS to provision my new service.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/29/2025-news-ecsbg-6.png)

**Testing blue/green deployments**Now, it’s time to test my blue/green deployments. For this test, Amazon ECS will trigger my Lambda function after the test traffic shift is completed. My Lambda function will return `FAILED` in this case as it performs file upload to my application, but my application doesn’t have this capability.

I update my service and check **Force new deployment**, knowing the blue/green deployment capability will roll back if it detects a failure. I select this option because I haven’t modified the task definition but still need to trigger a new deployment.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/10/2025-news-ecsbg-rev-3.png)

At this stage, I have both blue and green environments running, with the green revision handling all the test traffic. Meanwhile, based on [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) Logs of my Lambda function, I also see that the deployment lifecycle hooks work as expected and emit the following payload:

```
[INFO]	2025-07-10T13:15:39.018Z	67d9b03e-12da-4fab-920d-9887d264308e	Event:
{
    "executionDetails": {
        "testTrafficWeights": {},
        "productionTrafficWeights": {},
        "serviceArn": "arn:aws:ecs:us-west-2:123:service/EcsBlueGreenCluster/nginxBGservice",
        "targetServiceRevisionArn": "arn:aws:ecs:us-west-2:123:service-revision/EcsBlueGreenCluster/nginxBGservice/9386398427419951854"
    },
    "executionId": "a635edb5-a66b-4f44-bf3f-fcee4b3641a5",
    "lifecycleStage": "POST_TEST_TRAFFIC_SHIFT",
    "resourceArn": "arn:aws:ecs:us-west-2:123:service-deployment/EcsBlueGreenCluster/nginxBGservice/TFX5sH9q9XDboDTOv0rIt"
}
```

As expected, my AWS Lambda function returns `FAILED` as `hookStatus` because it failed to perform the test.

```
[ERROR]	2025-07-10T13:18:43.392Z	67d9b03e-12da-4fab-920d-9887d264308e	File upload test failed: HTTPConnectionPool(host='xyz.us-west-2.elb.amazonaws.com', port=80): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.HTTPConnection object at 0x7f8036273a80>, 'Connection to xyz.us-west-2.elb.amazonaws.com timed out. (connect timeout=30)'))
```

Because the validation wasn’t completed successfully, Amazon ECS tries to roll back to the blue version, which is the previous working deployment version. I can monitor this process through ECS events in the **Events** section, which provides detailed visibility into the deployment progress.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/10/2025-news-ecsbg-rev-5.png)

Amazon ECS successfully rolls back the deployment to the previous working version. The rollback happens near-instantaneously because the blue revision remains running and ready to receive production traffic. There is no end-user impact during this process, as production traffic never shifted to the new application version—ECS simply rolled back test traffic to the original stable version. This eliminates the typical deployment downtime associated with traditional rolling deployments.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/10/2025-news-ecsbg-rev-7.png)

I can also see the rollback status in the **Last deployment** section.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/07/10/2025-news-ecsbg-rev-8.png)

Throughout my testing, I observed that the blue/green deployment strategy provides consistent and predictable behavior. Furthermore, the deployment lifecycle hooks provide more flexibility to control the behavior of the deployment. Each service revision maintains immutable configuration including task definition, load balancer settings, and Service Connect configuration. This means that rollbacks restore exactly the same environment that was previously running.

**Additional things to know**Here are a couple of things to note:

* **Pricing** – The blue/green deployment capability is included with Amazon ECS at no additional charge. You pay only for the compute resources used during the deployment process.
* **Availability** – This capability is available in all commercial AWS Regions.

Get started with blue/green deployments by updating your Amazon ECS service configuration in the [Amazon ECS console](https://console.aws.amazon.com/ecs/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el).

Happy deploying!

— [Donnie](https://www.linkedin.com/in/donnieprakoso)

![Donnie Prakoso](https://d2908q01vomqb2.cloudfront.net/667be543b02294b7624119adc3a725473df39885/2023/05/30/donnie_profile_400x400.jpeg)

### [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso")

Donnie Prakoso is a software engineer, self-proclaimed barista, and Principal Developer Advocate at AWS. With more than 17 years of experience in the technology industry, from telecommunications, banking to startups. He is now focusing on helping the developers to understand varieties of technology to transform their ideas into execution. He loves coffee and any discussion of any topics from microservices to AI / ML.

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