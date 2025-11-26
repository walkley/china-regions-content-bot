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

# Amazon Nova Canvas update: Virtual try-on and style options now available

by Matheus Guimaraes on 02 JUL 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Nova](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-nova/ "View all posts in Amazon Nova"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Retail](https://aws.amazon.com/blogs/aws/category/industries/retail/ "View all posts in Retail") [Permalink](https://aws.amazon.com/blogs/aws/amazon-nova-canvas-update-virtual-try-on-and-style-options-now-available/)  [Comments](https://aws.amazon.com/blogs/aws/amazon-nova-canvas-update-virtual-try-on-and-style-options-now-available/#Comments)  Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Have you ever wished you could quickly visualize how a new outfit might look on you before making a purchase? Or how a piece of furniture would look in your living room? Today, we’re excited to introduce a new virtual try-on capability in [Amazon Nova Canvas](https://aws.amazon.com/ai/generative-ai/nova/creative??trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) that makes this possible. In addition, we are adding eight new style options for improved style consistency for text-to-image based style prompting. These features expand Nova Canvas AI-powered image generation capabilities making it easier than ever to create realistic product visualizations and stylized images that can enhance the experience of your customers.

Let’s take a quick look at how you can start using these today.

**Getting started**

The first thing is to make sure that you have access to the Nova Canvas model through the usual means. Head to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el), choose **Model access** and [enable Amazon Nova Canvas for your account](https://docs.aws.amazon.com/nova/latest/userguide/getting-started-console.html#getting-started-access?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) making sure that you select the appropriate regions for your workloads. If you already have access and have been using Nova Canvas, you can start using the new features immediately as they’re automatically available to you.

**Virtual try-on** The first exciting new feature is **virtual try-on**. With this, you can upload two pictures and ask Amazon Nova Canvas to put them together with realistic results. These could be pictures of apparel, accessories, home furnishings, and any other products including clothing. For example, you can provide the picture of a human as the source image and the picture of a garment as the reference image, and Amazon Nova Canvas will create a new image with that same person wearing the garment. Let’s try this out!

My starting point is to select two images. I picked one of myself in a pose that I think would work well for a clothes swap and a picture of an AWS-branded hoodie.

[![Matheus and AWS-branded hoodie](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/26/nova-canvas-source-images.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/26/nova-canvas-source-images.png)

Note that Nova Canvas accepts images containing a maximum of 4.1M pixels – the equivalent of 2,048 x 2,048 – so be sure to scale your images to fit these constraints if necessary. Also, if you’d like to run the Python code featured in this article, ensure you have Python 3.9 or later installed as well as the Python packages boto3 and pillow.

To apply the hoodie to my photo, I use the Amazon Bedrock Runtime invoke API. You can find full details on the request and response structures for this API in the [Amazon Nova User Guide](https://docs.aws.amazon.com/nova/latest/userguide/image-generation.html). The code is straightforward, requiring only a few inference parameters. I use the new `taskType` of `"VIRTUAL_TRY_ON"`. I then specify the desired settings, including both the source image and reference image, using the `virtualTryOnParams` object to set a few required parameters. Note that both images must be converted to Base64 strings.

```
import base64

def load_image_as_base64(image_path):
   """Helper function for preparing image data."""
   with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode("utf-8")

inference_params = {
   "taskType": "VIRTUAL_TRY_ON",
   "virtualTryOnParams": {
      "sourceImage": load_image_as_base64("person.png"),
      "referenceImage": load_image_as_base64("aws-hoodie.jpg"),
      "maskType": "GARMENT",
      "garmentBasedMask": {"garmentClass": "UPPER_BODY"}
   }
}
```

Nova Canvas uses masking to manipulate images. This is a technique that allows AI image generation to focus on specific areas or regions of an image while preserving others, similar to using painter’s tape to protect areas you don’t want to paint.

You can use three different masking modes, which you can choose by setting `maskType` to the correct value. In this case, I’m using `"GARMENT"`, which requires me to specify which part of the body I want to be masked. I’m using `"UPPER_BODY"` , but you can use others such as `"LOWER_BODY"`, `"FULL_BODY"`, or `"FOOTWEAR"` if you want to specifically target the feet. [Refer to the documentation](https://docs.aws.amazon.com/nova/latest/userguide/image-generation.html) for a full list of options.

I then call the invoke API, passing in these inference arguments and saving the generated image to disk.

```
# Note: The inference_params variable from above is referenced below.

import base64
import io
import json

import boto3
from PIL import Image

# Create the Bedrock Runtime client.
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Prepare the invocation payload.
body_json = json.dumps(inference_params, indent=2)

# Invoke Nova Canvas.
response = bedrock.invoke_model(
   body=body_json,
   modelId="amazon.nova-canvas-v1:0",
   accept="application/json",
   contentType="application/json"
)

# Extract the images from the response.
response_body_json = json.loads(response.get("body").read())
images = response_body_json.get("images", [])

# Check for errors.
if response_body_json.get("error"):
   print(response_body_json.get("error"))

# Decode each image from Base64 and save as a PNG file.
for index, image_base64 in enumerate(images):
   image_bytes = base64.b64decode(image_base64)
   image_buffer = io.BytesIO(image_bytes)
   image = Image.open(image_buffer)
   image.save(f"image_{index}.png")
```

I get a very exciting result!

[![Matheus wearing AWS-branded hoodie](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/26/nova-canvas-try-on.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/26/nova-canvas-try-on.png)

And just like that, I’m the proud wearer of an AWS-branded hoodie!

In addition to the `"GARMENT"` mask type, you can also use the `"PROMPT"` or `"IMAGE"` masks. With `"PROMPT"`, you also provide the source and reference images, however, you provide a natural language prompt to specify which part of the source image you’d like to be replaced. This is similar to how the `"INPAINTING"` and `"OUTPAINTING"` tasks work in Nova Canvas. If you want to use your own image mask, then you choose the `"IMAGE"` mask type and provide a black-and-white image to be used as mask, where black indicates the pixels that you want to be replaced on the source image, and white the ones you want to preserve.

This capability is specifically useful for retailers. They can use it to help their customers make better purchasing decisions by seeing how products look before buying.

**Using style options**

I’ve always wondered what I would look like as an anime superhero. Previously, I could use Nova Canvas to manipulate an image of myself, but I would have to rely on my good prompt engineering skills to get it right. Now, Nova Canvas comes with pre-trained styles that you can apply to your images to get high-quality results that follow the artistic style of your choice. There are eight available styles including 3D animated family film, design sketch, flat vector illustration, graphic novel, maximalism, midcentury retro, photorealism, and soft digital painting.

Applying them is as straightforward as passing in an extra parameter to the Nova Canvas API. Let’s try an example.

I want to generate an image of an AWS superhero using the 3D animated family film style. To do this, I specify a `taskType` of `"TEXT_IMAGE"` and a `textToImageParams` object containing two parameters: `text` and `style`. The `text` parameter contains the prompt describing the image I want to create which in this case is “a superhero in a yellow outfit with a big AWS logo and a cape.” The `style` parameter specifies one of the predefined style values. I’m using `"3D_ANIMATED_FAMILY_FILM"` here, but you can find the full list in the [Nova Canvas User Guide](https://docs.aws.amazon.com/nova/latest/userguide/image-generation.html).

```
inference_params = {
   "taskType": "TEXT_IMAGE",
   "textToImageParams": {
      "text": "a superhero in a yellow outfit with a big AWS logo and a cape.",
      "style": "3D_ANIMATED_FAMILY_FILM",
   },
   "imageGenerationConfig": {
      "width": 1280,
      "height": 720,
      "seed": 321
   }
}
```

Then, I call the invoke API just as I did in the previous example. (The code has been omitted here for brevity.) And the result? Well, I’ll let you judge for yourself, but I have to say I’m quite pleased with the AWS superhero wearing my favorite color following the 3D animated family film style exactly as I envisioned.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/superhero_AWS.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/superhero_AWS.png)

What’s really cool is that I can keep my code and prompt exactly the same and only change the value of the style attribute to generate an image in a completely different style. Let’s try this out. I set `style` to `PHOTOREALISM`.

```
inference_params = {
   "taskType": "TEXT_IMAGE",
   "textToImageParams": {
      "text": "a superhero in a yellow outfit with a big AWS logo and a cape.",
      "style": "PHOTOREALISM",
   },
   "imageGenerationConfig": {
      "width": 1280,
      "height": 720,
      "seed": 7
   }
}
```

And the result is impressive! A photorealistic superhero exactly as I described, which is a far departure from the previous generated cartoon and all it took was changing one line of code.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/superhero_AWS_photorealistic.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/06/11/superhero_AWS_photorealistic.png)

**Things to know**

Availability – Virtual try-on and style options are available in Amazon Nova Canvas in the US East (N. Virginia), Asia Pacific (Tokyo), and Europe (Ireland). Current users of Amazon Nova Canvas can immediately use these capabilities without migrating to a new model.

Pricing – See the [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing?trk=ac97e39c-d115-4d4a-b3fe-c695e0c9a7ee&sc_channel=el) for details on costs.

For a preview of virtual try-on of garments, you can visit [nova.amazon.com](https://nova.amazon.com/) where you can upload an image of a person and a garment to visualize different clothing combinations.

If you are ready to get started, please check out the [Nova Canvas User Guide](https://docs.aws.amazon.com/nova/latest/userguide/image-generation.html) or visit the [AWS Console](http://console.aws.amazon.com/bedrock).

[Matheus Guimaraes | @codingmatheus](https://link.codingmatheus.com/linkedin)

![Matheus Guimaraes](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/16/me_standing_outdoor-square-2.jpg)

### Matheus Guimaraes

Matheus Guimaraes (@codingmatheus) is a digital transformation specialist focused on AI adoption and microservices architecture. An international keynote speaker with over 20 years in tech, he’s worn many hats: from junior game programmer to CTO and tech co-founder. Matheus has helped companies of all sizes modernize and scale their systems, leading transformation programs and designing cloud-native, AI-ready architectures. Today, he shares his expertise globally through talks, blogs, and videos, passionate about helping others grow in the industry. Outside his professional life, he’s a gamer, swimmer, musician, and firm believer in the powerful intersection of creativity and technology.

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