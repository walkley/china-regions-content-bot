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

# Using Load Balancer Capacity Unit Reservation to prepare for sharp increases in traffic

by Petar Staev and Jon Zobrist on 28 JAN 2025 in [Elastic Load Balancing](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/elastic-load-balancing/ "View all posts in Elastic Load Balancing"), [Foundational (100)](https://aws.amazon.com/blogs/networking-and-content-delivery/category/learning-levels/foundational-100/ "View all posts in Foundational (100)"), [Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/ "View all posts in Networking & Content Delivery"), [Technical How-to](https://aws.amazon.com/blogs/networking-and-content-delivery/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/networking-and-content-delivery/using-load-balancer-capacity-unit-reservation-to-prepare-for-sharp-increases-in-traffic/) Share

## **Introduction**

In this post we explore the new Load Balancer Capacity Unit Reservation (LCU Reservation) feature of Application and Network Load Balancers (ALBs and NLBs). It allows you to prepare for sharp increases in traffic due to planned events such as a new product launch, sale, traffic migration, and more. [Elastic Load Balancers](https://aws.amazon.com/elasticloadbalancing/) (ELBs) scale automatically to support virtually any workload. When we talk about scaling, we are really talking about two things: the rate of scaling and the overall scaling capacity. The LCU Reservation feature is about the rate, for information about the overall capacity checkout this [post on scaling your ELBs with large workloads](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-strategies-for-elastic-load-balancing/). Here we cover what the feature is and how to use it, and share next steps you can take to get started using LCU Reservation!

Until the launch of the LCU Reservation feature, we offered users the capability of opening a support case to proactively scale their load balancer in preparation for an event, otherwise known as “prewarming” a load balancer. Now LCU Reservation gives users direct access to reserve the capacity of their load balancers without the need to open a support case.

To better understand when and how you might want to use LCU Reservation, we go over how ELB products scale dynamically. The underlying infrastructure design and scaling for ELB products use two different scaling systems: one for ALB, and a second one for NLB. If you are already familiar with the ELB scaling systems strategy, then you can skip ahead to the LCU Reservation section.

## **ELB scaling**

ALB and NLB both scale reactively based on the detected volume of traffic, but each one uses different dimensions. ALB scales on every dimension of traffic, including bandwidth, connection rate, and concurrency, and the expense of any additional processing needed for features you are using such as [AWS WAF](https://aws.amazon.com/waf/) or [AWS Lambda](https://aws.amazon.com/lambda/). On the other hand, NLB scales on every dimension of bandwidth.

For both ALB and NLB, LCU Reservation only affects the minimum capacity that is provisioned. It does not, and cannot, prevent or block additional scaling above what you requested. Therefore, if you set a capacity and notice that your load balancer is still scaling, then don’t worry, it’s the scaling system taking care of your workload.

ALB and NLB have different rates that they can scale because they’re built on different technology. In the following section, we briefly go over the specifics for each product.

### **ALB scaling**

ALB can scale to accommodate virtually any workloads, but in some cases we recommend distributing the traffic over more than one load balancer to reduce the blast radius. This process is called ELB Sharding and you can find more information in the AWS post, [Scaling strategies for Elastic Load Balancing](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-strategies-for-elastic-load-balancing/).

ALB scales to adapt to the current workload automatically and scales up/out aggressively, while scaling down/in is conservative. For smaller workloads, ALB scales by using larger capacity nodes (scaling up), and for larger workloads the scaling is achieved by adding more nodes to work in parallel (scaling out).

You can expect your ALB to scale up to support doubling your workload in five minutes. For example, an ALB handling one Gbps of traffic can be increased to two Gbps within five minutes, then to four Gbps in the next five minutes, and so on. This also applies for other dimensions of your traffic, such as the rate of new connections, and the total number of concurrent connections.

### **NLB scaling**

NLB can scale to accommodate most workloads. However, in rare cases a specific workload may need to be spread over more than one load balancer. As previously described, this is called ELB Sharding and you can find more information in the AWS post, [Scaling strategies for Elastic Load Balancing](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-strategies-for-elastic-load-balancing/).

The NLB scaling system works differently when compared with ALB. An NLB consists of a single independent Hyperplane elastic network interface (ENI) per selected subnet/[Availability Zone (AZ),](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) which in the background is backed by multiple independent high-capacity nodes. This allows the IPs of those ENIs to be static and scaling activity to be transparent to the client by not changing the IP, as opposed to ALB.

NLB scales based on every dimension of bandwidth to accurately provision the necessary capacity for your workload. Your NLB starts out with three Gbps of capacity and scales up at a rate of increase of three Gbps more per minute.

## **What is LCU Reservation?**

As mentioned in the previous section, the ELB scaling system has been designed to react quickly to changes in the workload to provide sufficient capacity to handle the increase for most cases. However, there may be situations where large traffic spikes may increase the traffic faster than the recommended growth rate. The LCU Reservation feature was implemented for these cases.

LCU Reservation is a proactive mechanism to scale your ELB ahead of time in preparation for events such as seasonal events, event ticket sales, new product/feature launches, or a new episode release of a popular show. LCU Reservation works in parallel with the ELB reactive scaling system that we described in the previous section to provide sufficient capacity for your workload.

ALB and NLB with TCP and/or UDP listeners support this new feature.

As well as preparing for a single event, LCU Reservation can be used to provide a constant minimum capacity for use cases where traffic spikes can’t be predicted. Our recommended approach is to use [ELB Sharding](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-strategies-for-elastic-load-balancing/).

### **How does it work?**

The LCU Reservation feature offers the ability to set a minimum capacity for your load balancer and allocate the requested capacity to your load balancer in advance of an expected spike. When the minimum capacity is provisioned, the scaling system continues to increase or decrease your load balancer’s capacity based on the actual traffic. These scaling activities will not reduce the capacity beneath the minimum capacity you specified.

### **Estimating capacity**

[![The Capacity tab in the AWS Console for ELB displays historic usage in terms of LCU.](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/22/Screenshot-2024-11-13-125151outline-1024x616.png)](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/22/Screenshot-2024-11-13-125151outline.png)

Figure 1: LCU Reservation panel with usage graph

To streamline the estimation process for ALB, the [AWS Management Console](https://aws.amazon.com/console/) displays a new metric called “PeakLCUs” (Figure 1), while for NLB it provides an LCU Usage graph that converts the existing ProcessedBytes metric into an hourly LCU value. The PeakLCUs metric accounts for peaks in your traffic pattern that the load balancer must scale across all scaling dimensions to support your workload. These two metrics show the usage of the load balancer for a given period. Those values can be used directly as an input into the LCU Reservation field if you are expecting the same workload/event to repeat.

The easiest way to determine how much capacity to provision is through the Console. If you have the workload already on an ALB or NLB, then you can use their metrics from a period when you had similar load and possibly with a multiplier for how much larger you expect the traffic to be.

You can also use the metrics in the [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) console. For ALB you can look at the one-minute sum of PeakLCUs for the period if available, and use the highest value, or you can also use the following formula for one-hour data points: PeakLCUs(max) \* ( PeakLCUs(sample count) \* 60 / PERIOD(PeakLCUs) ), multiplying it by the scale of increase you expect for this event. For example, if you are expecting five times more load, then you multiply this by five.

For NLB the LCU Usage metric is derived in a two-step process. The first step is converting your traffic into a rate in Megabits per second (Mbps). This can be done by converting the ProcessedBytes metric into a rate by using the formula: ProcessedBytes(per min) \* 8/60/(10^6). The second step is to divide the resulting value by 2.2. 2.2 (Mbps) is the equivalent of one GB transferred over the course of one hour, which is equal to one LCU.

The best way to calculate the capacity you need is to perform a load test on the load balancer and use the resulting PeakLCUs (ALB) or ProcessedBytes (NLB) metric with the aforementioned formula.

We recommend not using the metric “ConsumedLCUs” for calculating capacity, as it is only intended for billing purposes and only the metrics discussed previously should be used for capacity estimation.

To learn more, refer to the [ALB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/capacity-unit-reservation.html) and [NLB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/capacity-unit-reservation.html).

### **How to set LCU Reservation?**

You can set the LCU Reservation by using either the Console or the [AWS Command Line Interface (AWS CLI).](https://aws.amazon.com/cli/)

In the Console, you can select your load balancer and open the new Capacity tab. In this new section you can see the relevant information regarding the selected load balancer and its LCU Reservation. Then, select the **Edit LCU Reservation** button as pictured in Figure 2.

[![In the Capacity tab of the AWS Console for ELB a user can select the Edit LCU Reservation button to modify the desired capacity](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/22/Screenshot-2024-11-12-144600-1024x365.png)](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/22/Screenshot-2024-11-12-144600.png)

Figure 2: Edit LCU Reservation button within the Capacity tab

This takes you to the Edit LCU Reservation menu (Figure 3) where you can select whether you’d like to use a Historic-reference based estimate or a Manual estimate. In this example I have used the Historic-reference based estimate, which allows me to see the PeakLCUs during a previous event. I then used that metric as a reference to prepare for the next event.

[![When editing an LCU Reservation users can select to reference a past event or manually estimate the expected traffic.](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/22/Screenshot-2024-11-12-145432-1024x626.png)](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/22/Screenshot-2024-11-12-145432.png)

Figure 3: PeakLCUs usage graph in red with Reserved LCU displayed in green

To learn more, refer to the [ALB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/request-capacity-unit-reservation.html) and [NLB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/request-capacity-unit-reservation.html).

**AWS CLI

 [ALB/NLB]** aws elbv2 modify-capacity-reservation –load-balancer-arn <ALB/NLB ARN> –minimum-load-balancer-capacity CapacityUnits=267

***Output ALB***

```
{
    "CapacityReservationState": [
        {
            "AvailabilityZone": "us-east-1a",
            "State": {
                "Code": "pending"
            }
        },
        {
            "AvailabilityZone": "us-east-1b",
            "State": {
                "Code": "pending"
            }
        },
        {
            "AvailabilityZone": "us-east-1c",
            "State": {
                "Code": "pending"
            }
        }
    ],
    "DecreaseRequestsRemaining": 2,
    "LastModifiedTime": "2024-11-13T23:58:08.613000+00:00",
    "MinimumLoadBalancerCapacity": {
        "CapacityUnits": 267
    }
}
```

***Output NLB***

```
{
    "CapacityReservationState": [
        {
            "AvailabilityZone": "eu-north-1a",
            "State": {
                "Code": "pending"
            }
        },
        {
            "AvailabilityZone": "eu-north-1b",
            "State": {
                "Code": "pending"
            }
        },
        {
            "AvailabilityZone": "eu-north-1c",
            "State": {
                "Code": "pending"
            }
        }
    ],
    "DecreaseRequestsRemaining": 2,
    "LastModifiedTime": "2024-11-13T23:32:55.002000+00:00",
    "MinimumLoadBalancerCapacity": {
        "CapacityUnits": 9000
    }
}
```

### **How do I know when the reserved capacity is ready to use?**

You can find when the reserved capacity is ready to use by using either the Console or the AWS CLI.

In the Console you can select your load balancer and open the **new Capacity** tab. In the **Reservation** status, you can see that our request has been successfully completed and is in the **Provisioned** status as shown in Figure 4.

[![The Capacity tab in the AWS Console for ELB displays the current reservation status.](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/22/Screenshot-2024-11-12-144025-1024x625.png)](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/22/Screenshot-2024-11-12-144025.png)

Figure 4: LCU Reservation status displayed in the Capacity tab

To learn more, refer to the [ALB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/monitor-capacity-unit-reservation.html) and [NLB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/monitor-capacity-unit-reservation.html).

**AWS CLI

 [ALB/NLB]** aws elbv2 describe-capacity-reservation –load-balancer-arn <ALB/NLB ARN>

Output ALB

```
{
    "CapacityReservationState": [
        {
            "AvailabilityZone": "us-east-1a",
            "EffectiveCapacityUnits": 89.0,
            "State": {
                "Code": "provisioned"
            }
        },
        {
            "AvailabilityZone": "us-east-1b",
            "EffectiveCapacityUnits": 89.0,
            "State": {
                "Code": "provisioned"
            }
        },
        {
            "AvailabilityZone": "us-east-1c",
            "EffectiveCapacityUnits": 89.0,
            "State": {
                "Code": "provisioned"
            }
        }
    ],
    "DecreaseRequestsRemaining": 2,
    "LastModifiedTime": "2024-11-13T23:53:04.690000+00:00",
    "MinimumLoadBalancerCapacity": {
        "CapacityUnits": 267
    }
}
```

Output NLB

```
{
    "CapacityReservationState": [
        {
            "AvailabilityZone": "eu-north-1a",
            "EffectiveCapacityUnits": 3000.0,
            "State": {
                "Code": "provisioned"
            }
        },
        {
            "AvailabilityZone": "eu-north-1b",
            "EffectiveCapacityUnits": 3000.0,
            "State": {
                "Code": "provisioned"
            }
        },
        {
            "AvailabilityZone": "eu-north-1c",
            "EffectiveCapacityUnits": 3000.0,
            "State": {
                "Code": "provisioned"
            }
        }
    ],
    "DecreaseRequestsRemaining": 2,
    "LastModifiedTime": "2024-11-13T23:32:55.002000+00:00",
    "MinimumLoadBalancerCapacity": {
        "CapacityUnits": 9000
    }
}
```

### **How do I remove the LCU Reservation?**

You can remove the LCU Reservation by using either the Console or the AWS CLI.

In the Console, you can select your load balancer and then open the **new Capacity** tab. When you have an active LCU Reservation you can then use the **Cancel capacity** button to cancel the reservation as shown in Figure 5.

[![Cancel capacity button is available when LCU Reservation is set](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/30/Screenshot-2024-11-12-152047.png)](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/30/Screenshot-2024-11-12-152047.png)

Figure 5: Cancel capacity button is available when LCU Reservation is set

To learn more, refer to the [ALB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/update-capacity-unit-reservation.html) and [NLB Documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/update-capacity-unit-reservation.html).

**AWS CLI

 [ALB/NLB]** aws elbv2 modify-capacity-reservation –load-balancer-arn <ALB/NLB ARN> –reset-capacity-reservation

Output ALB

```
{
    "CapacityReservationState": [
        {
            "AvailabilityZone": "us-east-1a",
            "State": {
                "Code": "pending"
            }
        },
        {
            "AvailabilityZone": "us-east-1b",
            "State": {
                "Code": "pending"
            }
        },
        {
            "AvailabilityZone": "us-east-1c",
            "State": {
                "Code": "pending"
            }
        }
    ],
    "DecreaseRequestsRemaining": 1,
    "LastModifiedTime": "2024-11-13T23:58:08.613000+00:00",
    "MinimumLoadBalancerCapacity": {
        "CapacityUnits": 0
    }
}
```

Output NLB

```
{
    "CapacityReservationState": [
        {
            "AvailabilityZone": "eu-north-1a",
            "State": {
                "Code": "pending"
            }
        },
        {
            "AvailabilityZone": "eu-north-1b",
            "State": {
                "Code": "pending"
            }
        },
        {
            "AvailabilityZone": "eu-north-1c",
            "State": {
                "Code": "pending"
            }
        }
    ],
    "DecreaseRequestsRemaining": 1,
    "LastModifiedTime": "2024-11-13T23:58:08.613000+00:00",
    "MinimumLoadBalancerCapacity": {
        "CapacityUnits": 0
    }
}
```

## **Considerations**

* The LCU Reservation feature is intended to be used in short intervals, when you know traffic is going to potentially increase faster than scaling systems can react. We expect you to set it for short periods, such as a few hours, and occasionally longer periods, such as a few days.
* Sharding may be a more appropriate and cost-effective long-term strategy for use cases with unpredictable spikes in usage. Using multiple load balancers to distribute the incoming workload helps by allocating smaller portions of the overall traffic to each load balancer. This approach also benefits from the concurrent scaling capability of having multiple load balancers.
* LCU Reservation is billed for the amount of reserved capacity. For example, if you provision 100 LCU for one hour and you use 120 LCU constantly for that one hour, then 20 LCU are charged at the standard LCU pricing and 100 LCU are charged at the Reserved LCU pricing.
* LCU Reservation capacity is reserved at the regional level and is evenly distributed across AZs. We recommend provisioning an equal number of targets in each AZ and making sure there are no AZs without registered targets.
* When using LCU Reservation, you’re always configuring at the load balancer level, and ELB systems provision the desired capacity evenly between all active AZs. AZs without any registered targets aren’t included in the provisioning process. However, the ELB system still provisions enough capacity in the remaining AZs to match your request fully.
* When LCU Reservation is set on your load balancer, further capacity that is dedicated to your load balancer is provisioned. Capacity that is provisioned is charged at the Reserved LCU rate. Therefore, you must have accurate capacity estimations, and remove the provisioned capacity after your event concludes or when it is no longer needed.
* LCU Reservation can be used for use cases that need permanent minimum capacity to be available due to contractual obligations/SLA/policy requirements. However, you should estimate the cost ahead of time if a large amount of that capacity isn’t going to be highly used.

## Conclusion

LCU Reservation is an exciting new feature that provides users with more control over their load balancer’s minimum capacity. It can be used to proactively increase the capacity in anticipation of large sudden bursts of traffic, usually associated with seasonal events, sales promotions, or launching a new product/feature.

LCU Reservation works in parallel to the ELB scaling system. Understanding and combining dynamic scaling with LCU Reservation is recommended for optimal use.

ELB continues to increase capacity if needed while LCU Reservation is set, but it doesn’t reduce capacity lower than the reserved LCU.

We recommend reviewing the AWS post, [Scaling strategies for Elastic Load Balancing](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-strategies-for-elastic-load-balancing/), to better understand when sharding may be a more suitable choice.

***A correction was made on January 30, 2025:** An earlier version of this post was missing Figure 5.*

## About the authors

![Petar Staev](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/23/profile-badge-picture-square-Custom.jpg)

### Petar Staev

Petar Staev is a Senior Customer Success Engineer at AWS, working at the Application Networking team based in Dublin. He specializes in Networking and helps customers design highly-available and resilient architectures. In his free time, he enjoys tinkering with his smart home automation project or playing video games.

![Jon Zobrist](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/01/23/Screenshot-2025-01-23-174253.png)

### Jon Zobrist

Jon Zobrist is the head of Customer Success for Application Networking and is based in Seattle, where he helps customers and those supporting them. He loves being involved with people solving complex problems. In his spare time he hangs out with his many cats and dogs.

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