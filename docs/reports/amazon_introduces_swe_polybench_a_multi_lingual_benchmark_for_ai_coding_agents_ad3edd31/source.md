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

# Amazon introduces SWE-PolyBench, a multilingual benchmark for AI Coding Agents

by Christian Bock, Luca Franceschi, Laurent Callot, Martin Wistuba, Shihab Rashid, Prabhu Teja, Simon Valentin, Woojung Kim, Giovanni Zappella, and Yuan Zhuang on 23 APR 2025 in [Announcements](https://aws.amazon.com/blogs/devops/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/devops/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Thought Leadership](https://aws.amazon.com/blogs/devops/category/post-types/thought-leadership/ "View all posts in Thought Leadership") [Permalink](https://aws.amazon.com/blogs/devops/amazon-introduces-swe-polybench-a-multi-lingual-benchmark-for-ai-coding-agents/) Share

Coding agents powered by large language models have shown impressive capabilities in software engineering tasks, but evaluating their performance across diverse programming languages and real-world scenarios remains challenging. This led to a recent explosion in benchmark creation to assess the coding effectiveness of said systems in controlled environments. In particular, [SWE-Bench](https://www.swebench.com/) which measures the performance of systems in the context of GitHub issues has spurred the development of capable coding agents resulting in over 50 leaderboard submissions, thereby becoming the de-facto standard for coding agent benchmarking. Despite its significant impact as a pioneering benchmark, SWE-Bench, and in particular its “verified” subset, also shows some limitations. It contains only Python repositories, the majority of tasks are bug fixes, and at over 45% of all tasks, the Django repository is significantly over-represented.

Today, Amazon introduces SWE-PolyBench, the first industry benchmark to evaluate AI coding agents’ ability to navigate and understand complex codebases, introducing rich metrics to advance AI performance in real-world scenarios. SWE-PolyBench contains over 2,000 curated issues in four languages. In addition, it contains a stratified subset of 500 issues (SWE-PolyBench500) for the purpose of rapid experimentation. SWE-PolyBench evaluates the performance of AI coding agents through a comprehensive set of metrics: pass rates across different programming languages and task complexity levels, along with precision and recall measurements for code/file context identification. These evaluation metrics can help the community address challenges in understanding how well AI coding agents can navigate through and comprehend complex codebases

The leaderboard is accessible [here](https://amazon-science.github.io/SWE-PolyBench/). The SWE-PolyBench dataset is available on [Hugging Face](https://huggingface.co/collections/AmazonScience/swe-polybench-67f41a0585f1ecaed5fa3aea) and the paper at [arxiv](https://arxiv.org/abs/2504.08703). Evaluations can be run using the [SWE-PolyBench codebase](https://github.com/amazon-science/SWE-PolyBench).

Below, we describe the key features, characteristics, and the creation process of our dataset alongside the new evaluation metrics, and performance of open source agents from our experiments.

## Key features of SWE-PolyBench at a glance

1. **Multi-Language Support:** Java (165 tasks), JavaScript (1017 tasks), TypeScript (729 tasks), and Python (199 tasks).
2. **Extensive Dataset:** 2110 instances from 21 repositories ranging from web frameworks to code editors and ML tools, on the same scale as SWE-Bench full with more repository.
3. **Task Variety:** Includes bug fixes, feature requests, and code refactoring.
4. **Faster Experimentation:** SWE-PolyBench500 is a stratified subset for efficient experimentation.
5. **Leaderboard:** A [leaderboard](https://amazon-science.github.io/SWE-PolyBench/) with a rich set of metrics for transparent benchmarking.

## Building a comprehensive dataset

The creation of SWE-PolyBench involved a data collection and filtering process designed to ensure the quality and relevance of the benchmark tasks. SWE-Bench, a benchmark for Python code generation, evaluates agents on real-world programming tasks by utilizing GitHub issues and their corresponding code and test modifications. We extended the SWE-Bench data acquisition pipeline to support 3 additional languages besides Python and used it to gather and process coding challenges from real-world repositories as shown in Figure 1.

![A flowchart diagram showing a software development process. It starts with an issue (#3039) and pull request (#3147) on the left, goes through a metadata filter in the middle, then splits into a runtime setup and testing phase on the right. The testing phase feeds into a test-based filter at the end. The diagram includes icons for programming languages like JavaScript, TypeScript, Python, and Java.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/Picture11-4-1024x259.png)

Figure 1: Overview of the SWE-PolyBench data generation pipeline, illustrating the process of collecting, filtering, and validating coding tasks.

The data acquisition pipeline collects pull requests (PRs) that close issues from popular repositories across Java, JavaScript, TypeScript, and Python. These PRs undergo filtering and are set up in containerized environments for consistent test execution. The process categorizes tests as fail-to-pass (F2P) or pass-to-pass (P2P) based on their outcomes before and after patch application. Only PRs with at least one F2P test are included in the final dataset, ensuring that each task represents a meaningful coding challenge. This streamlined approach results in a dataset that closely mimics real-world coding scenarios, providing a robust foundation for evaluating AI coding assistants.

## Dataset characteristics

When constructing SWE-PolyBench, we aimed to collect GitHub issues that represent diverse programming scenarios: issues involving modifications across multiple code files and spanning different task categories (such as bug fixes, feature requests, and refactoring). Tables 1 and 2 provide descriptive statistics on the composition and complexity of SWE-PolyBench full (PB) and SWE-PolyBench500 (PB500). To offer a point of reference, we compare these statistics with those of SWE-Bench (SWE) and SWE-Bench verified (SWEv). Tasks in SWE-PolyBench require on average more files to be modified and more nodes to be changed, which indicates that they have higher complexity and are closer to tasks in real-world projects. The distribution of tasks is also more diverse, in particular for SWE-PolyBench500.

![A comparison table showing statistics for different software benchmarks (SWE-PolyBench, SWE-PolyBench500, SWE-Bench, and SWE-Bench verified). The table has two main sections: Modified Files showing average changes across programming languages (Python, Java, JavaScript, TypeScript), and Task Category distribution showing percentages for Bug Fix, Feature Request, Refactoring, and Miscellaneous tasks](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/Screenshot-2025-04-23-at-11.03.56-AM-1024x264.png)

![A detailed table comparing dataset complexity across different programming languages and benchmarks (SWE, SWEv, PB, and PB500). The table shows statistics for syntax tree node changes, divided into two main sections: Node Change Category percentages (None, Function only, Class only, Mixed) and Node Change Count averages (Function, Class, Number of Nodes). The highest values in each column are shown in bold, with notable variations across Python, Java, JavaScript, and TypeScript implementations.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/Screenshot-2025-04-10-at-3.28.11-PM-1024x547.png)

## New evaluation metrics

To comprehensively evaluate AI coding assistants, SWE-Polybench introduces multiple new metrics in addition to the pass rate. The pass rate is the proportion of tasks successfully solved as measured by the generated patch passing all relevant tests. It is the primary metric for assessing coding agent performance, but it doesn’t provide a complete picture of an agent’s capabilities. In particular, it doesn’t give much information on an agent’s ability to navigate and understand complex code repositories. SWE-PolyBench introduces a new set of metrics based on [Concrete Syntax Tree](https://en.wikipedia.org/wiki/Parse_tree) (CST) node analysis and the established file-level localization metric:

1. **File-level Localization:** assesses the agent’s ability to identify the correct files that need to be modified within a repository. Let us assume that we would need to modify file.py to solve our problem. If our coding agent implements a change in any other file, it would receive a file retrieval score of 0.
2. **CST Node-level Retrieval:** evaluates the agent’s ability to identify specific code structures that require changes. It uses the Concrete Syntax Tree (CST) representation of the code to measure how accurately the agent can locate the exact functions or classes that need modification.

![A side-by-side comparison showing two Git version control diffs. Each diff shows a line being removed (in red, prefixed with '-') where my_var equals 3, and a line being added (in green, prefixed with '+') where my_var equals 2. Above the diffs are connected dots in different colors (green, pink, blue, and yellow) representing Git commit history visualization.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/diagram-20250326-1-300x191.png)

Figure 2: Illustration of CST node changes.

In Figure 2, we see a change in *class node* A materialized by a change in its initialization function on the left path starting from the file node. In contrast to the first change, the change in class B is considered a *function node* change as it doesn’t impact class construction.

Let us assume the change that would solve our problem is the change in the `__init__` function. If our coding agent implements the change in `my_func`, it receives both a class and function node retrieval score of 0.

By combining pass rate assessment with both file-level and CST node-level retrieval metrics, SWE-PolyBench offers a detailed evaluation of AI coding assistants’ capabilities in real-world scenarios. This approach provides deeper insights into how well agents navigate and comprehend complex codebases, going beyond simple task completion to assess their understanding of code structure and organization.

## Performance of open-source coding agents

### Key Findings

1. **Language Proficiency:** Python is the strongest language for all agents, likely due to its prevalence in training data and existing benchmarks.
2. **Complexity Challenges:** Performance degrades as task complexity increases, particularly when modifications to 3 or more files are required.
3. **Task Specialization:** Different agents show strengths in various task categories (bug fixes, feature requests, refactoring).
4. **Context Importance:** The informativeness of problem statements impacts success rates across all agents (refer to [Figure 5](https://arxiv.org/html/2504.08703#A1.F5) of the appendix paper for details about this analysis).

Many existing open-source agents are designed primarily for Python. Adapting them to work for all four languages of SWE-PolyBench required adjusting test execution commands, modifying parsing mechanisms, and adapting containerization strategies for each language. We adapted and evaluated three open-source agents on SWE-PolyBench. The aforementioned adjustments are reflected by the added “-PB” suffix to the original agent names.

![Two radar charts comparing three AI models: Aider-PB Sonnet 3.5, Agentless-PB Sonnet 3.5, and SWE-agent-PB Sonnet 3.5. The left chart shows performance across programming languages (Java, JavaScript, TypeScript, Python). The right chart displays performance in different coding styles (Functional only, Single Function, All, Mixed, No nodes, Single Class, Class only). Each model is represented by a different colored line, with Aider-PB generally showing the highest performance across categories.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/radar_plot_ful_vs_nodes-1024x528.png)

Figure 3: Performance of coding agents across programming languages and task complexities, highlighting strengths and areas for improvement.

Figure 3 provides a visual representation of agent performance across different dimensions:

* **Language Proficiency:** The left side of the chart shows that all three agents perform best in Python, with significantly lower pass rates in other languages. This highlights the current bias towards Python in many coding agents and their underlying large language models.
* **Task Complexity:** The right side of the chart illustrates how performance degrades as task complexity increases. Agents show higher pass rates for tasks involving single class or function changes, but struggle with tasks requiring modifications to multiple classes or functions and in instances where both class and function changes are required.

This comprehensive view of agent performance underscores the value of SWE-PolyBench in identifying specific strengths and weaknesses of different coding assistants, paving the way for targeted improvements in future iterations.

In addition to these insights, the evaluation revealed interesting patterns across different task categories as shown in Table 2. The performance data across bug fixes, feature requests, and refactoring tasks reveals varying strengths among AI coding assistants. The performance on bug fixing tasks is relatively consistent. There is more variability between different agents and between multiple runs of a given agent for feature request tasks and refactoring tasks.

![Table 3 showing average pass rates with standard error by task category for three agents: Agentless-PB, SWE-Agent-PB, and Aider-PB. The task categories are Bug Fix, Feature Request, and Refactoring. Aider-PB has the highest pass rates for Bug Fix (13.8) and Feature Request (15.1), while SWE-Agent-PB leads in Refactoring (16.1). Standard errors are provided for each value.](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/Screenshot-2025-04-15-at-11.18.46-AM.png)

## Join the SWE-PolyBench community

SWE-PolyBench and its evaluation framework are publicly available. This open approach invites the global developer community to build upon this work and advance the field of AI-assisted software engineering. As coding agents continue to evolve, benchmarks like SWE-PolyBench play a crucial role in ensuring they can meet the diverse needs of real-world software development across multiple programming languages and task types.

Explore [SWE-PolyBench](https://amazon-science.github.io/SWE-PolyBench/) today and contribute to the future of AI-powered software engineering!

## Resources

* [Dataset](https://huggingface.co/collections/AmazonScience/swe-polybench-67f41a0585f1ecaed5fa3aea)
* [Evaluation harness](https://github.com/amazon-science/SWE-PolyBench)
* [Research paper](https://arxiv.org/abs/2504.08703)
* [Leaderboard](https://amazon-science.github.io/SWE-PolyBench/)

## Authors

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/image9-1.png)

### Christian Bock

Christian Bock is an Applied Scientist at Amazon Web Services working on AI for code.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/badgephotos.corp_.amazon-1.jpg)

### Laurent Callot

Laurent Callot is a Principal Applied Scientist at Amazon Web Services leading teams creating AI agents for software development.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/image10.png)

### Luca Franceschi

Luca Franceschi is an Applied Scientist at Amazon Web Services working on ML models to improve the efficiency of AI agents for code generation.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/badge_photo.jpeg)

### Woo Jung Kim

Woo Jung Kim is an applied scientist at Amazon Web Services. He is developing an AI agentic tool designed to improve developer’s productivity.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/download-2.jpeg)

### Shihab Rashid

Shihab Rashid is an Applied Scientist at Amazon Web Services working on agentic AI for code generation with a focus on multi agent systems.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/image11-1.png)

### Prabhu Teja

Prabhu Teja is an Applied Scientist at Amazon Web Services. Prabhu works on LLM assisted code generation with a focus on natural language interaction.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/simval.jpg)

### Simon Valentin

Simon Valentin is an Applied Scientist at Amazon Web Services working on AI for code.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/image12.png)

### Martin Wistuba

Martin Wistuba is a senior applied scientist at Amazon Web Services. As part of Amazon Q Developer, he is helping developers to write more code in less time.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/image13-2.png)

### Giovanni Zappella

Giovanni Zappella is a Principal Applied Scientist working on the creations of intelligent agents for code generation. While at Amazon he also contributed to the creation of new algorithms for Continual Learning, AutoML and recommendations systems.

![](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2025/04/23/Screenshot-2024-10-04-at-1.28.59-PM.jpg)

### Yuan Zhuang

Yuan Zhuang is an Applied Scientist at Amazon Web Services working on AI agents for code generation.

TAGS: [AI/ML](https://aws.amazon.com/blogs/devops/tag/ai-ml/), [Developer Tools](https://aws.amazon.com/blogs/devops/tag/developer-tools/), [Open Source](https://aws.amazon.com/blogs/devops/tag/open-source/)

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