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

# Unlock new possibilities: AWS Organizations service control policy now supports full IAM language

by Swara Gandhi and Niti Prasad on 19 SEP 2025 in [Announcements](https://aws.amazon.com/blogs/security/category/post-types/announcements/ "View all posts in Announcements"), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [AWS Organizations](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-organizations/ "View all posts in AWS Organizations") [Permalink](https://aws.amazon.com/blogs/security/unlock-new-possibilities-aws-organizations-service-control-policy-now-supports-full-iam-language/)  [Comments](https://aws.amazon.com/blogs/security/unlock-new-possibilities-aws-organizations-service-control-policy-now-supports-full-iam-language/#Comments)  Share

[Amazon Web Service (AWS)](https://aws.amazon.com) recently announced that [AWS Organizations](https://aws.amazon.com/organizations/) now offers full [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) policy language support for service control policies (SCPs). With this feature, you can use conditions, individual resource Amazon Resource Names (ARNs), and the `NotAction` element with `Allow` statements. Additionally, you can now use wildcards at the beginning or middle of the `Action` element strings and implement the `NotResource` element in both `Allow` and `Deny` statements in SCPs. This feature is now available across [AWS commercial and AWS GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-differences.html) Regions.

In this blog post, we walk through a set of newly supported SCP language capabilities that simplify permission management cases. These enhancements enable more intuitive and concise policy designs. We explore how these capabilities address past limitations to reduce operational overhead and improve policy readability. We also show what the previous implementation looked like and provide an example of how the new capability makes the intent clearer and implementation simpler.

## Overview of the newly supported elements

The following table lists the supported SCP language elements along with their purpose and applicable effects. Elements and effects shown in **bold** indicate newly supported capabilities.

|  |  |  |
| --- | --- | --- |
| Element | Purpose | Supported effects |
| [Version](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-version) | Specifies the language syntax rules to use for processing the policy. | `Allow`, `Deny` |
| [Statement](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-statement) | Serves as the container for policy elements. You can have multiple statements in an SCP. | `Allow`, `Deny` |
| [Statement ID (Sid)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-sid) | (Optional) Provides a friendly name for the statement. | `Allow`, `Deny` |
| [Effect](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-effect) | Defines whether the SCP statement [allows](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#allowlist) or [denies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#denylist) access to the IAM users and roles in an account. | `Allow`, `Deny` |
| [Action](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-action) | Specifies the AWS service and actions that the SCP allows or denies. | `Allow`, `Deny` |
| [NotAction](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-action) | Specifies the AWS service and actions that are exempt from the SCP. Used instead of the `Action` element. | `Allow`, `Deny` |
| [Resource](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-resource) | Specifies the AWS resources that the SCP applies to. | `Allow`, `Deny` |
| [NotResource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notresource.html) | Specifies the AWS resources that are exempt from the SCP. Used instead of the `Resource` element. | `Allow`, `Deny` |
| [Condition](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-condition) | Specifies the conditions for when the statement is in effect. | `Allow`, `Deny` |

Additionally, you can now use the wildcard characters \* and ? anywhere in the [Action or NotAction](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html#scp-syntax-action) element. Previously, these wildcards were only allowed by themselves or at the end of an element. For example, all of the following are now valid:

* `"servicename:action*"`
* `"servicename:*action"`
* `"servicename:some*action"`
* `"servicename:*"`

## Navigating new SCP language capabilities

Let’s explore recommended policy strategies and best practices by walking through some examples.

### Using `Deny` with NotResource

You can use the `NotResource` element to apply a policy across resources except those explicitly listed. This is especially useful for implementing broad deny-by-default policies with scoped exceptions, simplifying policy structure while enforcing strong boundaries.

**Example 1:**

The goal of this example is to enforce a resource perimeter that blocks access to resources outside the organization, except for a defined set of [service-owned resources](https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_owned_resources.md).

* **Previous implementation:** The policy used a tag-based approach to manage exceptions. It required tagging IAM principals with `dp:exclude:resource:s3=true` to grant access to external resources. This created operational overhead in tag management and introduced potential security risks if tags were incorrectly applied.
* **Improved implementation:** With support for `NotResource` in `Deny` statements, the updated SCP uses a single, consolidated `Deny` statement denying the action except for a defined set of AWS-owned resources.

|  |  |
| --- | --- |
| **Policy structure before NotResource support** | **Policy structure after NotResource support** |
| ``` {   "Version": "2012-10-17",   "Statement": [     {       "Sid": "EnforceResourcePerimeterAWSResourcesS3",       "Effect": "Deny",       "Action": "s3:GetObject",       "Resource": "*",       "Condition": {         "StringNotEqualsIfExists": {           "aws:ResourceOrgID": "<my-org-id>",           "aws:PrincipalTag/dp:exclude:resource:s3": "true"         }       }     }   ] } ``` | ``` {   "Version": "2012-10-17",   "Statement": [     {       "Sid": "EnforceResourcePerimeterAWSResources",       "Effect": "Deny",       "Action": "s3:GetObject",       "NotResource": [         "arn:aws:s3:::service-owned-bucket/*",         "arn:aws:s3:::service-owned-bucket2/*"       ],       "Condition": {         "StringNotEquals": {           "aws:ResourceOrgID": "<org-id>"         }              }     }   ] } ``` |

**Example 2:**

This example denies access to [Amazon Bedrock](https://aws.amazon.com/bedrock) models except for one specific model.

* **Before this change:** SCP relied on a broad permission baseline for AWS accounts within the organization by allowing access to Amazon Bedrock actions by default, while explicitly denying invocation of three specific models (examples: `Deepseek`, `Anthropic`, and `meta`). However, this approach requires continuous operational overhead to make sure policies are updated to deny access to newly added models to avoid exposure to potentially unwanted models.
* **Improved implementation:** With support for `NotResource` in `Deny` statements, the updated SCP uses a single, consolidated `Deny` statement that denies actions except Amazon models.

|  |  |
| --- | --- |
| **Policy structure before NotResource support** | **Policy structure after NotResource support** |
| ``` { 	"Version": "2012-10-17", 	"Statement": [ 		{ 			"Effect": "Allow", 			"Action": "bedrock:*", 			"Resource": "*" 		}, 		{ 			"Effect": "Deny", 			"Action": [ 				"bedrock:InvokeModel", 				"bedrock:InvokeModelWithResponseStream", 				"bedrock:PutFoundationModelEntitlement" 			], 			"Resource": [ 				"arn:aws:bedrock:*::foundation-model/deepseek.*", 				"arn:aws:bedrock:*::foundation-model/anthropic.*", 				"arn:aws:bedrock:*::foundation-model/meta.*" 			] 		} 	] } ``` | ``` { 	"Version": "2012-10-17", 	"Statement": [ 		{ 			"Effect": "Allow", 			"Action": "bedrock:*", 			"Resource": "*" 		}, 		{ 			"Sid": "Statement1", 			"Effect": "Deny", 			"Action": [ 				"bedrock:InvokeModel", 				"bedrock:InvokeModelWithResponseStream", 				"bedrock:PutFoundationModelEntitlement" 			], 			"NotResource": [ 				"arn:aws:bedrock:*::foundation-model/amazon.*" 			] 		} 	] } ``` |

### Using `Allow` with conditions

By using the `Condition` element, you can specify the circumstances under which a policy statement is in effect. While optional, this element is now supported in `Allow` statements within SCPs, enabling more precise and scalable access control.

**Note:** We recommend using explicit `Deny` statements when authoring SCPs in most cases. Using `Deny` statements help make sure that each control works independently and remains enforceable. Relying solely on allow statements and the implicit deny-by-default model can lead to unintended access, because broader or overlapping `Allow` statements can override more restrictive ones.

The following example allows access to specific AWS services in certain AWS Regions.

* **Before this change:** The policy uses a single `Allow` statement under the Sid: `AllowSpecificServices`. It lists broad service-level actions (for example, `"ec2:"`, `"s3:"`, and so on) in the `Action` element and applies them across resources (`"Resource": "*"`). Because AWS SCPs operate under a deny-by-default model, this setup effectively permits actions across the listed services while implicitly denying access to other services not included. For example, an explicit `Deny` restricts actions outside `us-east-1`, `us-west-2`, and `eu-central-1` using a Region condition.
* **Improved implementation:**In the updated example, the policy allows the same services, but only when they are requested in specific Regions (for example, `"us-east-1"`, `"us-west-2"`, and `"eu-central-1"`). This is achieved using the [aws:RequestedRegion](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requestedregion) condition key in the `Allow` statement. This enhancement allows organizations to retain basic Allow logic while introducing contextual boundaries—such as limiting access by Region, account, or resource tag—previously only possible with `Deny` conditions.

**Note:** We recommend using one broad `Allow` statement and multiple targeted `Deny` statements in your policies. Avoid writing additional `Allow` statements that might overlap, because doing so could lead to unintended access. The recommended approach is to start with a broad `Allow` statement and then use `Deny` statements to refine and restrict access as needed.

|  |  |
| --- | --- |
| **Policy structure before support for Allow with conditions** | **Policy structure after support for Allow with conditions** |
| ``` {    "Version":"2012-10-17",    "Statement":[       {          "Sid":"AllowSpecificServices",          "Effect":"Allow",          "Action":[             "ec2:*",             "s3:*",             "rds:*",             "lambda:*",             "cloudformation:*",             "iam:*",             "cloudwatch:*"          ],          "Resource":"*"       },       {          "Sid":"AllowAccessOnlyTo3Regions",          "Effect":"Deny",          "Action":"*",          "Resource":"*",          "Condition":{             "StringNotEquals":{                "aws:RequestedRegion":[                   "us-east-1",                   "us-west-2",                   "eu-central-1"                ]             }          }       }    ] } ``` | ``` {   "Version": "2012-10-17",   "Statement": [     {       "Sid": "AllowServicesBasedOnRegion",       "Effect": "Allow",       "Action": [         "ec2:*",         "s3:*",         "rds:*",         "lambda:*",         "cloudformation:*",         "iam:*",         "cloudwatch:*"       ],       "Resource": "*",       "Condition": {         "StringEquals": {           "aws:RequestedRegion": [             "us-east-1",             "us-west-2",             "eu-central-1"           ]         }       }     }   ] } ``` |

### Other newly supported elements

To bring SCPs to full IAM policy language support, additional elements are now supported. While technically valid, some of these constructs require additional considerations and testing in practice because of their potential for unintended access if not carefully managed.

|  |  |
| --- | --- |
| **Newly supported feature** | **Important considerations** |
| `Action` with wildcards (`*`, `?`) | Can help shorten policies but use with caution—new actions added by AWS will match existing wildcard patterns as designed, potentially granting unintended permissions. |
| `NotAction` with wildcards (`*`, `?`) | We recommend using `NotAction` with a `Deny` statement if you want to deny all actions *except* those listed, which helps future-proof your controls (for example, denying everything in Amazon EC2 except actions that don’t match `“*vpn*”`. |
| `Allow` with `NotResource` | Limited use cases. While supported, `Allow` with `NotResource` can default to including all resources—potentially allowing access to new resources added later. Use with caution and prefer explicit `Deny` statements when possible. |
| `Allow` with `NotAction` | Limited use cases. While supported, `Allow` with `NotAction` can unintentionally permit access to new actions added by AWS. Use with caution and prefer explicit `Deny` statements to maintain control as services evolve. |
| `Allow` with `Resource` other than wildcard `“*”`. | When using Allow with specific resources (not `"*"`), make sure your policy design avoids conflicting or overlapping `Allow` statements. Start with a broad `Allow`, then use targeted `Deny` statements to restrict access—this helps prevent unintended access from overlapping `Allow` statements. |

## Validate your policies with IAM Access Analyzer

You can use [AWS IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer) to validate your SCPs before applying them, using both policy validation and custom policy checks.

IAM Access Analyzer [validates your policy against IAM policy grammar and best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html). You can view policy validation check findings that include security warnings, errors, general warnings, and suggestions. These findings provide actionable recommendations to help you author policies that are both functional and aligned with security best practices.

[Custom policy checks](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-custom-policy-checks.html) are an IAM Access Analyzer capability that security teams can use to help them accurately and proactively identify critical permissions in their policies. Custom policy checks can determine whether a new version of a policy is more permissive than the previous version. They use automated reasoning—a form of static analysis—to provide a higher level of security assurance in the cloud.

Custom policy checks can be embedded into continuous integration and continuous delivery (CI/CD) pipelines, so that policies can be checked without being deployed. Developers can also run custom policy checks from their local development environments and receive fast feedback on whether the policies they are authoring comply with your organization’s security standards. For more information refer to [introducing IAM Access Analyzer custom policy checks](https://aws.amazon.com/blogs/security/introducing-iam-access-analyzer-custom-policy-checks/).

## Conclusion

The latest enhancements to AWS service control policies improve policy expressiveness and precision while reducing operational effort. By enabling constructs like `Allow` with conditions and specific resource ARNs, supporting `NotResource` in `Deny` statements, and expanding wildcard flexibility, you can simplify your policies and avoid layered or complex policies to achieve your goals. These updates bring SCPs in parity with IAM policy capabilities and empower organizations to implement cleaner, more intuitive access controls. As a best practice, it’s important to use these capabilities carefully—especially wildcard use—to avoid unintended permissions as AWS services evolve. We also encourage the implementation of explicit `Deny` statements as a best practice and using `Allow` statements when needed.

---

If you have feedback about this post, submit comments in the Comments section below. If you have questions about this post, [contact AWS Support](https://console.aws.amazon.com/support/home).

![Swara Gandhi](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/09/12/swaragandhi.ganswara.jpg)

### Swara Gandhi

Swara is a Senior Solutions Architect on the AWS Identity Solutions team. She works on building secure and scalable end-to-end identity solutions. She is passionate about everything identity, security, and cloud.

![Niti Prasad](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/09/12/nitiprasad.awsniti.jpg)

### Niti Prasad

Niti is a Senior Security Solutions Architect supporting Strategic Accounts. She supports customers as they look to secure and govern their AWS environment. Her enthusiasm for security drives her to continuously explore innovative ways to help customers protect their cloud workloads.

TAGS: [AWS IAM](https://aws.amazon.com/blogs/security/tag/aws-iam/), [AWS Organizations](https://aws.amazon.com/blogs/security/tag/aws-organizations/), [Policies](https://aws.amazon.com/blogs/security/tag/policies/)

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