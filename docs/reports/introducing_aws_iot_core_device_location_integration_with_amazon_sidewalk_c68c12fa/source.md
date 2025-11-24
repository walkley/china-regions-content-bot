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

# Introducing AWS IoT Core Device Location integration with Amazon Sidewalk

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 13 NOV 2025 in [AWS IoT Core](https://aws.amazon.com/blogs/aws/category/internet-of-things/aws-iot-platform/ "View all posts in AWS IoT Core"), [Internet of Things](https://aws.amazon.com/blogs/aws/category/internet-of-things/ "View all posts in Internet of Things"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/introducing-aws-iot-core-device-location-integration-with-amazon-sidewalk/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-aws-iot-core-device-location-integration-with-amazon-sidewalk/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, I’m happy to announce a new capability to resolve location data for [Amazon Sidewalk](https://www.amazon.com/Amazon-Sidewalk/b?ie=UTF8&node=21328123011) enabled devices with the [AWS IoT Core Device Location service](https://docs.aws.amazon.com/iot/latest/developerguide/device-location.html). This feature removes the requirement to install GPS modules in a Sidewalk device and also simplifies the developer experience of resolving location data. Devices powered by small coin cell batteries, such as smart home sensor trackers, use Sidewalk to connect. Supporting built-in GPS modules for products that move around is not only expensive, it can creates challenge in ensuring optimal battery life performance and longevity.

With this launch, Internet of Things (IoT) device manufacturers and solution developers can build asset tracking and location monitoring solutions using Sidewalk-enabled devices by sending Bluetooth Low Energy (BLE), Wi-Fi, or Global Navigation Satellite System (GNSS) information to [AWS IoT](https://aws.amazon.com/iot/) for location resolution. They can then send the resolved location data to an [MQTT topic](https://docs.aws.amazon.com/iot/latest/developerguide/topics.html) or [AWS IoT rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) and route the data to other [Amazon Web Services (AWS)](https://aws.amazon.com/) services, thus using different capabilities of AWS Cloud through AWS IoT Core. This would simplify their software development and give them more options to choose the optimal location source, thereby improving their product performance.

This launch addresses [previous challenges and architecture complexity](https://aws.amazon.com/blogs/iot/building-track-and-trace-applications-using-aws-iot-core-for-amazon-sidewalk/). You don’t need location sensing on network-based devices when you use the Sidewalk network infrastructure itself to determine device location, which eliminates the need for power-hungry and costly GPS hardware on the device. And, this feature also allows devices to efficiently measure and report location data from GNSS and Wi-Fi, thus extending the product battery life. Therefore, you can build a more compelling solution for asset tracking and location-aware IoT applications with these enhancements.

For those unfamiliar with Amazon Sidewalk and the AWS IoT Core Device Location service, I’ll briefly explain their history and context. If you’re already familiar with them, you can skip to the section on how to get started.

**AWS IoT Core integrations with Amazon Sidewalk**

Amazon Sidewalk is a shared network that helps devices work better through improved connectivity options. It’s designed to support a wide range of customer devices with capabilities ranging from locating pets or valuables, to smart home security and lighting control and remote diagnostics for appliances and tools.

Amazon Sidewalk is a secure community network that uses Amazon Sidewalk Gateways (also called Sidewalk Bridges), such as compatible Amazon Echo and Ring devices, to provide cloud connectivity for IoT endpoint devices. Amazon Sidewalk enables low-bandwidth and long-range connectivity at home and beyond using BLE for short-distance communication and LoRa and frequency-shift keying (FSK) radio protocols at 900MHz frequencies to cover longer distances.

Sidewalk now provides [coverage to more than 90% of the US population](https://coverage.sidewalk.amazon/) and supports long-range connected solutions for communities and enterprises. Users with Ring cameras or Alexa devices that act as a Sidewalk Bridge can choose to contribute a small portion of their internet bandwidth, which is pooled to create a shared network that benefits all Sidewalk-enabled devices in a community.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/27/2025-aws-iot-with-sidewalk.png)

In March 2023, [AWS IoT Core deepened its integration with Amazon Sidewalk](https://aws.amazon.com/about-aws/whats-new/2023/03/aws-iot-core-deepens-integration-amazon-sidewalk/) to seamlessly provision, onboard, and monitor Sidewalk devices with qualified hardware development kits (HDKs), SDKs, and sample applications. As of this writing, AWS IoT Core is the only way for customers to connect the Sidewalk network.

In the [AWS IoT Core console](https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/wireless/devices?tab=sidewalk), you can add your Sidewalk device, provision and register your devices, and connect your Sidewalk endpoint to the cloud. To learn more about onboarding your Sidewalk devices, visit the [Getting started with AWS IoT Core for Amazon Sidewalk](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-getting-started.html) in the AWS IoT Wireless Developer Guide.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/31/2025-aws-iot-with-sidewalk-console.png)

In November 2022, we [announced AWS IoT Core Device Location service](https://aws.amazon.com/about-aws/whats-new/2022/11/aws-iot-core-new-device-location-feature/), a new feature that you can use to get the geo-coordinates of their IoT devices even when the device doesn’t have a GPS module. You can use the Device Location service as a simple request and response HTTP API, or you can use it with IoT connectivity pathways like MQTT, LoRaWAN, and now with Amazon Sidewalk.

In the [AWS IoT Core console](https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/device-location-test), you can test the Device Location service to resolve the location of your device by importing device payload data. Resource location is reported as a GeoJSON payload. To learn more, visit the [AWS IoT Core Device Location](https://docs.aws.amazon.com/iot/latest/developerguide/device-location.html) in the AWS IoT Core Developer Guide.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/28/2025-aws-iot-core-device-location.png)

Customers across multiple industries like automotive, supply chain, and industrial tools have requested a simplified solution such as the Device Location service to extract location-data from Sidewalk products. This would streamline customer software development and give them more options to choose the optimal location source, thereby improving their product.

**Get started with a Device Location integration with Amazon Sidewalk**

To enable Device Location for Sidewalk devices, go to the **AWS IoT Core for Amazon Sidewalk** section under **LPWAN devices** in the [AWS IoT Core console](https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/wireless/devices?tab=sidewalk). Choose **Provision device** or your existing device to edit the setting and select **Activate positioning** in the **Geolocation** option when creating and updating your Sidewalk devices.

While activating position, you need to specify a destination where you want to send your location data. The destination can either be an AWS IoT rule or an MQTT topic.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/31/2025-aws-iot-with-sidewalk-location-1-1.png)

Here is a sample [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli) command to enable position while provisioning a new Sidewalk device:

```
$ aws iotwireless createwireless device --type Sidewalk \
  --name "demo-1" --destination-name "New-1" \
  --positioning Enabled
```

After your Sidewalk device establishes a connection to the Amazon Sidewalk network, the device SDK will send the GNSS-, Wi-Fi- or BLE-based information to AWS IoT Core for Amazon Sidewalk. If the customer has enabled Positioning, then AWS IoT Core Device Location will resolve the location data and send the location data to the specified Destination. After your Sidewalk device transmits location measurement data, the resolved geographic coordinates and a map pin will also be displayed in the Position section for the selected device.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/10/31/2025-aws-iot-with-sidewalk-location-2.png)

You will also get location information delivered to your destination in GeoJSON format, as shown in the following example:

```
{
    "coordinates": [
        13.376076698303223,
        52.51823043823242
    ],
    "type": "Point",
    "properties": {
        "verticalAccuracy": 45,
        "verticalConfidenceLevel": 0.68,
        "horizontalAccuracy": 303,
        "horizontalConfidenceLevel": 0.68,
        "country": "USA",
        "state": "CA",
        "city": "Sunnyvale",
        "postalCode": "91234",
        "timestamp": "2025-11-18T12:23:58.189Z"
    }
}
```

You can monitor the Device Location data between your Sidewalk devices and AWS Cloud by enabling [Amazon CloudWatch Logs for AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/cloud-watch-logs.html). To learn more, visit the [AWS IoT Core for Amazon Sidewalk](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk.html) in the AWS IoT Wireless Developer Guide.

**Now available**

AWS IoT Core Device Location integration with Amazon Sidewalk is now generally available in the US East (N. Virginia) Region. To learn more about use cases, documentation, sample codes, and partner devices, visit the [AWS IoT Core for Amazon Sidewalk product page](https://aws.amazon.com/iot-core/sidewalk/).

Give it a try in the [AWS IoT Core console](https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/wireless/devices?tab=sidewalk) and send feedback to [AWS re:Post for AWS IoT Core](https://repost.aws/tags/TA-HbE5sc6Si6BzWWIPv4LfQ/aws-iot-core) or through your usual AWS Support contacts.

— [Channy](https://linkedin.com/in/channy/)

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