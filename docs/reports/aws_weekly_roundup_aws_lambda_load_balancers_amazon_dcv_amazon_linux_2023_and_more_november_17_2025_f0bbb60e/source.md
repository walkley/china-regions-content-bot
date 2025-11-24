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

# AWS Weekly Roundup: AWS Lambda for Rust, NLB for QUIC protocol, Amazon DCV for Mac, and more (November 17, 2025)

by [Sébastien Stormacq](https://aws.amazon.com/blogs/aws/author/stormacq/ "Posts by Sébastien Stormacq") on 17 NOV 2025 in [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-lambda-load-balancers-amazon-dcv-amazon-linux-2023-and-more-november-17-2025/)  [Comments](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-lambda-load-balancers-amazon-dcv-amazon-linux-2023-and-more-november-17-2025/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

The weeks before AWS re:Invent, my team is full steam ahead preparing content for the conference. I can’t wait to meet you at one of my three talks: [CMP346](https://registration.awsevents.com/flow/awsevents/reinvent2025/eventcatalog/page/eventcatalog?search=CMP346&trk=direct) : Supercharge AI/ML on Apple Silicon with EC2 Mac, [CMP344](https://registration.awsevents.com/flow/awsevents/reinvent2025/eventcatalog/page/eventcatalog?search=CMP344&trk=direct): Speed up Apple application builds with CI/CD on EC2 Mac, and [DEV416](https://registration.awsevents.com/flow/awsevents/reinvent2025/eventcatalog/page/eventcatalog?search=DEV416&trk=direct): Develop your AI Agents and MCP Tools in Swift.

Last week, [AWS announced three new AWS Heroes.](https://aws.amazon.com/blogs/aws/introducing-our-final-aws-heroes-of-2025/) The [AWS Heroes program](https://builder.aws.com/community/heroes) recognizes a vibrant, worldwide group of AWS experts whose enthusiasm for knowledge-sharing has a real impact within the community. Welcome to the community, Dimple, Rola, and Vivek.

We also opened the [GenAI Loft in Tel Aviv, Israel](https://aws-experience.com/emea/tel-aviv/gen-ai-loft-program). [AWS Gen AI Lofts](https://aws.amazon.com/startups/lp/aws-gen-ai-lofts) are collaborative spaces and immersive experiences for startups and developers. The Loft content is tailored to address local customer needs – from startups and enterprises to public sector organizations, bringing together developers, investors, and industry experts under one roof.

[![GenAI Loft - TLV](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/17/2025_11_11-AWS-Gen-Ai-Loft-Tel-Aviv-253-1024x683.jpg)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/11/17/2025_11_11-AWS-Gen-Ai-Loft-Tel-Aviv-253.jpg)

The loft is open in Tel Aviv until Wednesday, November 19. If you’re in the area, [check the list of sessions, workshops, and hackathons today.](https://aws-experience.com/emea/tel-aviv/gen-ai-loft-program)

If you are a serverless developer, last week was really rich with news. Let’s start with these.

**Last week’s launches** Here are the launches that got my attention this week:

* [AWS Lambda officially supports Rust](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-lambda-rust/) , [AWS Lambda supports Java 25,](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-lambda-java-25/) and [AWS Lambda adds an experimental runtime interface client for Swift](https://aws.amazon.com/blogs/opensource/the-swift-aws-lambda-runtime-moves-to-awslabs/) – What a busy time for the Lambda service team! The support for the Rust programming language is now generally available. Although the runtime interface client existed for years, it has just been graduated to version 1.0.0. My colleagues [Julian](https://www.linkedin.com/in/julianrwood/) and [Darko](https://www.linkedin.com/in/darko-mesaros/) [wrote a blog post to showcase the benefits of using Rust for your Lambda functions](https://aws.amazon.com/blogs/compute/building-serverless-applications-with-rust-on-aws-lambda/). Java 25 also has changes that make Lambda functions written in Java more efficient. My colleague [Lefteris](https://www.linkedin.com/in/lefkarag/) wrote [a blog post to describe these benefits](https://aws.amazon.com/blogs/compute/aws-lambda-now-supports-java-25/).
* [AWS Lambda announces Provisioned Mode for SQS event source mapping](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-lambda-provisioned-mode-sqs-esm/) – This provides you with the benefits to optimize throughput and handle traffic spikes by provisioning event polling resources.
* [Amazon EventBridge introduces enhanced visual rule builder](https://aws.amazon.com/about-aws/whats-new/2025/11/eventbridge-enhanced-visual-rule-builder/) – The Amazon EventBridge enhanced visual rule builder simplifies event-driven application development with an intuitive interface, comprehensive event catalog, and integration with the [EventBridge Schema Registry](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-registry.html).
* [AWS Service Reference Information now supports SDK Operation to Action mapping](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-service-reference-information-sdk-operation-action-mapping/) – Besides the serverless news, this is the biggest announcement of the week in my opinion. The service reference information now includes which operations are supported by AWS services and which IAM permissions are needed to call a given operation. This will help you answer questions such as “I want to call a specific AWS service operation, which IAM permissions do I need?” [You can automate the retrieval of service reference information through a simple JSON based API](https://docs.aws.amazon.com/service-authorization/latest/reference/service-reference.html).
* [AWS Network Load Balancer (NLB) now supports QUIC protocol in passthrough mode](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-network-load-balancer-quic-passthrough-mode/) – This provides ultra-low latency traffic forwarding with session stickiness using QUIC Connection IDs. This capability reduces application latency by 25-30% for mobile-first applications through minimized handshakes and connection resilience. NLB operates in passthrough mode, forwarding QUIC traffic directly to targets while maintaining customer control over TLS certificates and end-to-end encryption. [The blog post has the details](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-quic-protocol-support-for-network-load-balancer-accelerating-mobile-first-applications/).
* [Application Load Balancer (ALB) support client credential flow with JWT verification](https://aws.amazon.com/about-aws/whats-new/2025/11/application-load-balancer-jwt-verification/) – This one is important for API developers too. This simplifies the deployment of secure machine-to-machine (M2M) and service-to-service (S2S) communications. This provides ALB with the ability to verify JWTs, reducing architectural complexity and simplifying security implementation.
* [AWS KMS now supports Edwards-curve Digital Signature Algorithm (EdDSA)](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-kms-edwards-curve-digital-signature-algorithm/) – This capability provides 128-bit security equivalent to NIST P-256 with faster signing performance and compact sizes (64-byte signatures, 32-byte public keys). Ed25519 is ideal for IoT devices and blockchain applications requiring small key and signature sizes.
* [Amazon DCV now supports Amazon EC2 Mac instances](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-dcv-ed2-mac-instances/) – This provides high-performance remote desktop access with 4K resolution and 60 FPS performance. You can connect from Windows, Linux, macOS, or web clients with features including time zone redirection and audio output.
* [Amazon Linux 2023 version 2025110](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.9.20251110.html) is released – It now includes packages for [Mountpoint for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mountpoint.html), the [Swift 6.2.1 toolchain](https://www.swift.org/get-started/cloud-services/), and [Node.js 24](https://nodejs.org/en/blog/release/v24.0.0). Installing Swift on Amazon Linux 2023 virtual machines or containers is now as easy as `sudo dnf install -y swiftlang`.

**Additional updates**

Here are some additional projects, blog posts, and news items that I found interesting:

* [Amazon Elastic Kubernetes Service gets independent affirmation of its zero operator access design](https://aws.amazon.com/blogs/security/amazon-elastic-kubernetes-service-gets-independent-affirmation-of-its-zero-operator-access-design/) – Amazon EKS offers a zero operator access posture. AWS personnel cannot access your content. This is achieved through a combination of [AWS Nitro](https://aws.amazon.com/ec2/nitro/) System-based instances, restricted administrative APIs, and end-to-end encryption. An independent review by NCC Group confirmed the effectiveness of these security measures.
* [Make your web apps hands-free with Amazon Nova Sonic](https://aws.amazon.com/blogs/machine-learning/make-your-web-apps-hands-free-with-amazon-nova-sonic/) – Amazon Nova Sonic, a foundation model from A[Amazon Bedrock](https://aws.amazon.com/bedrock/), provides you with the ability to create natural, low-latency, bidirectional speech conversations for applications. This provides users with the ability to collaborate with applications through voice and embedded intelligence, unlocking new interaction patterns and enhancing usability. This blog post demonstrates a reference app, Smart Todo App. It shows how voice can be integrated to provide a hands-free experience for task management.
* [AWS X-Ray SDKs & Daemon migration to OpenTelemetry](https://aws.amazon.com/blogs/mt/aws-x-ray-sdks-daemon-migration-to-opentelemetry/) – AWS X-Ray is transitioning to OpenTelemetry as its primary instrumentation standard for application tracing. OpenTelemetry-based instrumentation solutions are recommended for producing traces from applications and sending them to AWS X-Ray. X-Ray’s existing console experience and functionality continue to be fully supported and remains unchanged by this transition.
* [Powering the world’s largest events: How Amazon CloudFront delivers at scale](https://aws.amazon.com/blogs/aws-insights/powering-the-worlds-largest-events-how-amazon-cloudfront-delivers-at-scale/) – Amazon CloudFront achieved a record-breaking peak of 268 terabits per second on November 1, 2025, during major game delivery workloads—enough bandwidth to simultaneously stream live sports in HD to approximately 45 million concurrent viewers. This milestone demonstrates the CloudFront massive scale, powered by 750+ edge locations across 440+ cities globally and 1,140+ embedded PoPs within 100+ ISPs, with the latest generation delivering 3x the performance of previous versions.

**Upcoming AWS events**

Check your calendars so that you can sign up for these upcoming events:

* [AWS Builder Loft](https://builder.aws.com/connect/events/builder-loft) – A community tech space in San Francisco where you can learn from expert sessions, join hands-on workshops, explore AI and emerging technologies, and collaborate with other builders to accelerate your ideas. Browse the [upcoming sessions](https://luma.com/aws-builder-loft-events) and join the events that interest you.
* [AWS Community Days](https://aws.amazon.com/events/community-day/) – Join community-led conferences that feature technical discussions, workshops, and hands-on labs led by experienced AWS users and industry leaders from around the world. I will deliver the opening keynote at the last Community Day of the year in [Kinshasa, Democratic Republic of Congo](https://www.meetup.com/aws-user-group-congo-kinshasa/events/308082108/) (November 22). The next Community Day will be in [Timişoara, România](https://aws-community.ro/) (April 2026). The [call for papers is now open](https://aws-community.ro/call-for-papers).
* [AWS Skills Center Seattle 4th Anniversary Celebration](https://pulse.aws/survey/LOLZYMRD?p=0) – A free, public event on November 20 with a keynote, learned panels, recruiter insights, raffles, and virtual participation options.

Join the [AWS Builder Center](https://builder.aws.com/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) to learn, build, and connect with builders in the AWS community. Browse here for [upcoming in-person events](https://aws.amazon.com/events/explore-aws-events/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), [developer-focused events](https://aws.amazon.com/developer/events/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), and [events for startups](https://aws.amazon.com/startups/events?trk=c4ea046f-18ad-4d23-a1ac-cdd1267f942c&sc_channel=el).

That’s all for this week. Check back next Monday for another [Weekly Roundup](https://aws.amazon.com/blogs/aws/tag/week-in-review/?trk=7c8639c6-87c6-47d6-9bd0-a5812eecb848&sc_channel=el)!

[— seb](https://linktr.ee/sebsto)

This post is part of our Weekly Roundup series. Check back each week for a quick roundup of interesting news and announcements from AWS!

TAGS: [Week in Review](https://aws.amazon.com/blogs/aws/tag/week-in-review/)

![Sébastien Stormacq](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2023/01/13/AWS-59-cropped.jpg)

### [Sébastien Stormacq](https://aws.amazon.com/blogs/aws/author/stormacq/ "Posts by Sébastien Stormacq")

Seb has been writing code since he first touched a Commodore 64 in the mid-eighties. He inspires builders to unlock the value of the AWS cloud, using his secret blend of passion, enthusiasm, customer advocacy, curiosity and creativity. His interests are software architecture, developer tools and mobile computing. If you want to sell him something, be sure it has an API. Follow @sebsto on Bluesky, X, Mastodon, and others.

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