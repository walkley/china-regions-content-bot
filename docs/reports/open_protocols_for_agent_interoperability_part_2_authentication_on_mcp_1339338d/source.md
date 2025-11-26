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

## [AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/)

# Open Protocols for Agent Interoperability Part 2: Authentication on MCP

by Darin McAdams and Elie Schoppik on 26 JUN 2025 in [Artificial Intelligence](https://aws.amazon.com/blogs/opensource/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Customer Solutions](https://aws.amazon.com/blogs/opensource/category/post-types/customer-solutions/ "View all posts in Customer Solutions"), [Generative AI](https://aws.amazon.com/blogs/opensource/category/artificial-intelligence/generative-ai/ "View all posts in Generative AI"), [Open Source](https://aws.amazon.com/blogs/opensource/category/open-source/ "View all posts in Open Source") [Permalink](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-2-authentication-on-mcp/)  [Comments](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-2-authentication-on-mcp/#Comments)  Share

In [Part 1](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/) of our blog series on Open Protocols for Agent Interoperability we covered how the Model Context Protocol (MCP) can be used to facilitate inter-agent communication and the MCP specification enhancements AWS is working on to enable that. In Part 2 of this blog series we dive deep into authentication in the [latest version](https://modelcontextprotocol.io/specification/2025-06-18) of the MCP specification and discuss some of the contributions from AWS in this release.

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), created by Anthropic, has seen remarkable adoption since its November 2024 launch, drawing interest from developers and organizations worldwide. Initially, MCP kept things straightforward — users simply downloaded and ran local MCP servers right on their workstations. In March, MCP formalized its approach to remote server communication using the Streamable HTTP paradigm. These remote servers eliminate the need for local software installation and updates, reducing security risks and deployment complexity while ensuring users always access the latest version of the service. However, moving to remote servers meant tackling a challenge: how to ensure secure access to these MCP server URLs? While authentication for web services is a well-established field, MCP’s unique objectives led us down some unexpected paths.

As MCP has evolved from Anthropic’s initial vision into a broader industry standard, collaboration with cloud providers like AWS has become essential to realize its full potential at enterprise scale.

Building on Anthropic’s foundational MCP framework, AWS has been working closely with MCP specification and implementation contributors to help address gaps around authentication, contributing to both technical discussions and security best practices in the specification while also submitting the [Java PR](https://github.com/modelcontextprotocol/java-sdk/pull/297) to implement authentication in the SDK. These improvements enable authenticated remote hosting of MCP servers, including on AWS. With the 2025-06-18 release of the MCP specification now including a comprehensive authentication approach, this is a good time to explore the technical solutions and the interesting constraints that shaped them.

## Beyond Just Another Protocol

The goal of MCP is to make AI-powered applications easier to use and integrate. MCP aims to enable a small number of well-designed client applications to connect to a wide array of MCP servers, just as a small number of web browsers and email clients enable connecting to a tremendous number of websites and individuals. Connecting to a new MCP server should be as simple as signing into a website — no special setup required.

When designing protocols, it’s common to provide implementors with flexibility in how they handle authentication. OpenAPI illustrates this pattern well – it allows developers to choose from various authentication mechanisms like API Keys, Bearer Tokens, or Mutual TLS, letting each implementation select what works best for their specific needs.

However, MCP’s goal of enabling seamless connections between clients and many different servers required a different approach. Rather than offering multiple options, the specification needed to establish a recommended path that would work consistently across all implementations. This more prescriptive approach ensures that clients and servers can reliably connect without prior coordination.

OAuth emerged as the natural choice for this standardized approach. As the industry-standard protocol for authorization, OAuth is widely understood, well-tested, and already powers the authentication for many of the services people use daily. More importantly, OAuth’s architecture provided the foundation needed to achieve MCP’s plug-and-play vision.

However, achieving true zero-configuration connectivity required going beyond traditional OAuth implementations. In typical OAuth setups, developers need to manually register their applications with each service provider, carefully copying client IDs, secrets, and endpoint URLs between systems. This manual configuration, while manageable when connecting to just one or two services, becomes unwieldy in MCP’s vision of clients easily connecting to many different servers.

The specification therefore leverages some newer and less commonly used parts of the OAuth framework — particularly around automated discovery and dynamic registration. These capabilities enable MCP clients to automatically discover the necessary endpoints and register themselves with new servers, all without requiring users to copy and paste credentials. To understand how MCP makes this simplicity possible, let’s look at the key pieces of its authentication approach.

## Key Elements of MCP Authentication

The official [MCP specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) provides a comprehensive description of the authentication flow, including this detailed [sequence diagram](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization#sequence-diagram):

[![MCP sequence diagram](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/26/sequence-diagram-1024x960.png)](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/26/sequence-diagram.png)

Let’s walk through how this works in practice, starting with how users first encounter an MCP server.

Adding a new MCP server starts with a URL – a web address that tells the MCP client where to find the server. Users typically discover these URLs from a known location, such as product documentation or online registries. What happens next is a sequence of steps that transforms this URL into a secure, authenticated connection.

As an initialization step, the process begins with the MCP client gathering essential information about how to use and authenticate with the server. To accomplish this, the client first requests the server’s OAuth Protected Resource Metadata (for those interested in the technical details, this is defined in a recent standard, [RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728)). This metadata is like a server’s business card – it contains crucial information about how to establish a secure connection, including where to find the OAuth Authorization Server, which acts as the trusted authority for issuing and managing access credentials.

Once it has located the Authorization Server, the MCP client takes one more preparatory step: it queries the Authorization Server’s own metadata document (a capability defined in [RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414)). This tells the client exactly how to interact with this particular Authorization Server – similar to getting an instruction manual for completing the security handshake.

With this information in hand, the MCP client can introduce itself to the Authorization Server through a process called Dynamic Client Registration. During this step, the client automatically provides details about itself and receives back a unique identifier. This automated approach simplifies what traditionally required manual configuration by administrators — copying and pasting credentials between systems. The MCP specification makes this process seamless to the end user.

By this point, the MCP client has gathered everything it needs to know about connecting securely to this particular MCP server. The final step follows the standard OAuth authorization flow, where the user is directed to the sign-in page for the service in their browser. Like any OAuth-protected service, the service provider handles user authentication and permission management through their standard OAuth implementation – for example, controlling what types of data the MCP client will be allowed to access. After the user authenticates and approves these permissions, the MCP client receives the OAuth access tokens it needs to securely call the MCP server.

Security remains a central consideration in this streamlined process, and comes with important trade-offs. Making connections easier for legitimate servers inevitably makes it easier to connect to malicious ones too. The specification includes technical safeguards against credential theft through [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707), ensuring that credentials issued for one server can’t be misused by another. This means that even if someone accidentally connects to a deceptive server (like Examp1e.com instead of Example.com), that server can’t gain access to the user’s legitimate accounts elsewhere. The MCP client includes the specific server URL as part of the authentication process, and the Authorization Server ensures credentials are strictly limited to that server.

Beyond these technical protections, the MCP registry working group is developing approaches for trusted registries of MCP servers, similar to how app stores and package repositories help users identify legitimate software. While this work is still in progress, the goal is to help users discover and verify trusted services through well-maintained directories of known MCP implementations.

By combining automated discovery, dynamic registration, and enhanced security controls, MCP has automated what was traditionally a manual setup while adding safeguards for this more dynamic world.

## Implementing MCP Authentication: Options and Trade-offs

The MCP specification relies on some newer and less commonly implemented OAuth capabilities, which naturally raises questions from implementors. A common one is about flexibility: what if a service provider wants to implement more, or less, functionality than the specification requires?

The MCP specification is best understood as defining a minimum bar for interoperability, not a maximum limit. Service providers are welcome to offer additional authentication options beyond what the specification prescribes. The main consideration is practical: while MCP SDKs implement this baseline functionality, extending beyond it may require custom client implementations rather than standard MCP clients.

But what about implementing less than the specification requires? The trade-offs here are straightforward. Services that don’t fully conform to the specification won’t be able to participate in the plug-and-play experiences that make MCP distinctive. This could make the service harder to adopt and potentially less compelling. It might also limit compatibility with open source SDKs and tools being developed by the community.

The impact of these trade-offs varies by context. In controlled environments, like corporate networks where both clients and servers are managed internally, deviating from the specification might have little consequence. However, for public APIs serving external customers, or services aiming for broad adoption, the implications of non-conformance become more significant.

A particular concern often comes from service providers who don’t currently use OAuth. For instance, many existing services rely solely on API Keys, leading to worries that supporting MCP would require rebuilding their entire authentication infrastructure – an understandably daunting prospect.

Fortunately, the reality is more manageable. Authentication can be handled in layers, with MCP’s OAuth requirements applying only to the front door of your MCP server. Behind this OAuth facade, your server can transform these tokens into whatever credential types your backend services expect, preserving your existing authentication architecture.

It’s true that implementing this front door does require work, even for organizations already familiar with OAuth. However, this investment in automated discovery and dynamic registration capabilities is what enables the plug-and-play vision described earlier – where clients can seamlessly connect to any MCP server without manual configuration.

Importantly, the MCP design allows this implementation effort to be centralized and done once for an entire organization. This is achieved through another powerful architectural option in the specification: the separation between MCP servers and Authorization Servers. This approach aligns with OAuth’s core principle of separating resource and authorization responsibilities. While an MCP server needs to validate incoming tokens, the more complex aspects of authentication can be delegated to a separate Authorization Server at another URL.

This separation is particularly valuable in enterprise settings, where organizations can designate a single, centralized Authorization Server to handle authentication for all their MCP servers, following OAuth security best practices of centralizing identity management. This approach allows enterprises to integrate their existing Single Sign-On (SSO) infrastructure, enabling users to access any MCP server using their standard corporate credentials. Security teams benefit from having a single control point for managing access policies, audit logging, and credential lifecycle management across all MCP deployments. Meanwhile, individual teams building MCP servers can focus on their core service capabilities, knowing that authentication is handled by the enterprise’s proven identity infrastructure. This pattern mirrors successful enterprise OAuth deployments for web applications and APIs, where centralized identity management has become the de facto standard for balancing security and usability.

The MCP authentication specification thus accommodates a wide range of implementation scenarios. The specification sets clear baseline requirements while providing multiple approaches to meet these requirements – from layered authentication that preserves existing backend systems to centralized Authorization Servers that can serve multiple MCP implementations. Each service provider can choose their optimal balance of compatibility and customization.

## What’s Next for MCP Authentication?

The 2025-06-18 release of the MCP authentication specification establishes a foundation for interactive scenarios, making it simple for users to connect with MCP services. However, as MCP adoption grows, new challenges are emerging that require additional consideration.

As AWS continues to build upon Anthropic’s MCP foundation, we’re exploring how cloud infrastructure can best support the protocol’s evolution. One significant area of focus is supporting autonomous agents — scenarios where there’s no interactive user present. These workload-to-workload interactions typically rely on different OAuth patterns, such as the client credentials flow, which allows services to acquire access tokens without user involvement. While the current specification acknowledges OAuth client secrets as one approach, the industry has learned hard lessons about the security challenges of managing long-lived credentials.

A more promising direction leverages JWT-based assertions in place of client secrets, as defined in [RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523) “JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants”. This approach is gaining popularity for several reasons. JWTs typically have shorter lifetimes than client secrets and can be automatically rotated, reducing the security risks associated with credential compromise. They also align well with modern workload identity standards like [SPIFFE](https://spiffe.io/), where JWTs are automatically available to workloads with built-in lifecycle management. The growing adoption of JWT-based authentication is reflected in the Internet Engineering Task Force (IETF) working group for [WIMSE](https://datatracker.ietf.org/wg/wimse/about/) (Workload Identity in Multi-System Environments), which is actively developing additional standards for workload identity representation using JWTs. These developments provide a path for MCP clients to authenticate to MCP servers using modern, secure practices that avoid the challenges of managing long-lived credentials.

Looking further ahead, MCP deployments are expected to evolve toward multi-hop scenarios, where multiple agents collaborate on complex tasks. These implementations will need to propagate important context across each hop – for example, preserving “on-behalf-of” relationships to track whether actions originated from an interactive user or an autonomous system, and maintaining consistent audit trails across the entire delegation chain. This will require new OAuth profiles tailored to the unique needs of agent-based ecosystems.

## Conclusion

MCP authentication reflects a careful balance between simplicity and security. Starting from the initial challenge of making connections effortless for users, through the practical considerations of implementation, to the emerging needs of autonomous systems, the specification continues to evolve. While the current specification delivers on its core promise of plug-and-play simplicity, the foundation it establishes will support increasingly sophisticated use cases as the MCP ecosystem grows.

This collaborative approach between Anthropic as MCP’s creator and AWS as a key implementation partner demonstrates how open standards can evolve through community contribution while maintaining their core vision. As MCP continues to mature, this model of cooperation between protocol designers and infrastructure providers will be essential for creating AI systems that are both powerful and accessible.

For those interested in diving deeper into these topics, the recent MCP Summit included [several helpful sessions](https://www.youtube.com/playlist?list=PLjULwdJUtFdigAsQ_GMzcPyXaZOeLG04L) that expand on the concepts covered here. These talks provide practical examples and technical context to better understand both the ‘how’ and ‘why’ of MCP authentication:

* [Intro to OAuth for MCP Servers](https://www.youtube.com/watch?v=mYKMwZcGynw) offers a detailed walkthrough of the authorization flows described here.
* [From Experiment to Enterprise](https://www.youtube.com/watch?v=IDWqWdLESgY): How Block Operationalized MCP at Scale shares a real-world implementation story, highlighting why simple authentication was crucial for broad enterprise adoption.
* [MCP 201: The Protocol in Depth](https://www.youtube.com/watch?v=C_nqAWHsldo) provides insider perspective from one of MCP’s co-creators, offering valuable context about the specification’s design decisions and evolution.

As MCP SDKs add support for the latest authentication enhancements, this will enable remote hosting of MCP servers, including on AWS. For teams looking to implement these capabilities, the [MCP Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) documentation and [Security Best Practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices) provide essential guidance. Community feedback has been instrumental in shaping these technologies, and we continue to learn from customers about their needs for secure AI integrations and agent interoperability. We welcome your insights and experiences in the [MCP Discussions](https://github.com/orgs/modelcontextprotocol/discussions).

![Darin McAdams](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/26/Darin-McAdams.png)

### Darin McAdams

Darin McAdams is a Senior Principal Engineer at AWS. During his 25 years at Amazon, Darin has worked across the Amazon.com and AWS landscape, from ordering systems to identity and access management. He co-created the open-source Cedar Policy language and currently focuses on enabling IAM for agentic workloads. He actively participates in the OpenID Foundation and IETF OAuth working groups, contributing to identity standards development.

![Elie Schoppik](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2025/06/26/Elie-Schoppik.png)

### Elie Schoppik

Elie Schoppik leads live education at Anthropic as their Head of Technical Training. He has spent over a decade in technical education, working with multiple coding schools and starting one of his own. With a background in consulting, education, and software engineering, Elie brings a practical approach to teaching Software Engineering and AI. He’s shared his insights at a variety of technical conferences as well as universities including MIT, Columbia, Wharton, and UC Berkeley.

Loading comments…

### Resources

* [Open Source at AWS](https://aws.amazon.com/opensource?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=opensource-resources)
* [Projects on GitHub](https://aws.github.io/)

---

### Follow

* [AWS Open Source Twitter](https://twitter.com/awsopen)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Open Source RSS Feed](https://aws.amazon.com/blogs/opensource/feed?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=opensource-follow)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=opensource-social)

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