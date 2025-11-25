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

# Simplify access to external services using AWS IAM Outbound Identity Federation

by [Donnie Prakoso](https://aws.amazon.com/blogs/aws/author/donnie/ "Posts by Donnie Prakoso") on 19 NOV 2025 in [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [Identity](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/identity/ "View all posts in Identity"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/)  [Comments](https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

When building applications that span multiple cloud providers or integrate with external services, developers face a persistent challenge: managing credentials securely. Traditional approaches require storing long-term credentials like API keys and passwords, creating security risks and operational overhead.

Today, we’re announcing a new capability called AWS Identity and Access Management (IAM)[outbound identity federation](https://aws.amazon.com/identity/federation/) that customers can use to securely federate their Amazon Web Services (AWS) identities to external services without storing long-term credentials. You can now use short-lived JSON Web Tokens (JWTs) to authenticate your AWS workloads with a wide range of third-party providers, software-as-a-service (SaaS) platforms and self-hosted applications.

This feature enables IAM principals—such as IAM roles and users—to obtain cryptographically signed JWTs that assert their AWS identity. External services, such as third-party providers, SaaS platforms, and on-premises applications, can verify the token’s authenticity by validating its signature. Upon successful verification, you can securely access the external service.

**How it works** With IAM outbound identity federation, you exchange your AWS IAM credentials for short-lived JWTs. This mitigates the security risks associated with long-term credentials while enabling consistent authentication patterns.

Let’s walk through a scenario where your application running on AWS needs to interact with an external service. To access the external service’s APIs or resources, your application calls the AWS Security Token Service (AWS STS) `GetWebIdentityToken` API to obtain a JWT.

The following diagram shows this flow:

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/18/news-2025-iam-web-identity-3-4.png)

1. Your application running on AWS requests a token from AWS STS by calling the `GetWebIdentityToken` API. The application uses its existing AWS credentials obtained from the underlying platform (such as Amazon EC2 instance profiles, AWS Lambda execution roles, or other AWS compute services) to authenticate this API call.
2. AWS STS returns a cryptographically signed JSON Web Token (JWT) that asserts the identity of your application.
3. Your application sends the JWT to the external service for authentication.
4. The external service fetches the verification keys from the JSON Web Key Set (JWKS) endpoint to verify the token’s authenticity.
5. The external service validates the JWT’s signature using these verification keys and confirms the token is authentic and was issued by AWS.
6. After successful verification, the external service exchanges the JWT for its own credentials. Your application can then use these credentials to perform its intended operations.

**Setting up AWS IAM outbound identity federation** To begin using this feature, I need to enable outbound identity federation for my AWS account. I navigate to [IAM](https://console.aws.amazon.com/iam/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) and choose **Account settings** under **Access management** in the left-hand navigation pane.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/13/news-2025-iam-web-identity-2.png)

After I enable the feature, AWS generates a unique issuer URL for my AWS account that hosts the OpenID Connect (OIDC) discovery endpoints at `/.well-known/openid-configuration` and `/.well-known/jwks.json`. The OpenID Connect (OIDC) discovery endpoints contain the keys and metadata necessary for token verification.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/14/news-2025-iam-web-identity-4-1.png)

Next, I need to configure IAM permissions. My IAM principal (role or user) must have the `sts:GetWebIdentityToken` permission to request tokens.

For example, the following identity policy specifies access to the STS `GetWebIdentityToken` API, enabling the IAM principal to generate tokens.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:GetWebIdentityToken",
      "Resource": "*",
    }
  ]
}
```

At this stage, I need to configure the external service to trust and accept tokens issued by my AWS account. The specific steps vary by service, but generally involve:

1. Registering my AWS account issuer URL as a trusted identity provider
2. Configuring which claims to validate (audience, subject patterns)
3. Mapping token claims to permissions in the external service

**Let’s get started** Now, let me walk you through an example showing both the client-side token generation and server-side verification process.

First, I call the STS `GetWebIdentityToken` API to obtain a JWT that asserts my AWS identity. When calling the API, I can specify the intended audience, signing algorithm, and token lifetime as request parameters.

* `Audience`: Populates the `aud` claim in the JWT, identifying the intended recipient of the token (for example, “my-app”)
* `DurationSeconds`: The token lifetime in seconds, ranging from 60 seconds (1 minute) to 3600 seconds (1 hour), with a default of 300 seconds (5 minutes)
* `SigningAlgorithm`: Choose either ES384 (ECDSA using P-384 and SHA-384) or RS256 (RSA using SHA-256)
* `Tags` (optional): An array of key-value pairs that appear as custom claims in the token, which you can use to include additional context that enables external services to implement fine-grained access control

Here’s an example of getting an identity token using the [AWS SDK](https://builder.aws.com/build/tools?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) for Python (Boto3). I can also do this using [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el).

```
import boto3

sts_client = boto3.client('sts')
response = sts_client.get_web_identity_token(
    Audience=['my-app'],
    SigningAlgorithm='ES384',  # or 'RS256'
    DurationSeconds=300
)
jwt_token = response['WebIdentityToken']
print(jwt_token)
```

This returns a signed JWT that I can inspect using any JWT parser.

```
{
eyJraWQiOiJFQzM4NF8wIiwidHlwIjoiSldUIiwiYWxnIjoiRVMzODQifQ.hey<REDACTED FOR BREVITY>...
```

I can decode the token using any JWT parser like this [JWT Debugger](https://www.jwt.io/). The token header shows it’s signed with ES384 (ECDSA).

```
{
  "kid": "EC384_0",
  "typ": "JWT",
  "alg": "ES384"
}
```

Also, the payload contains standard OIDC claims plus AWS specific metadata. The standard OIDC claims include subject (“sub”), audience (“aud”), issuer (“iss”), and others.

```
{
  "aud": "my-app",
  "sub": "arn:aws:iam::ACCOUNT_ID:role/MyAppRole",
  "https://sts.amazonaws.com/": {
    "aws_account": "ACCOUNT_ID",
    "source_region": "us-east-1",
    "principal_id": "arn:aws:iam::ACCOUNT_ID:role/MyAppRole"
  },
  "iss": "https://abc12345-def4-5678-90ab-cdef12345678.tokens.sts.global.api.aws",
  "exp": 1759786941,
  "iat": 1759786041,
  "jti": "5488e298-0a47-4c5b-80d7-6b4ab8a4cede"
}
```

AWS STS also enriches the token with identity-specific claims (such as account ID, organization ID, and principal tags) and session context. These claims provide information about the compute environment and session where the token request originated. AWS STS automatically includes these claims when applicable based on the requesting principal’s session context. You can also add custom claims to the token by passing request tags to the API call. To learn more about claims provided in the JWT, visit the [documentation page](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_token_claims.html).

Note the `iss` (issuer) claim. This is your account-specific issuer URL that external services use to verify that the token originated from a trusted AWS account. External services can verify the JWT by validating its signature using AWS’s verification keys available at a public JSON Web Key Set (JWKS) endpoint hosted at the `/.well-known/jwks.json` endpoint of the issuer URL.

Now, let’s look at how external services handle this identity token.

Here’s a snippet of Python example that external services can use to verify AWS tokens:

```
import json
import jwt
import requests
from jwt import PyJWKClient

# Trusted issuers list - obtained from EnableOutboundFederation API response
TRUSTED_ISSUERS = [
    "https://EXAMPLE.tokens.sts.global.api.aws",
    # Add your trusted AWS account issuer URLs here
    # Obtained from EnableOutboundFederation API response
]

def verify_aws_jwt(token, expected_audience=None):
    """Verify an AWS IAM outbound identity federation JWT"""
    try:
        # Get issuer from token
        unverified_payload = jwt.decode(token, options={"verify_signature": False})
        issuer = unverified_payload.get('iss')

 	# Verify issuer is trusted
        if not TRUSTED_ISSUERS or issuer not in TRUSTED_ISSUERS:
            raise ValueError(f"Untrusted issuer: {issuer}")

        # Fetch JWKS from AWS using PyJWKClient
        jwks_client = PyJWKClient(f"{issuer}/.well-known/jwks.json")
        signing_key = jwks_client.get_signing_key_from_jwt(token)

        # Verify token signature and claims
        decoded_token = jwt.decode(
            token,
            signing_key.key,
            algorithms=["ES384", "RS256"],
            audience=expected_audience,
            issuer=issuer
        )
        return decoded_token
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None
```

**Using IAM policies to control access to token generation** An IAM principal (such as a role or user) must have the `sts:GetWebIdentityToken` permission in their IAM policies to request tokens for authentication with external services. AWS account administrators can configure this permission in all relevant AWS policy types such as identity policies, service control policies (SCPs), resource control policies (RCPs), and virtual private cloud endpoint (VPCE) policies to control which IAM principals in their account can generate tokens.

Additionally, administrators can use the new condition keys to specify signing algorithms (`sts:SigningAlgorithm`), permitted token audiences (`sts:IdentityTokenAudience`), and maximum token lifetimes (`sts:DurationSeconds`). To learn more about the condition keys, visit [IAM and STS Condition keys documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-sts) page.

**Additional things to know** Here are key details about this launch:

* **Availability** – AWS IAM outbound identity federation is available at no additional cost in all [AWS commercial Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el), [AWS GovCloud (US) Regions](https://aws.amazon.com/govcloud-us/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el), and China Regions.
* **Pricing** – This feature is available at no additional cost.

Get started with AWS IAM outbound identity federation by visiting [AWS IAM console](https://console.aws.amazon.com/iam/?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el) and enabling the feature in your AWS account. To learn more on how to programmatically enable this feature, refer to this [Getting Started](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html) page. For more information, visit [Federating AWS Identities to External Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound.html) documentation page.

Happy building!

— [Donnie](https://www.linkedin.com/in/donnieprakoso)

Editors note: 11/22/25- Getting Started documentation added

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