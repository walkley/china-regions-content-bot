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

# Amazon Nova Reel 1.1: Featuring up to 2-minutes multi-shot videos

by Elizabeth Fuentes on 07 APR 2025 in [Amazon Nova](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-nova/ "View all posts in Amazon Nova"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/amazon-nova-reel-1-1-featuring-up-to-2-minutes-multi-shot-videos/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

At re:Invent 2024, we [announced Amazon Nova models](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-frontier-intelligence-and-industry-leading-price-performance/), a new generation of [foundation models (FMs),](https://aws.amazon.com/what-is/foundation-models/) including [Amazon Nova Reel](https://docs.aws.amazon.com/ai/responsible-ai/nova-reel/overview.html), a video generation model that creates short videos from text descriptions and optional reference images (together, the “prompt”).

Today, we introduce [Amazon Nova Reel 1.1](https://docs.aws.amazon.com/ai/responsible-ai/nova-reel/overview.html), which provides quality and latency improvements in 6-second single-shot video generation, compared to Amazon Nova Reel 1.0. This update lets you generate multi-shot videos up to 2-minutes in length with consistent style across shots. You can either provide a single prompt for up to a 2-minute video composed of 6-second shots, or design each shot individually with custom prompts. This gives you new ways to create video content through [Amazon Bedrock](https://aws.amazon.com/es/bedrock/?trk=fccf147c-636d-45bf-bf0a-7ab087d5691a&sc_channel=el).

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/awsnews-1526_Underwater%20Racoon.mp4?_=1)

Amazon Nova Reel enhances creative productivity, while helping to reduce the time and cost of video production using [generative AI](https://aws.amazon.com/ai/generative-ai/?trk=fccf147c-636d-45bf-bf0a-7ab087d5691a&sc_channel=el). You can use Amazon Nova Reel to create compelling videos for your marketing campaigns, product designs, and social media content with increased efficiency and creative control. For example, in advertising campaigns, you can produce high-quality video commercials with consistent visuals and timing using natural language.

**To get started with Amazon Nova Reel 1.1**

If you’re new to using [Amazon Nova Reel models](https://aws.amazon.com/ai/generative-ai/nova/creative/), go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock), choose **Model access** in the navigation panel and request access to the **Amazon Nova Reel** model. When you get access to Amazon Nova Reel, it applies both to 1.0 and 1.1.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/07/2025-nova-reel-1.1-access-1024x645.png)

After gaining access, you can try **Amazon** **Nova Reel 1.1** directly from the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock), AWS SDK, or [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=fccf147c-636d-45bf-bf0a-7ab087d5691a&sc_channel=el).

To test the **Amazon Nova Reel 1.1** model in the console, choose **Image/Video** under **Playgrounds** in the left menu pane. Then choose **Nova Reel 1.1** as the model and input your prompt to generate video.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/07/2025-nova-reel-1.1-playground-1024x553.png)

Amazon Nova Reel 1.1 offers two modes:

* **Multishot Automated –** In this mode, Amazon Nova Reel 1.1 accepts a single prompt of up to 4,000 characters and produces a multi-shot video that reflects that prompt. This mode doesn’t accept an input image.
* ******Multishot Manual –****** For those who desire more direct control over a video’s shot composition, with manual mode (also referred to as storyboard mode), you can specify a unique prompt for each individual shot. This mode does accept an optional starting image for each shot. Images must have a resolution of 1280×720. You can provide images in base64 format or from an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) location.

For this demo, I use the [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/) to invoke the model using the [Amazon Bedrock API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Scenario_AmazonNova_TextToVideo_section.html) and [StartAsyncInvoke operation](https://docs.aws.amazon.com/nova/latest/userguide/video-gen-access.html#video-gen-start-a-job) to start an asynchronous invocation and generate the video. I used [GetAsyncInvoke](https://docs.aws.amazon.com/nova/latest/userguide/video-gen-access.html#video-gen-check-progress) to check on the progress of a video generation job.

This Python script creates a 120-second video using `MULTI_SHOT_AUTOMATED`mode as [TaskType parameter](https://docs.aws.amazon.com/nova/latest/userguide/video-gen-access.html#video-gen-input-params) from this text prompt, created by [Nitin Eusebius](https://www.linkedin.com/in/nitinbeusebius/).

```
import random
import time

import boto3

AWS_REGION = "us-east-1"
MODEL_ID = "amazon.nova-reel-v1:1"
SLEEP_SECONDS = 15  # Interval at which to check video gen progress
S3_DESTINATION_BUCKET = "s3://<your bucket here>"

video_prompt_automated = "Norwegian fjord with still water reflecting mountains in perfect symmetry. Uninhabited wilderness of Giant sequoia forest with sunlight filtering between massive trunks. Sahara desert sand dunes with perfect ripple patterns. Alpine lake with crystal clear water and mountain reflection. Ancient redwood tree with detailed bark texture. Arctic ice cave with blue ice walls and ceiling. Bioluminescent plankton on beach shore at night. Bolivian salt flats with perfect sky reflection. Bamboo forest with tall stalks in filtered light. Cherry blossom grove against blue sky. Lavender field with purple rows to horizon. Autumn forest with red and gold leaves. Tropical coral reef with fish and colorful coral. Antelope Canyon with light beams through narrow passages. Banff lake with turquoise water and mountain backdrop. Joshua Tree desert at sunset with silhouetted trees. Iceland moss- covered lava field. Amazon lily pads with perfect symmetry. Hawaiian volcanic landscape with lava rock. New Zealand glowworm cave with blue ceiling lights. 8K nature photography, professional landscape lighting, no movement transitions, perfect exposure for each environment, natural color grading"

bedrock_runtime = boto3.client("bedrock-runtime", region_name=AWS_REGION)
model_input = {
    "taskType": "MULTI_SHOT_AUTOMATED",
    "multiShotAutomatedParams": {"text": video_prompt_automated},
    "videoGenerationConfig": {
        "durationSeconds": 120,  # Must be a multiple of 6 in range [12, 120]
        "fps": 24,
        "dimension": "1280x720",
        "seed": random.randint(0, 2147483648),
    },
}

invocation = bedrock_runtime.start_async_invoke(
    modelId=MODEL_ID,
    modelInput=model_input,
    outputDataConfig={"s3OutputDataConfig": {"s3Uri": S3_DESTINATION_BUCKET}},
)

invocation_arn = invocation["invocationArn"]
job_id = invocation_arn.split("/")[-1]
s3_location = f"{S3_DESTINATION_BUCKET}/{job_id}"
print(f"\nMonitoring job folder: {s3_location}")

while True:
    response = bedrock_runtime.get_async_invoke(invocationArn=invocation_arn)
    status = response["status"]
    print(f"Status: {status}")
    if status != "InProgress":
        break
    time.sleep(SLEEP_SECONDS)

if status == "Completed":
    print(f"\nVideo is ready at {s3_location}/output.mp4")
else:
    print(f"\nVideo generation status: {status}")
```

After the first invocation, the script periodically checks the status until the creation of the video has been completed. I pass a random seed to get a different result each time the code runs.

I run the script:

```
Status: InProgress
. . .
Status: Completed
Video is ready at s3://<your bucket here>/<job_id>/output.mp4
```

After a few minutes, the script is completed and prints the output Amazon S3 location. I download the output video using the AWS CLI:

```
aws s3 cp s3://<your bucket here>/<job_id>/output.mp4 output_automated.mp4
```

This is the video that this prompt generated:

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/awsnews-1526_Natural-Wonders.mp4?_=2)

In the case of `MULTI_SHOT_MANUAL` mode as TaskType parameter, with a prompt for multiples shots and a description for each shot, it is not necessary to add the variable `durationSeconds.`

Using the prompt for multiples shots, created by Sanju Sunny.

I run Python script:

```
import random
import time

import boto3

def image_to_base64(image_path: str):
    """
    Helper function which converts an image file to a base64 encoded string.
    """
    import base64

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode("utf-8")

AWS_REGION = "us-east-1"
MODEL_ID = "amazon.nova-reel-v1:1"
SLEEP_SECONDS = 15  # Interval at which to check video gen progress
S3_DESTINATION_BUCKET = "s3://<your bucket here>"

video_shot_prompts = [
    # Example of using an S3 image in a shot.
    {
        "text": "Epic aerial rise revealing the landscape, dramatic documentary style with dark atmospheric mood",
        "image": {
            "format": "png",
            "source": {
                "s3Location": {"uri": "s3://<your bucket here>/images/arctic_1.png"}
            },
        },
    },
    # Example of using a locally saved image in a shot
    {
        "text": "Sweeping drone shot across surface, cracks forming in ice, morning sunlight casting long shadows, documentary style",
        "image": {
            "format": "png",
            "source": {"bytes": image_to_base64("arctic_2.png")},
        },
    },
    {
        "text": "Epic aerial shot slowly soaring forward over the glacier's surface, revealing vast ice formations, cinematic drone perspective",
        "image": {
            "format": "png",
            "source": {"bytes": image_to_base64("arctic_3.png")},
        },
    },
    {
        "text": "Aerial shot slowly descending from high above, revealing the lone penguin's journey through the stark ice landscape, artic smoke washes over the land, nature documentary styled",
        "image": {
            "format": "png",
            "source": {"bytes": image_to_base64("arctic_4.png")},
        },
    },
    {
        "text": "Colossal wide shot of half the glacier face catastrophically collapsing, enormous wall of ice breaking away and crashing into the ocean. Slow motion, camera dramatically pulling back to reveal the massive scale. Monumental waves erupting from impact.",
        "image": {
            "format": "png",
            "source": {"bytes": image_to_base64("arctic_5.png")},
        },
    },
    {
        "text": "Slow motion tracking shot moving parallel to the penguin, with snow and mist swirling dramatically in the foreground and background",
        "image": {
            "format": "png",
            "source": {"bytes": image_to_base64("arctic_6.png")},
        },
    },
    {
        "text": "High-altitude drone descent over pristine glacier, capturing violent fracture chasing the camera, crystalline patterns shattering in slow motion across mirror-like ice, camera smoothly aligning with surface.",
        "image": {
            "format": "png",
            "source": {"bytes": image_to_base64("arctic_7.png")},
        },
    },
    {
        "text": "Epic aerial drone shot slowly pulling back and rising higher, revealing the vast endless ocean surrounding the solitary penguin on the ice float, cinematic reveal",
        "image": {
            "format": "png",
            "source": {"bytes": image_to_base64("arctic_8.png")},
        },
    },
]

bedrock_runtime = boto3.client("bedrock-runtime", region_name=AWS_REGION)
model_input = {
    "taskType": "MULTI_SHOT_MANUAL",
    "multiShotManualParams": {"shots": video_shot_prompts},
    "videoGenerationConfig": {
        "fps": 24,
        "dimension": "1280x720",
        "seed": random.randint(0, 2147483648),
    },
}

invocation = bedrock_runtime.start_async_invoke(
    modelId=MODEL_ID,
    modelInput=model_input,
    outputDataConfig={"s3OutputDataConfig": {"s3Uri": S3_DESTINATION_BUCKET}},
)

invocation_arn = invocation["invocationArn"]
job_id = invocation_arn.split("/")[-1]
s3_location = f"{S3_DESTINATION_BUCKET}/{job_id}"
print(f"\nMonitoring job folder: {s3_location}")

while True:
    response = bedrock_runtime.get_async_invoke(invocationArn=invocation_arn)
    status = response["status"]
    print(f"Status: {status}")
    if status != "InProgress":
        break
    time.sleep(SLEEP_SECONDS)

if status == "Completed":
    print(f"\nVideo is ready at {s3_location}/output.mp4")
else:
    print(f"\nVideo generation status: {status}")
```

As in the previous demo, after a few minutes, I download the output using the AWS CLI:

`aws s3 cp s3://<your bucket here>/<job_id>/output.mp4 output_manual.mp4`

This is the video that this prompt generated:

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/awsnews-1526-Above-Zero.mp4?_=3)

**More creative examples**

When you use Amazon Nova Reel 1.1, you'll discover a world of creative possibilities. Here are some sample prompts to help you begin:

Color Burst, created by [Nitin Eusebius](https://www.linkedin.com/in/nitinbeusebius/)

`prompt = "Explosion of colored powder against black background. Start with slow-motion closeup of single purple powder burst. Dolly out revealing multiple powder clouds in vibrant hues colliding mid-air. Track across spectrum of colors mixing: magenta, yellow, cyan, orange. Zoom in on particles illuminated by sunbeams. Arc shot capturing complete color field. 4K, festival celebration, high-contrast lighting"`

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/awsnews-1526_Colo-Burst.mp4?_=4)

Shape Shifting, created by [Sanju Sunny](https://www.linkedin.com/in/sanju-sunny/)

```
prompt = "A simple red triangle transforms through geometric shapes in a journey of self-discovery. Clean vector graphics against white background. The triangle slides across negative space, morphing smoothly into a circle. Pan left as it encounters a blue square, they perform a geometric dance of shapes. Tracking shot as shapes combine and separate in mathematical precision. Zoom out to reveal a pattern formed by their movements. Limited color palette of primary colors. Precise, mechanical movements with perfect geometric alignments. Transitions use simple wipes and geometric shape reveals. Flat design aesthetic with sharp edges and solid colors. Final scene shows all shapes combining into a complex mandala pattern."
```

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/awsnews-1526_shape.mp4?_=5)

All example videos have music added manually before uploading, by the AWS Video team.

**Things to know**

**Creative control** – You can use this enhanced control for lifestyle and ambient background videos in advertising, marketing, media, and entertainment projects. Customize specific elements such as camera motion and shot content, or animate existing images.

**Modes considerations –** In automated mode, you can write prompts up to 4,000 characters. For manual mode, each shot accepts prompts up to 512 characters, and you can include up to 20 shots in a single video. Consider planning your shots in advance, similar to creating a traditional storyboard. Input images must match the 1280x720 resolution requirement. The service automatically delivers your completed videos to your specified S3 bucket.

**Pricing and availability –** Amazon Nova Reel 1.1 is available in Amazon Bedrock in the US East (N. Virginia) [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). You can access the model through the Amazon Bedrock console, AWS SDK, or AWS CLI. As with all Amazon Bedrock services, pricing follows a pay-as-you-go model based on your usage. For more information, refer to [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

Ready to start creating with Amazon Nova Reel? Visit the [Amazon Nova Reel AWS AI Service Cards](https://docs.aws.amazon.com/ai/responsible-ai/nova-reel/overview.html) to learn more and dive into the [Generating videos with Amazon Nova](https://docs.aws.amazon.com/nova/latest/userguide/video-generation.html). Explore Python code examples in the [Amazon Nova model cookbook repository](https://github.com/aws-samples/amazon-nova-samples), enhance your results using the [Amazon Nova Reel prompting best practices](https://docs.aws.amazon.com/nova/latest/userguide/prompting-video-generation.html), and discover video examples in the [Amazon Nova Reel gallery](https://www.amazon.science/blog/amazon-nova-reel-examples)—complete with the prompts and reference images that brought them to life.

The possibilities are endless, and we look forward to seeing what you create! Join our growing community of builders at [community.aws](https://community.aws/), where you can create your [BuilderID](https://community.aws/builderid?trk=fccf147c-636d-45bf-bf0a-7ab087d5691a&sc_channel=el), share your video generation projects, and connect with fellow innovators.

— [Eli](https://www.linkedin.com/in/lizfue/)

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

![Elizabeth Fuentes](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2024/06/03/Elizabeth-Fuentas.jpeg)

### Elizabeth Fuentes

My mission is to break down complex concepts into easily digestible explanations, inspiring developers to continually expand their skills and knowledge. Through conferences, tutorials, and online resources, I share my expertise with the global developer community, providing them with the tools and confidence to reach their full potential. With a hands-on approach and a commitment to simplifying the complex, I strive to be a catalyst for growth and learning in the world of AWS technology.

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