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

# Introducing attribute-based access control for Amazon S3 general purpose buckets

by Matheus Guimaraes on 20 NOV 2025 in [Amazon Simple Storage Service (S3)](https://aws.amazon.com/blogs/aws/category/storage/amazon-simple-storage-services-s3/ "View all posts in Amazon Simple Storage Service (S3)"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance"), [Storage](https://aws.amazon.com/blogs/aws/category/storage/ "View all posts in Storage") [Permalink](https://aws.amazon.com/blogs/aws/introducing-attribute-based-access-control-for-amazon-s3-general-purpose-buckets/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-attribute-based-access-control-for-amazon-s3-general-purpose-buckets/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

As organizations scale, managing access permissions for storage resources becomes increasingly complex and time-consuming. As new team members join, existing staff changes roles, and new S3 buckets are created, organizations must constantly update multiple types of access policies to govern access across their S3 buckets. This challenge is especially pronounced in multi-tenant S3 environments where administrators must frequently update these policies to control access across shared datasets and numerous users.

Today we’re introducing [attribute-based access control (ABAC)](https://aws.amazon.com/identity/attribute-based-access-control/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) for [Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) general purpose buckets, a new capability you can use to automatically manage permissions for users and roles by controlling data access through tags on S3 general purpose buckets. Instead of managing permissions individually, you can use tag-based IAM or bucket policies to automatically grant or deny access based on tags between users, roles, and S3 general purpose buckets. Tag-based authorization makes it easy to grant S3 access based on project, team, cost center, data classification, or other bucket attributes instead of bucket names, dramatically simplifying permissions management for large organizations.

**How ABAC works** Here’s a common scenario: as an administrator, I want to give developers access to all S3 buckets meant to be used in development environments.

With ABAC, I can tag my development environment S3 buckets with a key-value pair such as `environment:development` and then attach an ABAC policy to an [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) principal that checks for the same `environment:development` tag. If the bucket tag matches the condition in the policy, the principal is granted access.

Let’s see how this works.

**Getting started**

First, I need to explicitly enable ABAC on each S3 general purpose bucket where I want to use tag-based authorization.

I navigate to the [Amazon S3 console](https://console.aws.amazon.com/s3?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el), select my general purpose bucket then navigate to **Properties** where I can find the option to enable ABAC for this bucket.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/19/image-21-3.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/19/image-21-3.png)

I can also use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) to enable it programmatically by using the new PutBucketAbac API. Here I am enabling ABAC on a bucket called my-demo-development-bucket located in the US East (Ohio) us-east-2 [AWS Region](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el).

```
aws s3api put-bucket-abac --bucket my-demo-development-bucket abac-status Status=Enabled --region us-east-2
```

Alternatively, if you use [AWS CloudFormation](https://aws.amazon.com/cloudformation/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el), you can enable ABAC by setting the `AbacStatus` property to `Enabled` in your template.

Next, let’s tag our S3 general purpose bucket. I add an `environment:development` tag which will become the criteria for my tag-based authorization.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/19/adding-user-defined-tags.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/19/adding-user-defined-tags.png)

Now that my S3 bucket is tagged, I’ll create an ABAC policy that verifies matching `environment:development` tags and attach it to an IAM role called dev-env-role. By managing developer access to this role, I can control permissions to all development environment buckets in a [single place](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html).

I navigate to the [IAM console](https://console.aws.amazon.com/iam?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el), choose **Policies**, and then **Create policy.**In the **Policy editor**, I switch to JSON view and create a policy that allows users to read, write and list S3 objects, but only when they have a tag with a key of “environment” attached and its value matches the one declared on the S3 bucket. I give this policy the name of s3-abac-policy and save it.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/environment": "development"
                }
            }
        }
    ]
}
```

I then attach this s3-abac-policy to the dev-env-role.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/15/adding-abac-policy-to-iam-role.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/15/adding-abac-policy-to-iam-role.png)

That’s it! Now a user assuming the dev-role can access any ABAC-enabled bucket with the tag environment:development such as my-demo-development-bucket.

**Using your existing tags**

Keep in mind that although you can use your existing tags for ABAC, because these tags will now be used for access control, we recommend reviewing your current tag setup before enabling the feature. This includes reviewing your existing bucket tags and tag-based policies to prevent unintended access, and updating your tagging workflows to use the standard TagResource API (since enabling ABAC on your buckets will block the use of the PutBucketTagging API). You can use [AWS Config](https://aws.amazon.com/config/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) to check which buckets have ABAC enabled and review your usage of PutBucketTagging API in your application using [AWS Cloudtrail](https://aws.amazon.com/cloudtrail/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) management events.

Additionally, the same tags you use for ABAC can also serve as cost allocation tags for your S3 buckets. Activate them as cost allocation tags in the [AWS Billing Console](https://aws.amazon.com/aws-cost-management/aws-billing/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) or through APIs, and your [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) and [Cost and Usage Reports](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) will automatically organize spending data based on these tags.

**Enforcing tags on creation**

To help standardize access control across your organization, you can now enforce tagging requirements when buckets are created through service control policies (SCPs) or IAM policies using the `aws:TagKeys` and `aws:RequestTag` condition keys. Then you can enable ABAC on these buckets to provide consistent access control patterns across your organization. To tag a bucket during creation you can add the tags to your CloudFormation templates or provide them in the request body of your call to the existing S3 CreateBucket API. For example, I could enforce a policy for my developers to create buckets with the tag environment=development so all my buckets are tagged accurately for cost allocation. If I want to use the same tags for access control, I can then enable ABAC for these buckets.

**Things to know**

With ABAC for Amazon S3, you can now implement scalable, tag-based access control across your S3 buckets. This feature makes writing access control policies simpler, and reduces the need for policy updates as principals and resources come and go. This helps you reduce administrative overhead while maintaining strong security governance as you scale.

Attribute-based access control for Amazon S3 general purpose buckets is available now through the [AWS Management Console](https://console.aws.amazon.com/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el), API, [AWS SDKs](https://builder.aws.com/build/tools?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el), AWS CLI, and AWS CloudFormation at no additional cost. Standard API request rates apply according to [Amazon S3 pricing](https://aws.amazon.com/s3/pricing?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el). There’s no additional charge for tag storage on S3 resources.

You can use [AWS CloudTrail](https://aws.amazon.com/cloudtrail/?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) to audit access requests and understand which policies granted or denied access to your resources.

You can also use ABAC with other S3 resources such as S3 directory bucket, S3 access points and S3 tables buckets and tables. To learn more about ABAC on S3 buckets see the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html).

You can use the same tags you use for access control for cost allocation as well. You can activate them as cost allocation tags through the AWS Billing Console or APIs. Check out the documentation for more details on [how to use cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el).

![Matheus Guimaraes](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/16/me_standing_outdoor-square-2.jpg)

### Matheus Guimaraes

Matheus Guimaraes (@codingmatheus) is a digital transformation specialist focused on AI adoption and microservices architecture. An international keynote speaker with over 20 years in tech, he’s worn many hats: from junior game programmer to CTO and tech co-founder. Matheus has helped companies of all sizes modernize and scale their systems, leading transformation programs and designing cloud-native, AI-ready architectures. Today, he shares his expertise globally through talks, blogs, and videos, passionate about helping others grow in the industry. Outside his professional life, he’s a gamer, swimmer, musician, and firm believer in the powerful intersection of creativity and technology.

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