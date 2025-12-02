# Deploy CrowdStrike Falcon Next-Gen SIEM for AWS through AWS Marketplace

by Jenn Reed and Kunjal Botadra on 01 DEC 2025 in Amazon EventBridge, Amazon GuardDuty, Amazon Simple Storage Service (S3), Announcements, Architecture, AWS CloudTrail, AWS Identity and Access Management (IAM), AWS Key Management Service, AWS Marketplace, AWS re:Invent, AWS Security Hub, Configuration, compliance, and auditing, Security, Technical How-to Permalink  Comments   Share

[CrowdStrike Falcon for AWS](https://aws.amazon.com/marketplace/pp/prodview-vubjuepxztndi) in [AWS Marketplace](https://aws.amazon.com/marketplace/) is a pay-as-you-go offering AWS customers can use to help protect their cloud workloads using the CrowdStrike Falcon platform and only pay for what they use. The Falcon platform on [Amazon Web Services (AWS)](https://aws.amazon.com/) is a unified security platform for enterprise-grade security solutions at scale. This offering includes security information event management (SIEM) and cloud security modules, CrowdStrike Falcon Next-Gen SIEM and CrowdStrike Falcon Cloud Security. Falcon Next-Gen SIEM includes a new automation experience that simplifies the onboarding of the complex configurations of [AWS Organizations](https://aws.amazon.com/organizations/) to provide visibility and security monitoring, analysis, detection, and response all within one platform. It does this by using [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) cross-account read-only asset discovery roles using [AWS CloudFormation](https://aws.amazon.com/cloudformation/). In addition to IAM, AWS Marketplace deploys the Falcon Next-Gen SIEM connectors for [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), [Amazon GuardDuty](https://aws.amazon.com/guardduty/) and [AWS Security Hub](https://aws.amazon.com/security-hub/).

In this post, we show you how to use the automation experience in AWS Marketplace to deploy Falcon Next-Gen SIEM for AWS across all AWS Accounts in your AWS Organization. We then demonstrate how to connect AWS CloudTrail, AWS Security Hub, and Amazon GuardDuty.

## Solution overview

CrowdStrike and AWS have created an enhanced version of [SaaS Quick Launch](https://aws.amazon.com/about-aws/whats-new/2023/11/saas-quick-launch-aws-marketplace/) for Falcon Next-Gen SIEM in AWS Marketplace, delivering a streamlined deployment experience so customers can quickly deploy and access [Falcon Next-Gen SIEM for AWS](https://www.crowdstrike.com/en-us/platform/next-gen-siem/) in minutes.

### CrowdStrike Falcon Next-Gen SIEM for AWS architecture

Falcon Next-Gen SIEM is a security software-as-a-service (SaaS) hosted on AWS. It uses AWS services running in a customer’s AWS accounts to deploy customer data connectors using [Amazon EventBridge](https://aws.amazon.com/eventbridge/), [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/), and [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) to send AWS event and security data to Falcon Next-Gen SIEM. The customer’s Falcon Next-Gen SIEM infrastructure is fully managed by CrowdStrike using IAM using cross-account roles and AWS CloudFormation.

The following diagram shows the solution architecture.

![CrowdStrike Next-Gen SIEM Architecture Diagram](https://d2908q01vomqb2.cloudfront.net/761f22b2c1593d0bb87e0b606f990ba4974706de/2025/11/23/CrowdStrikeMarketplaceArch20251028.png)

*Figure 1: CrowdStrike Falcon Next-Gen SIEM for AWS architecture*

## Solution walkthrough: Deploy CrowdStrike Next-Gen SIEM for AWS through AWS Marketplace

In the following steps, we show you how to subscribe to CrowdStrike Falcon for AWS in AWS Marketplace. We then use the new launch experience to deploy Falcon Next-Gen SIEM. The solution follows a two-step process:

1. Start your CrowdStrike Falcon for AWS subscription
2. Deploy CrowdStrike Falcon Next-Gen SIEM for AWS

### **Start your CrowdStrike Falcon for AWS subscription**

Follow these steps to subscribe to CrowdStrike Falcon for AWS in AWS Marketplace:

1. In your AWS management account, open the [CrowdStrike Falcon for AWS](https://aws.amazon.com/marketplace/pp/prodview-vubjuepxztndi) product detail page and choose **View purchase options**.
2. Choose **Subscribe**.
3. Your subscription might take a couple minutes to process. In the meantime, to begin the deployment integration process, click **Set up your account** (Figure 2).
4. If you receive a dialog box to Enable AWS Marketplace deployment integration, choose **Enable and continue**.

![Set up Your Account](https://d2908q01vomqb2.cloudfront.net/761f22b2c1593d0bb87e0b606f990ba4974706de/2025/11/23/SetupYourAccount-scaled.jpg)

*Figure 2:* *Set up your account redirect*

### **Deploy CrowdStrike Falcon Next-Gen SIEM for AWS**

You will be taken to the new streamlined experience that will guide you through CrowdStrike authentication, Falcon Next-Gen SIEM for AWS configuration, and launch. Follow these steps:

1. You will be redirected to the CrowdStrike account registration page. Follow the on-screen prompts to register with CrowdStrike. This can take 15 minutes for activation. Wait until you receive the account activation email before you proceed to the next step. .
2. Return to AWS Marketplace and notice the success message indicating that your CrowdStrike account has been linked, as shown in the following screenshot. Choose **Next**.

![CrowdStrike Account Linking Successful](https://d2908q01vomqb2.cloudfront.net/761f22b2c1593d0bb87e0b606f990ba4974706de/2025/11/23/CrowdStrikeAccountLinkinSuccess-scaled.jpg)

*Figure 3: Cr**owdStrike account linking confirmation message*

3. In the **Configure deployment R****and access role** section, keep the default parameters. Choose **Next**.
4. In the **Configure AWS CloudTrail i** section, it will have selected the location where your organizational AWS CloudTrail for management events is configured. Keep the default parameters. Choose **Next**.
5. In the **Configure AWS Security Hub integration** section, it will have selected the AWS account and home Region where either AWS Security Hub [cloud security posture management (CSPM)](https://aws.amazon.com/what-is/cspm/) or AWS Security Hub is configured. It will then create an Amazon EventBridge rule to send AWS Security Hub events to the CrowdStrike Amazon EventBridge event-bus for Falcon Next-Gen SIEM. Keep the default. Choose **Next**.
6. In the **Configure Amazon GuardDuty** **integration** section, it will have selected the AWS account and Regions where Amazon GuardDuty is configured. It will then create an Amazon EventBridge rule to send Amazon GuardDuty events to the CrowdStrike Amazon EventBridge event-bus for Falcon Next-Gen SIEM. Keep the default parameters. Choose **Next**.
7. In the **Review and launch** section, choose **Deploy resources**. During the next few minutes, the application integration and identity resources necessary to deploy Falcon Next-Gen SIEM, will be installed across all AWS accounts in your AWS Organization. Follow the on-screen prompts to access your new Falcon Next-Gen SIEM quick start connectors page, as shown in the following screenshot.

![CrowdStrike Falcon Next-Gen SIEM quick start connectors page](https://d2908q01vomqb2.cloudfront.net/761f22b2c1593d0bb87e0b606f990ba4974706de/2025/11/23/2a-Quickstart-AWS-CloudTrail.png)

*Figure 4: CrowdStrike Falcon Next-Gen SIEM quick start connectors page*

## **Conclusion**

In this post, we demonstrated how to subscribe to and use CrowdStrike Next-Gen SIEM for AWS available in AWS Marketplace. For more information, visit [CrowdStrike Falcon for AWS](http://go.crowdstrike.com/crowdstrike-and-aws/).

## **About Authors**

![Jenn Reed](https://d2908q01vomqb2.cloudfront.net/761f22b2c1593d0bb87e0b606f990ba4974706de/2025/11/21/Jenn.png)

### Jenn Reed

Jenn Reed is a Global Principal Security Solutions Architect at AWS with over 25 years of deep experience working in cyber security and software development. She is based out of Ann Arbor MI. At AWS, she is focused on helping customers build securely with AWS.

![Kunjal Botadra ](https://d2908q01vomqb2.cloudfront.net/761f22b2c1593d0bb87e0b606f990ba4974706de/2025/11/21/kb.jpg)

### Kunjal Botadra

Kunjal Botadra is a Senior Product Manager at Amazon Web Services (AWS), focusing on software delivery and procurement solutions. He drives the strategy and roadmap for enterprise software deployment. Previously at Akamai Technologies, Kunjal developed web performance optimization products and services. He specializes in customer-centric product development and building high-performing cross-functional teams.