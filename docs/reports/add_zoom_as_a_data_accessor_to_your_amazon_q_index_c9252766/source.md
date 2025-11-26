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

## [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Add Zoom as a data accessor to your Amazon Q index

by David Girling, Chinmayee Rane, and Sonali Sahu on 17 APR 2025 in [Amazon Q](https://aws.amazon.com/blogs/machine-learning/category/amazon-q/ "View all posts in Amazon Q"), [Amazon Q Business](https://aws.amazon.com/blogs/machine-learning/category/amazon-q/amazon-q-business/ "View all posts in Amazon Q Business"), [Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Customer Solutions](https://aws.amazon.com/blogs/machine-learning/category/post-types/customer-solutions/ "View all posts in Customer Solutions"), [Enterprise Strategy](https://aws.amazon.com/blogs/machine-learning/category/enterprise-strategy/ "View all posts in Enterprise Strategy"), [Generative AI](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI") [Permalink](https://aws.amazon.com/blogs/machine-learning/add-zoom-as-a-data-accessor-to-your-amazon-q-index/)  [Comments](https://aws.amazon.com/blogs/machine-learning/add-zoom-as-a-data-accessor-to-your-amazon-q-index/#Comments)  Share

For many organizations, vast amounts of enterprise knowledge are scattered across diverse data sources and applications. Organizations across industries seek to use this cross-application enterprise data from within their preferred systems while adhering to their established security and governance standards.

This post demonstrates how [Zoom](https://www.zoom.com/en/products/ai-assistant/) users can access their [Amazon Q Business](https://aws.amazon.com/q/) enterprise data directly within their Zoom interface, alleviating the need to switch between applications while maintaining enterprise security boundaries. Organizations can now configure Zoom as a [data accessor](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-accessing-cross-account.html) in Amazon Q Business, enabling seamless integration between their [Amazon Q index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv.html) and Zoom AI Companion. This integration allows users to access their enterprise knowledge in a controlled manner directly within the Zoom platform.

## How Amazon Q Business and Zoom AI Companion work together

The Amazon Q Business data accessor is a core component within Amazon Q Business. It manages and controls access to data stored in an enterprise’s internal knowledge repositories on Amazon Q Business from an external [independent software vendor (ISV)](https://aws.amazon.com/q/software-provider/) such as Zoom while maintaining security and data access compliance. This feature allows Zoom to retrieve relevant content, enhancing the Zoom AI Companion’s knowledge. It serves as an intermediary that enforces access control lists (ACLs), defining both data source permissions and user access rights to the existing Amazon Q Business index.

Zoom AI Companion, the foundation of Zoom’s AI-first work platform, enhances human connection by working behind the scenes to boost productivity, improve work quality, and strengthen relationships. This April, Zoom [launched](https://news.zoom.com/zoom-agentic-ai/) the Custom AI Companion add-on, enabling organizations to customize AI agents and skills to help meet their specific needs and drive company-wide efficiency. Through its partnership with Amazon Q Business, customers can now connect their indexed data in Amazon Q index to Zoom AI Companion, providing enhanced knowledge and contextual insights.

As an Amazon Q Business data accessor, Zoom AI Companion can interact with the enterprise Amazon Q index in a managed way, enriching content beyond what’s available in Zoom alone. Enterprise users can retrieve contextual information from their Amazon Q index’s multiple connected data sources directly within Zoom, with results seamlessly presented through Zoom AI Companion. Zoom AI Companion can access Amazon Q index data with its native data sources, such as previous call transcripts, to quickly surface relevant information to users. This integration alleviates the need to manually switch between various enterprise systems like Google Drive, Confluence, Salesforce, and more, saving time and reducing workflow disruptions.

For example, while preparing for a Zoom call, users can quickly find answers to questions like “When is customer AnyCustomer’s contract up for renewal, and who signed the last one?” The Amazon Q index processes these queries and delivers results through Zoom AI Companion in real time.

## Solution overview

The following diagram is a high-level architecture that explains how enterprises can set up and access Amazon Q Business indexed data from within the Zoom AI Companion application.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/17/Zoom_as_data_accessor_white.png)

In the following sections, we demonstrate how to configure Zoom as a data accessor and get started using Zoom AI Companion.

## Prerequisites

To implement this solution, you need an AWS account with appropriate permissions.

## Create an Amazon Q Business application

To access indexed data from Amazon Q Business through Zoom AI Companion, organizations must first set up their Amazon Q Business application. The application must be configured with [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) to enable the Zoom data accessor functionality. For detailed guidance on creating an Amazon Q Business application, refer to [Configure application](https://catalog.workshops.aws/amazon-q-business/en-US/200-configure-application).

## Configure access control with IAM Identity Center

Through IAM Identity Center, Amazon Q Business uses trusted identity propagation to provide proper authentication and fine-grained authorization based on user ID and group-based resources, making sure access to sensitive data is tightly controlled and document ACLs are enforced. The ISV is only permitted to access this index using the assigned data accessor.

If you’re using an identity provider (IdP) such as Okta, CyberArk, or others, you can add the IdP to IAM Identity Center as a trusted token issuer. For additional information, see [Configure Amazon Q Business with AWS IAM Identity Center trusted identity propagation](https://aws.amazon.com/blogs/machine-learning/configuring-amazon-q-business-with-aws-iam-identity-center-trusted-identity-propagation/).

For more information on IAM Identity Center, refer to [IAM Identity Center identity source tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html).

## Add Zoom as a data accessor

After creating an Amazon Q Business application with IAM Identity Center, administrators can configure Zoom as a data accessor through the Amazon Q Business console. Complete the following steps:

1. On the Amazon Q Business console, choose **Data accessors** in the navigation pane.

   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/16/add-data-accessor.png)
2. Choose **Add data accessor.**

   ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/16/add-data-accessor-2.png)
3. Choose Zoom as your data accessor.
4. For **Accessor name**, enter a name for your data accessor.
5. For **Data source access**, configure your level of access.

You can select specific data sources to be available through the data accessor. This allows you to control which content is surfaced in the ISV environment. You can use Amazon Q Business pre-built connectors to synchronize content from various systems. For more information, refer to [Supported connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connectors-list.html).

6. For **User access**, specify which users can access the Amazon Q index through the data accessor.

This option enables you to configure granular permissions for data accessor accessibility and manage organizational access controls.

For more information about data access, refer to [Accessing a customer’s Amazon Q index as a data accessor using cross-account access](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-accessing-cross-account.html).

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/16/add-data-accessor-3.jpg)

Administrators can modify data accessor settings at any time after implementation. You can adjust user access permissions, update available data sources, and change the scope of accessibility. To revoke access, complete the following steps:

7. On the Amazon Q Business console, choose **Data accessors** in the navigation pane.
8. Locate the accessor you want to delete and choose **Delete**.
9. Confirm the deletion when prompted.

Removing a data accessor from a data source immediately cancels the ISV’s access to your organization’s Amazon Q index.

## Configure Amazon Q for Zoom AI Companion

To start using Zoom as a data accessor for your Amazon Q Business index, the following information from your enterprise Amazon Q Business application must be shared with Zoom:

* Amazon Q Business application ID
* Amazon Q Business AWS Region
* Amazon Q Business retriever ID
* Data accessor application Amazon Resource Name (ARN)
* IAM Identity Center instance Region

For more information, refer to [Accessing a customer’s Amazon Q index as a data accessor using cross-account access](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv-accessing-cross-account.html).

After you add Zoom as a data accessor, a pop-up window will appear on the Amazon Q Business console. This pop-up contains the required parameters, as shown in the following screenshot.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/16/modal.png)

Navigate to the Zoom App Marketplace to configure Amazon Q in Zoom, and enter the information you collected.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/16/zoom-marketplace.png)

After you submit this information, you’re ready to access Amazon Q index data from Zoom AI Companion.

With AI Companion connected to Amazon Q index, you have the information you need instantly. For example, you could make AI Companion aware of your organization’s IT troubleshooting guides so employees could quickly get help with questions like *“How do I fix a broken keyboard?”*

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/04/17/zoom-pic-new.png)

## Using the SearchRelevantContent API

When an enterprise customer with an Amazon Q index enables a data accessor, it allows authenticated Amazon Q Business users to search and retrieve relevant content in real time while using external ISV platforms (like Zoom). This functionality is achieved through the ISV calling the Amazon Q index [SearchRelevantContent](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SearchRelevantContent.html) API as an external data accessor across accounts. The `SearchRelevantContent` API is specifically designed to return search results from the Amazon Q index, which can be further enhanced by the ISV’s generative AI stack. By using the Amazon Q index `SearchRelevantContent` API, Zoom and other ISVs can integrate query results directly into their environment.

The `SearchRelevantContent` API is an identity-aware API, which means it operates with knowledge of the user’s identity and associated information (such as email and group membership) through the credentials used to call the API. This [identity awareness](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/making-sigv4-authenticated-api-calls.html) is a prerequisite for using the API. When querying the index, it reconciles document access controls against the authenticated user’s permissions. As a result, users can only retrieve results from content they are authorized to access.

When an ISV calls the `SearchRelevantContent` API as a data accessor, both sparse and dense searches are applied to the Amazon Q index, combining keyword search and vector embedding proximity. Results are ranked before being returned to the ISV interface.

For example, if you ask in Zoom, “What is Company XYZ’s engagement on the cancer moonshot project?”, Zoom AI Companion triggers a call to the `SearchRelevantContent` API as a data accessor.

For a more comprehensive code example, see the notebook in [Module 2 – Amazon Q cross-app index](https://github.com/aws-samples/sample-amazon-q-business-isv-workshop/blob/main/02-module-2.ipynb).

The following is a code snippet in Python showing what that search request might look like:

```
search_params = {  'applicationId': Q_BIZ_APP_ID,
    'contentSource': {
        'retriever': {
            'retrieverId': Q_RETRIEVER_ID
            }
    },
    'queryText': 'What is Company XYZ engagement on the cancer moonshot project?',
    'maxResults': 10
}

search_response = qbiz.search_relevant_content(**search_params)
```

The search response will contain an array of results with relevant chunks of text, along with source information, document attributes, and confidence scores. The following is a snippet from the `SearchRelevantContent` API response. This is an example of results you might see from the web crawler data connector used with Amazon Q Business.

```
[
    {
        "content": "\nSeveral initiatives have been launched or will soon launch to address the goals of this next phase, including:\nIncluding more people in expanded and modernized cancer clinical trials\nIncreasing the pipeline of new cancer drugs\nEnsuring access to current and new standards of cancer care\nEnhancing diversity in the cancer research workforce",
        "documentId": "Cancermoonshot",
        "documentTitle": "About The Cancer Moonshot",
        "documentUri": "https://companyxyz/cancermoonshot.html",
        "documentAttributes": [
            {
                "name": "_source_uri",
                "value": {
                    "stringValue": "https://companyxyz.com/cancermoonshot.html"
                }
            }
        ],
        "scoreAttributes": {
            "scoreConfidence": "VERY_HIGH"
        }
    },...]
```

The `SearchRelevantContent` API has a rich set of optional parameters available that ISVs can choose to use. For example, document attributes can be used as filters. If documents with meta attributes have been indexed, and one of these attributes contains the author, it would be possible for an ISV to apply a filter where you can specify an author name. In the following example, results returned are constrained to only documents that have the specified attribute author name “John Smith.”

```
search_params = {
    'applicationId': Q_BIZ_APP_ID,
    'contentSource': {
        'retriever': {
            'retrieverId': Q_RETRIEVER_ID
            }
    },
    'queryText': myQuestion,
    'maxResults': 5,
    'attributeFilter': {
        'equalsTo': {
            'name': 'Author',
            'value': {
                'stringValue': 'John Smith'
            }
        }
    }
}
```

For a more comprehensive reference on what is available in the `SearchRelevantContent` API request object, refer to [search\_relevant\_content](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/search_relevant_content.html).

## Clean up

When you’re done using this solution, clean up the resources you created.

1. Delete the Zoom data accessor from the **Data accessors** console. Deleting this data accessor will delete permissions and access to the data accessor for all users.
2. Delete the Amazon Q Business application that you created as a prerequisite.
   * Navigate to the Amazon Q Business console.
   * Choose **Applications** on the left menu.
   * Select the application you created.
   * Choose **Delete** from under **Actions** to delete the application.

Deleting the Amazon Q Business application will remove the associated index and data source connectors, and prevent incurring additional costs.

## Conclusion

Amazon Q indexes offers a transformative approach to workplace efficiency. By creating a centralized, secure repository for your organization’s data, you can seamlessly integrate vital information with your everyday productivity tools like Zoom AI Companion.

In this post, we explored how Amazon Q Business enterprise users can add data accessors to integrate with external parties like Zoom AI Companion, allowing users to access their enterprise knowledge in a managed way directly from within those platforms.

Ready to supercharge your workforce’s productivity? Start your Amazon Q Business journey today alongside Zoom. To learn more about Amazon Q Business data accessors, see [Enhance enterprise productivity for your LLM solution by becoming an Amazon Q Business data accessor](https://aws.amazon.com/blogs/machine-learning/enhance-enterprise-productivity-for-your-llm-solution-by-becoming-an-amazon-q-business-data-accessor/).

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/04/09/girling.jpg)****David Girling** is a Senior AI/ML Solutions Architect with over 20 years of experience in designing, leading, and developing enterprise systems. David is part of a specialist team that focuses on helping customers learn, innovate, and utilize these highly capable services with their data for their use cases.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/02/18/chinrane-1-1.png)****Chinmayee Rane** is a Generative AI Specialist Solutions Architect at AWS, with a core focus on generative AI. She helps Independent Software Vendors (ISVs) accelerate the adoption of generative AI by designing scalable and impactful solutions. With a strong background in applied mathematics and machine learning, she specializes in intelligent document processing and AI-driven innovation. Outside of work, she enjoys salsa and bachata dancing.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2020/07/22/sonali-sahu-100.jpg)****Sonali Sahu** is leading the Generative AI Specialist Solutions Architecture team in AWS. She is an author, thought leader, and passionate technologist. Her core area of focus is AI and ML, and she frequently speaks at AI and ML conferences and meetups around the world. She has both breadth and depth of experience in technology and the technology industry, with industry expertise in healthcare, the financial sector, and insurance.

Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=machine-learning-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=machine-learning-resources)

---

### Blog Topics

* [Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/)
* [Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-comprehend/)
* [Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-kendra/)
* [Amazon Lex](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-lex/)
* [Amazon Polly](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-polly/)
* [Amazon Q](https://aws.amazon.com/blogs/machine-learning/category/amazon-q/)
* [Amazon Rekognition](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-rekognition/)
* [Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/sagemaker/)
* [Amazon Textract](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-textract/)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=maching-learning-social)

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