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

# Implementing just-in-time privileged access to AWS with Microsoft Entra and AWS IAM Identity Center

by Rodney Underkoffler and Aidan Keane on 03 JUN 2025 in [Advanced (300)](https://aws.amazon.com/blogs/security/category/learning-levels/advanced-300/ "View all posts in Advanced (300)"), [AWS IAM Identity Center](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-single-sign-on-sso/ "View all posts in AWS IAM Identity Center"), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-identity-and-access-management-iam/ "View all posts in AWS Identity and Access Management (IAM)"), [AWS Management Console](https://aws.amazon.com/blogs/security/category/management-tools/aws-management-console/ "View all posts in AWS Management Console"), [Security, Identity, & Compliance](https://aws.amazon.com/blogs/security/category/security-identity-compliance/ "View all posts in Security, Identity, & Compliance"), [Technical How-to](https://aws.amazon.com/blogs/security/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/security/implementing-just-in-time-privileged-access-to-aws-with-microsoft-entra-and-aws-iam-identity-center/)  [Comments](https://aws.amazon.com/blogs/security/implementing-just-in-time-privileged-access-to-aws-with-microsoft-entra-and-aws-iam-identity-center/#Comments)  Share

> **June 19, 2025**: We made a correction to the windows of access that a user could have when using this solution.

---

Controlling access to your privileged and sensitive resources is critical for all AWS customers. Preventing direct human interaction with services and systems through automation is the primary means of accomplishing this. For those infrequent times when automation is not yet possible or implemented, providing a secure method for temporary elevated access is the next best option. In a privileged access management solution, there are several elements that should be included:

* User access should follow the principle of least privileged
* Users should be granted only the minimum amount of access required to perform their job duties
* Access granted should persist only for the time necessary to perform the assigned tasks
* The solution should include:
  + An eligibility process for granting access
  + An approval process for granting access
  + Auditing of the access grants and activities taken

Entra Privileged Identity Management (PIM) is a third-party solution that provides dynamic group management, access control, and audit capabilities that integrate with [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center).

In this post, we show you how to configure just-in-time access to AWS using Entra PIM’s integration with IAM Identity Center.

## Just-in-time privileged access with Entra PIM and IAM Identity Center

Privileged Identity Management is a Microsoft Entra ID feature that enables management, control, and access monitoring of your important cloud resources. There are many different configuration options when it comes to eligibility and assignment to privileged security groups, including time-bound access with start and end dates, multi-factor authentication (MFA) enforcement, justification tracking, and so on. You can read more about those options in [Microsoft’s product documentation](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure).

Figure 1 shows the just-in-time access solution powered by Entra PIM group activation requests. In this solution, Entra PIM is integrated with IAM Identity Center to provide temporary, limited access to AWS resources based on user requests and approvals. Entra ID users can submit requests for specific access to specific AWS permissions sets, which are then automatically granted for a set duration.

![Figure 1 – Entra PIM solution integrated with IAM Identity Center](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/28/Just-in-time-privileged-access-1.png)

Figure 1 – Entra PIM solution integrated with IAM Identity Center

## Prerequisites

To try the solution described in this post, you need to have the following in place:

* An AWS account with an organization instance of IAM Identity Center enabled. For more information, see [What is IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/step1.html).
* An Azure account subscription with Entra ID P1 or P2 licensing.
* Entra ID as an external identity provider (IdP) for IAM Identity Center as described in [Configure SAML and SCIM with Microsoft Entra ID and IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/idp-microsoft-entra.html#step1-entra-microsoft-prep). Follow Steps 1.1, 3.1, 3.2, and 3.3.
* A sample user in Entra ID as described in the step 4.1 of [Step 4: Configure and test your SCIM synchronization](https://docs.aws.amazon.com/singlesignon/latest/userguide/idp-microsoft-entra.html#step4-entra-scim) or use an existing user within Entra ID for testing.
* Automatic provisioning enabled in Entra ID and IAM Identity Center. Follow Steps 4.2 and 4.3 in this [Step 4: Configure and test your SCIM synchronization](https://docs.aws.amazon.com/singlesignon/latest/userguide/idp-microsoft-entra.html#step4-entra-scim).

## Step-by-step configuration

In the following steps, you create configurations to enable Entra PIM for Groups to automatically assign users to groups based on approval criteria. The groups will be Entra ID security groups that use direct assignment. Note that, at the time of this writing, [dynamic groups and groups that you have synchronized from a self-managed Active Directory cannot be used with Microsoft Entra PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups#relationship-between-role-assignable-groups-and-pim-for-groups). While it might be possible to also populate these groups using a third-party synchronization tool, for the purposes of this exercise, we assume that administration is occurring solely within Entra ID.

In the example scenario, the role corresponds to a specific job function within your organization. We use a group called *AWS – Amazon EC2 Admin*, which corresponds to a DevOps on-call site reliability engineer (SRE) lead.

### Step 1: Create a group representing a specific privilege level.

Create a group in Entra ID that represents a specific privilege level that your employees can request for access to the AWS Management Console.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) with your credentials.
2. Select **Groups** and then **All groups**.
3. Choose **New group**.
4. Specify **Security** in the **Group type** dropdown list.
   * In the **Group name** field, enter `AWS - Amazon EC2 Admin`.
   * In the **Group description** field, enter `Amazon EC2 administrator permissions`.
   * Choose **Create**.

### Step 2: Assign access for the group in Entra ID

Now you need to assign the newly created group to your enterprise application.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) with your credentials
2. Select **Applications** and then **Enterprise applications** and select the IAM Identity Center application that you created.
3. Select **Users and groups** from the **Manage** menu group and select **+ Add user/group**.
4. Select the **None selected** option from the **Users and groups** section.
5. Select the **AWS – Amazon EC2 Admin** group checkbox.
6. Choose **Select** and then choose **Assign**.
7. Select **Provisioning** from the **Manage** menu group and begin synchronizing the empty group by selecting the **Start provisioning** option.

When you first enable provisioning, [the initial Microsoft Entra ID sync is triggered immediately. After that, subsequent syncs are triggered every 40 minutes](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/how-provisioning-works), with the exact frequency depending on the number of users and groups in the application.

When the initial sync completes, the AWS – Amazon EC2 Admin group will be ready for configuration in IAM Identity Center.

### Step 3: Create permission sets in IAM Identity Center

As you prepare to configure your permission set, let’s consider session duration from both the AWS and Entra PIM perspectives. There are two session durations on the AWS side: AWS access portal session duration and permission set session duration. The AWS access portal session duration defines the maximum length of time that a user can be signed in to the AWS access portal without reauthenticating. The default session duration is 8 hours but can be configured anywhere between 15 minutes and 7 days.

> **Note:** Entra does not pass the [SessionNotOnOrAfter](https://docs.aws.amazon.com/singlesignon/latest/userguide/configure-user-session.html) attribute to IAM Identity Center as part of the SAML assertion. Meaning the duration of the AWS access portal session is controlled by the duration set in IAM Identity Center.

The session duration defined within a permission set specifies the length of time that a user can have a session for an AWS account. The default and minimum value is 1 hour (with a maximum value of 12). Entra PIM allows you to configure an *activation* *maximum duration*. The activation maximum duration is the length of time that the specified group will contain the activated user account. The activation maximum duration has a default value of 8 hours but can be configured between 30 minutes and 24 hours.

You should carefully consider the values that you provide for each of these durations. The AWS access portal will display permission sets that the user had access to at the time that they signed in for the duration of the active AWS access portal session.

When you set the permission set session duration, you need to keep in mind that active sessions are not terminated when the Entra PIM activation maximum duration has been reached. Let’s look at an example:

* AWS access portal session duration: default (8 hours)
* Session duration defined in the permission set: 1 hour
* Entra PIM group activation maximum duration: 1 hour

You might be inclined to think that an hour after being added to the group in Entra, the user would no longer have access to AWS resources. This is not necessarily the case. Even after the Entra PIM group activation period expires, [it can take up to 30 minutes for the user to lose access to applications, and in some cases, it can take up to an hour](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html#sessionsconcept). Additionally, their session would remain active for the duration of the session setting defined in the permission set, which is one hour in this case. In the example shown in Figure 2, we have a potential window of access of up to three hours.

![Figure 2 – Calculating session duration](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/06/19/Picture1-11.png)

Figure 2 – Calculating session duration

> **Note**: In most situations, Entra ID group membership changes will be synchronized to IAM Identity Center within 2–10 minutes but can revert to the standard 40-minute interval if activity runs up against Entra PIM throttling limits.

With this in mind, configure your test environment with the default setting of 8 hours for the AWS access portal and 1 hour for the permission set session duration value.

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).
2. Under **Multi-account permissions**, choose **Permission sets**.
3. Choose **Create permission set**.
4. On the **Select permission set type** page, under **Permission set type**, select **Custom permission set**, and then choose **Next**.
5. On the **Specify policies and permissions boundary** page, expand **AWS managed policies**.
6. Search for and select **AmazonEC2FullAccess** policy, and then choose **Next**.
7. On the **Specify permission set details** page, enter `EC2AdminAccess` for the **Permission set name** and choose **Next**.
8. On the **Review and create** page, review the selections, and choose **Create**.

### Step 4: Assign group access in your organization

At this point, you’re ready to assign the Microsoft Entra group to the corresponding permission set in IAM Identity Center. This allows users who are members of the group to be granted the appropriate access level in AWS.

1. In the navigation pane, under **Multi-account permissions**, choose **AWS accounts**.
2. On the **AWS accounts** page, select the check box next to one or more AWS accounts to which you want to assign access.
3. Choose **Assign users or groups**.
4. On the **Groups** tab, select **AWS – Amazon EC2 Admin** and choose **Next**
5. On the **Assign permission sets to *“<AWS-account-name>”*** page, select the **EC2AdminAccess** permission set.
6. Check that the correct permission set was selected and choose **Next**.
7. On the **Review and submit** page, verify that the correct group and permission set are selected, and choose **Submit**.

### Step 5: Configure Entra PIM

To use this Microsoft Entra group with Entra PIM, you bring the group under the management of PIM by using the Entra admin console to activate the group. You can read more about group management with PIM in the [Microsoft documentation](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-discover-groups). Begin by activating the Entra group that you created.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) with your credentials.
2. Select **Groups** and then **All groups**
3. Select the **AWS – Amazon EC2 Admin** group.

   ![Figure 3 – Selecting groups for PIM enablement](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/28/Just-in-time-privileged-access-3.png)

   Figure 3 – Selecting groups for PIM enablement
4. Select **Privileged Identity Management** under the **Activity** menu list.
5. Choose **Enable PIM for this group**.

   ![Figure 4 – Enable PIM for this group](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/28/Just-in-time-privileged-access-4.png)

   Figure 4 – Enable PIM for this group

Now, you will configure the [PIM settings](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-role-settings) for the group. These settings define *Member* or *Owner* properties and requirements. It’s here that you can establish MFA requirements, configure notifications, conditional access, approvals, durations, and so on. The Owner role can elevate their permissions using just-in-time access to manage a group, while the Member role is limited to requesting just-in-time membership within the group. In this example, you use the Member properties to demonstrate group membership level temporary elevated access and set a 1-hour duration for the group assignment.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) with your credentials.
2. Select **Identity Governance**, **Privileged Identity Management**, and then **Groups**.
3. Select the **AWS – Amazon EC2 Admin** group.

   ![Figure 5 – Selecting groups for PIM configuration](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/28/Just-in-time-privileged-access-5.png)

   Figure 5 – Selecting groups for PIM configuration
4. From the **Manage** menu select **Settings**.
5. Choose **Member** to view the default role setting details.

   ![Figure 6 – Settings option for the Member role](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/28/Just-in-time-privileged-access-6.png)

   Figure 6 – Settings option for the Member role
6. Review the default settings. The activation maximum duration should be set to 1 hour and require a justification from the user.
7. Close the **Role setting details – Member** blade.

   ![Figure 7 – Closing the Role setting details – Member blade](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/28/Just-in-time-privileged-access-7.png)

   Figure 7 – Closing the Role setting details – Member blade
8. From the **Manage** menu select **Assignments** and choose **+ Add assignments**.

   ![Figure 8 – Adding eligibility assignments to the PIM enabled groups](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/28/Just-in-time-privileged-access-8.png)

   Figure 8 – Adding eligibility assignments to the PIM enabled groups
9. Select **Member** from the **Select role** dropdown menu and choose **No member selected**. Select the test account, Rich Roe in this example, and then choose **Select**.

   ![Figure 9 – Adding the test user as an eligible identity for PIM activation to the group](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/28/Just-in-time-privileged-access-9.png)

   Figure 9 – Adding the test user as an eligible identity for PIM activation to the group
10. Choose **Next** and leave the default setting of 1 year of eligibility. Duration eligibility defines the period that the user can request activation for the group. Depending on your use case, you will define this as permanent or for a set period. For testing purposes, keep the default setting. Choose **Assign**.

    ![Figure 10 – Completing the eligibility assignment](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/28/Just-in-time-privileged-access-10.png)

    Figure 10 – Completing the eligibility assignment

## Test the configuration

You should now have a test configuration of Entra PIM and IAM Identity Center. Use the test account to verify just-in-time access.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) using the test account (Rich Roe in this example).
2. Select **Identity Governance**, **Privileged Identity Management**, and then **My roles**.

   ![Figure 11 – Browsing to the My Roles section of the Entra admin center](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/29/Just-in-time-privileged-access-11.png)

   Figure 11 – Browsing to the My Roles section of the Entra admin center
3. From the **Activate** menu list, select **Groups**. Your eligible group assignments should be listed.
4. Choose **Activate** for the **AWS – Amazon EC2 Admin** group.

   ![Figure 12 – Activating the just-in-time group membership](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/29/Just-in-time-privileged-access-12.png)

   Figure 12 – Activating the just-in-time group membership
5. In the **Activate – Member** blade, enter a justification for the access request and choose **Activate**.

   ![Figure 13 – Providing a justification for access](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/29/Just-in-time-privileged-access-13.png)

   Figure 13 – Providing a justification for access

In this example, there are no approval workflow processes configured for the group, so Entra validates the eligibility requirements and adds the test account to the AWS – Amazon EC2 Admin group. If you want to dive deeper into the approval workflow process, you can read more about it on the [Configure PIM for Groups settings page](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-role-settings). Because the group is assigned to the enterprise application and configured for provisioning, the updated group membership is automatically synchronized using the SCIM protocol with the connected IAM Identity Center instance. The provisioning time can vary based on the number of PIM enabled users that are activating their memberships within a given 10-second period. In most situations, group memberships are synchronized within 2–10 minutes, but can revert to the standard 40-minute interval if activity runs up against Entra PIM throttling limits. IAM Identity Center responds to SCIM requests as they arrive from Entra ID.

To test access with the newly activated group assignment, use a separate browser or a private window.

1. Sign in to the [My Apps portal](https://myapps.microsoft.com/) with the test user credentials and select the IAM Identity Center app that you created for testing. If you experience an error or don’t see the expected permission set, wait a few minutes until the group membership has synchronized to IAM Identity Center and try again.

   ![Figure 14 – Accessing IAM Identity Center through the My apps portal](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/29/Just-in-time-privileged-access-14.png)

   Figure 14 – Accessing IAM Identity Center through the My apps portal
2. Expand the associated AWS account and confirm the **EC2ReadOnly** permission set has been granted.
3. Close the AWS tab. Wait for the access to be revoked, which has been set to 60 minutes in this example.

   ![Figure 15 – Just-in-time access to the EC2AdminAccess permission set](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/29/Just-in-time-privileged-access-15.png)

   Figure 15 – Just-in-time access to the EC2AdminAccess permission set
4. Sign back in to the [My Apps portal](https://myapps.microsoft.com/) and select the **AWS IAM Identity Center** app. Notice that the **EC2ReadOnly** permission set has been revoked.

## Conclusion

The combination of AWS IAM Identity Center and Entra PIM provides a robust solution for managing just-in-time elevated access to AWS. By using security groups in Entra and mapping them to permission sets in IAM Identity Center, you can automate the provisioning and deprovisioning of privileged access based on defined policies and approval workflows. This approach helps to make sure the principle of least privilege is enforced, with access granted only for the duration required to complete a task. The detailed auditing capabilities of both services also provide comprehensive visibility into privileged access activities.

For AWS customers seeking a comprehensive, secure, and scalable privileged access management solution, the Entra PIM and IAM Identity Center integration is a common option that’s worth investigating to see if it’s a good fit for your use case.

If you have feedback about this post, submit comments in the **Comments** section below. If you have questions about this post, [contact AWS Support](https://console.aws.amazon.com/support/home).

![Rodney Underkoffler](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/05/29/Rodney-Underkoffler.jpg)

### Rodney Underkoffler

Rodney is a Senior Solutions Architect at Amazon Web Services, focused on guiding enterprise customers on their cloud journey. He has a background in infrastructure, security, and IT business practices. He is passionate about technology and enjoys building and exploring new solutions and methodologies.

![Aidan Keane](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2020/09/15/Aidan-Keane-Author.jpg)

### Aidan Keane

Aidan is a Senior Specialist Solutions Architect at Amazon Web Services, focused on Microsoft Workloads. He partners with enterprise customers to optimize their Microsoft environments on AWS and accelerate their cloud journey. Outside of work, he is a sports enthusiast who enjoys golf, biking, and watching Liverpool FC, while also enjoying family time and travelling to Ireland and South America.

TAGS: [AWS IAM](https://aws.amazon.com/blogs/security/tag/aws-iam/), [AWS IAM Identity Center](https://aws.amazon.com/blogs/security/tag/aws-iam-identity-center/), [AWS Identity and Access Management (IAM)](https://aws.amazon.com/blogs/security/tag/aws-identity-and-access-management-iam/), [AWS Management Console](https://aws.amazon.com/blogs/security/tag/aws-management-console/), [Privileged access](https://aws.amazon.com/blogs/security/tag/privileged-access/), [Security Blog](https://aws.amazon.com/blogs/security/tag/security-blog/), [Temporary elevated access](https://aws.amazon.com/blogs/security/tag/temporary-elevated-access/)

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