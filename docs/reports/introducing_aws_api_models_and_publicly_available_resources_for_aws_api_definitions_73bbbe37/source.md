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

# Introducing AWS API models and publicly available resources for AWS API definitions

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 05 JUN 2025 in [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Developer Tools](https://aws.amazon.com/blogs/aws/category/developer-tools/ "View all posts in Developer Tools"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/introducing-aws-api-models-and-publicly-available-resources-for-aws-api-definitions/)  [Comments](https://aws.amazon.com/blogs/aws/introducing-aws-api-models-and-publicly-available-resources-for-aws-api-definitions/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Today, we’re announcing a new publicly available source of API models for [Amazon Web Services (AWS)](https://aws.amazon.com/). We are now publishing AWS API models on a daily basis to [Maven Central](https://central.sonatype.com/search?namespace=software.amazon.api.models&sort=name) and providing open source access to a new repository on [GitHub](https://github.com/aws/api-models-aws). This repository includes a definitive, up-to-date source of [Smithy API models](https://smithy.io/) that define AWS public interface definitions and behaviors.

These Smithy models can be used to better understand AWS services and build developer tools like custom SDKs and command line interfaces (CLIs) for connecting to AWS or testing tools for validating your application integrations on AWS.

Since 2018, we have been generating SDK clients and CLI tools using [Smithy models](https://aws.amazon.com/blogs/developer/tag/smithy/). All AWS services are modeled in Smithy to thoroughly document the API contract including operations and behaviors like protocols, authentication, request and response types, and errors.

With this public resource, you can build and test your own applications that can integrate directly with AWS services with confidence such as:

* **Generate SDK clients** – You can build your own, purpose-built SDKs for language communities without [official AWS SDK support](https://docs.aws.amazon.com/sdkref/latest/guide/version-support-matrix.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and client code generator using Smithy toolchain to [generate client SDK libraries](https://smithy.io/2.0/tutorials/full-stack-tutorial.html#generating-the-client).
* **Generating API implementations** – You can generate server stubs for language-specific framework, even [model context protocol (MCP)](https://modelcontextprotocol.io/introduction) server configurations for your AI agents. You have built-in validation to ensure you adhere to your own API standards.
* **Build your own developer tools** – You can build your own tools on top of AWS such as mock testing tools, IAM policy generators, or higher-level abstractions for connecting to AWS.
* **Understand AWS API behaviors** – You can concisely and easily investigate your artifact to quickly review and understand how SDKs interpret API calls and the behaviors to expect with those calls.

**Learn about AWS API models**

You can browse the AWS service models directly on GitHub by accessing the `api-models-aws` repository. This repository contains Smithy models with the [JSON AST](https://smithy.io/2.0/spec/json-ast.html) format for all public AWS API services. All Smithy models consist of shapes and traits. [Shapes](https://smithy.io/2.0/spec/model.html#shapes) are instances of `types` and [traits](https://smithy.io/2.0/spec/model.html#traits) are used to add more information to shapes that might be useful for clients, servers, or documentation.

The AWS models repository contains:

* Top-level service directories are named using the `<sdk-id>` of the service, where `<sdk-id>` is the value of the model’s [sdkId](https://smithy.io/2.0/aws/aws-core.html#sdkid), lowercased and with spaces converted to hyphens
* Each service directory contains one directory per `<version>` of the service, where `<version>` is the value of the service shape’s [version property](https://smithy.io/2.0/spec/service-types.html#service).
* Contained within a service-version directory, a model file named <`sdk-id>-<version>.json` will be present

For example, when you want to define a `RunInstances` API in [Amazon EC2](https://aws.amazon.com/ec2) service, the model uses `service` type, an entry point of an API that aggregates resources and operations together. The shape referenced by a member is called its `target`.

```
com.amazonaws.ec2#AmazonEC2": {
      "type": "service",
      "version": "2016-11-15",
      "operations": [
....
        {
          "target": "com.amazonaws.ec2#RunInstances"
        },
....
	  ]
```

The `operation` type represents the input, output, traits, and possible errors of an API operation. Operation shapes are bound to [resource](https://smithy.io/2.0/spec/service-types.html#resource) shapes and [service](https://smithy.io/2.0/spec/service-types.html#service) shapes. An operation is defined in the IDL using an [operation\_statement](https://smithy.io/2.0/spec/idl.html#idl-operation). In the traits, you can find detailed API information such as documentation, examples, and so on.

```
"com.amazonaws.ec2#RunInstances": {
      "type": "operation",
      "input": {
        "target": "com.amazonaws.ec2#RunInstancesRequest"
      },
      "output": {
        "target": "com.amazonaws.ec2#Reservation"
      },
      "traits": {
        "smithy.api#documentation": "<p>Launches the specified number of instances using an AMI for which you have....",
        smithy.api#examples": [
          {
            "title": "To launch an instance",
            "documentation": "This example launches an instance using the specified AMI, instance type, security group, subnet, block device mapping, and tags.",
            "input": {
              "BlockDeviceMappings": [
                {
                  "DeviceName": "/dev/sdh",
                  "Ebs": {
                    "VolumeSize": 100
                  }
                }
              ],
              "ImageId": "ami-abc12345",
              "InstanceType": "t2.micro",
              "KeyName": "my-key-pair",
              "MaxCount": 1,
              "MinCount": 1,
              "SecurityGroupIds": [
                "sg-1a2b3c4d"
              ],
              "SubnetId": "subnet-6e7f829e",
              "TagSpecifications": [
                {
                  "ResourceType": "instance",
                  "Tags": [
                    {
                      "Key": "Purpose",
                      "Value": "test"
                    }
                  ]
                }
              ]
            },
            "output": {}
          }
        ]
      }
    },
```

We use Smithy extensively to model our service APIs and provide the daily releases of the [AWS SDKs](https://aws.amazon.com/developer/tools/) and [AWS CLI](https://aws.amazon.com/cli/). AWS API models can be helpful for implementing server stubs to interact with AWS services.

**How to build with AWS API models** Smithy API models provide [building resources](https://github.com/smithy-lang/awesome-smithy) such as build tools, client or server code generators, IDE support, and implementations. For example, with [Smithy CLI](https://smithy.io/2.0/guides/smithy-cli/index.html), you can easily build your models, run ad-hoc validation, compare models for differences, query models, and more. The Smithy CLI makes it easy to get started working with Smithy without setting up Java or using the [Smithy Gradle Plugins](https://smithy.io/2.0/guides/gradle-plugin/index.html#smithy-gradle-plugin).

I want to show two examples how to build your own applications with AWS API models and Smithy build tools.

* **Build a minimal SDK client** – This sample project provides a template to get started using [Smithy TypeScript](https://github.com/smithy-lang/smithy-typescript/) to create a minimal AWS SDK client for Amazon DynamoDB. You can build the minimal SDK from the Smithy model, and then run the example code. To learn more, visit the [example project](https://github.com/smithy-lang/smithy-examples/tree/main/smithy-typescript-examples/minimal-aws-sdk-client) here.
* **Build MCP servers** – This sample project provides a template to generate a fat jar which contains all the dependencies required to run an MCP `StdIO` server using the Smithy CLI. You can find `MCPServerExample` to build an MCP server by modeling tools as Smithy APIs and `ProxyMCPExample` to create a proxy MCP Server for any Smithy service. To learn more, visit the [GitHub repository](https://github.com/smithy-lang/smithy-java/tree/main/examples/mcp-server).

**Now available** You can now access AWS API models on a daily basis providing open-source access on the [AWS API models repository](https://github.com/aws/api-models-aws) and service model packages available on [Maven Central](https://central.sonatype.com/search?namespace=software.amazon.api.models&sort=name). You can import models and add dependencies using the maven package of your choice.

To learn more about the AWS preferred API modeling language, visit [Smithy.io](https://smithy.io/) and its [code generation guide](https://smithy.io/2.0/guides/using-code-generation/index.html). To learn more each AWS SDKs, visit [Tools to Build on AWS](https://aws.amazon.com/developer/tools/) and its [respective repository](https://github.com/aws) for SDK specific support or through your usual AWS Support contacts.

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