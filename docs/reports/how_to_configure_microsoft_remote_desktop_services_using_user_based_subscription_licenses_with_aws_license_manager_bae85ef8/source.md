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

## [Microsoft Workloads on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/)

# How to configure Microsoft Remote Desktop Services using user-based subscription licenses with AWS License Manager

by Chase Lindeman and Mingruo Qu on 27 JAN 2025 in [Amazon EC2](https://aws.amazon.com/blogs/modernizing-with-aws/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [AWS License Manager](https://aws.amazon.com/blogs/modernizing-with-aws/category/management-tools/aws-license-manager/ "View all posts in AWS License Manager"), [Technical How-to](https://aws.amazon.com/blogs/modernizing-with-aws/category/post-types/technical-how-to/ "View all posts in Technical How-to"), [Windows on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/category/aws-on-windows/ "View all posts in Windows on AWS") [Permalink](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-configure-microsoft-remote-desktop-services-using-user-based-subscription-licenses-with-aws-license-manager/) Share

Amazon Web Services (AWS) recently announced the general availability of AWS provided Subscriber Access Licenses (SAL) for Microsoft Remote Desktop Services (RDS). In this blog post we are going to show you how [AWS License Manager](https://aws.amazon.com/license-manager/) is used to provide subscription licenses for Microsoft RDS running on Amazon Elastic Compute Cloud (EC2).

## What is Microsoft Remote Desktop Services?

Microsoft RDS provides a session-based Windows Server virtual desktop environment, primarily used for GUI applications which must run inside a Windows Server session. By default, Windows Server allows two free remote connections for administrative purposes. If more than two sessions are needed on the same server then [Remote Desktop Services roles](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-roles) must be installed and additional licensing is necessary.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Picture1-4.png)

*Figure 1. Microsoft RDS role options in Windows Server*

Depending on the size and complexity of your Remote Desktop Services environment, there are multiple Microsoft RDS roles which can be used. At a minimum, you must have a Remote Desktop Session Host (RD Session Host) and a Remote Desktop Licensing (RD Licensing) server. The RD Session Host role allows multiple sessions on the same Windows Server, while the RD Licensing server manages the licenses for the user sessions. When using AWS License Manager to provide SALs for Microsoft RDS, new AWS-managed RD Licensing servers will be created.

## Why should I use AWS SALs for Microsoft RDS?

**Licensing flexibility**: Previously, Microsoft RDS could only be brought to AWS using a Bring-Your-Own-License (BYOL) model, which required maintaining active Software Assurance on Remote Desktop User Client Access Licenses (CALs) or by claiming Microsoft RDS SALs on your Services Provider Licensing Agreement (SPLA). However, [Microsoft announced](https://partner.microsoft.com/en-US/blog/article/new-licensing-benefits-make-bringing-workloads-and-licenses-to-partners-clouds-easier/) they will no longer allow SPLA licenses to be brought to Listed Providers after September 30, 2025. Using AWS SALs provides an alternative to maintaining active Software Assurance on RDS CALs, as well as ensuring business continuity for companies currently claiming Microsoft RDS SALs on their SPLA.

**No prerequisite of using AWS Managed Microsoft Active Directory**: AWS License Manager provides a managed RD Licensing server that reduces your need to manage the licensing server infrastructure. The managed RD Licensing server integrates directly with your AWS Managed Microsoft Active Directory or your self-managed Active Directory. This means you do not have to change your current Microsoft RDS architecture to use AWS-provided SALs; you just need to point your RD Session Hosts to the AWS RD Licensing servers. You also have the ability to register multiple Active Directories under one AWS account.

**Allow more than two concurrent user sessions:** Customers can use Microsoft RDS to allow more than two concurrent user sessions on Windows Server EC2 instances. This feature can also be used on AWS license-included Microsoft Visual Studio on EC2 and/or Microsoft Office on EC2.

**Scalability:** AWS provided licenses for Microsoft RDS are billed on a per-user, per-month basis. With this pay-as-you-go model, you can increase or decrease your licensing usage based on your monthly demand.

Let’s review the steps necessary to run Microsoft RDS with AWS SALs using AWS License Manager.

## Prerequisites

**Active Directory:** During the provisioning process, AWS License Manager will need to link to an existing Active Directory domain. Both AWS Managed Microsoft Active Directory and self-managed Active Directory options are supported. While AWS Managed Microsoft Active Directory is not required as a prerequisite for deploying AWS SALs for Microsoft RDS, it is a requirement if you want to use other user-based subscriptions such as Visual Studio and Microsoft Office.

If you would like to use an AWS Managed Microsoft Active Directory and don’t already have one configured, use the following links for more information on [AWS Managed Microsoft AD prerequisites](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started.html#ms_ad_getting_started_prereqs) and [how-to Create your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started.html#ms_ad_getting_started_create_directory) directory in the *AWS Directory Service User Guide*.

**Service Account:** AWS License Manager will need a user account inside your Active Directory domain to be used for joining the managed RD Licensing server to your domain. This service account is necessary for both Self-managed Active Directory and AWS Managed Microsoft Active Directory. AWS License Manager will reference the service account using credentials stored in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

1. Sign in to the AWS Management Console and open [AWS Secrets Manager](https://console.aws.amazon.com/secretsmanager/).

2. Click **Store a new secret**.

3. For Secret type, choose **Other type of secret**.

4. In the Key/value pairs section click **+ Add row**.

5. For the first key enter `username`, for the value enter the account’s name.

6. For the second key enter `password`, for the value enter the account’s password.

7. Click **Next** to proceed to the Configure Secret page.

8. Add a secret name with the prefix `license-manager-user-`

**![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Picture2-3.png)**

**Figure 2. Service account Secret name in AWS Secrets Manager**

9. Then click **next**, then **next**, then **Store**.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure3-2.png)

*Figure 3. Service account credentials in AWS Secrets Manager*

## Walkthrough

### Subscribe to Windows Remote Desktop Services SAL in AWS Marketplace

1. Sign in to the AWS Management Console and open the [AWS License Manager console](https://console.aws.amazon.com/license-manager/).

2. Under User-based subscriptions, click **Products**. If you’re viewing this page for the first time, you’ll be asked to create a service link role. Check the box, then click **Create**.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure4-1.png)

*Figure 4. Agree to create a service-linked role for User-based subscriptions*

3. In the right pane, click **Remote Desktop Services SAL**.

4. From the product details page, click **View in AWS Marketplace**.

5. Review the AWS Marketplace details, then click **View purchase options**, and then **Subscribe**.

6. Refresh the AWS License Manager User-based subscriptions: Products page. It should now show Remote Desktop Services SAL as **Active** under the Marketplace subscription status column.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure5-1.png)

*Figure 5. Active Marketplace subscription for Remote Desktop Services SAL.*

### Register Active Directory

1. From the User-based subscriptions: Products page, click **Remote Desktop Services SAL**.

2. Under Getting Started, click **Register Active Directory**.

3. You now have the option to choose an AWS Managed Active Directory or self-managed Active Directory

##### **AWS Managed Active Directory**

i. Click the drop down to **Choose an AWS Managed Microsoft AD,** then select your directory.

ii. Click **Add**.

##### Self-managed Active Directory

i. Under AWS Active Directory, add your fully qualified domain name.

ii. For the IPv4 addresses, add the IP addresses for two domain controllers.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure6-1.png)

*Figure 6. Example domain configuration when using self-managed Active Directory*

iii. Select the VPC containing your domain controllers.

iv. Select the subnets containing your domain controllers.

v. Under Secret, select the secret created in the *prerequisites* section.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure7.png)

*Figure 7. Example networking configuration when using self-managed Active Directory*

vi. At the bottom of the page, select **Register**.

### Configure Microsoft RDS Licensing Server

1. From the User-based subscriptions: Products page, click **Remote Desktop Services SAL**.
2. Under Getting Started, click **Configure RDS License Server**.
3. Under Secret, select the Secret created during the *prerequisites* section.
4. Click **Configure**.

Once the Microsoft RDS Licensing Server provisioning is complete you will be able to view the License Server endpoint and IP addresses under the Active Directory information on the Remote Desktop Services SAL page. This information will be referenced when configuring the RD Session Hosts.

### Subscribe Users

1. From the User-based subscriptions: Products page, click **Remote Desktop Services SAL**.
2. Under Getting Started, click **Subscribe Users**.
3. Select the **Active Directory domain** containing the users you want to subscribe.
4. Enter each user’s login name.
   * Optional: If the user is part of a sub domain, enter the fully qualified domain name.
5. Click **Next**.
6. Click **Subscribe**.

### Configure RD Session Host(s)

RD Session Hosts will need to be configured with the endpoint of the managed Microsoft RDS Licensing Servers. This configuration can be specified during the provisioning of the RD Session Hosts or can be set with Group Policy. Refer to Microsoft’s documentation [Configure licensing for an RDS deployment that includes only the RD Session Host role and the RD Licensing role](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-license-session-hosts#configure-licensing-for-an-rds-deployment-that-includes-only-the-rd-session-host-role-and-the-rd-licensing-role) for step-by-step instructions.

Alternatively, the Microsoft RDS Licensing Servers can also be referenced by the Server IPs. The Microsoft RDS Licensing Server endpoint and Server IP addresses can be viewed under the Active Directory information section of the Remote Desktop Services SAL page.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure8.png)

*Figure 8. Managed RDS Licensing Server endpoint and Server IP addresses*

Once the Microsoft RDS License Server endpoint has been configured, you can verify your configuration using the Microsoft RD Licensing Diagnoser tool. RD Licensing Diagnoser will provide configuration details on your current RD License Server endpoint, the number of licenses you have available for clients, and verification your licensing mode is set to Per User.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure9.png)

*Figure 9. Microsoft RD Licensing Diagnoser configuration details*

Your RD Session Host should now be able to bypass the default 2 user session limitation. Task Manager can be used to view each user session’s resource consumption details by using the Users tab.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure10.png)

*Figure 10. Task Manager user resource consumption details.*

## Rollback Options

#### Unsubscribing Users

1. From the User-based subscriptions: Products page, click **Remote Desktop Services SAL**.

2. Choose your Active Directory from the dropdown to populate user information.

3. Choose one or more user accounts, then click **Unsubscribe users**.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure11.png)

*Figure 11. Check the box for the user account, then click Unsubscribe users.*

4. Type `unsubscribe` in the box to confirm, then click **Unsubscribe**.

5. Verify the user account status has changed to *Unsubscribed*.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure12.png)

*Figure 12. User accounts will display as Unsubscribed.*

Note: Billing is based on license tokens associated with user accounts in Active Directory which have a 90-day expiration. If you need to stop billing for a user immediately, you need to both unsubscribe this user in AWS License Manager, as well as remove this user from your Active Directory.

#### Deregister Active Directory

Before an Active Directory can be deregistered, all user accounts must be unsubscribed.

1. From the User-based subscriptions: Products page, click **Remote Desktop Services SAL**.
2. Choose your Active Directory from the dropdown, the click **View in Settings**.
3. Select your Active Directory by the **Active Directory ID** to view details.
4. Click **Deregister Active Directory**.
5. The Active Directory status will now display as *Deregistered*.

![](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/24/Figure13.png)

*Figure 13. Active Directory status will display as Deregistered.*

## Conclusion

In this blog, we have reviewed the AWS provided licenses for Microsoft Remote Desktop Services. For companies who use Windows Server on Amazon EC2 to run their Microsoft RDS applications, AWS provides a flexible option for purchasing per-user subscription licensing for Microsoft RDS from the AWS Marketplace, as well as licensing management of those subscriptions using AWS License Manager. To get started, visit <https://aws.amazon.com/license-manager/>.

---

AWS has significantly more services, and more features within those services, than any other cloud provider, making it faster, easier, and more cost effective to move your existing applications to the cloud and build nearly anything you can imagine. Give your Microsoft applications the infrastructure they need to drive the business outcomes you want. Visit our [.NET on AWS](https://aws.amazon.com/blogs/dotnet/) and [AWS Database](https://aws.amazon.com/blogs/database/) blogs for additional guidance and options for your Microsoft workloads. [Contact us](https://pages.awscloud.com/MAP-windows-contact-us.html) to start your migration and modernization journey today.

TAGS: [Amazon EC2](https://aws.amazon.com/blogs/modernizing-with-aws/tag/amazon-ec2/), [AWS License Manager](https://aws.amazon.com/blogs/modernizing-with-aws/tag/aws-license-manager/), [AWS Managed Microsoft AD](https://aws.amazon.com/blogs/modernizing-with-aws/tag/aws-managed-microsoft-ad/), [Microsoft](https://aws.amazon.com/blogs/modernizing-with-aws/tag/microsoft/), [Windows On AWS](https://aws.amazon.com/blogs/modernizing-with-aws/tag/windows-on-aws/), [Windows Server](https://aws.amazon.com/blogs/modernizing-with-aws/tag/windows-server/)

![Chase Lindeman](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2022/10/25/badge.png)

### Chase Lindeman

Chase Lindeman is a Senior Specialist Solutions Architect at Amazon Web Services with over 20 years of experience working with Microsoft technologies. He has expertise in running Microsoft workloads on AWS with specialization in migrations, cost optimization, and infrastructure architecture.

![Mingruo Qu](https://d2908q01vomqb2.cloudfront.net/8effee409c625e1a2d8f5033631840e6ce1dcb64/2025/01/25/image-16.png)

### Mingruo Qu

Mingruo Qu is a Senior Technical Product Manager for AWS Migrations and Modernizations. At AWS, Mingruo focuses on overall AWS License Manager, user-based subscription licenses, and generative-AI powered licensing assessment and optimization and transformation of software workloads.

### Resources

* [Windows on AWS](https://aws.amazon.com/windows/)
* [SQL Server on AWS](https://aws.amazon.com/sql)
* [.NET on AWS](https://aws.amazon.com/developer/language/net/)
* [Modernize Windows Workloads with AWS](https://aws.amazon.com/windows/modernization/)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [RSS Feed](http://feeds.feedburner.com/AmazonWebServicesBlog)
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