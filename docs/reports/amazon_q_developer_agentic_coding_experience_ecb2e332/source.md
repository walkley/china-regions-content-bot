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

# Intelligent coding at your fingertips: Introducing an agentic coding experience in your IDE

by Brian Beach on 05 MAY 2025 in [Amazon Q](https://aws.amazon.com/blogs/devops/category/amazon-q/ "View all posts in Amazon Q"), [Amazon Q Developer](https://aws.amazon.com/blogs/devops/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Announcements](https://aws.amazon.com/blogs/devops/category/post-types/announcements/ "View all posts in Announcements") [Permalink](https://aws.amazon.com/blogs/devops/amazon-q-developer-agentic-coding-experience/) Share

Back in March, I wrote about the [new agentic coding experience within the Amazon Q Developer CLI](https://aws.amazon.com/blogs/devops/introducing-the-enhanced-command-line-interface-in-amazon-q-developer/). Recently, [Amazon Q Developer](https://aws.amazon.com/q/developer/) announced that it has [added a similar experience to the integrated development environement (IDE)](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-q-developer-agentic-coding-experience-ide/). Agentic coding in the IDE allows you to work with Amazon Q Developer to read and write files locally, run bash commands, build code, and more in near real-time through natural language conversations. The new experience redefines how you write, modify, and maintain code by leveraging natural language understanding to seamlessly execute complex workflows. The new agentic coding experience is now available in VS Code with support in other IDEs coming soon.

## Background

Before I explain the new agentic coding experience, let’s take a minute to review the existing chat capabilities within the Amazon Q Developer IDE. As the name implies, the traditional chat allows me to have a conversation with Q Developer. This is a great option when I’m learning and planning. It provides a natural back-and-forth dialogue. Personally, I like the traditional chat during the planning phase of the Software Development Lifecycle (SDLC). I can chat with Q Developer to discuss my architecture and the various tradeoffs of different designs before I start working.

However, once I move into the build phase of the SDLC, I prefer the new agentic coding experience. In this new experience, Q Developer can do so much more than just have a conversation. It can directly interact with the development environment, reading and writing files, using various development tools, and even querying AWS resources. This allows for a far more dynamic, hands-on coding workflow compared to the traditional chat interface.

Rather than just discussing requirements, the agentic agent can take direct action to implement them. It can scaffold new projects, update existing code, and provide step-by-step summaries of its progress – all through a seamless, conversational interface right within the IDE. The great news is that I now have both options available to me. I can simply toggle between a traditional chat in the planning phase, and the new agentic coding in the build phase.

## Walkthrough

Let’s walk through a simple example using the [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/). I love CDK, and I use it all the time in my role. However, let’s assume that I don’t have a lot of experience, and want to learn more about CDK before I start using it. Since I just want to learn, I’ll start in the traditional chat experience, and ask Q Developer “How do I create an new CDK app?” As you can see in the following image, Q Developer starts to teach me about CDK. Along with the instructions, Q provides commands that I could copy and paste into my shell to get started.

![A screenshot of an Amazon Q Developer chat interface showing instructions for creating a new AWS CDK app. The interface displays a dark theme with a conversation about CDK app creation. The response includes step-by-step instructions: installing the AWS CDK toolkit via npm, creating a new directory for the CDK project, and beginning to explain initialization commands. Command examples are shown in code blocks with copy buttons. The bottom of the screen shows an input field and a notice about Amazon Q's AI capabilities.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/05/02/ide-agentic-coding-01.png)

While this is a great, I am already familiar with CDK. I don’t need to learn how to create a new application. I am ready to start building! Therefore, I will toggle from traditional chat to agentic coding by clicking on the angle bracket pair in the bottom left corner of the chat window. Then, I will ask Q Developer to “Create a new CDK app in this folder using TypeScript.” First, notice that I am not asking a question like I did previously, but I am giving a command. In the following image, you can see that Q Developer is acting on my command rather that teaching me what to do.

![A screenshot of an Amazon Q Developer chat interface with a dark theme. The image shows a conversation about creating a new AWS CDK app using TypeScript. The assistant provides instructions to initialize a CDK project in the current directory. A command prompt is displayed with the command "npx aws-cdk init app --language typescript" to create a new CDK TypeScript application. The interface includes "Reject" and "Run" options for the command. At the bottom, there's an input field for asking questions and a note about Amazon Q's use of generative AI.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/05/02/ide-agentic-coding-02.png)

This is the power of the new agentic coding. It is not simply teaching me how to create a CDK app. Amazon Q Developer is creating the app for me. There are a few important things that I want to call out here. First, Amazon Q Developer can use tools when it is running agentic coding mode. In this example, Q is using a series of shell commands — `mkdir`, `cd`, `npx`, `npm`, etc. — to create the CDK app. I will discuss other tools later in this post. Second, Q Developer is asking my permission before it runs these commands. This allows me to retain control over the development process. I’ll click the **Run** button and allow Q to create the new application resulting in the following project structure.

![A screenshot of a directory view showing the structure of a TypeScript-based AWS CDK project. The project root folder "IDE-BLOG-POST" displays a typical CDK project structure, containing four main directories (bin, lib, node_modules, and test) along with several configuration and documentation files: .gitignore, .npmignore, cdk.json, jest.config.js, package-lock.json, package.json, README.md, and tsconfig.json. The interface uses a dark theme with distinctive icons indicating different file types and folder structures.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/05/02/ide-agentic-coding-03.png)

It’s easy to overlook the power of allowing Q Developer to use tools. By using shell commands, it was able to generate the project using the latest template, and install dependencies for me. Running shell commands is just one of many changes with the agentic coding experience. Next, let’s look at how code generation works in agentic coding.

## Code Generation

Amazon Q Developer has been generating code since it [first launched in June of 2022](https://aws.amazon.com/about-aws/whats-new/2022/06/aws-announces-amazon-codewhisperer-preview/). Since then, Amazon Q Developer has evolved, adding new features over time. Code generation began with [inline suggestions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/inline-suggestions.html), followed by [chat](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-chat.html), and [the agent for software development](https://aws.amazon.com/blogs/devops/amazon-q-developers-new-context-features/). The new agentic coding, reinvents the code generation experience again. In the following example, I am going to add a Lambda function to the CDK stack that Q Developer created earlier. I ask Q Developer to “Add a new Lambda function that is triggered from the arrival of a file in an existing S3 bucket.”

![A screenshot of an Amazon Q Developer chat interface showing instructions for adding an S3-triggered Lambda function to an existing CDK stack. The interface displays several steps being executed: modifying the stack file (ide-blog-post-stack.ts with +41/-6 changes), creating a lambda directory using the "mkdir -p lambda" command (marked as completed), creating a Lambda function in index.js (+25/-0 changes), and updating the README.md file (+26/-4 changes). Each modification shows an "Undo" option, and there's an "Undo all changes" button at the bottom. The interface features a dark theme and includes the standard input field and AI disclosure notice at the bottom.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/05/02/ide-agentic-coding-04.png)

Multiple important things happened in this example that I want to explain. First, notice that Q Developer edited the CDK Stack to add the new [AWS Lambda](https://aws.amazon.com/pm/lambda) function. Second, Q Developer used a shell command to create a new folder. Third, Q created a new file for the Lambda function. Forth, it updated the README file. Q took all four of these actions in response to a single prompt. In addition, note that Q Developer is providing a diff for each change, making it easy for me to review the changes. You can see an example of the changes it make to the README.md in the following image. Finally, note that I can undo any of the changes that Q Developer made along the way.

![A screenshot of a README.md file in a code editor with a dark theme. The file shows both removed content (in red) and new content (in green). The removed content is the default CDK TypeScript project introduction, while the new content describes an S3-triggered Lambda function CDK project. The new documentation includes an architecture section detailing the Lambda function, S3 bucket, and event notification components, followed by deployment instructions that include steps for building the project with 'npm run build' and deploying the stack with CDK using parameters for an existing bucket name.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/05/02/ide-agentic-coding-05.png)

This is a big improvement over the traditional chat experience. Now let’s look at how Q Developer can describe my AWS resources.

## Describing AWS resources

Remember that I am building an application that is triggered by the arrival of a file in an existing [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket. In the prior example, you can see that I need to pass the name of the bucket in the `ExistingBucketName` parameter when deploying the stack.

Let’s assume that I have forgotten the name of the bucket I want to use. The new agentic coding experience can help me with this too. In the following example, I ask Q to “List my S3 buckets in the ca-central-1 region?” Once again, Q Developer asks for permission to use the shell. After I accept, Q Developer uses the AWS CLI and lists the buckets I have available in Canada (ca-central-1).

![A screenshot of Amazon Q Developer displaying an AWS CLI command and its output showing S3 bucket listing for the ca-central-1 region. The command uses aws s3api list-buckets with jq filtering to show only buckets in the Canada Central region. The output displays one bucket named "blog-post-demo-bucket" with explanatory text about using it with Lambda functions and CDK stack deployment.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/05/02/ide-agentic-coding-06.png)

With the name of the bucket, I am ready to deploy my stack. Of course, there still more work to do, but I’ll leave that for another post.

## Conclusion

The new agentic coding experience within the Amazon Q Developer IDE represents a significant step forward in integrating powerful AI-driven capabilities directly into the developer’s workflow. By enabling the coding agent to read, write, and execute code locally, access tools, and interact with AWS resources, Q Developer promises to dramatically streamline and enhance the coding process. You can visit the [Amazon Q Developer User Guide](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/getting-started-q-dev.html) to install the IDE and start leveraging the new agent chat for free. Give it a try and let me know what you think!

TAGS: [Developer Tools](https://aws.amazon.com/blogs/devops/tag/developer-tools/), [Development](https://aws.amazon.com/blogs/devops/tag/development/)

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