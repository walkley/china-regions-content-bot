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

# Simplified developer access to AWS with ‘aws login’

by Shreya Jain and Sowjanya Rajavaram on 19 NOV 2025 in [AWS CLI](https://aws.amazon.com/blogs/security/category/programing-language/aws-cli/ "View all posts in AWS CLI"), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [AWS Security Token Service](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-security-token-service/ "View all posts in AWS Security Token Service"), [Developer Tools](https://aws.amazon.com/blogs/security/category/developer-tools/ "View all posts in Developer Tools"), [Foundational (100)](https://aws.amazon.com/blogs/security/category/learning-levels/foundational-100/ "View all posts in Foundational (100)"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/security/simplified-developer-access-to-aws-with-aws-login/)  [Comments](https://aws.amazon.com/blogs/security/simplified-developer-access-to-aws-with-aws-login/#Comments)  Share

Getting credentials for local development with AWS is now simpler and more secure. A new AWS Command Line Interface ([AWS CLI](http://aws.amazon.com/cli/)) command, `aws login`, lets you start building immediately after signing up for AWS without creating and managing long-term access keys. You use the same sign-in method you already use for the [AWS Management Console](http://aws.amazon.com/console/).

In this blog, we’ll show you how to get temporary credentials to your workstation for use with the AWS CLI, AWS Software Development Kits (AWS SDKs), and tools or applications built using them with the new `aws login` command.

## Getting started with programmatic access to AWS

You can use the `aws login` command with your AWS Management Console sign-in method, as described in the following sections.

### Scenario 1: Using IAM credentials (root or IAM user)

To obtain programmatic credentials using your root or IAM user username and password:

1. Install the latest [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) (version 2.32.0 or later).
2. Run the `aws login` command.
3. If you have not set a default Region, the CLI prompts you to specify the [AWS Region](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html) of your choice (e.g., us-east-2, eu-central-1). The CLI remembers which Region you set once you enter it into this prompt.

   ![Figure 1: CLI Region prompt](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/19/Fig1-rev.jpg)

   Figure 1: CLI Region prompt
4. The CLI opens your default browser.
5. Follow the instructions in the browser window:
   1. If you have already signed into the AWS Management Console, you will see a screen that says, “Continue with an active session.”

      ![Figure 2: Sign in to AWS - active session selection](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/19/image2-2.png)

      Figure 2: Sign in to AWS – active session selection
   2. If you haven’t signed into the AWS Management Console, you will see the sign-in options page. Select “Continue with Root or IAM user” and log in to your AWS account.

      ![Figure 3: AWS Sign in to AWS - Sign-in options](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/19/image3-3.png)

      Figure 3: AWS Sign in to AWS – Sign-in options
6. Success! You’re ready to run AWS CLI commands. Try the `aws sts get-caller-identity` command to verify the identity you’re currently using.

   ![Figure 4: Sign in to AWS - completion](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/19/image4-2.png)

   Figure 4: Sign in to AWS – completion

### Scenario 2: Using federated sign-in

This scenario applies when you authenticate through your organization’s identity provider. To retrieve programmatic credentials for roles you assumed with federation:

1. Complete steps 1–4 from Scenario 1, then continue with the following instructions.
2. Follow the instructions in the browser window:
   1. If you have already signed into the AWS Management Console, the browser provides you with the option to select your active IAM role session from federated sign-in to the console. This enables you to switch between 5 active AWS sessions if you have [multi-session support](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/multisession.html) enabled on your AWS Management Console.

      ![Figure 5: Sign in to AWS - active IAM role session selection](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/19/image5-1.png)

      Figure 5: Sign in to AWS – active IAM role session selection
   2. If you have not signed into the AWS Management Console or want to get temporary credentials for a different IAM role, sign into your AWS account using your current authentication mechanism in another browser tab. Upon successful login, switch back to this tab and select the “Refresh” button. Your console session should now be available under the active sessions.
3. Return to the AWS CLI once you have successfully completed the `aws login` process.

Regardless of the console sign-in method you choose, the temporary credentials issued by the `aws login` command are automatically rotated by the AWS CLI, AWS Tools for PowerShell and AWS SDKs every 15 minutes. They are valid up to the set session duration of the IAM principal (maximum of 12 hours). After reaching the session duration limit, you will be prompted to log in again.

![Figure 6: AWS Sign in - session expiration](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/19/Fig6-r2.jpg)

Figure 6: AWS Sign in – session expiration

### Accessing AWS using local developer tools

The `aws login` command supports switching between multiple AWS accounts and roles using profiles. You can configure a profile with `aws login --profile <PROFILE_NAME>` and run AWS commands with the profile using: `aws sts get-caller-identity --profile <PROFILE_NAME>`. The short-term credentials issued by `aws login` work with more than the AWS CLI. You can also use them with:

* [AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html): If you use AWS SDKs for development, the SDK clients can use these temporary credentials to authenticate with AWS.
* [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/v5/userguide/creds-idc.html): Use the `Invoke-AWSLogin` command.
* [Remote development servers](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html): Use `aws login --remote` on a remote server without browser access, to deliver temporary credentials from your device with browser access to the AWS console.
* Older versions of AWS SDKs that do not support the new console credentials provider: Any software written using these older SDKs can support credentials delivered by `aws login` by using the [credential\_process provider](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html#cli-configure-sign-in-cached-credentials) with the AWS CLI.

### Controlling access to aws login with IAM policies

The `aws login` command is controlled by two IAM actions: **signin:AuthorizeOAuth2Access** and **signin:CreateOAuth2Token**. Use the [SignInLocalDevelopmentAccess](https://docs.aws.amazon.com/signin/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-SignInLocalDevelopmentAccess) managed policy or add these actions to your IAM policies to allow IAM users and IAM roles with console access to use this feature.

[AWS Organizations](http://aws.amazon.com/organizations/) customers looking to control the usage of this login feature on member accounts can deny the two actions above using Service Control Policies (SCPs). These IAM actions and their resources are usable in all relevant IAM policies.

AWS recommends using [centralized root access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) in AWS Organizations to eliminate long-term root credentials from member accounts. This feature allows security teams to perform privileged tasks through short-term, task-scoped root sessions from a central management account. After you enable centralized root management and delete root credentials on member accounts, root login to member accounts is denied, which also prevents programmatic access with root credentials using `aws login`. For developers using root credentials or IAM users, `aws login` delivers short-lived credentials to development tools, providing a secure alternative to long-term static access keys.

### Logging and security of programmatic access using aws login

AWS Sign-In logs API activity through [AWS CloudTrail](https://aws.amazon.com/cloudtrail), which now includes two new events specific to `aws login`. The service logs two new event names called AuthorizeOAuth2Access and CreateOauth2Token in the AWS Region where the user logs in.

Here’s a CloudTrail sample for an AuthorizeOAuth2Access event:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROATJHQDX737YZP72NTF:testuser”,
        "arn": "arn:aws:sts::225989345271:assumed-role/Admin/testuser,
        "accountId": “111111111111”,
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROATJHQDX737YZP72NTF",
                "arn": "arn:aws:iam::111111111111:role/Admin",
                "accountId": “11111111111”,
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-17T22:50:14Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-17T22:51:32Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "AuthorizeOAuth2Access",
    "awsRegion": "us-east-1",
    "sourceIPAddress": “192.0.2.2”,
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "requestParameters": {
        "scope": "openid",
        "redirect_uri": "http://127.0.0.1:53037/oauth/callback",
        "code_challenge_method": "SHA-256",
        "client_id": "arn:aws:signin:::devtools/same-device"
    },
    "responseElements": null,
    "additionalEventData": {
        "success": "true",
        "x-amzn-vpce-id": ""
    },
    "requestID": "e2854c76-1cba-4360-9fd1-5037b591466b",
    "eventID": "59e1720d-3deb-44ff-933d-6828be2a860a",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": “111111111111”,
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "us-east-1.signin.aws.amazon.com"
    }
}
```

Here’s a CloudTrail sample for a CreateOAuth2Token event:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROATJHQDX737YZP72NTF:testuser-Isengard",
        "arn": "arn:aws:sts::111111111111:assumed-role/Admin/testuser-Isengard",
        "accountId": "111111111111",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROATJHQDX737YZP72NTF",
                "arn": "arn:aws:iam::111111111111:role/Admin",
                "accountId": "111111111111",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-18T20:38:10Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-18T20:38:44Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CreateOAuth2Token",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.2",
    "userAgent": "aws-cli/2.32.0 md/awscrt#0.28.4 ua/2.1 os/macos#24.6.0 md/arch#arm64 lang/python#3.13.9 md/pyimpl#CPython m/b,AA,Z,E cfg/retry-mode#standard md/installer#exe sid/35033f4ca1bd md/prompt#off md/command#login",
    "requestParameters": {
        "client_id": "arn:aws:signin:::devtools/same-device"
    },
    "responseElements": null,
    "additionalEventData": {
        "success": "true",
        "x-amzn-vpce-id": ""
    },
    "requestID": "94562943-c85b-4dc1-bf72-43b0fd42d6de",
    "eventID": "0b338fac-6a10-4740-b34d-1bb6923e799e",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111111111111",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "us-east-1.signin.aws.amazon.com"
    }
}
```

The `aws login` command uses the OAuth 2.0 authorization code flow with PKCE (Proof Key for Code Exchange) to protect against authorization code interception attacks. This provides a secure alternative to setting up IAM user access keys for getting started with development on AWS. For guidance on additional modern authentication approaches and alternatives to long-term IAM access keys, see the AWS Security Blog post “[Beyond IAM access keys: Modern authentication approaches for AWS](https://aws.amazon.com/blogs/security/beyond-iam-access-keys-modern-authentication-approaches-for-aws/).”

## Conclusion

##

The login for AWS local development feature is a secure-by-default enhancement that helps customers eliminate the use of long-term credentials for programmatic access with AWS. With `aws login`, you can start building immediately using the same credentials you use to sign in to the AWS Management Console. This feature is now available across all AWS commercial Regions (excluding China and GovCloud) at no additional cost to customers.

For more information, visit the authentication and access section in the [CLI user guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html).

If you have feedback about this post, submit comments in the **Comments** section below.

![Shreya Jain](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/19/Shreya-Jain.jpg)

### Shreya Jain

Shreya is a Senior Technical Product Manager in AWS Identity. She is energized by bringing clarity and simplicity to complex ideas. When she’s not applying her creative energy at work, you’ll find her at Pilates, dancing, or discovering her next favorite coffee shop.

![Sowjanya Rajavaram](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/08/26/Sowjanya-Rajavaram-author.jpg)

### Sowjanya Rajavaram

Sowjanya is a Sr Solutions Architect who specializes in Identity and Security in AWS. She works on helping customers of all sizes solve their identity and access management problems. She enjoys traveling and exploring new cultures and food.

TAGS: [AWS CLI](https://aws.amazon.com/blogs/security/tag/aws-cli/), [AWS IAM](https://aws.amazon.com/blogs/security/tag/aws-iam/), [AWS STS](https://aws.amazon.com/blogs/security/tag/aws-sts/), [IAM](https://aws.amazon.com/blogs/security/tag/iam/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/)

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