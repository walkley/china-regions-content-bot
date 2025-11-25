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

# Should I use managed login or create a custom UI in Amazon Cognito?

by Joshua Du Lac, Edward Sun, Jeremy Ware, and Kiran Dongara on 08 OCT 2025 in [Amazon Cognito](https://aws.amazon.com/blogs/security/category/security-identity-compliance/amazon-cognito/ "View all posts in Amazon Cognito"), [Best Practices](https://aws.amazon.com/blogs/security/category/post-types/best-practices/ "View all posts in Best Practices"), [Intermediate (200)](https://aws.amazon.com/blogs/security/category/learning-levels/intermediate-200/ "View all posts in Intermediate (200)"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/security/use-the-hosted-ui-or-create-a-custom-ui-in-amazon-cognito/)  [Comments](https://aws.amazon.com/blogs/security/use-the-hosted-ui-or-create-a-custom-ui-in-amazon-cognito/#Comments)  Share

> **October 8, 2025:** This blog post has been updated to include the Amazon Cognito managed login experience. The managed login experience has an updated look, additional features, and enhanced customization options.

> **September 8, 2023:** It’s important to know that if you activate user sign-up in your user pool, anyone on the internet can sign up for an account and sign in to your apps. Don’t enable self-registration in your user pool unless you want to open your app to allow users to sign up.

> **June 9, 2023:** Original publication date.

---

[Amazon Cognito](https://aws.amazon.com/cognito/) is an authentication, authorization, and user management service for your web and mobile applications. Your users can sign in directly through many different authentication methods, such as user accounts within Amazon Cognito or through social providers such as Facebook, Amazon, Apple, or Google. You can also configure federation through a third-party [OpenID Connect (OIDC)](https://openid.net/connect/) or SAML 2.0 identity provider (IdP).

[Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) are user directories that provide sign-up and sign-in functions for your application users, including federated authentication capabilities. A Cognito user pool has two primary UI options:

* **Managed login**: AWS hosts, preconfigures, maintains, and scales the UI—including [managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html) branding and classic Hosted UI branding—with a set of options that you can customize or configure for sign-up and sign-in for app users.
* **Custom UI**: You can configure an Amazon Cognito user pool with a completely custom UI by using the [SDK](https://aws.amazon.com/cognito/dev-resources/). You’re accountable for hosting, configuring, maintaining, and scaling your custom UI as a part of your responsibility in the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

In this blog post, we review the benefits of using the managed login or creating a custom UI with the SDK and things to consider in determining which to choose for your application.

## Managed login

Managed login provides web interfaces for sign-up, sign-in, multi-factor authentication (MFA), password management, and passwordless and passkey sign-in capabilities in your user pool. The managed login provides an authorization server based on the OAuth 2.0 specification, and has a default implementation of user flows for sign-up and sign-in. Your application can redirect to the managed login, which will handle the user flows through the [authorization code grant flow](https://www.rfc-editor.org/rfc/rfc6749#page-24). The managed login also supports sign-in through social providers and federation from OIDC-compliant and SAML 2.0 providers. Amazon Cognito offers two visual modes and branding and customization experiences: managed login branding with branding editor and hosted UI (classic) branding.

**Managed login branding with branding editor**

Managed login branding provides an improved user experience with the most up-to-date authentication options for the user pool UI experience. Figure 1 shows managed login using the default branding settings.

![Figure 1: Managed login default branding settings](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-1.png)

Figure 1: Managed login default branding settings

The branding editor is a no-code visual editor that you can use to customize the look and feel of the entire user journey. You can customize each user pool application client individually, and preview screens in real-time with different screen sizes, as shown in Figure 2.

![Figure 2: Customization in the Amazon Cognito branding editor (Image credits)](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-2.png)

Figure 2: Customization in the Amazon Cognito branding editor ([Image credits](https://stock.adobe.com/images/jumping-puppy-on-a-light-background-advertising-banner-template-for-pet-store-or-veterinary-clinic/854028815?prev_url=detail))

As shown in Figure 3, You can customize various components using the branding editor, including background, header and footer, buttons, focus state, icons, and more.

![Figure 3: Various components customization options](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-3.png)

Figure 3: Various components customization options

Additionally, managed login branding adds support for passwordless sign-in with passkeys, email one-time-passwords (OTP) and SMS OTPs, as shown in Figure 4. After you enable passwordless login in your user pool, managed login branding adapts to curated user flows with users’ preferred authentication methods.

![Figure 4: Sign in with passkey flow (left) and user-selected sign-in method flow (right)](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-4.png)

Figure 4: Sign in with passkey flow (left) and user-selected sign-in method flow (right)

Managed login branding also offers localization options in [several languages](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-localization) (two are shown in Figure 5). You can add a `lang` query parameter in the link you distribute to users, and Amazon Cognito will set a cookie in users’ browsers with their language preference after the initial request.

![Figure 5: Cognito user sign up page in Japanese (left) and user sign in page in Simplified Chinese (right)](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-5.png)

Figure 5: Cognito user sign up page in Japanese (left) and user sign in page in Simplified Chinese (right)

**Hosted UI (classic) branding**

For customers who prefer a traditional approach, Amazon Cognito continues to support the Hosted UI (classic) branding (shown in Figure 6) with basic customization where you can upload a CSS file to design the UI styling and upload a brand-specific logo. Hosted UI (classic) supports standard authentication flows with MFA and self-service sign up.

![Figure 6: Hosted UI (classic) branding](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-6.png)

Figure 6: Hosted UI (classic) branding

The managed login branding with branding editor is available to Amazon Cognito user pools with Essentials and Plus feature tiers, and Hosted UI (classic) branding is available to most Cognito user pools including Lite tier. To learn more about Cognito feature tiers, visit [Amazon Cognito pricing](https://aws.amazon.com/cognito/pricing/).

**Security and compliance capabilities**

Both managed login branding and Hosted UI (classic) branding are designed to help you meet your compliance and security requirements and your users’ needs. Managed login supports custom OAuth scopes and OAuth 2.0 flows. If you want single sign-on (SSO), you can use managed login to support a single login across many application clients, with browser session cookies for the same domain. Actions are logged in [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), and you can use the logs for audit and reactionary automation. The managed login experience also supports the full suite of [threat protection](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html) features for Amazon Cognito. For additional protection, managed login has support for [AWS WAF web ACLs](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html) and for [AWS WAF CAPTCHA](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge.html), which can help protect your Cognito user pools from web-based exploits and unwanted bots.

![Figure 7: Example default managed login with several login providers enabled](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-7.png)

Figure 7: Example default managed login with several login providers enabled

For federation, managed loginsupports federation with third-party IdPs that support OIDC and SAML 2.0, as well as social IdPs, as shown in Figure 7. Identity providers are connected to your Amazon Cognito user pool. In managed login, users use a button to select the federation source, and redirection is automatic. With SAML and OIDC IdPs, you can also configure mapping by using the domain in the user’s email address. In this case, a single text field is visible to your application users to enter an email address, as shown in Figure 8, and the lookup and redirect to the appropriate SAML IdP is automatic, as described in [Choosing SAML identity provider names](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managing-saml-idp-naming.html).

![Figure 8: Managed login that links to corporate IdP through an email domain](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-8.png)

Figure 8: Managed login that links to corporate IdP through an email domain

Managed login integrates with [Application Load Balancer (ALB)](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) for web applications and works with [AWS Amplify](https://aws.amazon.com/amplify/) to enable social identity provider and enterprise federation (SAML and OIDC) capabilities. Beyond these integrations, Amazon Cognito user pools integrate with various AWS services (such as [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html)), that require user authentication and authorization, and [Amazon API Gateway](https://aws.amazon.com/api-gateway/) through [Cognito authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) to secure your REST and HTTP endpoints.

You might choose to use managed login for many reasons. AWS fully manages the hosting, maintenance, and scaling of the managed login, which can contribute to the speed of go-to-market for customers. If your app requires OAuth 2.0 custom scopes, federation, social login, or native users with basic but customized branding and potentially numerous Amazon Cognito user pools, you might benefit from using managed login.

For more information about how to configure and use the hosted UI, see [Using the Amazon Cognito hosted UI for sign-up and sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-app-integration.html).

## Create a custom UI

Creating a custom UI using the SDK for Amazon Cognito provides a host of benefits and features that can help you completely customize the UI for your application users. With a custom UI, you have complete control over the look and feel of the UI that your application users will land on, including designing your app to support multiple languages, and you can build and design custom authentication flows.

There are numerous features that are supported when you build a custom UI. As with the managed login, the [APIs invoked](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_Operations.html) from a custom UI using the [SDK](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-integrate-apps.html) will create log entries in CloudTrail, and you can use the logs for audit and automation. You can also create a custom authentication flow for your users with a fully custom authentication experience beyond the those available in managed login.

In a custom UI, you can build custom session management and integrate with AWS WAF. A custom UI also works with the [threat protection features](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html) of Amazon Cognito.

![Figure 9: Example of a custom user interface](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-9.png)

Figure 9: Example of a custom user interface

With a custom UI, such as the one shown in Figure 10, you can orchestrate a suite of sign-in options and sign-in flows for your users. For example, you can collect a user or tenant identifier at the beginning of the authentication flow and apply your own logic for user authentication flow, such as redirecting federated users to external IdPs, displaying a password prompt for local users, or directing users to create a new account if they don’t exist. You can also build flows to let a user choose alternative MFA methods if their preferred choices aren’t available.

![Figure 10: Custom UI example](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Image-10.png)

Figure 10: Custom UI example

When you build a custom UI, there is support for custom endpoints and proxies so that you have a wider range of options for management and consistency across application development as it relates to authentication. [Custom authentication flows](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html#amazon-cognito-user-pools-custom-authentication-flow) are only available in applications with a custom UI, which gives you the ability to make customized challenge prompts and answers to help you meet custom security requirements by using [AWS Lambda](https://aws.amazon.com/lambda/) triggers. For example, you could use it to implement [OAuth 2.0 device grant flows](https://aws.amazon.com/blogs/security/implement-oauth-2-0-device-grant-flow-by-using-amazon-cognito-and-aws-lambda/). Lastly, a custom UI supports a [remember device](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html) feature where you can add low-effort sign-in from trusted devices.

You might choose to build a custom UI with an SDK when full customization is a requirement or where you want to incorporate customized authentication flows using the custom authentication challenge Lambda triggers. A custom UI is a great choice if you aren’t required to use OAuth 2.0 flows and you have the resources to develop and implement a unique UI for your application users.

For more information about how to configure and use a custom UI, see [Using the Amazon Cognito managed login for sign-up and sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-app-integration.html). You can also visit the documentation on [Building custom UIs with Amplify](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-integrate-apps.html#cognito-integrate-apps-amplify-ui).

## Decision criteria matrix

When deciding between Amazon Cognito managed login branding options and a custom UI, there are some unique differences that can help you determine which UI is best for your application needs. Managed login offers a modern, customizable authentication experience with advanced features like no-code visual customization, dark mode themes, and support for passwordless options. It supports OAuth 2.0 flows, custom OAuth scopes, the ability to sign in one time and access many Cognito application clients (using SSO), and full use of the Cognito threat protection features. For applications requiring complete control over the authentication experience and UX—including custom authentication flows, device fingerprinting, and reduced token expiration—a custom UI is the better choice. This option allows for full UI customization, implementation of custom authentication flows, and integration with specific frameworks or libraries not supported by managed login.

When making your decision, consider factors such as the level of customization required, specific authentication features needed, development resources available, integration requirements with other AWS services, security and compliance needs, and user experience priorities. Remember that your application authentication requirements and customer experience should take precedence over other considerations. You can use the following table to help select the best UI for your requirements.

|  |  |  |  |
| --- | --- | --- | --- |
| **Requirements** | **Managed login** | **Hosted UI (classic)** | **Custom UI (SDK)** |
| **OAuth 2.0 flows** | Supported | Supported | Not available |
| **Custom OAuth scopes** | Supported | Supported | Supported |
| **Customization of UI** | No-code branding designer | Limited CSS customization | Full custom control |
| **Custom user input forms** | Not available | Not available | Supported |
| **Custom authentication flow** | Not available | Not available | Supported |
| **Passwordless authentication flow** | Supported | Not available | Custom implementation available |
| **Localization with multiple languages** | Supported | Not available | Supported |
| **Login once across many app clients** | Supported | Supported | Not available |
| **Session expiration configurable under 1 hour** | Not available | Not available | Supported |
| **Trusted-device authentication** | Not available | Not available | Supported |
| **AWS WAF integration** | Supported | Supported | Supported |
| **Support for AWS WAF CAPTCHA** | Supported | Supported | Not available |
| **Ability to use a custom endpoint or proxy** | Not available | Not available | Supported |
| **AWS Application Load Balancer integration** | Supported | Supported | Not available |

*Figure 11: Decision criteria matrix*

## Conclusion

In this post, you learned about using managed login, including its two branding options and creating a custom UI in Amazon Cognito and the many supported features and benefits of each. Each UI option targets a specific need. Choose from available options based on your list of requirements for authentication and the user sign-up and sign-in experience. You can use the information in this post as a reference as you add Amazon Cognito to your mobile and web applications for authentication.

Have a question? [Contact us](https://aws.amazon.com/contact-us/?nc1=f_m) for general support services.

![Author photo](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2019/06/11/du-lac-bio-photo.jpeg)

### Joshua Du Lac

Josh is a Senior Manager of Security Solutions Architects at AWS. He has advised hundreds of enterprise, global, and financial services customers to accelerate their journey to the cloud while improving their security along the way. Outside of work, Josh enjoys searching for the best tacos in Texas and practicing his handstands.

![Jeremy Wave](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2022/12/08/Jeremy-Ware.jpg)

### Jeremy Ware

Jeremy is a Security Specialist Solutions Architect focused on Identity and Access Management. Jeremy and his team enable AWS customers to implement sophisticated, scalable, and secure IAM architecture and Authentication workflows to solve business challenges. With a background in Security Engineering, Jeremy has spent many years working to raise the Security Maturity gap at numerous global enterprises. Outside of work, Jeremy loves to explore the mountainous outdoors, and participate in sports such as snowboarding, wakeboarding, and dirt bike riding.

![Edward Sun](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2024/01/09/Edward_Sun.jpg)

### Edward Sun

Edward is a Security Specialist Solutions Architect focused on identity and access management. He loves helping customers throughout their cloud transformation journey with architecture design, security best practices, migration, and cost optimizations. Outside of work, Edward enjoys hiking, golfing, and cheering for his alma mater, the Georgia Bulldogs.

![Kiran Dongara](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/10/03/Kiran-Dongara-Author.jpg)

### Kiran Dongara

Kiran Dongara is a Solutions Architect at Amazon Web Services (AWS) in the Worldwide Public Sector, primarily supporting US state and local government (SLG) customers and partners. His expertise lies in designing scalable and efficient architectures that adhere to well-architected framework practices, maximizing value and return on investment for his customers. When not working, Kiran prioritizes family time, nature walks, and cycling.

TAGS: [Amazon Cognito](https://aws.amazon.com/blogs/security/tag/amazon-cognito/), [Identity](https://aws.amazon.com/blogs/security/tag/identity/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/)

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