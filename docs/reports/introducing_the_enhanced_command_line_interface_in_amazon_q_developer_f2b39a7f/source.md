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

## [AWS DevOps & Developer Productivity Blog](https://aws.amazon.com/blogs/devops/)

# A lightning fast, new agentic coding experience within the Amazon Q Developer CLI

by Brian Beach on 06 MAR 2025 in [Amazon Q](https://aws.amazon.com/blogs/devops/category/amazon-q/ "View all posts in Amazon Q"), [Amazon Q Developer](https://aws.amazon.com/blogs/devops/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Announcements](https://aws.amazon.com/blogs/devops/category/post-types/announcements/ "View all posts in Announcements") [Permalink](https://aws.amazon.com/blogs/devops/introducing-the-enhanced-command-line-interface-in-amazon-q-developer/) Share

Earlier today, [Amazon Q Developer](https://aws.amazon.com/q/developer/) announced [an enhanced CLI agent](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-q-developer-cli-agent-command-line/) within the [Amazon Q command line interface (CLI).](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line.html) With this announcement, Q Developer brings the latest agentic experience to the CLI that provide a more dynamic, interactive coding experience that works with you, and iteratively makes changes based on your feedback. Amazon Q Developer can now use the information in your CLI environment to help you read and write files locally, query AWS resources write code, or automatically debug issues.

## Introduction

As a developer, I appreciate my Integrated Development Environment (IDE) along with the integrated linters and auto-completion features that help streamline my workflow. The addition of AI assistants, like Amazon Q Developer, have changed the way I work in profound ways. I can discuss best practices with Q Developer in chat, or ask it to refactor a complex method in seconds. I am increasingly using the Amazon Q Developer agents to develop new features, write documentation, generate unit tests, and automate code reviews. These powerful agent capabilities have further transformed how I approach my daily development tasks.

However, as a developer, I spend as much time at the command-line interface (CLI) as I do in the IDE, maybe even more. Tools like the [Amazon Web Services (AWS) CLI](https://aws.amazon.com/cli/), Git, package managers, and linters have revolutionized the way I manage infrastructure, automate repetitive tasks, and collaborate with my team. Tools like Docker and Kubernetes have transformed the way I develop and deploy my applications. Looking at the extensions tab in my IDE, I have extensions installed for Maven, Docker, and Vue, but I rarely use them, preferring the flexibility and power of the CLI.

Amazon Q Developer has been available in the CLI for over a year now, and it has become an indispensable part of my daily development routine. The assistant’s ability to provide intelligent command completions that can list my Git branches, [Amazon S3](https://aws.amazon.com/s3/) buckets, etc. has saved me countless hours. The chat feature allows me to engage in natural language conversations with Amazon Q Developer, asking it to help me learn how to accomplish specific tasks, while the translate capability seamlessly converts my plain-language prompts into the corresponding shell commands.

While Amazon Q Developer’s CLI capabilities are helpful, I miss the power of the agents I have access to in my IDE. Earlier today, Amazon Q Developer announced an enhanced CLI agent within the Amazon Q CLI. Amazon Q Developer, and the new agent is powered by Amazon Bedrock, as a result, the CLI has the power of [Claude 3.7 Sonnet step-by-step reasoning](https://aws.amazon.com/blogs/aws/anthropics-claude-3-7-sonnet-the-first-hybrid-reasoning-model-is-now-available-in-amazon-bedrock/). In addition, the new CLI agent can make use of tools installed on my system including compilers, package managers, and the [AWS CLI](https://aws.amazon.com/cli/). Finally, the enhanced CLI supports [multi-turn conversations](https://aws.amazon.com/about-aws/whats-new/2025/01/amazon-bedrock-flows-multi-turn-conversation-support/) allowing dynamic, back-and-forth conversations with the agent. This enables me to get more work done, faster, without ever leaving the comfort of my preferred command-line environment.

Rather than being constrained by the features and workflows of an IDE, the CLI agent gives me direct access to the underlying tools and commands I need to get my work done. Let’s look at an example.

## Walkthrough

To see how the CLI agent capabilities work, I’ll walk you through an example. I’m preparing for an internal developer community summit happening in April. I need an application to manage the call for content. The Call for Content application allows community members to propose topics for the summit. I’m going to use the Amazon Q Developer CLI to build the application.

I already have the [CLI installed](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html), so I’ll run `q chat` to begin a new conversation with the agent. Then I will ask Q Developer to “scaffold a new application named `call-for-content` using React and Vite, and then commit it to Git.” As you can see in the following video, the agent understands my intent, and carries out the work needed to build the application. In the past, the Q Developer CLI would provide instructions for me to execute. In this new enhanced version, the CLI agent uses the tools installed on my laptop to complete each step for me. *I should note that I have disabled confirmations, but Q Developer can prompt me before each action so I can verify it.*

![Animated screen recording of a terminal window showing Amazon Q Developer CLI in action. The terminal displays a welcome message 'Hi, I'm Amazon Q. Ask me anything.' The flow of events in the recording is captured in the next image.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/03/13/cli-1-scaffold-animated.gif)

The agent is working quickly in that video. So quickly that is hard to keep up. So I broke it down, step-by-step in the following image. The agent begins by calling `npm create` to create the new app, followed by `npm install` to add all the dependencies. It then runs a series of `git` commands to create a new repository, add my files, and commit the changes including a descriptive commit message.

![Terminal screenshot showing a sequence of commands executed by Amazon Q Developer to create a new React application. The sequence includes: creating a new Vite React project called 'call-for-content', installing dependencies with npm install, initializing a Git repository, adding files to Git, and making an initial commit. Each command is preceded by 'Execute shell command' and shows the exact command to be run in green text.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/03/13/cli-2-scaffold-unfurl.png)

Notice that agent is not simply generating files. It is running the same commands that I would have run on my own. However, the CLI agent is doing it much faster, and more accurately than I could have done. The enhanced Amazon Q Developer CLI can use tools, including other command line tools installed on my system, to complete its work. Once Q Developer is done, it provides me a summary of the work it has completed, and suggests next steps. In the following image, you can see that Q Developer is suggesting I run the development server to preview the changes. That is a great suggestion, so I ask Q Developer to start the server and confirm that everything is working.

![Split screen view showing two panels. On the left, a terminal displays a summary of completed actions including project creation, dependency installation, and Git initialization, along with instructions for starting the development server. On the right, the default Vite+React application page showing the Vite and React logos, a counter set to 0, and instructions to edit src/App.jsx to test Hot Module Replacement.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/02/28/cli-3-scaffold-running.png)

With the application template running, I’m ready to start building the Call for Content application. The CLI agent supports multi-turn conversations, so I can pick up where we left off. I simply explain my requirements at the command line, and agent begins to generate code. This is what Amazon Q Developer does best. In this example, it needs to update the `App.jsx` and `App.css` files.

![Terminal screenshot showing Amazon Q Developer processing a request to create a form application. The sequence shows: a prompt requesting a form with specific fields, followed by status messages indicating updates to App.jsx (completed in 0.1s) and App.css (completed in 0.2s), and ending with a Vite server startup message showing the local development server running at http://localhost:5173.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/02/28/cli-4-generate-unfurl.png)

Notice that the agent can read and write files on my local system in addition to running commands as we saw in the prior example. So, as Q Developer generates code, the agent can put it in the correct place in my local file system. Once it is done, the agent starts the development server using `npm run dev`. I asked it to start the server last time, so it correctly guesses that I will want to check the progress. Just like last time, the agent provides another summary of the changes it made. Personally, I appreciate these periodic summaries. They help me build confidence in the work that Q Developer is doing. I’m not happy with the color of the title. I could ask Q Developer to update it, but I will simply update the file myself. Note that I can edit files on my own while using the CLI. the agent will read files before editing them to check if I have made any changes manually.

![Split screen view showing development results. Left panel contains terminal output describing the form's features including field validations and counters. Right panel shows the rendered web form with fields for Name, Email, Talk Title (with 0/100 character counter), Abstract (with 0/100 word counter), Talk Level dropdown defaulted to '100 - Introductory', and a blue 'Submit Talk Proposal' button at the bottom.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/02/28/cli-5-generate-running.png)

The application is looking great! However, it is currently writing it’s output to the console. I never told the agent what to do with the data. I would like the application to write to a DynamoDB table. In fact, I created one already. However, I cannot remember which region the table is in. In the following image, I ask the agent to figure it out for me. Let’s see how it responds.

![Terminal window showing a sequence of AWS DynamoDB commands. The initial prompt asks to update an app to write to a DynamoDB table named 'call-for-content'. The sequence shows three 'Execute shell command' operations: first checking the table in us-east-1 region, then in us-west-2 region, followed by installing AWS SDK dependencies. The final line shows successful creation of a new DynamoDB service file.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/02/28/cli-6-dynamodb-unfurl.png)

As you can see in the prior image, the agent is able to think about my vague request, and figure out what to do. It starts by looking in us-east-1. When it can not find the table, it moves to us-west-2 and tries again. The table was in us-west-2, but if it were not, the agent would have continued searching. Q Developer understands how to **list** and **describe** AWS resources. Once the agent found the table, it uses `npm` to install the DynamoDB SDK, and then updates the application files. Note that the agent actually updated multiple files, but I kept the image simple.

With just a few simple prompts, I was able to use the enhanced CLI agent to collaborate with Q Developer throughout the entire development process. I’ll keep working on the application to add authentication, etc. However
~~,~~
I assume you have a good understanding of how the Q Developer CLI works and are eager to get started. So, let’s stop here.

## Conclusion

Amazon Q Developer’s new CLI agent has completely transformed the way I approach software development. By bringing the power of an advanced AI assistant directly into my preferred command-line environment, I can now accomplish complex tasks faster than ever before. Q Developer’s natural language understanding and contextual awareness, combined with the CLI agent’s ability to reason and use a wide range of development tools, make it an indispensable part of my daily workflow. Finally, support for multi-turn conversations, enable me to collaborate with, and work along side the agent to get more work done, faster.

If you’re a developer who spends a significant amount of time in the CLI, I highly recommend trying out the Amazon Q Developer’s CLI agent. You can follow the [Amazon Q Developer User Guide](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html) to install the CLI and start leveraging the new agent capabilities right away, for free. I’m confident it will change the way you work, just as it has for me. Give it a try and let me know what you think!

TAGS: [AWS Command Line Interface](https://aws.amazon.com/blogs/devops/tag/aws-command-line-interface/), [Development](https://aws.amazon.com/blogs/devops/tag/development/)

### Resources

* [AWS Developer Tools Blog](https://aws.amazon.com/blogs/developer)
* [AWS Frontend Web & Mobile Blog](https://aws.amazon.com/blogs/mobile/)
* [AWS Developers YouTube](https://www.youtube.com/%40awsdevelopers)
* [Amazon Q Developer](https://aws.amazon.com/q/developer/)
* [AWS CDK](https://aws.amazon.com/cdk/)
* [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
* [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
* [AWS CodeBuild](https://aws.amazon.com/codebuild/)

---

### Follow

* [AWS .NET on Twitter](https://twitter.com/dotnetonaws)
* [AWS Cloud on Twitter](https://twitter.com/awscloud)
* [AWS on Reddit](https://www.reddit.com/user/amazonwebservices)
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