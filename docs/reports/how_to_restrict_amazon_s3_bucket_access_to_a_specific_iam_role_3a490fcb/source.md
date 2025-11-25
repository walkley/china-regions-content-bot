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

# How to restrict Amazon S3 bucket access to a specific IAM role

by Chris Craig, Laura Verghote, and Ashwin Phadke on 14 FEB 2025 in [Amazon Simple Storage Service (S3)](https://aws.amazon.com/blogs/security/category/storage/amazon-simple-storage-services-s3/ "View all posts in Amazon Simple Storage Service (S3)"), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [How-To](https://aws.amazon.com/blogs/security/category/how-to/ "View all posts in How-To"), [Identity](https://aws.amazon.com/blogs/security/category/security-identity-compliance/identity/ "View all posts in Identity"), [Top Posts](https://aws.amazon.com/blogs/security/category/top-posts/ "View all posts in Top Posts") [Permalink](https://aws.amazon.com/blogs/security/how-to-restrict-amazon-s3-bucket-access-to-a-specific-iam-role/)  [Comments](https://aws.amazon.com/blogs/security/how-to-restrict-amazon-s3-bucket-access-to-a-specific-iam-role/#Comments)  Share

> **February 14, 2025:** This post was updated with the recommendation to restrict S3 bucket access to an IAM role by using the `aws:PrincipalArn` condition key instead of the `aws:userid` condition key.

> **April 2, 2021**: In the section “Granting cross-account bucket access to a specific IAM role,” we updated the second policy to fix an error.

> **July 11, 2016**: This post was first published.

---

Customers often ask how to limit access to an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket to only a specific [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) user or role. A popular approach has been to use the `Principal` element to list the users or roles who need access to the bucket. However, the `Principal` element needs the exact values of the `user` ARN, `role` ARN, or `assumed-role` ARN. It does not support using a wildcard (\*) to include all role sessions, nor does it allow you to use policy variables.

In this blog post, we show how to restrict S3 bucket access to a specific IAM role or user within an account by using the `Conditions` element. Even if another user in the same account has an `Admin` policy or a policy with `s3:*`, they will be denied access if they are not explicitly listed in the `Conditions` element. You can use this approach, for example, to limit access to a bucket with sensitive content or additional security requirements.

## Solution overview

The solution in this post uses a bucket policy to restrict access to an S3 bucket, even if an entity has access to the full API of S3 through an attached identity-based policy. The following diagram illustrates how this works for accessing an S3 bucket within the same account as your IAM user or IAM role. We recommend that you use IAM roles, and only use IAM users for use cases that aren’t supported by federated users.

![Figure 1: Diagram illustrating how to access an S3 bucket within the same account as your IAM user or IAM role](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/02/13/img1.png)

Figure 1: Diagram illustrating how to access an S3 bucket within the same account as your IAM user or IAM role

The workflow in Figure 1 is as follows:

1. The IAM user’s policy and the IAM role’s identity-based policy grant access to `“s3:*”`.
2. The S3 bucket policy associated with Bucket B restricts access to only the IAM role. This means that only the IAM role is able to access its content.
3. Both the IAM user and the IAM role can access other S3 buckets (for example, Bucket A) in the account. The IAM role is able to access both buckets, but the user can access only the S3 buckets without the bucket policy attached to them. Even though both the role and the user have full `“s3:*”` permissions, the bucket policy negates access to the bucket for anyone that has not assumed the role.

The main difference in the cross-account approach is that every bucket must have a bucket policy attached to allow access to the IAM role from the other account. The following diagram illustrates how this works in a cross-account deployment scenario.

![Figure 2: Diagram illustrating how to access an S3 bucket in a different account than your IAM role](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/02/13/img2.png)

Figure 2: Diagram illustrating how to access an S3 bucket in a different account than your IAM role

The workflow in Figure 2 is as follows:

1. The IAM role’s identity-based policy and the IAM users’ policy in the bucket account both grant access to `“s3:*”`
2. Bucket policy B denies access to all IAM users and roles **except** the role specified, and the policy defines what the role is allowed to do with the bucket.
3. Bucket policy A allows access to the IAM role from the other account.
4. The IAM user and IAM role can both access Bucket A because the IAM user is in the same account and there is an explicit `Allow` in bucket policy A for the role. The role can access both buckets because the `Deny` in bucket policy B is only for principals other than the IAM role.

## Using the `aws:PrincipalArn` condition

You can use different types of condition keys to compare details about the principal making the request with the principal properties that you specify in the policy. We recommend that you use the `aws:PrincipalArn` key. The `aws:PrincipalArn` key compares the Amazon Resource Name (ARN) of the principal that made the request with the ARN that you specify in the policy.

You could also use the `aws:userid` policy variable to uniquely identify a user or role in their explicit `Deny` statements. There is added complexity with using `aws:userid` to find the value because you have to perform an API call using valid credentials. When working with IAM roles this activity has additional complexity because you are required to get the [AssumedRoleUser](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumedRoleUser.html) information, which will not only include the unique role ID, but also the `role-session-name` that was provided while assuming the role. For example, the `aws:userid` for an `AssumedRoleUser` will be as follows:

```
aws:userid – AROADBQP57FF2AEXAMPLE:role-session-name
```

It becomes inconvenient to manage and track these IDs when you have a large list of users and roles to be included in the policy.

To mitigate these challenges, we recommend that you use the `aws:PrincipalArn` condition key. For IAM roles, the request context returns the ARN of the role, not the ARN of the user that assumed the role. AWS recommends that you specify the ARN for resources in policies instead of unique IDs and that you perform IAM policy audits on a periodic basis. Let’s look at how to use the condition key in an IAM policy.

## Granting same-account bucket access to a specific role

When accessing a bucket from within the same account, in most cases it is not necessary to use a bucket policy because the policy defines access that is already granted by the user’s direct IAM policy. S3 bucket policies are usually used for cross-account access, but you can also use them to restrict access through an explicit `Deny`. The `Deny` would be applied to all principals whether they were in the same account as the bucket or within a different account.

In this case, you use the IAM user or role [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) with the `aws:PrincipalArn` [condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) in a `StringNotEquals` or `StringNotLike` condition with a wildcard string. In addition, you use the `aws:PrincipalARN` key to compare the ARN of the principal that made the request with the ARN that you specify in the policy. Using a conditional logic element allows for the use of a wildcard string to allow for any role session name to be accepted.

Once you have the ARN of the role to which you want to allow access, you need to block the access of other users from within the same account as the bucket. An example policy to block access to the bucket and its objects for users that are not using the IAM role credentials would look like the following.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket",
        "arn:aws:s3:::amzn-s3-demo-bucket/*"
      ],
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalArn": [
            "arn:aws:iam::111122223333:role/<ROLE-NAME>"
          ]
        }
      }
    }
  ]
}
```

Use this same policy for IAM users as shown below.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket",
        "arn:aws:s3:::amzn-s3-demo-bucket/*"
      ],
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalARN": [
            "arn:aws:iam::111122223333:role/<ROLE-NAME>”,
            “arn:aws:iam::111122223333:user/<USER-NAME>"
          ]
        }
      }
    }
  ]
}
```

## Granting cross-account bucket access to a specific IAM role

When granting cross-account bucket access to an IAM user or role, you must define what the IAM user or role is allowed to do with the granted access. Learn more about the permissions needed to allow an IAM entity to access a bucket via the CLI/API and the console in `Writing IAM Policies: How to Grant Access to an Amazon S3 Bucket`. Using the information found in [this blog post](https://aws.amazon.com/blogs/security/writing-iam-policies-how-to-grant-access-to-an-amazon-s3-bucket/), an example bucket policy would look like the following.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/<ROLE-NAME>"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/<ROLE-NAME>"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
        },
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket",
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ],
            "Condition": {
                "StringNotEquals": {
                    "aws:PrincipalARN": [
                        "arn:aws:iam::111122223333:role/<ROLE-NAME>"
                    ]
                }
            }
        }
    ]
}
```

To grant access to an IAM user in another account, you need to add the `ARN` for the IAM user to the `aws:PrincipalArn` condition as outlined in the previous section of this blog post. In addition to the `aws:PrincipalArn` condition, you would also need to add the IAM user’s full ARN to the `Principal` element of these policies. An example policy is shown below.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": [
                {
                    "AWS": [
                        "arn:aws:iam::444455556666:role/<ROLE-NAME>”,
                        “arn:aws:iam::444455556666:user/<USER-NAME>"
                    ]
                }
            ],
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
        },
        {
            "Effect": "Allow",
            "Principal": [
                {
                    "AWS": [
                        "arn:aws:iam::444455556666:role/<ROLE-NAME>”,
                        “arn:aws:iam::444455556666:user/<USER-NAME>"
                    ]
                }
            ],
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
        },
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket",
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ],
            "Condition": {
                "StringNotEquals": {
                    "aws:PrincipalARN": [
                        "arn:aws:iam::444455556666:role/<ROLE-NAME>”,
                        “arn:aws:iam::444455556666:user/<USER-NAME>"
                    ]
                }
            }
        }
    ]
}
```

In addition to including role permissions in the bucket policy, you need to define these permissions in the IAM user’s or role’s user policy. The permissions are added to a [customer managed policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-using.html#create-managed-policy-console) and [attached](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-using.html#attach-managed-policy-console) to the role or user in the IAM console, with the following example policy document.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
    }
  ]
}
```

By following the guidance in this post, you restrict S3 bucket access to a specific IAM role or user in same-account and cross-account scenarios, even if the user has an `Admin` policy or a policy with `“s3:*”`. There are many applications of this logic in which requirements will vary across use cases. We recommend to employ the principle of least privilege wherever possible, and to grant only the minimum permissions that are required to perform necessary tasks.

If you have feedback about this post, submit comments in the Comments section below. If you have questions about this post, start a new thread on the [AWS Identity and Access Management re:Post](https://repost.aws/tags/TAO7Z4bI5hQVWMiYFs34QhIA) or [contact AWS Support](https://console.aws.amazon.com/support/home).

Chris Craig

The original author of this blog post is no longer at AWS. In 2016, when this post was first published, we did not include author bios.

![Laura Verghote](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2024/11/13/Laura-Verghote.jpg) Laura Verghote

Laura is a Senior Solutions Architect for public sector customers in the Europe, Middle East, and Africa (EMEA) region. She works with customers to design and build solutions in the AWS Cloud, bridging the gap between complex business requirements and technical solutions. She joined AWS as a technical trainer and has wide experience delivering training content to developers, administrators, architects, and partners across EMEA.

![Ashwin Phadke](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2023/11/14/phadkea.jpg) Ashwin Phadke

Ashwin is a Senior Solutions Architect working with large enterprises and independent software vendor (ISV) customers to build highly available, scalable, and secure applications, and to help them successfully navigate their cloud journeys. He is passionate about information security and enjoys working on creative solutions for customers’ security challenges.

TAGS: [Best of](https://aws.amazon.com/blogs/security/tag/best-of/), [IAM roles](https://aws.amazon.com/blogs/security/tag/iam-roles/), [NotPrincipal element](https://aws.amazon.com/blogs/security/tag/notprincipal-element/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/)

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