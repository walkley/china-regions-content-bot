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

# Use Model Context Protocol with Amazon Q Developer for context-aware IDE workflows

by Ritik Khatwani on 12 JUN 2025 in [Amazon Q](https://aws.amazon.com/blogs/devops/category/amazon-q/ "View all posts in Amazon Q"), [Amazon Q Developer](https://aws.amazon.com/blogs/devops/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Announcements](https://aws.amazon.com/blogs/devops/category/post-types/announcements/ "View all posts in Announcements"), [Developer Tools](https://aws.amazon.com/blogs/devops/category/developer-tools/ "View all posts in Developer Tools"), [Generative AI](https://aws.amazon.com/blogs/devops/category/generative-ai-2/ "View all posts in Generative AI") [Permalink](https://aws.amazon.com/blogs/devops/use-model-context-protocol-with-amazon-q-developer-for-context-aware-ide-workflows/) Share

Earlier today, [Amazon Q Developer](https://aws.amazon.com/q/developer/) announced Model Context Protocol (MCP) support in their Integrated Development Environment (IDE) plugins for Visual Studio Code and JetBrains. This allows developers to connect external tools or MCP servers to Q Developer, enabling more context-aware responses and complex workflows. MCP support has already been available in [Amazon Q Developer for Command Line](https://aws.amazon.com/blogs/devops/extend-the-amazon-q-developer-cli-with-mcp/) since April 29, 2025.

## Introduction

Q Developer already had the ability to use tools within the IDE such as executing shell commands, reading local files, and generating code with the addition of the [agentic coding](https://aws.amazon.com/blogs/devops/amazon-q-developer-agentic-coding-experience/) experience. Now, developers have the ability to add additional tools that support MCP to their toolkit. MCP is an open protocol that standardizes how Large Language Models (LLMs) integrate with applications. It provides a way to share context, access data sources, and interact with APIs. You can read more about MCP in this [introduction](https://modelcontextprotocol.io/introduction).

This ability to add additional context and tools allows Q Developer to write more accurate code, integrate with your planning tools, create UI components from designs, generate database documentation by examining your actual schema, and execute complex multi-tool tasks – all without the need for custom integration code. I’m excited to see this functionality coming to Q Developer IDE plugins, enhancing the development process right where developers spend most of their time.

In this post, I’ll walk you through a common scenario where I, as a developer, am tasked with working on an issue defined in a project management tool like [Jira](https://www.atlassian.com/software/jira). The issue contains a user story, acceptance criteria, a link to a [Figma](https://www.figma.com/) design of the user interface, and additional technical implementation notes. To accomplish this efficiently, I’ll demonstrate how Q Developer can streamline the entire process by using two separate MCP servers to interact with Jira and Figma independently. Rather than manually switching between browser tabs, copying information, and trying to keep track of requirements across multiple tools, I’ll show how Q Developer can automatically fetch details using MCP and help me implement the feature while maintaining context across both platforms as shown in the figure below.

![Q Developer extension in Visual Studio Code interacting with external tools using MCP servers](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/MCP_In_IDE_Architecture.png)

Figure 1: Q Developer extension in Visual Studio Code interacting with external tools using MCP servers

## Configuring MCP Servers

To begin setup, click on the [**Configure** **MCP servers**](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-ide-configuration.html) button at the top of the Chat tab bar as shown in the image below. This will bring up the list of MCP servers currently configured. Click the + (Add new MCP) button to add a new server.

![Add MCP server configuration in Visual Studio Code’s Q Developer extension](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/ConfigMCP_NewIcon.gif)

Figure 2: Add MCP server configuration in Visual Studio Code’s Q Developer extension

You will set the scope of your MCP servers during configuration. A Global scope allows you to use the MCP server across all your projects, whereas a Workspace scope sets it up for only the current IDE workspace. Here’s an example configuration for the [Atlassian](https://www.atlassian.com/platform/remote-mcp-server) and [Figma](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Dev-Mode-MCP-Server) MCPs I’ll be using:

|  |
| --- |
| **Atlassian** |
| **Scope:** This workspace |
| **Name:** Atlassian |
| **Transport:** stdio |
| **Command:** npx |
| **Arguments:**    -y   mcp-remote   https://mcp.atlassian.com/v1/sse |

|  |
| --- |
| **Figma** |
| **Scope:** This workspace |
| **Name:** Figma |
| **Transport:** stdio |
| **Command:** npx |
| **Arguments:**    -y   mcp-remote   http://127.0.0.1:3845/sse |

Note: The first time you set up the Atlassian MCP server, you’ll be asked to complete the OAuth authentication flow in your browser and provide access permissions to your Jira projects. Similarly, to connect to the Figma Dev Mode MCP server, you’ll need to [enable it](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Dev-Mode-MCP-Server#h_01JVAXW87T435SJDASMZB59AFG) via the Figma desktop app.

![Q Developer’s MCP management window showing configured Figma and Atlassian MCPs servers](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/MCPs_Configured-1024x656.png)

Figure 3: Q Developer’s MCP management window showing configured Figma and Atlassian MCPs servers

To understand an MCP server’s individual tools, click on the expand icon next to its name as shown in the image below. Tools are executable functions exposed by the MCP server. They enable Q Developer’s agentic chat to perform actions and interact with external systems on your behalf. You can also configure permissions for individual tools. Each tool presents the option to Ask, Always allow, or Deny it such that Q Developer can’t invoke it. In my example, I’ll set all tools that only read data to **Always allow** for my workspace and set the rest of the tools to **Ask**.

![MCP tool descriptions and configuration dropdown with options to Ask, Always allow or Deny](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/tool_perms_vscode-1024x312.png)

Figure 4: MCP tool descriptions and configuration dropdown with options to Ask, Always allow or Deny

With the MCP servers configured, let’s see how I can integrate them into my workflow.

## Walkthrough

Q Developer is now enriched with additional information and tools available via the configured MCP servers. To demonstrate how this accelerates my developer productivity, I’ll be working with the [Q Words game](https://catalog.workshops.aws/qwords/en-US).

### Scenario

**Q-Words** is an interactive word guessing game used in our customers’ workshops to demonstrate Q Developer’s capabilities. I’ve been tasked by the Product Manager to add a dark mode to the game. The User Story is logged in Jira and links to a Figma design that our designers have prepared.

![Jira ticket showing user story and acceptance criteria for adding dark mode to a Q-Words game application](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/Jira-1024x656.png)

Figure 5: Jira ticket showing user story and acceptance criteria for adding dark mode to a Q-Words game application

![Figma design showing dark and light mode interfaces for a QWords game application](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/FigmaDevMode-1024x656.png)

Figure 6: Figma design showing dark and light mode interfaces for a QWords game application

### Integrating MCPs into your development workflow

Let’s begin by asking Q Developer to check on tasks assigned to me in Jira by typing the following prompt in the agentic chat:

`List issues that I need to work on`

Q Developer will understand your intent and interact with your Atlassian MCP server to filter and show Jira issues that are assigned to you and in the To Do state. You can optionally prompt Q Developer to use a particular MCP server. Just as with any prompt, providing clear instructions will yield better results. In the image below, Q Developer retrieves details for the issue I’m assigned to work on.

![Q Developer retrieves and describes issues assigned to me in Jira using the Atlassian MCP server](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/ToDoIssues_Q-1024x656.png)

Figure 7: Q Developer retrieves and describes issues assigned to me in Jira using the Atlassian MCP server

Let’s begin work on the issue with the following prompt:

`Move issue CRM-9 to In Progress and checkout a new git branch named after the issue id to begin working on it`

![Prompt Q Developer to begin working on an assigned issue](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/MoveToInProgress_New_Q-1024x656.png)

Figure 8: Prompt Q Developer to begin working on an assigned issue

Next, I’d like to understand the impact of the design changes on the current application. I can use the following prompt to accomplish this:

`Analyze the Jira User Story and linked Figma design. Give me a technical implementation plan explaining the UI components that will need to be modified in the ex``isting code.`

![Prompt Q Developer to help you analyze changes in existing code to implement the new UI](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/ImplementationPlan_Q.mov.gif)

Figure 9: Prompt Q Developer to help you analyze changes in existing code to implement the new UI

Q Developer automatically pulls in issue details from Jira, along with the design specifics like colors from Figma. Before MCP, I would have had to add those details directly into the prompt or provided them as context from a local file. Now, my prompt only includes the description of the task whereas the context is enriched with details from the MCP servers. Review the proposed plan and suggest edits if needed. Once satisfied, prompt Q Developer to begin working on the changes:

`Implement the plan`

![The diff view of changes by Q Developer to implement a dark mode feature in HTML and CSS ](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/Diff_HomeTemplate-1024x656.png)

Figure 10: The diff view of changes by Q Developer to implement a dark mode feature in HTML and CSS

After reviewing the diff of the files changed by Q Developer, I can verify that the new Dark Mode feature has been implemented as desired. Let’s test the changes and ensure all acceptance criteria is met. To run the application, I use the following prompt:

`Run the application locally`

Q Developer will ask permission and run commands to spin up the local web server. I can then test the changes in my browser.

![Updated application with dark mode toggle button implemented by Q Developer using MCP](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/DarkModeDemo.mov.gif)

Figure 11: Updated application with dark mode toggle button implemented by Q Developer using MCP

After a bit of testing, I can confirm that we’ve met all the acceptance criteria for the story. Let’s update the rest of the team on what we’ve accomplished with the following prompt:

`Update the Jira issue status to Done and add a comment summarizing the changes made.`

This convenient integration between Q Developer and Jira via MCP, saves me the back and forth between different tools to document the work accomplished.

![A Jira ticket comment detailing the completed implementation of dark mode features, including theme toggle, CSS variables, and UI components](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/IssueDone-1024x656.png)

Figure 12: A Jira ticket comment detailing the completed implementation of dark mode features, including theme toggle, CSS variables, and UI components

## Conclusion

The addition of MCP support in Amazon Q Developer for the IDE provides a standardized way to share context and interact with additional tools. In this post, I’ve demonstrated how I can use Q Developer in the IDE to interact with Atlassian Jira for task management and Figma for UI updates. I was able to do this without explicitly including user story details in my prompts or separately downloading design assets from UI mockups. Instead, Q Developer could automatically access user story context and easily integrate design assets using tools exposed by MCP servers. I encourage you to explore the new MCP capabilities and also check out the [AWS MCP Servers](https://github.com/awslabs/mcp) repository on GitHub. Refer [MCP configuration for Q Developer in the IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-ide-configuration.html) to learn more.

To learn more about Amazon Q Developer’s features and pricing details, visit the [Amazon Q Developer product page](https://aws.amazon.com/q/developer/).

## About the Author

![Ritik Khatwani](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/06/12/profile_pic.jpg)

### Ritik Khatwani

Ritik is a Generative AI Specialist Solutions Architect at AWS based in New York City. He has deep expertise in building products as an engineer, architect, and founder. At AWS, he previously advised startups on how to build and grow in the cloud and now works with developers to reimagine their software development lifecycle using Amazon Q Developer.

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