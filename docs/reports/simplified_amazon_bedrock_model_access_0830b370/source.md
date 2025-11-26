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

## [AWS Security Blog](https://aws.amazon.com/blogs/security/)

# Simplified model access in Amazon Bedrock

by Vadim Omeltchenko and Kyle Dickinson on 15 OCT 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/security/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/security/simplified-amazon-bedrock-model-access/)  [Comments](https://aws.amazon.com/blogs/security/simplified-amazon-bedrock-model-access/#Comments)  Share

> **October 22, 2025:** This post was updated to reflect additional IAM permissions necessary for Amazon Bedrock serverless models offered through AWS Marketplace.

---

[Amazon Bedrock](https://aws.amazon.com/bedrock) has simplified how you access foundation models, streamlining the integration of AI capabilities into your applications. Here’s what’s changed and how to maintain control over model access in your organization.

## What’s new: Simplified model access

Amazon Bedrock now provides automatic access to the serverless models in your AWS Region, eliminating the previous requirement for manual enablement of each individual model. This change brings Amazon Bedrock in line with other AWS services by relying on standard AWS access controls rather than requiring customers to enable each model through a model access dashboard. This simplification effort has retired the Model Access page along with the `PutFoundationModelEntitlement` [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) permission and its corresponding API call. IAM statements with the `PutFoundationModelEntitlement` permission no longer have an effect.

The change delivers immediate benefits for developers and organizations. You can now access models through the AWS Management Console for Amazon Bedrock, AWS SDK, or Amazon Bedrock API without additional setup steps, dramatically accelerating your development timeline. Previously enabled models continue to work exactly as before, so that there are no disruptions to existing applications. Most importantly, any models currently blocked through IAM policies or service control policies (SCPs) remain restricted, preserving your existing security posture. You can review model [end user license agreements (EULAs) any time](https://aws.amazon.com/legal/bedrock/third-party-models/). EULAs can also be accessed on the model card in the [Model Catalog](https://console.aws.amazon.com/bedrock/).

## Maintaining control: IAM and SCP options

IAM policies provide account-level control over foundation model access. You can use these policies to permit or deny `Invoke*` actions for specific foundation models within individual AWS accounts.

SCPs offer organizational-level governance for [AWS Organizations](https://aws.amazon.com/organizations) users. You can use SCPs to implement model restrictions across multiple accounts in your organization simultaneously, providing consistent governance policies regardless of how your teams are structured. Similar to IAM policies, SCP policies can block entire families of models through pattern matching, providing centralized governance that scales with your organizational structure.

SCP and IAM policies work together seamlessly, and you can use them to establish broad organizational controls while giving individual accounts access that they can use to implement more specific restrictions based on their particular use cases and requirements.

## Implementation examples and best practices

You can use IAM policies to implement granular permissions, giving your builders access to a single, specific model. The following example demonstrates how to explicitly allow only the Amazon Nova Lite model.

```
{

  “Version”: “2012-10-17”,
  “Statement”: [
    {
      “Sid”: "AllowAmazonNovaLiteModelOnly",
      “Effect”: “Allow”,
      “Action”: [
        “bedrock:InvokeModel”,
        “bedrock:InvokeModelWithResponseStream”,
      ],
    “Resource”:
	"arn:aws:bedrock:*::inference-profile/us.amazon.nova-lite-v1:0",
	"arn:aws:bedrock:*::foundation-model/amazon.nova-lite-v1:0"
	]
   }
  ]
}
```

You can also implement comprehensive control strategies using wildcard patterns. By using an asterisk (`*`) for the model ID in your policies, you can enable access to a broader set of foundation models by default and then create separate deny policies for select models that aren’t approved in your organization.

The following is an IAM policy example using `NotResource` that denies the models except [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/) models.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BroadBedrockAllow",
      "Effect": "Allow",
      "Action": "bedrock:*",
      "Resource": "*"
    },
    {
      "Sid": "DenyInferenceExceptApprovedModels",
      "Effect": "Deny",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
     ],
     "NotResource": [
        "arn:aws:bedrock:*::foundation-model/amazon.nova-*",
     ]
   }
  ]
}
```

When you deny InvokeModel access in your policies, actions such as Converse will not work either. This is because [Converse relies on Invoke](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html).

While IAM supports a high level of precision, it’s not always used in larger organizations, which might use SCP policies instead. SCPs can be attached to entire organizations or organizational units (OUs) and used to simplify permissions management at scale. Organizations that use SCPs can restrict families of models on organization or OU levels. The following is an example of SCP policy that blocks specific models (or model families) across an entire organization.

```
{
  “Version”: “2012-10-17”,
  “Statement”: [
    {
      “Sid”: “DenyDeepseekEverywhere”,
      “Effect”: “Deny”,
      “Action”: “bedrock:*”,
      “Resource”:
        “arn:aws:bedrock:*::foundation-model/deepseek.*”
      }
    ]
}
```

This approach requires ongoing maintenance; explicitly specifying blocked models isn’t practical because you would have to maintain the policy to include new models as they become available. By using the recently introduced NotResource property for SCP policies, a more elegant solution is to block all models except allowed ones. The following example shows how it’s done:

```
{
  “Version”: “2012-10-17”,
   “Statement”: [
  {
    “Sid”: “Statement1”,
    “Effect”: “Deny”,
    “Action”: “bedrock:*”,
      “NotResource”: [
        “arn:aws:bedrock:*::foundation-model/amazon.nova*”
     ]
    }
  ]
}
```

## Considerations for Anthropic models

While you can start using serverless foundation models from most providers instantly, Anthropic models, although enabled by default, still require you to submit a one-time usage form before first use. You can complete this form through either the Amazon Bedrock playground (in AWS Bedrock console) or through direct API submission using [PutUserCaseForModelAccess API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutUseCaseForModelAccess.html).

Customers using AWS Organizations can complete the first-time usage form at the organization management account level using API. Its approval automatically extends to the child accounts within your organization (but only if done via the API). This streamlined process reduces the need for individual form submissions across multiple accounts.

## Considerations for Amazon Bedrock serverless models offered via AWS Marketplace

A subset of serverless models on Amazon Bedrock are offered through AWS Marketplace and therefore require a subscription before use. This subscription gets created automatically at an account level on the first invocation as shown the following diagram.

![Figure 1: Subscriptions are created automatically at an account level on the first invocation.](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/22/Image2-1.png)

Figure 1: Subscriptions are created automatically at an account level on the first invocation.

[These marketplace models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-product-ids.html) have product IDs associated with them which can be used in an IAM conditional statement for access control.

The following is a sample IAM policy which permits invocation of Anthropic Sonnet 3.7, Sonnet 4 and Haiku 4.5 3P models with “just-in-time” subscription automatically created on the 1st call:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAnthropicAndAmazonModelsOnly",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": [
                "arn:aws:bedrock:*::inference-profile/us.anthropic.claude-haiku-4-5-20251001-v1:0",
                "arn:aws:bedrock:*::foundation-model/anthropic.claude-haiku-4-5-20251001-v1:0",
                "arn:aws:bedrock:*::inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0",
                "arn:aws:bedrock:*::foundation-model/anthropic.claude-3-7-sonnet-20250219-v1:0",
                "arn:aws:bedrock:*::inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0",
                "arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-20250514-v1:0"
            ]
        },
        {
            "Sid": "AllowOnlySpecificMarketplaceSubscription",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:ViewSubscriptions",
                "aws-marketplace:Subscribe"
            ],
            "Resource": "*",
            "Condition": {
                "ForAllValues:StringEquals": {
                    "aws-marketplace:ProductId": [
                        "prod-4pmewlybdftbs",
                        "prod-xdkflymybwmvi",
                        "prod-4dlfvry4v5hbi"
                    ]
                },
                "StringEquals": {
                    "aws:CalledViaLast": "bedrock.amazonaws.com"
                }
            }
        }
    ]
}
```

If your organization relies exclusively on SCPs to allow and deny models, consider using the [AmazonBedrockLimitedAccess policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockLimitedAccess.html), which is managed by AWS and has all the permissions required for making calls to all Amazon Bedrock models, including the ones offered through the AWS Marketplace.

## An alternative to the “subscribe-on-first-call” approach

In scenarios where adding the Subscribe permission to every user’s IAM policy is not desirable, AWS Marketplace models can be enabled by a designated administrator or authorized persona with the necessary aws-marketplace privileges.

The designated user can enable the models through the AWS Management Console, the Invoke API call, or by making ListFoundationModelAgreementOffers and subsequent CreateFoundationModelAgreement APIs calls.

Once enabled, all users in the account can invoke the models without requiring aws-marketplace permissions. These steps must be repeated whenever new AWS Marketplace models are introduced.

## Moving forward

The simplified model access in Amazon Bedrock represents a significant improvement in developer experience while helping to preserve the security and governance controls that organizations require. Your existing configurations continue to function seamlessly, and you can immediately begin accessing new models while maintaining your organization’s security controls. If you previously relied on the Model Access page to govern access to foundation models in your organization, you should switch to using SCP and IAM policies instead.

These changes position Amazon Bedrock as a more accessible service for AI integration while making sure that enterprise governance requirements remain supported. Whether you’re a developer looking to quickly prototype with new models or an organization managing AI usage across hundreds of accounts, these improvements help deliver tangible benefits without compromising security or governance requirements.

### Resources:

* [Identity-based policy examples for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html)
* [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
* [Implementing least privilege access for Amazon Bedrock](https://aws.amazon.com/blogs/security/implementing-least-privilege-access-for-amazon-bedrock/)
* [AWS Organizations service control policy now support full IAM language](https://aws.amazon.com/blogs/security/unlock-new-possibilities-aws-organizations-service-control-policy-now-supports-full-iam-language/)

If you have feedback about this post, submit comments in the Comments section below. If you have questions about this post, [contact AWS Support](https://console.aws.amazon.com/support/home).

---

![Vadim Omeltchenko](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/15/Vadim-Omeltchenko-Author.png)

### Vadim Omeltchenko

Vadim is a Sr. AI/ML Solutions Architect who is passionate about helping AWS customers innovate in the cloud. His prior IT experience was predominantly on the ground.

![Kyle Dickinson](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/15/Kyle-Dickinson-Author2.jpg)

### Kyle Dickinson

Kyle was once a Gibson explorer turned cloud security expert; as a Sr. Security Solution Architect at AWS, he now protects the systems he once explored. When not safeguarding AWS customers, Kyle is building LEGO creations or attempting to improve his longboarding skills without major injury. His home life revolves around a tiny dog with massive confidence and his spirited 4-year-old daughter, who keeps him laughing.

Loading comments…

### Resources

* [AWS Cloud Security](https://aws.amazon.com/security?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
* [AWS Compliance](https://aws.amazon.com/compliance?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-resources)
* [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html?secd_ip5)
* [Best Practices](https://aws.amazon.com/architecture/security-identity-compliance)
* [Data Protection at AWS](https://aws.amazon.com/compliance/data-protection/)
* [Zero Trust on AWS](https://aws.amazon.com/security/zero-trust/)
* [Cryptographic Computing](https://aws.amazon.com/security/cryptographic-computing/)

---

### Follow

* [Twitter](https://twitter.com/AWSsecurityinfo)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=security-social)

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