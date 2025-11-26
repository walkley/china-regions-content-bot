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

# How to monitor, optimize, and secure Amazon Cognito machine-to-machine authorization

by Abrom Douglas and Nisha Notani on 13 JAN 2025 in [Advanced (300)](https://aws.amazon.com/blogs/security/category/learning-levels/advanced-300/ "View all posts in Advanced (300)"), [Amazon API Gateway](https://aws.amazon.com/blogs/security/category/application-services/amazon-api-gateway-application-services/ "View all posts in Amazon API Gateway"), [Amazon Cognito](https://aws.amazon.com/blogs/security/category/security-identity-compliance/amazon-cognito/ "View all posts in Amazon Cognito"), [Management & Governance](https://aws.amazon.com/blogs/security/category/management-and-governance/ "View all posts in Management & Governance"), [Management Tools](https://aws.amazon.com/blogs/security/category/management-tools/ "View all posts in Management Tools"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/security/how-to-monitor-optimize-and-secure-amazon-cognito-machine-to-machine-authorization/)  [Comments](https://aws.amazon.com/blogs/security/how-to-monitor-optimize-and-secure-amazon-cognito-machine-to-machine-authorization/#Comments)  Share

> **September 4, 2025:**The Amazon CloudWatch Logs Insights query in this blog has been updated to reflect the current AWS CloudTrail log for an Amazon Cognito M2M token issue event. This CloudTrail event now includes the client ID for all M2M token requests by default.

---

[Amazon Cognito](https://aws.amazon.com/cognito) is a developer-centric and security-focused customer identity and access management (CIAM) service that simplifies the process of adding user sign-up, sign-in, and access control to your mobile and web applications. Cognito is a highly available service that supports a range of use cases, from managing user authentication and authorization to enabling secure access to your APIs and workloads. It’s a managed service that can act as an identity provider (IdP) for your applications, can scale to millions of users, provides advanced security features, and can support identity federation with third-party IdPs.

A feature of Amazon Cognito is support for [OAuth 2.0 client credentials grants](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.4), used for machine-to-machine (M2M) authorization. As your M2M use cases scale, it becomes important to have proper monitoring, optimization of token issuance, and awareness of security best practices and considerations. It’s a best practice for app clients to locally cache and reuse access tokens while still valid and not expired. You can customize how long issued tokens are valid, so it’s important to make sure that the timeframe is aligned with your security requirements. If caching and reusing access tokens isn’t possible at the client level or cannot be enforced, then combining your M2M use cases with a REST API proxy integration using [Amazon API Gateway](https://aws.amazon.com/api-gateway/) enables you to [cache token responses](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-caching-tokens.html). By using API Gateway caching, you can optimize the request and response of access tokens for M2M authorization. This reduces redundant calls to Cognito for access tokens, thus improving the overall performance, availability, and security of your M2M use cases.

In this post, we explore strategies to help monitor, optimize, and secure Amazon Cognito M2M authorization. You’ll first learn some effective monitoring techniques to keep track of your usage, then delve into optimization strategies using API Gateway and token caching. Lastly, we will cover security best practices and considerations to bolster the security of your M2M use cases. Let’s dive in and discover how to make the most out of your Amazon Cognito M2M implementation.

## Machine-to-machine authorization

Amazon Cognito uses an [OAuth 2.0 client credentials grant](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.4) to handle M2M authorization. A Cognito user pool can issue a client ID and client secret to allow your service to request a JSON web token (JWT)-compliant access token to access protected resources. Figure 1 illustrates how an app client requests an access token using the client credentials grant flow with Amazon Cognito.

![Figure 1: Client credentials grant flow](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/01/06/image1.png)

Figure 1: Client credentials grant flow

The client credential grant flow (Figure 1) includes the following steps:

1. The app client makes an HTTP POST request to the Amazon Cognito user pool `/token` endpoint (see [The token issuer endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/token-endpoint.html) for more information), which provides an authorization header consisting of the client ID and client secret, and request parameters consisting of grant type, client ID, and scopes.
2. After validating the request, Cognito will return a JWT-compliant access token.
3. The client can make subsequent requests to a downstream resource server using the Cognito issued access token.
4. The resource server gets a JSON Web Key Set (JWKS) from the Cognito user pool. The JWKS contains the user pool’s public keys, which should be used to verify the token signature.
5. The resource server uses the public key to verify the signature of the access token is valid (proving the token has not been tampered with). The resource server also needs to verify that the token is not expired and required claims and values are present, including scopes. The resource server should use the [aws-jwt-verify library](https://github.com/awslabs/aws-jwt-verify) to verify that the access token is valid.
6. After the access token is verified and the app client is authorized, the requested resource is returned to the app client.

You can learn more about OAuth 2.0 support for client credentials grants and other authentication flows that Amazon Cognito supports in [How to use OAuth 2.0 in Amazon Cognito: Learn about the different OAuth 2.0 grants](https://aws.amazon.com/blogs/security/how-to-use-oauth-2-0-in-amazon-cognito-learn-about-the-different-oauth-2-0-grants/).

Now, let’s dive deep into the monitoring, optimization, and security considerations around M2M authorization with Amazon Cognito.

## Monitoring usage and costs

In May 2024, Amazon Cognito introduced pricing for M2M authorization to support continued growth and expand M2M features. Customer accounts using M2M with Cognito prior to May 9, 2024, are exempt from M2M pricing until May 9, 2025 (for more information, see [Amazon Cognito introduces tiered pricing for machine-to-machine (M2M) usage](https://aws.amazon.com/about-aws/whats-new/2024/05/amazon-cognito-tiered-pricing-m2m-usage/)). To get better visibility into your existing Amazon Cognito usage types, you can use the [Security](https://cid.workshops.aws.dev/demo?dashboard=cudos&sheet=security) tab of the [Cost and Usage Dashboards Operations Solution (CUDOS)](https://catalog.us-east-1.prod.workshops.aws/workshops/86d8a62a-7714-40be-b0a2-98b6531388e5/en-US/dashboards/foundational/cudos-cid-kpi/#cudos-dashboard) dashboard. This dashboard is part of the [Cloud Intelligence Dashboard](https://wellarchitectedlabs.com/cloud-intelligence-dashboards/), an opensource framework that provides AWS customers actionable insights and optimization opportunities at an organization scale. As shown in Figure 2, the Security tab in the CUDOS dashboard provides visuals that show the cost and spend of Amazon Cognito per usage type and the projected cost for M2M app clients and token requests after the exemption period with daily granularity. This daily breakdown allows you to track how your cost optimization efforts are trending.

![Figure 2: Example Amazon Cognito spend and projected cost with daily granularity](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/01/06/image2.png)

Figure 2: Example Amazon Cognito spend and projected cost with daily granularity

You can also see the monthly spend per account for each usage type, as shown in Figure 3.

![Figure 3: Example Amazon Cognito spend and projected cost per AWS account](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/01/06/image3.png)

Figure 3: Example Amazon Cognito spend and projected cost per AWS account

You can see the usage and spend per resource ID of user pools contributing to the cost, as shown in Figure 4. This resource-level granularity enables you to identify the top spending user pool and prioritize usage and cost management efforts accordingly. An [interactive demo of this dashboard](https://cid.workshops.aws.dev/demo?dashboard=cudos&sheet=a4b17c03-a3ea-4057-95c9-9411f837b45a) is available. For more information, see [Cloud Intelligence Dashboards](https://wellarchitectedlabs.com/cloud-intelligence-dashboards/).

![Figure 4: Example Amazon Cognito resource usage and cost by resource ID, account, and AWS Region](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/01/06/image4.png)

Figure 4: Example Amazon Cognito resource usage and cost by resource ID, account, and AWS Region

In addition to using the CUDOS dashboard to help understand Cognito M2M usage and costs, you can also request fine-grained usage details down to the app client level. This can include the number of access tokens successfully requested per app client and the last time the app client was used to issue tokens. The [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) log event for a M2M token request will include the `client ID` within the `additionalEventData` JSON object that is associated with the client credentials token request, as shown in Figure 5.

![Figure 5: Sample CloudTrail event log including clientId](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/09/04/Figure-5-how-to-monitor.png)

Figure 5: Sample CloudTrail event log including clientId

You can also use an [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) log group to capture and store your CloudTrail logs for longer retention and [analysis](https://docs.aws.amazon.com/cognito/latest/developerguide/analyzingcteventscwinsight.html). Then using [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html), you can use the following sample query to gather app client usage.

```
fields additionalEventData.userPoolId as user_pool_id, additionalEventData.clientId as client_id, eventName, additionalEventData.responseParameters.status
| filter additionalEventData.requestParameters.grant_type.0="client_credentials" and eventName="Token_POST" and additionalEventData.responseParameters.status="200"
| stats count(*) as count, latest(eventTime) as lastUsed by user_pool_id, client_id
| sort count desc
```

Figure 6 is an example result from the preceding CloudWatch Logs Insights query. The result includes the `user_pool_id`, `client_id`, `count`, and `last_used` columns. The total number of successful token requests grouped per user pool and client ID will be displayed in the `count` column and the last time the app client successfully issued an access token will be displayed in the `last_used` column.

![Figure 6: Example screenshot result set from CloudWatch Logs Insights query](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/01/06/image6.png)

Figure 6: Example screenshot result set from CloudWatch Logs Insights query

## Optimizing token requests

Now that you know how to better monitor your Amazon Cognito usage and costs, let’s dive deeper into how to optimize your token requests usage. For M2M, it’s recommended that clients use mechanisms to locally cache access tokens to use for authorization. This will reduce the need for the client to request a new access token until the previously issued token is no longer valid. However, the environment where the client runs could be hosted by an external third party or owned by a different team and as the resource owner, you won’t have control over whether the third party implements token caching at the client side. If this is a scenario that you have, you can use a [HTTP proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-http.html) to cache the access token using API Gateway. Because the M2M use case follows the client credentials grant flow of the OAuth 2.0 specification, the `/token` endpoint of your user pool is what will be configured with the API Gateway proxy integration. This proxy integration is where [caching in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html) can be used. With caching, you can reduce the number of token requests made to your user pool `/token` endpoint and improve the latency of the client receiving a cached token in the response. With caching, you can achieve additional benefits, such as cost optimization, improved performance efficiency, higher levels of availability, and custom domain flexibility.

## Solution overview

![Figure 7: Token caching solution](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/01/06/image7.jpeg)

Figure 7: Token caching solution

The solution (shown in the Figure 7) includes the following steps.

1. The client makes an HTTP POST request to an API Gateway REST API.
2. The API Gateway method request caches the `scope` URL query string parameter and the `Authorization` HTTP request header as caching keys. The integration request is configured as a proxy to the `/oauth2/token` endpoint of your Amazon Cognito user pool.
3. Ensure the Authorization header and the scope query string parameter are set as being required. Visit the Caching machine-to-machine access tokens with Amazon API Gateway section of the Cognito developer guide for more details.
4. Cognito validates the request, making sure that the client ID and client secret are correct from the authorization header, a valid client ID has been provided as a query string parameter, and the client is authorized for the requested scopes.
5. If the request is valid, Cognito returns an access token to the gateway through the integration response. With caching enabled, the response from the HTTP integration (Cognito token endpoint) is cached for the specified time-to-live (TTL) period.
6. The method response of the gateway returns the access token to the client.
7. Subsequent token requests with a remaining cached TTL will be returned, using the authorization header and scope as the caching keys.

To set up token caching, follow the steps in [Managing user pool token expiration and caching](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-caching-tokens.html). After a valid token request is returned through the API Gateway proxy integration and cached, subsequent token requests to the proxy that match the caching keys (authorization header and scope parameter) will return that same access token. This token will be returned to the client until the TTL of the cached token has expired. It’s recommended to set the TTL of the cache to be a few minutes less than the TTL of the access token issued from Amazon Cognito. For example, if your security posture requires access tokens to be valid for 1 hour, then set your caching TTL to be a few minutes less than the 1-hour token validity. It’s also important to understand the ideal caching capacity for your use case. The caching capacity affects the CPU, memory, and network bandwidth of the cache instance within the gateway. As a result, the cache capacity can affect the performance of your cache. See [Enable Amazon API Gateway caching](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html#enable-api-gateway-caching) for more information. For information about how to determine the ideal cache capacity for your use case, see [How do I select the best Amazon API Gateway Cache capacity to avoid hitting a rate limit?](https://repost.aws/knowledge-center/api-gateway-cache-capacity). Let’s now explore some security best practices and considerations to raise the security bar of your M2M use cases.

## Security best practices

Now that you know how to monitor Amazon Cognito M2M usage and costs and how to optimize access token requests, let’s review some security best practices and considerations. Using OAuth 2.0 client credentials grant for M2M authorization helps protect your APIs. One of the key factors for this is that the access token used by the client to connect to the resource server is a temporary and time-bound token. The client must obtain a new access token after its previous token has expired so you won’t have to issue long-lived credentials that are used directly between the client and the resource server. The client ID and client secret remain confidential on the client and are only used between the client and the Amazon Cognito user pool to request an access token.

### Use AWS Secrets Manager

If the workload is running on AWS, use [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) so you don’t have to worry about hard-coding credentials into workloads and applications. If the workload is running on premises or through another provider, then use a similar secrets’ vault or privileged access management solution to house the workload credentials. The workload should retrieve credentials for authentication only at runtime.

### Use AWS WAF

It’s a security best practice to use [AWS WAF](https://aws.amazon.com/waf/) to protect your Amazon Cognito user pool endpoints. This can help protect your user pools from unwanted HTTP web requests by forwarding selected non-confidential headers, request body, query parameters, and other request components to an AWS WAF web access control list (ACL) associated with your user pool. By using AWS WAF, you can also add managed rule groups to your user pool, such as the AWS managed rule group for [Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html), to add protection against automated bots that can consume excess resources, cause downtime, or perform malicious activities. Learn more about how to [associate an AWS WAF Web ACL with your Cognito user pool](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html).

### Always verify tokens

After a client has obtained an access token, it’s important to make sure the client is authorized to access the requested resources. If the resource is using API Gateway and the built-in [Amazon Cognito authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html), then the integrity of the token, the signature, and token expiration are checked and validated for you. However, if you require a more custom authorization decision with API Gateway, you can use an [AWS Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) along with the [aws-jwt-verify library](https://github.com/awslabs/aws-jwt-verify). By doing so, you can verify that the signature of the JWT token is valid, make sure that the token isn’t expired, and that the necessary and expected claims are present (including necessary scopes). For more fine-grained authorization decisions, look into using [Amazon Verified Permissions](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-authorization-with-avp.html) with the resource server or even within a [Lambda authorizer](https://aws.amazon.com/blogs/security/authorize-api-gateway-apis-using-amazon-verified-permissions-and-amazon-cognito/). If the resource server is an external system that is, outside of AWS or a custom resource server, you want to make sure that the access token is validated and verified before the requested resources are returned to the client.

### Define scopes at the app client level

It’s important to carefully define and constrain the scope of access for each app client to align with the principle of least privilege. By restricting each client ID to only the necessary scopes, organizations can minimize the risk of issuing access tokens with more access and permissions than is required. If your use case aligns with M2M multi-tenancy, consider creating a dedicated app client per tenant and using defined custom scopes for that tenant. Remember that the number of M2M app clients is a pricing dimension and will incur a cost. See [Custom scope multi-tenancy best practices](https://docs.aws.amazon.com/cognito/latest/developerguide/scope-based-multi-tenancy.html) for more information.

## Security considerations

If you’re using API Gateway to proxy token requests and caching access tokens, the following are some security considerations to raise the security bar of your M2M workload.

### Allow token requests only through an API Gateway proxy

After your API Gateway proxy integration is configured and set up for optimization and you have AWS WAF configured for your user pool, you can add an additional layer of security by using an allow list so that only requests from your API Gateway proxy to your Amazon Cognito user pool are accepted. For this, inject a custom HTTP header within the integration request of the POST method execution and create an allow rule within your web ACL that looks for that specific header. You will also create an additional web ACL rule to block all traffic. The single allow rule will have a priority order of `0` and the block-all-traffic rule will have a priority order of `1`. Ultimately, this will block all requests that go directly to your Cognito user pool `/token` endpoint and only allow requests that have been made through the API Gateway proxy. Figure 8 that follows is a deeper explanation of this setup.

![Figure 8: Token caching solution with AWS WAF](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/01/06/image8.png)

Figure 8: Token caching solution with AWS WAF

The process shown in Figure 8 has the following steps:

1. The client makes a direct HTTP POST call to the `/oauth2/token` endpoint of the Amazon Cognito user pool. This request would be denied by the AWS WAF web ACL deny all rule.
2. The client initiates an OAuth2 client credentials grant (HTTP POST) against an API Gateway stage (`/token`).
3. The REST API gateway is a proxy integration to the `/oauth2/token` endpoint of the Cognito user pool.
   1. Within the integration request settings, configure a custom header (for example, `x-wafAuthAllowRule`). Treat the value of this header as a secret that remains only within the API Gateway integration request and is not exposed outside of the gateway.
   2. Consider using [Lambda](https://aws.amazon.com/lambda/), [Amazon EventBridge](https://aws.amazon.com/eventbridge/), and [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) to automatically rotate this header value in both the API Gateway integration request and in the AWS WAF web ACL rule.
4. The request is proxied to the Cognito `/oauth2/token` endpoint and AWS WAF is configured to protect the Cognito user pool endpoints and therefore web ACL rules are evaluated.
   1. The custom header from the integration request (the preceding step) is evaluated against the web ACL rules to allow this request.
5. Cognito will verify the authorization header (containing the client ID and client secret) and requested scopes.
6. After successful credential validation, an access token is returned to the gateway within the integration response.
7. The access token is cached using the following caching keys:
   1. Authorization header.
   2. Scope query string parameter.
8. The access token is returned to the client through API Gateway.
9. Subsequent token requests with a remaining cached TTL are returned to client immediately, using the authorization header and scope as the caching keys.

### Additional authorizer with API Gateway

Using the client credentials grant is designed to obtain an access token so that an app client can access downstream resources. If you’re using API Gateway as a proxy integration to your token endpoint, as described previously, you can also use a separate authorizer with an API Gateway proxy. Therefore, to begin the OAuth 2.0 client credentials grant flow, a separate authorization takes place first. For example, if you’re in a highly regulated industry, you might require the use of [mTLS authentication](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html) to obtain an access token. This might seem like a double-authentication scenario; however, this helps prevent unauthenticated attempts against your API Gateway proxy integration to get an access token from Amazon Cognito.

### Encrypting the API cache

While configuring your API Gateway proxy integration and provisioning your API cache, you can enable [encryption of the cached response data](https://docs.aws.amazon.com/apigateway/latest/developerguide/data-protection-encryption.html#data-protection-at-rest). Because this caches access tokens for the set TTL of your choosing, you should consider encrypting this data at rest if necessary to help meet your security requirements. You can use the default method caching or set an override stage-level caching and enable encryption at rest.

## Conclusion

In this post, we shared how you can monitor, optimize, and enhance the security posture of your machine-to-machine (M2M) authorization use cases with Amazon Cognito. This involved using the Cost and Usage Dashboards Operations Solution (CUDOS) to understand your Cognito M2M token requests and costs. We also discussed using caching from Amazon API Gateway as an HTTP proxy integration to the Cognito user pool `/oauth2/token` endpoint. By following the guidance in this post, you can better understand your M2M usage and costs and achieve added benefits such as cost optimization, performance efficiency, and higher levels of availability. Lastly, we provided several security best practices and considerations that can be used as additional layers to elevate your security posture.

If you have feedback about this post, submit comments in the **Comments** section below. If you have questions about this post, start a new thread on [Amazon Cognito re:Post](https://repost.aws/tags/TAkhAE7QaGSoKZwd6utGhGDA/amazon-cognito) or [contact AWS Support](https://console.aws.amazon.com/support/home "contact AWS Support").

![Abrom Douglas](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2023/01/12/Abrom.jpg)

### Abrom Douglas III

Abrom is a Senior Solutions Architect within AWS Identity and has over 19 years of software engineering and security experience, specializing in the identity and access management (IAM) space. He loves speaking with customers about how IAM can provide secure outcomes that enable both business and technology goals. In his free time, he enjoys cheering for Arsenal FC, photography, travel, and competing in duathlons.

![Nisha Notani](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/01/06/Nisha-Notani.jpg)

### Nisha Notani

Nisha is a Senior Technical Account Manager for AWS in London, working closely with enterprise customers to accelerate their cloud journey through strategic guidance and technical expertise. She helps organizations build cloud maturity across the AWS Well-Architected pillars, with a focus on operational excellence, observability, and reliability. As an active member of the cloud financial management community, she supports customers in implementing FinOps best practices and cost optimization strategies across their organizations. A passionate mentor, she guides colleagues in their professional development, serves on the AWS Support Give Back program core team to promote volunteering, and actively mentors students in local schools and colleges, providing guidance on their career journeys.

TAGS: [Amazon API Gateway](https://aws.amazon.com/blogs/security/tag/amazon-api-gateway/), [Amazon Cognito](https://aws.amazon.com/blogs/security/tag/amazon-cognito/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/)

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