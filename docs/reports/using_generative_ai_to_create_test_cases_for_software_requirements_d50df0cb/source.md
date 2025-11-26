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

## [AWS for Industries](https://aws.amazon.com/blogs/industries/)

# Using generative AI to create test cases for software requirements

by Tobias Drees, Daniel Krumpholz, and Stanislav Kruglov on 13 JAN 2025 in [Amazon API Gateway](https://aws.amazon.com/blogs/industries/category/application-services/amazon-api-gateway-application-services/ "View all posts in Amazon API Gateway"), [Amazon Bedrock](https://aws.amazon.com/blogs/industries/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon DynamoDB](https://aws.amazon.com/blogs/industries/category/database/amazon-dynamodb/ "View all posts in Amazon DynamoDB"), [Automotive](https://aws.amazon.com/blogs/industries/category/industries/automotive/ "View all posts in Automotive"), [AWS Lambda](https://aws.amazon.com/blogs/industries/category/compute/aws-lambda/ "View all posts in AWS Lambda"), [Generative AI](https://aws.amazon.com/blogs/industries/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Industries](https://aws.amazon.com/blogs/industries/category/industries/ "View all posts in Industries") [Permalink](https://aws.amazon.com/blogs/industries/using-generative-ai-to-create-test-cases-for-software-requirements/)  [Comments](https://aws.amazon.com/blogs/industries/using-generative-ai-to-create-test-cases-for-software-requirements/#Comments)  Share

In today’s automotive industry, managing software system requirements is a significant challenge due to the growing complexity and critical nature of these systems. These requirements include functional requirements, such as autonomous driving, infotainment, and user interfaces, and nonfunctional requirements that establish the system’s operational criteria, such as performance, security, and reliability.

A recent [whitepaper](https://resources.sw.siemens.com/en-US/white-paper-automotive-requirements-management/) states that 450,000 software and electronics requirements have to be managed for a well-equipped mid-sized vehicle. This results in hundreds of thousands of test cases to validate each requirement and verify that the software meets the specified criteria. Despite advancements in requirement management tools and methodologies, this process remains repetitive and labor intensive, highlighting the necessity for more automated and efficient methods.

The [Virtual Engineering Workbench (VEW)](https://aws.amazon.com/blogs/industries/stellantis-sdv-transformation-with-the-virtual-engineering-workbench-on-aws/) is a cloud-based framework designed to streamline and automate the development and testing processes in automotive software engineering. VEW provides digital toolchains, virtual hardware abstractions, and self-service portals for runtime environments, all aimed at helping increase developer efficiency.

By using Amazon Web Services (AWS), the VEW framework currently offers a range of tools and targets to help enhance the software development lifecycle. To further increase efficiency for testers and integrators, generative AI services can be integrated to help validate artifacts created in VEW environments against specifications. This approach helps to reduce manual effort and enhance the accuracy and effectiveness of the testing as well as integration processes across the automotive software engineering spectrum.

Furthermore, the VEW supports future developments by letting testers experiment with different prompts and models, thus facilitating customization and workflow improvement. By incorporating feedback loops and fine-tuning capabilities, VEW facilitates continuous improvement in the quality of generated test cases. As a result, the VEW not only addresses the current challenges faced by system testers but also paves the way for more innovative and efficient testing methodologies in the automotive software industry.

### Current automotive tester workflow

Today, the process of creating test cases is often manual and time-consuming, involving extensive documentation and iterative reviews to verify completeness and accuracy. Functional requirements are derived from user stories and use cases, while nonfunctional requirements are informed by industry standards and regulatory guidelines.

### Workflow with AI-powered capabilities

To address this challenge, we created an artificial intelligence (AI)–powered extension of VEW built on AWS, helping make this process more efficient.

The workflow involves four main steps:

1. Export requirement data from the requirement management system

2. Import this data into VEW

3. Use the VEW feature to generate test cases

4. Export the test cases data from VEW to then use it in the testing tool

First, testers upload requirement data from their requirement management system into VEW. The requirement data is parsed on the user side and saved.

[![Figure1](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/02/Figure1.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/02/Figure1.png)

For each requirement, the test case capability on VEW can generate a detailed description of the applicable classification categories, such as “control function” or “functional safety,” based on the definitions provided in the prompt. This helps testers better understand the type of requirement they’re dealing with and the relevant characteristics to consider.

[![Figure2](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/02/Figure2.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/02/Figure2.png)

Before moving to the next step, the tester must validate whether the classification is accurate and edit it if necessary. The classification from the tester will then be used as input for the following phase.

In the next phase, VEW generates detailed test case descriptions for each requirement using appropriate testing techniques for this use case, like black box testing. Testers can then review, edit, and accept these test cases.

[![Figure3](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/02/Figure3.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/02/Figure3.png)

Once the classification and test cases are generated and accepted by the tester, the workflow saves the accepted generated test cases, letting testers export the test cases and use them in a test-running tool.

For both classification and test case generation, the tester has to validate the system’s results before moving to the next step to promote accurate results. This changes the tester’s workflow from having to create these test cases from scratch or based on a template to simply reviewing them. This human-in-the-loop approach lets the tester use the efficiency and consistency of the automated system while maintaining oversight and control, helping testers develop more reliable and exhaustive test cases.

In this section, we discussed the workflow to automate test case generation using AI. The test case creation time is reduced by up to 80%, helping dramatically improve efficiency and maintain quality. In the next chapter, we’ll look at the solution architecture that enables this workflow.

### Solution architecture

The following diagram shows the core components of the feature with the AI capabilities being powered by [Amazon Bedrock](https://aws.amazon.com/bedrock/).

[![Figure 4](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/02/Figure-4.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/02/Figure-4.png)

1. Testers use the web interface to classify a requirement or generate a test case. The interface sends a request to [Amazon API Gateway](https://aws.amazon.com/api-gateway/), which is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.

2. Amazon API Gateway uses an integration in [AWS Lambda](https://aws.amazon.com/pm/lambda/?trk=8567f554-501a-4344-8225-14bff7b2aa90&sc_channel=ps&s_kwcid=AL!4422!10!71674651309632!71675180089924&ef_id=53ae5df2269c124ed5af3b04e450f38a:G:s&msclkid=53ae5df2269c124ed5af3b04e450f38a), which is a service that lets users run code without provisioning or managing servers, to forward the request to the API lambda entry point.

3. The AWS Lambda function calls the API in Amazon Bedrock, which is a fully managed service that provides a single API to access and use various high-performing foundation models, from a provisioned account. Response time is around 5 seconds. We used [Anthropic’s Claude in Amazon Bedrock](https://aws.amazon.com/bedrock/claude/), the Instant and 2.0 versions for the classification and test case generation steps, respectively, since the Claude models provide strong general capabilities and the chosen ones are particularly cost-effective.

4. Once the user accepts the classification and test cases, the results are saved to [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)—a serverless, NoSQL database service that allows you to develop modern applications at any scale.

This shows that this use case can be accessible and cost-effective for a range of organizations. Even if the setup for your test cases involves more complex conditions and requirements, today’s language models may be able to tackle your sophisticated testing needs and accelerate your workflow.

### Prompt engineering

A critical component for this workflow is the quality of the provided prompt. Besides the chosen model, the prompt carries the most weight in generating outcomes. We employed various [prompt engineering](https://aws.amazon.com/blogs/machine-learning/prompt-engineering-techniques-and-best-practices-learn-by-doing-with-anthropics-claude-3-on-amazon-bedrock/) techniques to achieve better results.

One such technique is role-playing – for example, the system can be asked to assume the persona of a test engineer.

The prompt is as follows: “You are a test engineer for software testing and black box test techniques with expertise in software requirement classification.” This sets the stage for a response grounded in industry expertise.

The prompt comes with instructions and background information on different types of functional and nonfunctional requirements, helping verify that the system has the required understanding of the classification criteria. This contextual information is crucial for the system to categorize the given software requirement.

Furthermore, the prompt structures the response format with clearly defined sections for each requirement type. This structured approach helps the system organize its thoughts and deliver a well-formatted output, aligning with the prompt’s expectations.

The prompt emphasizes precision and conciseness helping the system focus on relevant aspects without unnecessary commentary. To avoid extraneous text, the prompt could include: “Please skip any suggestions, affirmations, or confirmations in your responses. I prefer direct answers without additional commentary.”

In the second step of test case generation, similar prompt engineering techniques guide the system. The task is framed within the test engineer’s role, helping deliver structured test cases tailored to requirements and black box testing techniques.

Having explored prompt engineering for our AI-powered test case generation system, we now consider potential future developments and enhancements for this use case.

### Future developments

The capability can be expanded and made available more generally by letting the tester experiment with different prompts to determine which prompts, models, and parameters, such as temperature (Temperature in AI models controls the randomness of output, with low values producing more predictable and focused responses, while high values lead to more creative, diverse, and surprising outputs), yield the desired output. As a result of these experiments, custom prompts can be applied to the existing workflows and shared with other testers.

Both the input and output of the workflow are CSV exports and currently isolated from other tools. With the help of API integrations, the user could directly fetch the relevant requirements from the requirements software and upload the generated test cases to the testing software. In the future, this could enable end-to-end use cases from Application Lifecycle Management (ALM) to software development to testing and back to ALM, helping users greatly improve overall efficiency.

This solution features a feedback loop among the testers, the generated classifications, and the test cases. The testers have to actively validate the generated outputs before saving them. The accepted classifications and test cases can also be used as training data to fine-tune the large language model on Amazon Bedrock with the help of a fine-tuning job. This would help further improve the quality of the generated test cases and result in a more positive feedback loop for the quality of the outputs.

### Conclusion

The integration of AI into the Virtual Engineering Workbench (VEW) can help significantly improve automotive software testing efficiency. By using Amazon Bedrock and AWS services, we’ve developed a solution that helps address the complexity of automotive software requirements.

This AI-assisted workflow can reduce test case creation time by up to 80%, while helping users maintain accuracy through a human-in-the-loop approach. The solution can efficiently handle numerous requirements and was implemented in production within 4 weeks.

Looking ahead, end-to-end integration from ALM to software development and testing may offer further efficiencies. This AI-powered approach can tackle current challenges and enable innovative testing methodologies, helping companies manage the complexity of vehicle software systems.

TAGS: [automotive](https://aws.amazon.com/blogs/industries/tag/automotive/), [software defined vehicle](https://aws.amazon.com/blogs/industries/tag/software-defined-vehicle/)

![Tobias Drees](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2023/12/06/Tobias-Drees.jpg)

### Tobias Drees

Tobias Drees is a Cloud Application Architect at AWS Professional Services and supports customers in building and modernizing applications on AWS. He combines his academic background in machine learning and his experience with building cloud applications to develop impactful AI use cases in the automotive industry.

![Daniel Krumpholz](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2023/10/09/Daniel-Krumpholz.jpg)

### Daniel Krumpholz

Daniel Krumpholz is a Senior Engagement Manager at AWS ProServe he builds Virtual Engineering Workbenches and ADAS/AV solutions, exploring innovative approaches and new way of workings. Formerly a Product Manager in Infotainment himself, he's keen on the opportunities the Virtual Engineering Workbench offers to automotive.

![Stanislav Kruglov](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/01/09/Stanislav-Kruglov.jpg)

### Stanislav Kruglov

Stanislav Kruglov is a Senior DevOps Consultant at AWS Professional Services. He works to support enterprise customers in the automotive sector. He is passionate about cloud infrastructure automation and agility while being suspicious of manual processes and the waterfall approach.

Loading comments…

### Resources

* [AWS for Industry](https://aws.amazon.com/industries?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Events](https://aws.amazon.com/events?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Training & Certification](https://aws.amazon.com/training/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Whitepapers](https://aws.amazon.com/whitepapers/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Compliance Reports](https://aws.amazon.com/artifact/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-social)

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