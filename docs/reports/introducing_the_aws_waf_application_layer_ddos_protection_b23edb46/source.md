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

## [Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/)

# Introducing new application layer (L7) DDoS protections for AWS WAF and AWS Shield Advanced customers

by Dmitriy Novikov, Mark Ryland, and Tom Scholl on 12 JUN 2025 in [AWS WAF](https://aws.amazon.com/blogs/networking-and-content-delivery/category/security-identity-compliance/aws-waf/ "View all posts in AWS WAF"), [Launch](https://aws.amazon.com/blogs/networking-and-content-delivery/category/news/launch/ "View all posts in Launch"), [Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/ "View all posts in Networking & Content Delivery") [Permalink](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-the-aws-waf-application-layer-ddos-protection/) Share

As the global threat landscape shifts and evolves, AWS services that help protect our customers from those threats also evolve to meet their needs. One type of threat that has changed considerably over the past few years is Distributed Denial of Service (DDoS). DDoS attacks have evolved from targeting lower network layers (Layers 3 and 4) to focusing on the application layer (Layer 7), mainly HTTP/S traffic. Because of this shift, AWS services used to detect and mitigate DDoS events have evolved as well. In this blog, we will provide a background on DDoS attacks, solutions AWS customers have used to detect and mitigate DDoS events, the challenges customers face in addressing the evolving DDoS threat landscape with these existing solutions, and the new capabilities we are launching today to help customers protect against DDoS events.

### A brief history of the evolution of DDoS

Historically, network-layer attacks (layers 3 and 4 of the OSI stack) have been the focus of DDoS attacks. Those attacks used IP datagrams or TCP or UDP packets and were aimed at network congestion or state exhaustion on a range of stateful devices. Two common attack techniques have been used: The first are botnet attacks, which overwhelm networks using many compromised devices. The second technique is an amplification attack: malicious actors flood intermediary hosts with small packets using the victim’s spoofed address. The intermediary host sends an amplified response, resulting in state exhaustion on the victim.

The growth of these techniques has slowed. For the first, better vendor “cyber hygiene,” with more frequent software updates and patches, makes it harder for botnets to find and maintain presence on compromised devices. For the second, network edge providers have made it harder to use spoofed reply addresses by increasingly enforcing RFC 2827, which instructs edge networks to drop any outbound packet with a reply address that does not match their own address space. In response to those changes, while both approaches are still common, Layer 7 attacks have significantly increased to take their place.

Specifically, over the past few years there has been a large increase in attacks focused on Layer 7 (L7), or HTTP request floods, aiming to impair web servers and backend origin servers. Orchestrating these attacks is significantly simpler from an infrastructure standpoint than using botnets or amplification attacks. The “DDoS-as-a-Service” community, also known as booters or stressers, and a plethora of open proxies available on the internet make it easy to leverage application request flood attack methods. The bad actors ramping up these attacks continue to iterate on both increasing their size from a request-per-second perspective and evading fingerprinting techniques like TLS JA3 through request-level randomization.

### The evolution of AWS Shield and Shield Advanced

Amazon Web Services (AWS) has long provided DDoS detection and mitigation through AWS Shield and Shield Advanced. All AWS customers benefit from the basic version of Shield, which protects all AWS infrastructure and our customers from many basic internet risks, such as syn flood attacks. With Shield Advanced, customers can automatically detect and mitigate DDoS attacks targeting specific resources, as well as get access to our human experts who make up the Shield Response Team. We have continuously strengthened the detection and mitigation capabilities of the service since its inception in 2016. For example, in 2021, we launched L7 Automatic Application DDoS mitigation. But our work continued because we wanted to provide customers with improved controls, visibility, and improved efficacy. Moreover, it was a feature only available to AWS Shield Advanced customers, but many of our customers use AWS WAF without Shield Advanced.

We launched AWS WAF in 2015 primarily to protect customer workloads against application-specific attacks, such as SQL injection and cross-site scripting. But over the past few years changing attack patterns have brought WAF to the foreground in defending against DDoS attacks.

### Introducing AntiDDoS AMR

Today, we are happy to announce [AntiDDoS AMR](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.html), a new feature targeted specifically at automatic mitigation of application attacks that involve HTTP request floods. We implemented this new capability as an AWS Managed Rules rule group (AMR) through [AWS WAF](https://aws.amazon.com/waf/). It removes the complexity associated with customers having to manage various WAF rules and ACLs to handle these increasingly agile attacks. This new capability provides a simple set of configurations for you to use to implement your security preferences.

There are several benefits associated with the new L7 AntiDDoS AMR feature. It’s designed to operate rapidly, detecting and mitigating new and changing attacks within seconds. It profiles your traffic within 15 minutes of enabling it on your resources to improve its ability to understand your traffic patterns and, as a result, to identify anomalous attack patterns. In addition, we believe DDoS traffic should not result in a DDoS on your wallet, so any attack traffic we detect and mitigate with AntiDDoS AMR does not get charged to you. Finally, you can use this new AMR as part of your Shield Advanced subscription or as a totally standalone feature within AWS WAF.

The rest of this blog delves into the new DDoS protection rule group, shows how to implement it, and provides a guide for configuring it to secure your applications. It serves as an introductory overview, with a more detailed analysis to follow in a subsequent post.

### Overview and key features of the AntiDDoS AMR

The AntiDDoS AMR enhances protection against Layer 7 (L7) DDoS events. This AMR detection system is designed to distinguish between DDoS events and flash crowds, where many legitimate clients send a limited number of requests. When added to your AWS WAF web access control list (ACL) configuration, it quickly learns your traffic patterns and establishes baselines for each protected resource. The system identifies anomalies by comparing current traffic to these baselines, assigning suspicion scores to requests for use in subsequent mitigations.

**Performance and accuracy:**AntiDDoS AMR detects attacks within minutes of AMR activation for the protected resource after establishing a traffic baseline. Algorithms and techniques used in the ruleset enable time-to-mitigation within seconds. The logic inside AntiDDoS AMR is tuned to block only malicious volumetric traffic. It uses sensitivity level and suspicion scores to minimize both false positives and false negatives.

**Enhanced customization:**The AMR feature offers adjustable configuration, including customer-managed sensitivity controls based on the suspicion levels detected by the system for specific events and requests from suspicious sources. This allows you to customize the protection configuration to suit the needs of your specific application types.

**Built-in visibility:**As a native AWS WAF feature, AntiDDoS AMR provides all configuration controls and native dashboards that provide visibility within the AWS WAF console for DDoS activity.

### New controls

AntiDDoS AMR introduces new controls for mitigation actions such as `Challenge` and `Block` based on the AMR labels that mark suspicion level for inspected requests. Furthermore, it adds flexibility to exclude workload paths that don’t support `Challenge` from mitigation defaulting to block mitigations for them. The highlights of this feature are the following:

**Simplified configuration**

* One-click enable and disable rules like other AWS WAF AMRs.
* Ability to configure which URI paths don’t support the `Challenge` action to make sure that `Challenge` mitigation is only used for URI paths that support `Challenge`.
* Sensitivity controls to reduce false-positive blocking due to mitigation.

**DDoS response**

* Improve DDoS detection accuracy with reduced false negatives (missed detection events).
* Detection and mitigation response time in seconds.
* Flexible mitigation actions such as `Challenge` and `Block` actions based on the detection system’s suspicion labels.

**AntiDDoS dashboards**

* New AntiDDoS dashboard in the AWS WAF console provides real-time visibility of the DDoS events and request summary.
* Detailed match metrics for mitigation actions `Challenge`, `Challenge with Valid Token`, and `Block`.
* Ability to visualize top URI path, Traffic source geography, and Top 100 source IPs from [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) if the service is [configured](https://docs.aws.amazon.com/waf/latest/developerguide/logging-cw-logs.html) as a logs destination for the web ACL.

### Getting started with AntiDDoS AMR

To add AntiDDoS AMR into your web ACL and enable DDoS protection, follow these steps:

1. In the AWS WAF console, choose **Web ACLs** from the left menu. Open your web ACL or follow the steps to [create a web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-creating.html).
2. Choose the **Rules** tab and choose **Add rules**. Choose **Add managed rule groups** and proceed with the following settings:
   1. In the AWS managed rule groups section, choose the switch Add to web ACL to enable AntiDDoS Protection for Layer 7 attacks in the web ACL.
   2. To review the default configuration or change and provide extra information. choose the Save button.
   3. Choose Add rules.
3. To be effective in detection and mitigation, the **AWS-AWSManagedRulesAntiDDoSRuleSet** AMR should be inspecting as much traffic as possible. To accomplish this, it should have either the highest priority inside your web ACL, in other words, run before any other rules, or be placed right below any custom rules with [Allow action](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-action.html), such as **IP match conditions** rule lists in case you have them. This gives the rule group the ability to track the most traffic and apply mitigations when needed. By default, when added the new AMR is located at the bottom of the priority list of the web ACL. Move it up by choosing it and using the **Move up** button until the AMR is either at the top or right below custom rules with the resulting **Allow** action as mentioned earlier.
4. Choose **Save**.

The same logic covered in the Step 3 applies if you are configuring the AntiDDoS AMR through [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html). The key takeaway is that the AMR needs to stay as high in priority as possible inside your web ACL to have full visibility of traffic for effectiveness in detection and mitigation.

### Configuring the new rule group

One of the key features of the new AMR is the greater control it provides to you for mitigation. In this section we walk through various elements that allow you to tailor the protection to the needs of your web application, which is done by adjusting the behavior during mitigation. When configuring the AMR using the [AWS Management Console](https://console.aws.amazon.com/wafv2/homev2/start) the default configuration is pre-populated. If you are using APIs or infrastructure as code (IaC) tools, then this still needs to be explicitly passed. The following figure illustrates the default configuration in the console, which is configurable across a few dimensions.

![Figure 1: Rule group configuration](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/03/26/Rule_group_configuration-1024x962.png)

Figure 1: Rule group configuration

For the majority of scenarios and workloads the default settings of the AMR are sufficient to provide robust and reliable protection against volumetric DDoS traffic. This traffic is detected and blocked by the AWS WAF associated with the protected resource.

You should still delve into configuration to understand specifics and also to know what you may want to customize to fine-tune to your use case. The group provides two ways to mitigate web requests coming to resources that are under DDoS attack. You can tune both mitigation types to be more or less sensitive to the detected level of threat.

* Mitigation using challenge: The rule group can send silent browser challenges in response to requests that can handle the challenge interstitial.
* Mitigation by blocking malicious requests: The rule group can block requests altogether.

Block sensitivity level allows you to specify how sensitive you want the rule `DDoSRequests` to be when matching on the rule group’s DDoS suspicion labeling. The higher the sensitivity, the lower the levels of labeling that the rule matches:

* Low sensitivity is less sensitive, causing the rule to match only on the most obvious participants in an attack, which have the high suspicion label `awswaf:managed:aws:anti-ddos:high-suspicion-ddos-request`

* Medium sensitivity causes the rule to match on the medium and high suspicion labels.
* High sensitivity causes the rule to match on all of the suspicion labels: low, medium, and high.

Before moving on we should discuss Challenge action and AWS WAF tokens.

If you have been using AWS WAF and rule groups such as Bot Control you may be familiar with AWS WAF tokens and Challenge action. Challenges run silently to help distinguish regular client sessions from bot sessions and to make it more costly for bots to operate. When the challenge completes successfully, the challenge script automatically procures a new token from AWS WAF if needed, then updates the token’s challenge timestamp. The Challenge action can only be handled properly by a client that’s expecting HTML content. For more information about how the action works, see [CAPTCHA and Challenge action behavior](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge-how-it-works.html).

A token, sometimes called a fingerprint, is a collection of information about a single client session that the client stores and provides with every web request that it sends. AWS WAF uses tokens to identify and separate malicious client sessions from legitimate sessions, even when both originate from a single IP address. Token use imposes client-side computational processing costs that are negligible for legitimate users, but expensive at scale for botnets. AWS WAF creates, updates, and encrypts tokens for clients that successfully respond to silent challenges. When a client with a token sends a web request, it includes the encrypted token, and AWS WAF decrypts the token and verifies its contents.

**Enable Challenge** controls whether to enable the rules `ChallengeDDoSRequests` and `ChallengeAllDuringEvent` inside the rule group. The default setting is pre-populated in the Console, which applies the `Challenge` action to matching requests. If you’re using APIs or IaC tools, then this setting needs to be explicitly passed.

These two rules provide request handling that’s intended to permit requests from legitimate users to proceed while blocking the unwanted traffic of a DDoS attack. As with other AWS WAF rules you can override their action settings to `Allow` or `Count`, or you can disable their use entirely.

When `Challenge` is enabled you can customize its behavior. For **Challenge sensitivity level**, specify how sensitive you want the rule `ChallengeDDoSRequests` to be.

The higher the sensitivity, the lower the levels of labeling that the rule matches. This is how it works:

* Low sensitivity is less sensitive, causing the rule to match only on the most obvious participants in an attack, which have the high suspicion label `awswaf:managed:aws:anti-ddos:high-suspicion-ddos-request.`
* Medium sensitivity causes the rule to match on the medium and high suspicion labels.
* High sensitivity causes the rule to match on all of the suspicion labels: low, medium, and high.

**Exempt URI regular expressions** provide a regular expression that matches against URIs for web requests that can’t handle a silent browser challenge. The Challenge action effectively blocks requests from URIs that are missing the challenge token unless they can handle the silent browser challenge.

The default expression that’s provided in the console covers most use cases, but you should review and adapt it for your application. A common example can be made out of the API prefix. The default pre-populated in the console exempt regular expression uses /api/. Your application can use a custom name for the API URI path, for example /myapi/ or /apiv2/. In this case this setting should be modified to reflect your configuration.

Furthermore, you can add up to five exemptions for URIs that are non-challengeable. The rules use the specified regular expression to identify request URIs that can’t handle the Challenge action and prevent the rules from sending a Challenge back. Requests that you exclude in this way can still be blocked but only by the rule `DDoSRequests` in the rule group.

AWS WAF supports the pattern syntax used by the PCRE library `libpcre` with some exceptions. The library is documented at [PCRE – Perl Compatible Regular Expressions](http://www.pcre.org/). For information about AWS WAF support, see [Supported regular expression syntax in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-support.html).

### AntiDDoS AMR in action

AWS WAF web ACLs provide the [traffic overview dashboard](https://aws.amazon.com/blogs/security/introducing-the-aws-waf-traffic-overview-dashboard/) to gain better visibility and make informed decisions based on insights from the dashboards. Alongside the new AMR, AWS WAF now has a new AntiDDoS dashboard that is purpose-built for the new rule group. The following figure shows a typical layout for the traffic overview dashboard with traffic inspected by AntiDDoS AMR.

![Figure 2: Dashboard with sections showing overall statistics of inspected traffic](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/03/26/Picture2-11.png)

Figure 2: Dashboard with sections showing overall statistics of inspected traffic

On the dashboard you can get information about actions taken on requests for the chosen time period, and the most impacted resources to quickly assess targets among your web resources. You can also observe a breakdown across challenged requests.

The following dashboards are readily available with the AntiDDoS AMR:

1. Labels from the managed rule group: All labels generated by the AntiDDoS AMR, based on the events detected, request suspicion levels and labels for each managed rule.
2. Terminating rule actions such as **Challenge** and **Block**, **Total Challenged Requests** compared to **Total** and **ChallengeRuleMatchWithValidToken**. A single request can emit multiple **ChallengeRuleMatchWithValidToken** metrics if it matches multiple challenge rules.

![Figure 3: Dashboard with sections showing details across multiple categories and illustrates mitigation statistics](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/03/26/Picture3-7.png)

Figure 3: Dashboard with sections showing details across multiple categories and illustrates mitigation statistics

If you are sending your [AWS WAF logs to CloudWatch](https://docs.aws.amazon.com/waf/latest/developerguide/logging-cw-logs.html), then you can visualize further data such as:

* Traffic source geography: This identifies the top countries for the origin of the traffic.
* URI Path: Top URI paths ranked by request frequency.
* Client IPs: Top 100 clientIPs ranked by request frequency.

Resource-level metrics [available in CloudWatch](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html) allow you to analyze trends and data to deduce the Rule Set’s efficacy.

### Labels generated by AntiDDoS AMR

[Labels](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-overview.html), which plays the role of metadata appended to an inspected request, is a great mechanism to better understand the specifics of traffic and requests composition. The new AMR is not an exception and adds the following labels to applicable requests under the label namespace prefix `awswaf:managed:aws:anti-ddos:`

Labels of this AMR can be put into the following three categories.

**Mitigation**

`ddos-request` – Emitted when AMR detects a DDoS event for the requests that the system identifies as coming from suspicious sources.

`event-detected` – Emitted when AMR detects a DDoS event for all requests, such as legitimate and attack requests.

`DDoSRequests` – Emitted when the DDoSRequests rule matches the request.

**Challenge-related category**

`ChallengeAllDuringEvent` – Emitted when the ChallengeAllDuringEvent rule matches the request.

`challengeable-request` – Requests that can be challenged, such as excluding the URIs in the regex are labeled with this name.

`ChallengeDDoSRequests` – Emitted when challengeable-request matches the request.

Challenge-related labels are useful to make reviews and verify that configurations meet your requirements. For example, given that `challengeable-request` is added to all requests that don’t match the `ExemptURIRegex`, you can verify that label in your AWS WAF logs to see if it’s labelling the right traffic for challengeable.

**Suspicion levels**

`high-suspicion-ddos-request` – Emitted when AMR identifies a request originating from a highly suspicious source.

`low-suspicion-ddos-request` – Emitted when AMR identifies a request to be a probable DDoS attack request.

`medium-suspicion-ddos-request` – Emitted when AMR identifies a request to be a DDoS attack request from a very likely source.

Suspicion labels can be used in a custom AWS AWF rule to add extra logic upon traffic. For example, you can rate limit requests with a low suspicion level to safeguard your web application while avoiding false positives in case of a complete block. Another option is to block based on labels requests that are non-challengeable, in other words when dealing with non-HTML content.

![Figure 4: Details of traffic characteristics, such as targeted URIs and source geography. This data is handy for reinforcing protection by configuring extra logic in rules.](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/03/26/Picture4-Picsart-AiImageEnhancer.png)

Figure 4: Details of traffic characteristics, such as targeted URIs and source geography. This data is handy for reinforcing protection by configuring extra logic in rules.

### Availability and pricing

At the release AntiDDoS AMR is available for AWS WAF web ACLs that are associated with [Amazon CloudFront](https://aws.amazon.com/cloudfront/) and other AWS services supported by WAF such as [Application Load Balancer (ALB)](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/).

AntiDDoS AMR supports existing AWS WAF features, including scope-down statements labels, and label-matched statements. To selectively apply AntiDDoS AMR only on parts of your web application, you can use scope-down statements. However, it’s not recommended, as it decreases the efficacy and accuracy of the protection.

AntiDDoS AMR is a paid AWS Managed Rule that can be added to your web ACL and will consume 50 WCUs. The pricing depends on whether you are a Shield Advanced customer or a WAF customer.

If you are an existing Shield Advanced customer, you will get this feature as part of your subscription. We will limit each payer account to 50 billion Shield-protected WAF requests per month. If you exceed 50 billion requests in a month, there will be a charge of $0.15 per million requests. Most AWS Shield Advanced customers will not see any impact on their AWS bill. This change starts in October 2025 or the first full calendar month of your existing yearly subscription (whichever comes later). Until then, if you are an existing Shield Advanced customer who makes over 50 billion monthly requests, you will see no changes to your bill. For new Shield Advanced customers (those without an active subscription on launch day), the limit applies from their subscription start date.

Importantly, for both Shield Advanced and WAF customers, AWS will not charge for any requests that are detected as DDoS when protection rules are actively mitigating and are NOT in Count mode. So, for Shield Advanced customers, any request detected as DDoS will not count towards the 50 billion bundled monthly requests.

We are introducing this change because of the change in the threat landscape as discussed above in the introduction, and how that change has affected both the usage and costs associated with Layer 7 attacks. Shield Advanced customers have had unlimited WAF usage but have had to handcraft and constantly update their own rules to address DDoS use cases. The improved automation and speed of the new AntiDDoS AMR greatly benefit all WAF and Shield Advanced customers, especially high-usage customers who need better value. We will continue to invest in features to further improve detection speed and mitigation efficacy and provide greater visibility and insights. We will further simplify the onboarding experience by integrating the new AntiDDoS AMR capabilities into the Shield console.

If you are an AWS WAF customer, this is a new opt-in feature. Each AntiDDoS AMR costs $20 per month, prorated hourly. This AMR charges $0.15 per million requests beyond the base WAF charge of $0.60 per million.

### Conclusion

The AWS WAF Managed Rules AntiDDoS AMR allows you to protect your web applications against the growing volume of Layer 7 DDoS attacks using familiar and existing components of AWS WAF and its web ACL model.

In this post, you learned how the rule group automatically creates traffic baselines and distinguishes DDoS from legitimate traffic. We covered Rule Set internals, customization options, optimal ACL positioning, and handling of suspicious traffic based on your needs. For more information, review [AWS WAF Managed Rules AntiDDoS AMR documentation.](https://docs.aws.amazon.com/waf/latest/developerguide/waf-anti-ddos.html)

The AntiDDoS AMR is designed to meet most use cases and be a go-to default option for security against DDoS for web applications. However, if you’d prefer managed DDoS protection with access to Shield Response Team, then explore [Shield Advanced](https://aws.amazon.com/shield/).

### Authors Bio

**![](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/06/05/tscholl-1.jpg)Tom Scholl**

AWS VP and Distinguished Engineer Tom collaborates with networks across the globe to stop cyberattacks by tracking traffic from bad actors at its source.

**![](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/06/05/badgephotos.amazon.com_-225x300-1.jpg)****Dmitriy Novikov**

As a Senior Solutions Architect at AWS, Dmitriy supports AWS customers to use emerging technologies to generate business value. He’s a technology enthusiast who loves finding innovative solutions to complex challenges.

**![](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/06/11/Mark_Ryland_2018_120x160px-2.jpg)Mark Ryland**

Mark is the director of the Office of the CISO for AWS. He has more than 28 years of experience in the technology industry and has served in leadership roles in cybersecurity, software engineering, distributed systems, technology standardization and public policy.

### Resources

* [Networking Products](https://aws.amazon.com/products/networking?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)
* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)
* [Amazon CloudFront](https://aws.amazon.com/cloudfront?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
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