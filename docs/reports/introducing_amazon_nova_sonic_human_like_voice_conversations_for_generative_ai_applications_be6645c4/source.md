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

# Introducing Amazon Nova Sonic: Human-like voice conversations for generative AI applications

by [Danilo Poccia](https://aws.amazon.com/blogs/aws/author/danilop/ "Posts by Danilo Poccia") on 08 APR 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-bedrock-knowledge-bases/ "View all posts in Amazon Bedrock Knowledge Bases"), [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Amazon Nova](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-nova/ "View all posts in Amazon Nova"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Generative AI](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-sonic-human-like-voice-conversations-for-generative-ai-applications/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

***July 16, 2025**: Amazon Nova Sonic now [supports French, Italian, and German](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-nova-sonic-language-support-french-italian-german/), expanding its existing coverage of English and Spanish with six additional expressive voices offering both masculine and feminine-sounding options.*

***June 12, 2025**: Amazon Nova Sonic now also [supports Spanish language](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-nova-sonic-spanish-language/) with two additional (masculine and feminine-sounding) expressive voices.*

***April 14, 2025**: Post updated to clarify the context size.*

Voice interfaces are essential to enhance customer experience in different areas such as customer support call automation, gaming, interactive education, and language learning. However, there are challenges when building voice-enabled applications.

Traditional approaches in building voice-enabled applications require complex orchestration of multiple models, such as speech recognition to convert speech to text, language models to understand and generate responses, and text-to-speech to convert text back to audio.

This fragmented approach not only increases development complexity but also fails to preserve crucial linguistic context such as tone, prosody, and speaking style that are essential for natural conversations. This can affect conversational AI applications that need low latency and nuanced understanding of verbal and non-verbal cues for fluid dialog handling and natural turn-taking.

To streamline the implementation of speech-enabled applications, today we are introducing [Amazon Nova Sonic](https://aws.amazon.com/ai/generative-ai/nova/speech/), the newest addition to the [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) family of [foundation models (FMs)](https://aws.amazon.com/what-is/foundation-models/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) available in [Amazon Bedrock](https://aws.amazon.com/bedrock/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

Amazon Nova Sonic unifies speech understanding and generation into a single model that developers can use to create natural, human-like conversational AI experiences with low latency and industry-leading price performance. This integrated approach streamlines development and reduces complexity when building conversational applications.

Its unified model architecture delivers expressive speech generation and real-time text transcription without requiring a separate model. The result is an adaptive speech response that dynamically adjusts its delivery based on prosody, such as pace and timbre, of input speech.

When using Amazon Nova Sonic, developers have access to function calling (also known as tool use) and agentic workflows to interact with external services and APIs and perform tasks in the customer’s environment, including knowledge grounding with enterprise data using [Retrieval-Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

At launch, Amazon Nova Sonic provides robust speech understanding for American and British English across various speaking styles and acoustic conditions, with additional languages coming soon.

Amazon Nova Sonic is [developed with responsible AI](https://aws.amazon.com/ai/responsible-ai/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) at the forefront of innovation, featuring built-in protections for content moderation and watermarking.

**Amazon Nova Sonic in action** The scenario for this demo is a contact center in the telecommunication industry. A customer reaches out to improve their subscription plan, and Amazon Nova Sonic handles the conversation.

With tool use, the model can interact with other systems and use agentic RAG with [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) to gather updated, customer-specific information such as account details, subscription plans, and pricing info.

The demo shows streaming transcription of speech input and displays streaming speech responses as text. The sentiment of the conversation is displayed in two ways: a time chart illustrating how it evolves, and a pie chart representing the overall distribution. There’s also an AI insights section providing contextual tips for a call center agent. Other interesting metrics shown in the web interface are the overall talk time distribution between the customer and the agent, and the average response time.

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2025/Nova-s2s-blog.mp4?_=1)

During the conversation with the support agent, you can observe through the metrics and hear in the voices how customer sentiment improves.

The video includes an example of how Amazon Nova Sonic handles interruptions smoothly, stopping to listen and then continuing the conversation in a natural way.

Now, let’s explore how you can integrate voice capabilities in your applications.

**Using Amazon Nova Sonic**

To get started with Amazon Nova Sonic, you first need to toggle model access in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el), similar to how you would enable other FMs. Navigate to the **Model access** section of the navigation pane, find **Amazon Nova Sonic** under the **Amazon** models, and enable it for your account.

Amazon Bedrock provides a new bidirectional streaming API (`InvokeModelWithBidirectionalStream`) to help you implement real-time, low-latency conversational experiences on top of the [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2) protocol. With this API, you can stream audio input to the model and receive audio output in real time, so that the conversation flows naturally.

You can use Amazon Nova Sonic with the new API with this model ID: `amazon.nova-sonic-v1:0`

After the session initialization, where you can configure inference parameters, the model operate through an event-driven architecture on both the input and output streams.

There are three key event types in the input stream:

**System prompt** – To set the overall system prompt for the conversation

**Audio input streaming** – To process continuous audio input in real-time

**Tool result handling** – To send the result of tool use calls back to the model (after tool use is requested in the output events)

Similarly, there are three groups of events in the output streams:

**Automatic speech recognition (ASR) streaming** – Speech-to-text transcript is generated, containing the result of realtime speech recognition.

**Tool use handling** – If there are a tool use events, they need to be handled using the information provided here, and the results sent back as input events.

**Audio output streaming** – To play output audio in real-time, a buffer is needed, because Amazon Nova Sonic model generates audio faster than real-time playback.

You can find examples of using Amazon Nova Sonic in the [Amazon Nova model cookbook repository](https://github.com/aws-samples/amazon-nova-samples).

**Prompt engineering for speech**

When crafting prompts for Amazon Nova Sonic, your prompts should optimize content for auditory comprehension rather than visual reading, focusing on conversational flow and clarity when heard rather than seen.

When defining roles for your assistant, focus on conversational attributes (such as warm, patient, concise) rather than text-oriented attributes (detailed, comprehensive, systematic). A good baseline system prompt might be:

`You are a friend. The user and you will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation. Keep your responses short, generally two or three sentences for chatty scenarios.`

More generally, when creating prompts for speech models, avoid requesting visual formatting (such as bullet points, tables, or code blocks), voice characteristic modifications (accent, age, or singing), or sound effects.

**Things to know**

[Amazon Nova Sonic](https://aws.amazon.com/ai/generative-ai/nova/understanding/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) is available today in the US East (N. Virginia) [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el). Visit [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) to see the pricing models.

Amazon Nova Sonic can understand speech in different speaking styles and generates speech in expressive voices, including both masculine-sounding and feminine-sounding voices, in different English accents, including American and British. Support for additional languages will be coming soon.

Amazon Nova Sonic handles user interruptions gracefully without dropping the conversational context and is robust to background noise. The model supports a 300K context window, with a default connection time limit of 8 minutes. However, you can extend your session by establishing a new connection and passing the previous chat history as context.

The following [AWS SDKs](https://aws.amazon.com/tools/) support the new bidirectional streaming API:

* [AWS SDK for C++](https://aws.amazon.com/sdk-for-cpp/)
* [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el)
* [AWS SDK for JavaScript](https://aws.amazon.com/sdk-for-javascript/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el)
* [AWS SDK for Kotlin](https://aws.amazon.com/sdk-for-kotlin/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el)
* [AWS SDK for Ruby](https://aws.amazon.com/sdk-for-ruby/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el)
* [AWS SDK for Rust](https://aws.amazon.com/sdk-for-rust/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el)
* [AWS SDK for Swift](https://aws.amazon.com/sdk-for-swift/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el)

Python developers can use this [new experimental SDK](https://github.com/awslabs/aws-sdk-python) that makes it easier to use the bidirectional streaming capabilities of Amazon Nova Sonic. We’re working to add support to the other AWS SDKs.

I’d like to thank [Reilly Manton](https://www.linkedin.com/in/reilly-manton/) and [Chad Hendren](https://www.linkedin.com/in/chad-david-hendren/), who set up the demo with the contact center in the telecommunication industry, and [Anuj Jauhari](https://www.linkedin.com/in/anuj-jauhari/), who helped me understand the rich landscape in which speech-to-speech models are being deployed.

You can find more examples in Java, Node.js, and Python in the [Amazon Nova model cookbook repo](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech), including common integration patterns, such as RAG using Amazon Bedrock Knowledge Bases or [LangChain](https://www.langchain.com/).

To learn more, these articles that enter into the details of how to use the new bidirectional streaming API with compelling demos:

* [Build Your Own AI Podcast Co-Host: Step-by-Step with Amazon Q CLI and Amazon Nova Sonic](https://dev.to/salihgueler/build-your-own-ai-podcast-co-host-step-by-step-with-amazon-q-cli-and-amazon-nova-sonic-2281)
* [Speech-to-Speech AI: From Dr. Sbaitso to Amazon Nova Sonic](https://community.aws/content/2vEZph0MzNXYJJSrNkgN9V2kYLY)

Whether you’re creating customer service solutions, language learning applications, or other conversational experiences, Amazon Nova Sonic provides the foundation for natural, engaging voice interactions. To get started, visit the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el) today. To learn more, visit the [Amazon Nova section of the user guide](https://docs.aws.amazon.com/nova/latest/userguide/speech.html?trk=e61dee65-4ce8-4738-84db-75305c9cd4fe&sc_channel=el).

– [Danilo](https://x.com/danilop)

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

![Danilo Poccia](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2018/11/22/danilo.png)

### [Danilo Poccia](https://aws.amazon.com/blogs/aws/author/danilop/ "Posts by Danilo Poccia")

Danilo works with startups and companies of any size to support their innovation. In his role as Chief Evangelist (EMEA) at Amazon Web Services, he leverages his experience to help people bring their ideas to life, focusing on serverless architectures and event-driven programming, and on the technical and business impact of machine learning and edge computing. He is the author of AWS Lambda in Action from Manning.

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