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

# Amazon Q Developer in GitHub (in preview) accelerates code generation

by Matheus Guimaraes on 05 MAY 2025 in [Amazon Q Developer](https://aws.amazon.com/blogs/aws/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News") [Permalink](https://aws.amazon.com/blogs/aws/amazon-q-developer-in-github-now-in-preview-with-code-generation-review-and-legacy-transformation-capabilities/) Share

|  |
| --- |
| [![Voiced by Polly](https://a0.awsstatic.com/aws-blog/images/Voiced_by_Amazon_Polly_EN.png)](https://aws.amazon.com/polly/) |

Starting today, you can now use [Amazon Q Developer in GitHub](https://github.com/apps/amazon-q-developer) in preview! This is fantastic news for the millions of developers who use GitHub on a daily basis, whether at work or for personal projects. They can now use Amazon Q Developer for feature development, code reviews, and Java code migration directly within the GitHub interface.

To demonstrate, I’m going to use Amazon Q Developer to help me create an application from zero called StoryBook Teller. I want this to be an ASP.Core website using .NET 9 that takes three images from the user and uses [Amazon Bedrock](https://aws.amazon.com/bedrock/) with Anthropic’s Claude to generate a story based on them.

Let me show you how this works.

**Installation**

The first thing you need to do is install the [Amazon Q Developer application in GitHub](https://github.com/apps/amazon-q-developer), and you can begin using it immediately without connecting to an AWS account.

You’ll then be presented with a choice to add it to all your repositories or select specific ones. In this case, I want to add it to my storybook-teller-demo repo, so I choose **Only selected repositories** and type in the name to find it.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/selecting-only-specific-repositories.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/selecting-only-specific-repositories.png)

This is all you need to do to make the Amazon Q Developer app ready to use inside your selected repos. You can verify that the app is installed by navigating to your GitHub account **Settings** and the app should be listed in the **Applications** page.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/amazon-q-developer-in-my-github-app-marked.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/amazon-q-developer-in-my-github-app-marked.png)

You can choose **Configure** to view permissions and add Amazon Q Developer to repositories or remove it at any time.

Now let’s use Amazon Q Developer to help us build our application.

**Feature development** When Amazon Q Developer is installed into a repository, you can assign GitHub issues to the Amazon Q development agent to develop features for you. It will then generate code using the whole codebase in your repository as context as well as the issue’s description. This is why it’s important to list your requirements as accurately and clearly as possible in your GitHub issues, the same way that you should always strive for anyway.

I have created five issues in my StoryBook Teller repository that cover all my requirements for this app, from creating a skeleton .NET 9 project to implementing frontend and backend.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/17/empty-repository-with-5-issues.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/17/empty-repository-with-5-issues.png)

Let’s use Amazon Q Developer to develop the application from scratch and help us implement all these features!

To begin with, I want Amazon Q Developer to help me create the .NET project. To do this, I open the first issue, and in the **Labels** section, I find and select **Amazon Q development agent**.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/21/marked-choosing-label-setup-story.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/21/marked-choosing-label-setup-story.png)

That’s all there is to it! The issue is now assigned to Amazon Q Developer. After the label is added, the Amazon Q development agent automatically starts working behind the scenes providing progress updates through the comments, starting with one saying, `I'm working on it`.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/q-developer-i-am-working-on-it-comment.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/q-developer-i-am-working-on-it-comment.png)

As you might expect, the amount of time it takes will depend on the complexity of the feature. When it’s done, it will automatically create a pull request with all the changes.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/q-developer-finished-full-issue-loo-marked.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/q-developer-finished-full-issue-loo-marked.png)

The next thing I want to do is make sure that the generated code works, so I’m going to download the code changes and run the app locally on my computer.

I go to my terminal and type `git fetch origin pull/6/head:pr-6` to get the code for the pull request it created. I double-check the contents and I can see that I do indeed have an ASP.Core project generated using .NET 9, as I expected.

I then run `dotnet run` and open the app with the URL given in the output.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/17/running-app-after-setup-story-done.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/17/running-app-after-setup-story-done.png)

Brilliant, it works! Amazon Q Developer took care of implementing this one exactly as I wanted based on the requirements I provided in the GitHub issue. Now that I have tested that the app works, I want to review the code itself before I accept the changes.

**Code review**

I go back to GitHub and open the pull request. I immediately notice that Amazon Q Developer has performed some automatic checks on the generated code.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/pull-request-with-automated-code-review-done-marked.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/pull-request-with-automated-code-review-done-marked.png)

This is great! It has already done quite a bit of the work for me. However, I want to review it before I merge the pull request. To do that, I navigate to the **Files changed** tab.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/17/files-changed-tab-marked.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/17/files-changed-tab-marked.png)

I review the code, and I like what I see! However, looking at the contents of .gitignore, I notice something that I want to change. I can see that Amazon Q Developer made good assumptions and added exclusion rules for Visual Studio (VS) Code files. However, JetBrains Rider is my favorite integrated development environment (IDE) for .NET development, so I want to add rules for it, too.

You can ask Amazon Q Developer to reiterate and make changes by using the normal code review flow in the GitHub interface. In this case, I add a comment to the .gitignore code saying, `add patterns to ignore Rider IDE files`. I then choose **Start a review**, which will queue the change in the review.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/17/gitignore-comment-added-review-pending.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/17/gitignore-comment-added-review-pending.png)

I select **Finish your review** and **Request changes.**

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/selecting-request-change-marked.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/selecting-request-change-marked.png)

Soon after I submit the review, I’m redirected to the Conversation tab. Amazon Q Developer starts working on it, resuming the same feedback loop and encouraging me to continue with the review process until I’m satisfied.

Every time Q Developer makes changes, it will run the automated checks on the generated code. In this case, the code was somewhat straightforward, so it was expected that the automatic code review wouldn’t raise any issues. But what happens if we have more complex code?

Let’s take another example and use Amazon Q Developer to implement the feature for enabling image uploads on the website. I use the same flow I described in the previous section. However, I notice that the automated checks on the pull request flagged a warning this time, stating that the API generated to support image uploads on the backend is missing authorization checks effectively allowing direct public access. It explains the security risk in detail and provides useful links.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/security-warning-found-with-image-upload-full-view-with-message-of-q-working-on-fix-suggestion.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/security-warning-found-with-image-upload-full-view-with-message-of-q-working-on-fix-suggestion.png)

It then automatically generates a suggested code fix.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/generating-code-fix-suggestion-for-security-warning.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/generating-code-fix-suggestion-for-security-warning.png)

When it’s done, you can review the code and choose to Commit changes if you’re happy with the changes.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/commit-suggested-code-fix.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/commit-suggested-code-fix.png)

After fixing this and testing it, I’m happy with the code for this issue and move on applying the same process to other ones. I assign the Amazon Q development agent to each one of my remaining issues, wait for it to generate the code, and go through the iterative review process asking it to fix any issues for me along the way. I then test my application at the end of that software cycle and am very pleased to see that Amazon Q Developer managed to handle all issues, from project setup, to boilerplate code, to more complex backend and frontend. A true full-stack developer!

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/application-ready-after-all-issues-done.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/application-ready-after-all-issues-done.png)

I did notice some things that I wanted to change along the way. For example, it defaulted to using the Invoke API to send the uploaded images to Amazon Bedrock instead of the Converse API. However, because I didn’t state this in my requirements, it had no way of knowing. This highlights the importance of being as precise as possible in your issue’s titles and descriptions to give Q Developer the necessary context and make the development process as efficient as possible.

Having said that, it’s still straightforward to review the generated code on the pull requests, add comments, and let the Amazon Q Developer agent keep working on changes until you’re happy with the final result. Alternatively, you can accept the changes in the pull request and create separate issues that you can assign to Q Developer later when you’re ready to develop them.

**Code transformation**

You can also transform legacy Java codebases to modern versions with Q Developer. Currently, it can update applications from Java 8 or Java 11 to Java 17, with more options coming in future releases.

The process is very similar to the one I demonstrated earlier in this post, except for a few things.

First, you need to create an issue within a GitHub repository containing a Java 8 or Java 11 application. The title and description don’t really matter in this case. It might even be a short title such as “Migration,” leaving the description empty. Then, on **Labels,** you assign the **Amazon Q transform agent** label to the issue.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/21/q-transform-label.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/04/21/q-transform-label.png)

Much like before, Amazon Q Developer will start working immediately behind the scenes before generating the code on a pull request that you can review. This time, however, it’s the Amazon Q transform agent doing the work which is specialized in code migration and will take all the necessary steps to analyze and migrate the code from Java 8 to Java 17.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/transform-starts-working.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/transform-starts-working.png)

Notice that it also needs a workflow to be created, as per the documentation. If you don’t have it enabled yet, it will display clear instructions to help you get everything set up before trying again.

[![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/transform-needs-github-actions-enabled.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/05/01/transform-needs-github-actions-enabled.png)

As expected, the amount of time needed to perform a migration depends on the size and complexity of your application.

**Conclusion**

Using Amazon Q Developer in GitHub is like having a full-stack developer that you can collaborate with to develop new features, accelerate the code review process, and rely on to enhance the security posture and quality of your code. You can also use it to automate migration from Java 8 and 11 applications to Java 17 making it much easier to get started on that migration project that you might have been postponing for a while. Best of all, you can do all this from the comfort of your own GitHub environment.

**Now available**

You can now start using [Amazon Q Developer today for free in GitHub](https://github.com/apps/amazon-q-developer), no AWS account setup needed.

Amazon Q Developer in GitHub is currently in preview.

— [Matheus Guimaraes | codingmatheus](https://www.linkedin.com/in/codingmatheus/)

---

How is the News Blog doing? Take this [1 minute survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi)!

*(This [survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_eyD5tC5xNGCdCmi) is hosted by an external company. AWS handles your information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/?trk=4b29643c-e00f-4ab6-ab9c-b1fb47aa1708&sc_channel=blog). AWS will own the data gathered via this survey and will not share the information collected with survey respondents.)*

![Matheus Guimaraes](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/16/me_standing_outdoor-square-2.jpg)

### Matheus Guimaraes

Matheus Guimaraes (@codingmatheus) is a digital transformation specialist focused on AI adoption and microservices architecture. An international keynote speaker with over 20 years in tech, he’s worn many hats: from junior game programmer to CTO and tech co-founder. Matheus has helped companies of all sizes modernize and scale their systems, leading transformation programs and designing cloud-native, AI-ready architectures. Today, he shares his expertise globally through talks, blogs, and videos, passionate about helping others grow in the industry. Outside his professional life, he’s a gamer, swimmer, musician, and firm believer in the powerful intersection of creativity and technology.

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