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

# Luma AI’s Ray2 video model is now available in Amazon Bedrock

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 23 JAN 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/luma-ai-ray-2-video-model-is-now-available-in-amazon-bedrock/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

As we [preannounced](https://press.aboutamazon.com/aws/2024/12/luma-ai-announces-new-video-model-ray-2-will-soon-be-available-to-consumers-professionals-and-developers) at AWS re:Invent 2024, you can now use [Luma AI Ray2 video model in Amazon Bedrock](https://aws.amazon.com/bedrock/luma-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to generate high-quality video clips from text, creating captivating motion graphics from static concepts. AWS is the first and only cloud provider to offer fully managed models from Luma AI.

On January 16, 2025, [Luma AI](https://lumalabs.ai/) introduced [Luma Ray2](https://lumalabs.ai/ray), the large–scale video generative model capable of creating realistic visuals with natural, coherent motion with strong understanding of text instructions. Luma Ray2 exhibits advanced capabilities as a result of being trained on Luma’s new multi-modal architecture. It scales to ten times compute of Ray1, enabling it to produce 5 second or 9 second video clips that show fast coherent motion, ultra-realistic details, and logical event sequences with 540p and 720p resolution.

With Luma Ray2 in [Amazon Bedrock](https://aws.amazon.com/bedrock/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), you can add high-quality, realistic, production-ready videos generated from text in your [generative AI](https://aws.amazon.com/generative-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) application through a single API. Luma Ray2 video model understands the interactions between people, animals, and objects, and you can create consistent and physically accurate characters through state-of-the-art natural language instruction understanding and reasoning.

You can use Ray2 video generations for content creation, entertainment, advertising, and media use cases, streamlining the creative process, from concept to execution. You can generate smooth, cinematic, and lifelike camera movements that match the intended emotion of the scene. You can rapidly experiment with different camera angles and styles and deliver creative outputs for architecture, fashion, film, graphic design, and music.

Let’s take a look at the [impressive video generations](https://youtu.be/lIKRRRhHN2U) by Luma Ray2 that Luma has published.

**Get started with Luma Ray2 model in Amazon Bedrock**

Before getting started, if you are new to using Luma models, go to the [Amazon Bedrock console](https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#modelaccess&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and choose **Model access** on the bottom left pane. To access the latest Luma AI models, request access for Luma Ray2 in Luma AI.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/24/2025-luma-ray2-bedrock-1-enable-model-1.png)

To test the Luma AI model in Amazon Bedrock, choose **Image/Video** under **Playgrounds** in the left menu pane. Choose **Select model**, then select **Luma AI** as the category and **Ray** as the model.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/17/2025-luma-ray2-bedrock-1-choose-model.png)

For video generation models, you should have an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) bucket to store all generated videos. This bucket will be created in your AWS account, and Amazon Bedrock will have read and write permissions for it. Choose **Confirm** to create a bucket and generate a video.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/17/2025-luma-ray2-bedrock-2-creat-s3-bucekt.png)

I will generate a 5-second video with 720P and 24 frames per second with 16:9 aspect ratio for my prompt.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/01/17/2025-luma-ray2-bedrock-3-create-video.png)

Here is an example prompt and generated video. You can download it stored in the S3 bucket.

`a humpback whale swimming through space particles`

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/Ray2-Cosmic+Whale.mp4?_=1)

Here are another featured examples to demonstrate Ray2 model.

Prompt 1: `A miniature baby cat is walking and exploring on the surface of a fingertip`

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/Ray2-A+Miniature+Baby+Cat.mp4?_=2)

Prompt 2: `A massive orb of water floating in a backlit forest`

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/Ray2-Floating+Water+Orb.mp4?_=3)

Prompt 3: `A man plays saxophone` by [@ziguratt](https://x.com/ziguratt)

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/Ray2-Saxophone+Player.mp4?_=4)

Prompt 4: `Macro closeup of a bee pollinating`

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/Ray2-Pollen+Collector.mp4?_=5)

To check out more examples and generated videos, visit the [Luma Ray2](https://lumalabs.ai/ray) page.

By choosing **View API request** in the Bedrock console, you can also access the model using code examples in the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and AWS SDKs. You can use `luma.ray-v2:0` as the model ID.

Here is a sample of the AWS CLI command:

```
aws bedrock-runtime start-async-invoke \
    --region us-west-2 \
    --model-id luma.ray-v2:0 \
    --model-input  "{ \"prompt\": \"a humpback whale swimming through space particles\", \"duration\":\"5s\", \"resolution\": \"540p\", \"aspect_ratio\":\"16:9\"}" \
    --output-data-config "{\"s3OutputDataConfig\": {\"s3Uri\": \"s3:\/\/testing-bucket-ais-region-us-west-2\/\"}}"
```

You can use a [`StartAsyncInvoke` API action](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_StartAsyncInvoke.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to generate videos using [AWS SDKs](https://aws.amazon.com/developer/tools/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) to build your applications using various programming languages.

**Now available**

Luma Ray2 video model is generally available today in Amazon Bedrock in the US West (Oregon) AWS Region. Check the [full Region list](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for future updates. To learn more, check out the [Luma AI in Amazon Bedrock](https://aws.amazon.com/bedrock/luma-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) product page and the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) page.

Give Luma Ray2 a try in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) today, and send feedback to [AWS re:Post for Amazon Bedrock](https://repost.aws/tags/TAQeKlaPaNRQ2tWB6P7KrMag/amazon-bedrock) or through your usual AWS Support contacts.

— [Channy](https://twitter.com/channyun)

***Update January 24, 2025** – The AWS CLI command was fixed to use the `start-async-invoke` parameter instead of `invoke-model`.*

![Channy Yun (윤석찬)](https://d2908q01vomqb2.cloudfront.net/7b52009b64fd0a2a49e6d8a939753077792b0554/2020/06/05/channyun_400x400.jpg)

### [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)")

Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.

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