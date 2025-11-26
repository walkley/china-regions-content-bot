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

# AWS Certificate Manager introduces exportable public SSL/TLS certificates to use anywhere

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 17 JUN 2025 in [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [AWS Certificate Manager](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/aws-certificate-manager/ "View all posts in AWS Certificate Manager"), [AWS re:Inforce](https://aws.amazon.com/blogs/aws/category/events/aws-reinforce/ "View all posts in AWS re:Inforce"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/aws/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance") [Permalink](https://aws.amazon.com/blogs/aws/aws-certificate-manager-introduces-exportable-public-ssl-tls-certificates-to-use-anywhere/)  [Comments](https://aws.amazon.com/blogs/aws/aws-certificate-manager-introduces-exportable-public-ssl-tls-certificates-to-use-anywhere/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing exportable public SSL/TLS certificates from [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). Prior to this launch, you can [issue your public certificates](https://docs.aws.amazon.com/acm/latest/userguide/acm-public-certificates.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) or [import certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) issued by third-party certificate authorities (CAs) at no additional cost, and deploy them with integrated AWS services such as [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), [Amazon CloudFront](https://aws.amazon.com/cloudfront/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) distribution, and [Amazon API Gateway](https://aws.amazon.com/api-gateway/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

Now you can export public certificates from ACM, get access to the private keys, and use them on any workloads running on [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) instances, containers, or on-premises hosts. The exportable public certificate are valid for 395 days. There is a charge at time of issuance, and again at time of renewal. Public certificates exported from ACM are issued by [Amazon Trust Services](https://www.amazontrust.com/repository/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and are widely trusted by commonly used platforms such as Apple and Microsoft and popular web browsers such as Google Chrome and Mozilla Firefox.

**ACM exportable public certificates in action**

To export a public certificate, you first request a new exportable public certificate. You cannot export previously created public certificates.

To get started, choose **Request certificate** in the [ACM console](https://console.aws.amazon.com/acm/home#/certificates/request&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and choose **Enable export** in the **Allow export** section. If you select **Disable export**, the private key for this certificate will be disallowed for exporting from ACM and this cannot be changed after certificate issuance.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/12/2025-acm-exportable-certificates-1-create.jpg)

You can also use the `request-certificate` command to request a public exportable certificate with `Export=ENABLED` option on the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el).

```
aws acm request-certificate \
--domain-name mydomain.com \
--key-algorithm EC_Prime256v1 \
--validation-method DNS \
--idempotency-token <token> \
--options \
CertificateTransparencyLoggingPreference=DISABLED \
Export=ENABLED
```

After you request the public certificate, you must validate your domain name to prove that you own or control the domain for which you are requesting the certificate. The certificate is typically issued within seconds after successful domain validation.

When the certificate enters status **Issued**, you can export your issued public certificate by choosing **Export**.

![Export your public certificate](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/08/2025-acm-exportable-certificates-2-export.jpg)

Enter a passphrase for encrypting the private key. You will need the passphrase later to decrypt the private key. To get the public key, Choose **Generate PEM Encoding**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/16/2025-acm-exportable-certificates-3-export.png)

You can copy the PEM encoded certificate, certificate chain, and private key or download each to a separate file.

![Download PEM keys](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/08/2025-acm-exportable-certificates-4-download-PEM-keys.jpg)

You can use the `export-certificate` command to export a public certificate and private key. For added security, use a file editor to store your passphrase and output keys to a file to prevent being stored in the command history.

```
aws acm export-certificate \
     --certificate-arn arn:aws:acm:us-east-1:<accountID>:certificate/<certificateID> \
     --passphrase fileb://path-to-passphrase-file \
     | jq -r '"\(.Certificate)\(.CertificateChain)\(.PrivateKey)"' \
     > /tmp/export.txt
```

You can now use the exported public certificates for any workload that requires SSL/TLS communication such as Amazon EC2 instances. To learn more, visit [Configure SSL/TLS on Amazon Linux](https://docs.aws.amazon.com/linux/al2/ug/SSL-on-amazon-linux-2.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in your EC2 instances.

**Things to know**

Here are a couple of things to know about exportable public certificates:

* **Key security** – An administrator of your organization can set AWS IAM policies to authorize roles and users who can request exportable public certificates. ACM users who have current rights to issue a certificate will automatically get rights to issue an exportable certificate. ACM admins can also manage the certificates and take actions such as revoking or deleting the certificates. You should protect exported private keys using secure storage and access controls.
* **Revocation** – You may need to revoke exportable public certificates to comply with your organization’s policies or mitigate key compromise. You can only revoke the certificates that were previously exported. The certificate revocation process is global and permanent. Once revoked, you can’t retrieve revoked certificates to reuse. To learn more, visit [Revoke a public certificate](http://docs.aws.amazon.com/acm/latest/userguide/revoke-certificate.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the AWS documentation.
* **Renewal** – You can configure automatic renewal events for exportable public certificates by [Amazon EventBridge](https://aws.amazon.com/eventbridge/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to monitor certificate renewals and create automation to handle certificate deployment when renewals occur. To learn more, visit [Using Amazon EventBridge](https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-events.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the AWS documentation. You can also renew these certificates on-demand. When you renew the certificates, you’re charged for a new certificate issuance. To learn more, visit [Force certificate renewal](http://docs.aws.amazon.com/acm/latest/userguide/force-certificate-renewal.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the AWS documentation.

**Now available**

You can now issue exportable public certificates from ACM and export the certificate with the private keys to use other compute workloads as well as ELB, Amazon CloudFront, and Amazon API Gateway.

You are subject to additional charges for an exportable public certificate when you create it with ACM. It costs $15 per fully qualified domain name and $149 per wildcard domain name. You only pay once during the lifetime of the certificate and will be charged again only when the certificate renews. To learn more, visit the [AWS Certificate Manager Service Pricing](https://aws.amazon.com/certificate-manager/pricing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) page.

Give ACM exportable public certificates a try in the [ACM console](https://console.aws.amazon.com/acm/home#/certificates/request&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). To learn more, visit the [ACM Documentation page](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and send feedback to [AWS re:Post for ACM](https://repost.aws/tags/TAJ7zd4vjzSfC_8JNlsbq2tA/aws-certificate-manager) or through your usual AWS Support contacts.

— [Channy](https://twitter.com/channyun)

![Channy Yun (윤석찬)](https://d2908q01vomqb2.cloudfront.net/7b52009b64fd0a2a49e6d8a939753077792b0554/2020/06/05/channyun_400x400.jpg)

### [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)")

Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.

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