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

## [The Internet of Things on AWS – Official Blog](https://aws.amazon.com/blogs/iot/)

# Build a proof-of-concept IoT solution in under 3 hours with the AWS IoT Device Client

by Syed Rehan on 08 JAN 2025 in [AWS IoT Core](https://aws.amazon.com/blogs/iot/category/internet-of-things/aws-iot-platform/ "View all posts in AWS IoT Core"), [AWS IoT Device Defender](https://aws.amazon.com/blogs/iot/category/internet-of-things/aws-iot-device-defender/ "View all posts in AWS IoT Device Defender"), [AWS IoT Device Management](https://aws.amazon.com/blogs/iot/category/internet-of-things/aws-iot-device-management/ "View all posts in AWS IoT Device Management") [Permalink](https://aws.amazon.com/blogs/iot/build-a-proof-of-concept-iot-solution-in-under-3-hours-with-the-aws-iot-device-client/) Share

## Introduction

You may be starting on your IoT journey, or have thousands of devices connected already. Maybe you just built an IoT business application, and want to deploy it to your fleet. You’re looking for a way to build functionality to control, update, monitor, or secure your IoT devices. To guide you through this process and get you started on AWS IoT, AWS is happy to announce the “Get Started with AWS IoT Workshop”. [Click here to access the Workshop](https://catalog.workshops.aws/getstartedwithawsiot).

In this hands-on workshop, we use the [AWS IoT Device Client](https://github.com/awslabs/aws-iot-device-client) to provide a guided walk-through to create your proof-of-concept IoT project. In **3 hours**, you will learn to:

* Securely connect your IoT device to the internet, onboard and register it on [AWS IoT Core](https://aws.amazon.com/iot-core/)
* Remotely control your device using [AWS IoT Device Management](https://aws.amazon.com/iot-device-management/) – run a simple Over-The-Air (OTA) remote operation using Jobs, and set up SSH access for troubleshooting using Secure Tunneling
* Set up a daily security audit, and monitor a ‘heartbeat’ of health metrics from your device using [AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/)

![](https://d2908q01vomqb2.cloudfront.net/f6e1126cedebf23e1463aee73f9df08783640400/2021/10/18/image-1.png)

The AWS IoT Device Client is written in C++, open-source, and available on [GitHub](https://github.com/awslabs/aws-iot-device-client). You can compile and install on Embedded-Linux based IoT devices to get started with AWS IoT Core, AWS IoT Device Management, and AWS IoT Device Defender.

## Prerequisites

To complete this workshop, you need:

* An AWS account with admin privileges, or Event engine details. You can [create a new AWS account here](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).
* A computer with the latest browser – like Firefox or Chrome
* Basic understanding of Linux (e.g. create directories, set file permissions) and programming (compiling code)

## When to use the AWS IoT Device Client

### Example Use Cases:

The AWS IoT Device Client is a reference implementation, and the easiest way to create an IoT proof-of-concept (PoC). It provides an easy way to connect a fleet of devices to the internet, and route IoT data to AWS. By default, it enables you to operate, manage, and control your fleets, or secure them against threats using AWS IoT services. It is open-source, so you can modify it to fit your business needs, connect your business applications to take advantage of AWS IoT features, or optimize its resource utilization when you wish to scale up from a PoC to production. Here are some example use cases the AWS IoT Device Client solves for:

1. [**First Connect & Provisioning**] You want to provision a fleet of production devices and connect them to the internet.

   The IoT Device Client enables your devices to automatically connect to IoT Core, exchange a bulk certificate for secure individual identities from the [IoT Core Identity](https://aws.amazon.com/iot-core/features/#Authentication_and_Authorization) service, and register themselves in the [IoT Core Device Registry](https://aws.amazon.com/iot-core/features/#Registry).
2. You just built a custom business application for your IoT solution. The IoT Device Client provides a backbone of capabilities for your app.
   1. [**Messaging**] You want to exchange telemetry, state, or control messages with the app over MQTT.

      The IoT Device Client enables your device connect over MQTT to the [AWS IoT Core Device Gateway](https://aws.amazon.com/iot-core/features/#Device_Gateway) and shares that connection with your app. You can publish/subscribe to custom MQTT topics via the [AWS IoT Core Message Broker](https://aws.amazon.com/iot-core/features/#Message_Broker) by setting simple configurations on your device. You also have the option to publish data from your app directly to the [AWS IoT Core Rules Engine](https://aws.amazon.com/iot-core/features/#Rules_Engine) via [Basic Ingest](https://docs.aws.amazon.com/iot/latest/developerguide/iot-basic-ingest.html), reducing messaging costs.
   2. [**Control**] You want to read and control the state of your device or the configuration of your app.

      The IoT Device Client gives your app the ability to interact with [AWS IoT Core Device Shadows](https://aws.amazon.com/iot-core/features/#Device_Shadow) so you can get/set the state of your device or the configuration of your app even if it is offline for prolonged periods.
   3. [**Operate & Update**] You want to update your fleet to use a new version of your app, or deploy a firmware/OS update, or simply reboot the fleet remotely.

      With the IoT Device Client, you can directly use [AWS IoT Device Management Jobs](https://aws.amazon.com/iot-device-management/features/#:~:text=Remotely%20Manage%20Connected%20Devices) – it lets you deploy to targeted devices, control the speed of your deployment, and track the status of your updates, even if devices work in partially offline environments.
   4. [**Troubleshoot or Access**] You want to troubleshoot a device, retrieve logs, or access it using Secure Shell (SSH) for maintenance.

      With the IoT Device Client your device can directly connect using the [AWS IoT Device Management Secure Tunneling](https://aws.amazon.com/iot-device-management/features/#:~:text=to%20connected%20devices.-,Secure%20Tunneling,-AWS%20IoT%20Device) feature to an Admin console, providing synchronous access with admin privileges.
   5. [**Monitor & Secure**] You want to send a ‘heartbeat’ of device-side health metrics like ports open or bytes in/out to detect unusual security behaviors and guard your fleet against compromise.

      The IoT Device Client lets your device automatically publish your metrics over MQTT to the [AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender) service at regular intervals.

## AWS IoT Device Client: High Level Architecture

![](https://d2908q01vomqb2.cloudfront.net/f6e1126cedebf23e1463aee73f9df08783640400/2021/10/18/image-2.png)

### Compatibility:

The AWS IoT Device Client [[GitHub](https://github.com/awslabs/aws-iot-device-client)] currently works on IoT devices with common microprocessors (x86\_64, ARM, MIPS-32 architectures), and common Linux software environments (Debian, Ubuntu, and RHEL). We also provide a [meta-aws recipe for the AWS IoT Device Client](https://github.com/aws4embeddedlinux/meta-aws/tree/master/recipes-iot/aws-iot-device-client) that you can build into your Yocto Linux distribution for more constrained and purpose-built devices.

## Conclusion

Try out this [Workshop](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/6d30487a-48e1-4631-b6bc-5602582800b5/en-US) to get started with AWS IoT using the AWS IoT Device Client.

Using **AWS IoT Device Client** is the easiest way to create a proof-of-concept (PoC) for your IoT project. It takes away the generic heavy lifting involved in connecting, managing, and securing your IoT fleets, reducing the initial investment required for your IoT project. You can now focus on building your IoT business logic and apps. AWS is committed to the AWS IoT Device Client as a living tool. It is a reference implementation with operational and security best-practices baked in. As new AWS IoT features become generally available and IoT best practices are established, we will update this software to support them appropriately.

## **About the authors**

![syed](https://d2908q01vomqb2.cloudfront.net/f6e1126cedebf23e1463aee73f9df08783640400/2024/10/01/Syed125px.jpg)

### [Syed Rehan](https://www.linkedin.com/in/iamsyed/)

Syed is a Senior IoT Product Security Architect at AWS IoT. He specializes in enabling customers—from startups to large enterprises—to build secure IoT, Machine Learning (ML), and Artificial Intelligence (AI)-based solutions on AWS. With deep expertise in cybersecurity, cloud technologies, and IoT, Syed collaborates with security specialists, developers, and decision-makers to drive the adoption of AWS Security services and solutions. Before AWS, Syed designed and developed mission-critical systems for companies like Vodafone, FICO, Rackspace, Nokia, Barclays Bank, and Convergys. He is also a published author on AWS IoT, ML, and Cybersecurity, sharing his knowledge through books and public speaking engagements.

![](https://d2908q01vomqb2.cloudfront.net/f6e1126cedebf23e1463aee73f9df08783640400/2021/10/18/shantanu.jpeg)

### [Shantanu Sathe](https://www.linkedin.com/in/satheshantanu/)

is a Senior Product Manager – Technical at AWS IoT. He focuses on building IoT fleet management and monitoring solutions.

TAGS: [AWS IoT](https://aws.amazon.com/blogs/iot/tag/aws-iot/), [AWS IoT Core](https://aws.amazon.com/blogs/iot/tag/aws-iot-core/), [AWS IoT Device Defender](https://aws.amazon.com/blogs/iot/tag/aws-iot-device-defender/), [AWS IoT Device Defender Concepts](https://aws.amazon.com/blogs/iot/tag/aws-iot-device-defender-concepts/), [AWS IoT Device Management](https://aws.amazon.com/blogs/iot/tag/aws-iot-device-management/), [AWS IoT Device Management - Secure Tunneling](https://aws.amazon.com/blogs/iot/tag/aws-iot-device-management-secure-tunneling/), [Getting started](https://aws.amazon.com/blogs/iot/tag/getting-started/), [iot](https://aws.amazon.com/blogs/iot/tag/iot/), [IoT Device Agent](https://aws.amazon.com/blogs/iot/tag/iot-device-agent/), [IoT Device Client](https://aws.amazon.com/blogs/iot/tag/iot-device-client/), [IoT Device Software](https://aws.amazon.com/blogs/iot/tag/iot-device-software/), [IoT Jobs](https://aws.amazon.com/blogs/iot/tag/iot-jobs/), [Over-The-Air (OTA) remote operation with AWS IoT Jobs](https://aws.amazon.com/blogs/iot/tag/over-the-air-ota-remote-operation-with-aws-iot-jobs/), [secure tunneling](https://aws.amazon.com/blogs/iot/tag/secure-tunneling/), [SSH](https://aws.amazon.com/blogs/iot/tag/ssh/), [Step-by-step guide](https://aws.amazon.com/blogs/iot/tag/step-by-step-guide/), [Tutorial](https://aws.amazon.com/blogs/iot/tag/tutorial/), [Workshop](https://aws.amazon.com/blogs/iot/tag/workshop/)

### Resources

[Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=iot-resources)  [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=iot-resources)  [Top Posts](https://aws.amazon.com/blogs?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=iot-resources)  [Official AWS Podcast](https://aws.amazon.com/podcasts/aws-podcast?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=iot-resources)  [AWS Case Studies](https://aws.amazon.com/solutions/case-studies?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=iot-resources)

---

### Follow

[Twitter](https://twitter.com/awscloud)  [Facebook](https://www.facebook.com/amazonwebservices)  [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)  [Twitch](https://www.twitch.tv/aws)  [RSS Feed](http://feeds.feedburner.com/AmazonWebServicesBlog)  [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=iot-social)

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