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

## [AWS Partner Network (APN) Blog](https://aws.amazon.com/blogs/apn/)

# Streamline mNGS analysis with Micronbrane Medical and Basepair on AWS

by Gokhul Srinivasan, Charlie Lee, Kristi Ashton, Rajesh Sukumaran, and Simon Valentine on 09 APR 2025 in [Amazon EC2](https://aws.amazon.com/blogs/apn/category/compute/amazon-ec2/ "View all posts in Amazon EC2"), [Compute](https://aws.amazon.com/blogs/apn/category/compute/ "View all posts in Compute"), [Life Sciences](https://aws.amazon.com/blogs/apn/category/industries/life-sciences/ "View all posts in Life Sciences"), [Partner solutions](https://aws.amazon.com/blogs/apn/category/post-types/partner-solutions/ "View all posts in Partner solutions"), [Thought Leadership](https://aws.amazon.com/blogs/apn/category/post-types/thought-leadership/ "View all posts in Thought Leadership") [Permalink](https://aws.amazon.com/blogs/apn/streamline-mngs-analysis-with-micronbrane-medical-and-basepair-on-aws/)  [Comments](https://aws.amazon.com/blogs/apn/streamline-mngs-analysis-with-micronbrane-medical-and-basepair-on-aws/#Comments)  Share

*By Charlie Lee, Genomics Industry Lead – AWS*

*By Gokhul Srinivasan, Sr.Partner Solutions Architect – AWS*

*By Kristi Ashton, Chief Marketing Officer – Micronbrane Medical*

*By Rajesh Sukumaran, WWPS Sr.Partner Account Manager – AWS*

*By Simon Valentine, Chief Commercial Officer – Basepair*

|  |
| --- |
| [![basepair logo](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2025/04/07/Basepair-logo-apn.jpg)](https://partners.amazonaws.com/partners/0010h00001d50WHAAY/BasePair%20Inc) |
| Basepair |
| [![basepair cta](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2025/04/01/Basepair-APN-Blog-CTA-Button-2024.png)](https://partnercentral.awspartner.com/PartnerConnect?id=0010h00001d50WHAAY&source=&campaign=) |

Metagenomic Next-Generation Sequencing (mNGS) is transforming the ability to study and understand microorganisms, detect pathogens, advance infectious disease research and treatment. Unlike traditional methods, such as culture and PCR, [mNGS sequences](https://pmc.ncbi.nlm.nih.gov/articles/PMC9020267/) bacteria, viruses, fungi, and parasites, identifying [rare and emerging microorganisms](https://pmc.ncbi.nlm.nih.gov/articles/PMC6345613/). A 7-year [UCSF study](https://www.nature.com/articles/s41591-024-03275-1) of mNGS in cerebrospinal fluid for central nervous system infections shows specificity (99.6%), and accuracy (92.9%), outperforms traditional diagnostic methods.

Despite its utility, mNGS workflows are challenging. The technology generates large volumes of data, exceeding 1 GB per sample. This requires specialized bioinformatics tools and high-performance computing systems capable of processing over 100,000 reads/second. These requirements add layers of complexity and cost, limiting mNGS applications. Laboratories struggle with mNGS implementation because of this complexity, massive data analysis, and initial technology development.

In this blog, we explore how [Micronbrane Medical](https://micronbrane.com/) partnered with [Basepair](https://www.basepairtech.com/), an AWS Partner Network (APN) member, to build the PaRTI-Seq Analysis, a mNGS platform, in three months. The customer benefit includes a no-code graphical user interface that white-labels for consistent branding, rapid bioinformatic data analysis with AWS integration, that ensures security, compliance, and cost-efficiency. We explore the architecture, implementation details, and benefits of combining PaRTI-Seq with Basepair on AWS-powered solution.

## Innovating mNGS Workflows with PaRTI-Seq

Micronbrane Medical, a life sciences company based in the Asia-Pacific region, viewed these issues as an opportunity to innovate. The result is [PaRTI-Seq](https://micronbrane.com/micronbrane-medical-introduces-parti-seq-analysis/), the only genomic DNA-based mNGS workflow available on the market with integrated host depletion. A [zwitterionic membrane](https://www.genomeweb.com/sample-preparation/sepsis-study-shows-value-innovations-metagenomic-next-generation-sequencing) is a specific type of membrane technology developed by Micronbrane Medical. Using a novel zwitterionic membrane, the assay effectively reduces host DNA interference, amplifying microbial signal detection. To further ensure high-quality results, Micronbrane addressed contamination risks by incorporating mNGS-grade reagents.

Finally, proprietary TN5-based library kits normalize microbial DNA input, accommodating the wide variability of samples, from low-biomass to high microbial loads. With these advances, PaRTI-Seq minimizes contamination, simplifies the mNGS workflow, and reduces costs while delivering accurate and comprehensive microbial profiling. To complete the product line and offer an end-to-end mNGS solution, the company needed an analysis platform that eliminated the need for software development or setup Amazon EC2 computation resources.

## Addressing mNGS Data Analysis Challenges

While PaRTI-Seq overcomes contamination issues, the data analysis phase of mNGS—the final step in the workflow—presented additional hurdles:

* **Data complexity:** Each sequencing run generates terabytes of raw data, demanding high-performance bioinformatics tools and computational expertise for accurate processing and interpretation.
* **Time inefficiencies:** Data processing and analysis require days or even weeks, delaying critical findings.
* **Interpretation difficulties:** Translating sequencing data into actionable insights requires expertise in microbiology, bioinformatics, and clinical science, which is a challenge to integrate.
* **Data security concerns:** Managing and storing clinical genetic data requires compliance with stringent regulations, adding further complexity to the analysis process.
* **Lack of standardization:** The absence of universally accepted protocols for data analysis leads to inconsistent results across laboratories, reducing reproducibility and comparability.
* **High costs:** Advanced equipment and expertise for mNGS data analysis are expensive, reaching hundreds of thousands of dollars, making them inaccessible for many labs.

Resolving the analysis issues requires tailored bioinformatics solutions at the intersection of biology, computer science, and data analytics, which accelerates lifesaving discoveries.

## From Vision to Reality

Micronbrane Medical developed PaRTI-Seq Analysis, a specialized bioinformatics pipeline paired with a curated database containing genomic information for thousands of microorganisms. The next challenge was to make this software accessible on a platform capable of securely handling data uploads, processing sequencing results, and delivering actionable insights to end-users.

Building a platform in-house requires capital investment in software development, expanded bioinformatics support, and ongoing maintenance. Existing off-the-shelf solutions lacked the flexibility and scalability for mNGS. This left the company at a crossroads: invest heavily in building a custom platform or find an alternative approach to deliver their proprietary pipelines effectively.

## Delivering PaRTI-Seq Analysis Through Strategic Collaboration

To bring PaRTI-Seq Analysis to market efficiently, AWS facilitated a collaboration between Micronbrane Medical and Basepair. Through this collaboration, Micronbrane Medical leveraged Basepair to deliver PaRTI-Seq Analysis pipelines. Basepair offers a fully managed SaaS service on the AWS cloud or as a deployment within a customer’s own AWS account. This offers flexibility to meet varying user needs, including addressing data security concerns, maintaining compliance, and adhering to strict data residency requirements.

The Basepair platform eliminates the need for dedicated DevOps resources to manage data and analyses on AWS. This allowed Micronbrane to focus its expertise on refining and advancing its proprietary pipelines, avoiding the need to establish an in-house software engineering team.

“The partnership allowed us to significantly reduce time to market, enabling us to meet customer needs faster, generate revenue sooner, and rapidly innovate based on market feedback” said Dr. Mengchu Wu, Co-Founder, CEO, and Chairwoman of Micronbrane Medical. “This level of agility and scalability wouldn’t have been possible without Basepair and AWS.”

## Basepair Architecture

Built on AWS, the Figure 1 architecture diagram shows a cross-account AWS setup between Micronbrane Medical’s white-labeled Basepair AWS account and a Customer AWS account. The key components and flow between a Basepair AWS account and customer AWS account.

Basepair AWS Account comprises [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) to load-balance and route the front-end web requests and [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) hosting Basepair front-end and Application Programming Interface (API). There is also a [Amazon Relational Database Service](https://aws.amazon.com/rds/) to persist configuration and transactional data and [AWS Identity and Access Management (AWS IAM)](https://aws.amazon.com/iam/) for role configuration with assume role permissions.

Customer AWS Account AWS IAM configuration with role and permissions to access Basepair account and trust boundary containing Amazon S3 and compute such Amazon EC2 services.

[![Basepair Architecture on AWS](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2025/04/07/basepair-architecture-1.png)](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2025/04/07/basepair-architecture-1.png)

*Figure 1: Basepair AWS cross-account architecture*

The interaction shows three steps using [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html):

1. Initial IAM role authentication
2. Temporary credential exchange from customer to Basepair account
3. Another temporary credential flow, to access trust boundary

## Introducing PaRTI-Seq Analysis on the Basepair Infrastructure

The Basepair infrastructure for PaRTI-Seq Analysis eliminates the need for programming or high-performance computing expertise to perform metagenomic analyses. The user-friendly interface allows scientists to upload sequencing data from any location using any computer. Basepair simplifies the PaRTI-Seq analysis, as detailed Figure 2.

[![Basepair Partiseq](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2025/04/08/basepair-partiseq-1.png)](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2025/04/07/basepair-partiseq.png)

*Figure 2: PaRTI-Seq analysis on Basepair*

The PaRTI-Seq analysis process comprises three phases:

1. **Upload Samples:**
   * Scientists upload samples and choose parameters.
2. **Run Analysis:**
   * The PaRTI-Seq pipelines process both long and short-read sequencing data on Amazon EC2 instances with at least 16 cores ([m8g.xlarge](https://aws.amazon.com/ec2/instance-types/)).
   * The analysis aligns sample data to a database of 1600 clinically relevant pathogens to determine true positives and estimates pathogen populations in metagenomic samples.
   * Depending on sample size, processing time ranges from 30 minutes to 2 hours.
3. **See Results:**
   * PaRTI-Seq packages the pipeline’s output for scientific review. Output includes a list of organisms found by read number and percentage, providing a holistic report.

Basepair’s adoption by Micronbrane Medical transformed their PaRTI-Seq Analysis deployments, allowing for secure AWS cloud use while resolving crucial metagenomic data analysis problems.

“At Basepair, our vision is to empower genomic organizations to concentrate on their core competencies by providing rapid, user-friendly bioinformatics solutions,” said Amit U Sinha, CEO of Basepair. “Our collaboration with Micronbrane Medical exemplifies this commitment, offering a practical approach to advancing metagenomic research, bolstering data security, and enhancing operational efficiency.”

## Basepair advantages

Basepair’s point-and-click interface allows scientists to execute Micronbrane Medical’s bioinformatics pipeline without coding experience. Basepair’s platform allows white labeling within one hour, allowing Micronbrane Medical to offer the PaRTI-Seq Analysis pipelines under its own branding. Micronbrane Medical’s customers have a consistent brand experience eliminating the need for a separate business transaction. AWS integration speeds up sequencing data processes and reporting in 30 minutes, accelerating infectious disease research outcomes. This helps researchers generate insights, advancing the pace of infectious disease research.

The platform connects wet lab scientists with bioinformatician. Researchers explore data independently before conducting complex analyses, improving decision-making efficiency. Using customer AWS cloud resources for core processing reduces data transfer and storage costs while maintaining security compliance. This federation optimizes cost-effectiveness and data protection.

## Conclusion

The collaboration between Micronbrane Medical and Basepair simplified metagenomic data analysis, expedited results, and enhanced research workflows. By combining Micronbrane Medical mNGS innovations with Basepair, laboratories can easily implement mNGS to facilitate scientific discovery that benefits our health and sustainability.

Transform your metagenomic analysis with the combination of [Micronbrane Medical](https://micronbrane.com/)‘s PaRTI-Seq and [Basepair](https://www.basepairtech.com/). [Contact Basepair](https://www.basepairtech.com/demo/) for a personalized demonstration!

## [![Connect with Basepair](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2025/04/07/Partner-Name-APN-Blog-Connect-2-1-1024x170.png)](https://partnercentral.awspartner.com/PartnerConnect?id=0010h00001d50WHAAY&source=&campaign=)Basepair – AWS Partner Spotlight

---

**Basepair,** an AWS Advanced Technology Partner, provides a bioinformatics platform featuring a unique hybrid architecture. This architecture deploys within a customer’s AWS account, ensuring they maintain control over IT governance, security, and usage. Basepair speeds up the migration, deployment, scaling & orchestration of bioinformatics pipelines in AWS.

[Contact Basepair](https://partnercentral.awspartner.com/PartnerConnect?id=0010h00001d50WHAAY&source=&campaign=) | [Partner Overview](https://partners.amazonaws.com/partners/0010h00001d50WHAAY/BasePair%20Inc) | [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=93a65d41-c080-451a-9593-588a29de356d)

TAGS: [AWS Partner Solution](https://aws.amazon.com/blogs/apn/tag/aws-partner-solution/), [Basepair](https://aws.amazon.com/blogs/apn/tag/basepair/), [Compute](https://aws.amazon.com/blogs/apn/tag/compute/), [Life Sciences](https://aws.amazon.com/blogs/apn/tag/life-sciences/), [Micronbane Medical](https://aws.amazon.com/blogs/apn/tag/micronbane-medical/)

Loading comments…

### Resources

* [AWS Partner and Customer Case Studies](https://aws.amazon.com/partners/success/)
* [AWS Partner Network Case Studies](https://aws.amazon.com/partners/partner-success/)
* [Why Work with AWS Partners](https://aws.amazon.com/partners/work-with-partners/)
* [Join the AWS Partner Network](https://aws.amazon.com/partners/)
* [Partner Central Login](https://aws.amazon.com/partners/apn-portal)
* [AWS Training for Partners](https://aws.amazon.com/partners/training)
* [AWS Sponsorship Opportunities](https://aws.amazon.com/partners/marketing/sponsorships)

---

### Follow

* [AWS Partners LinkedIn](https://www.linkedin.com/showcase/aws-partners/)
* [AWS Partners Twitter](https://twitter.com/aws_partners)
* [AWS Partners YouTube](https://www.youtube.com/c/AWSPartnerNetwork)
* [AWS Email Updates](https://partners.awscloud.com/communication-preferences.html)
* [APN Blog RSS Feed](https://aws.amazon.com/blogs/apn/feed)

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