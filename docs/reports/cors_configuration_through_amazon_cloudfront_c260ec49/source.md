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

## [Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/)

# CORS configuration through Amazon CloudFront

by Rishu Gupta and Pawan Prabhu on 16 MAY 2025 in [Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/amazon-cloudfront/ "View all posts in Amazon CloudFront"), [Edge](https://aws.amazon.com/blogs/networking-and-content-delivery/category/edge/ "View all posts in Edge"), [Lambda@Edge](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/lambdaedge/ "View all posts in Lambda@Edge"), [Networking & Content Delivery](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/ "View all posts in Networking & Content Delivery"), [Technical How-to](https://aws.amazon.com/blogs/networking-and-content-delivery/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/blogs/networking-and-content-delivery/cors-configuration-through-amazon-cloudfront/) Share

Cross-origin resource sharing (CORS) is a security feature implemented by web browsers that controls which web pages or web applications are allowed to make requests to a different domain or [origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin). In other words, CORS is a mechanism that prevents a web page hosted on one domain from making requests for resources from a different domain unless the target domain explicitly allows it. This helps protect against potential security vulnerabilities such as [cross-site request forgery (CSRF)](https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#cross-site_request_forgery_csrf) and makes sure that sensitive data isn’t accessed by unauthorized websites. CORS is typically configured on the server-side by adding specific HTTP headers to responses, indicating which domains are permitted to access its resources. Furthermore, it applies to resources fetched through [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest), [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), [Web Fonts](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Web_fonts), and [WebGL textures](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Using_textures_in_WebGL) that are requested from a different domain from the one serving the web page. This helps make sure of secure and controlled data sharing between different websites or web applications.

## **Cross-origin working and the significance of CORS request/response headers**

Initially the browser/client sends an HTTP request to the application server, receives data as an HTTP response, and displays it. In browser terminology, the current browser URL is called the current origin and the third-party URL is the cross-origin.

When you make a cross-origin request, this is the request-response process:

1. **Initiation**: Browser sends an HTTP request from a web page hosted on one domain (domain, scheme, or port) to a different origin.
2. **Preflight request (optional)**: If the request is a non-simple request or uses certain methods (such as PUT, DELETE) or has headers (such as Authorization), then the browser may initially send a preflight OPTIONS request to the server to determine if the actual request is safe to send.
3. **Server processing**: The server evaluates its CORS policy to determine whether it allows requests from the origin of the requesting domain. It does this by inspecting the origin request header.
4. **CORS response headers**: If the server allows requests from the origin, then it includes specific CORS headers in the response, such as [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) along with other headers, indicating which origins are allowed.
5. **Browser validation**: The browser checks the CORS headers in the response. If the response headers allow the request, then the browser proceeds with sending the actual request. Otherwise, it blocks the request and may throw a CORS related error in the developer console.
6. **Response handling**: The browser sees the access control request headers and shares the returned data to the client application.

[![CORS preflight request workflow](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/04/13/figure1.png)](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/04/13/figure1.png)

*Figure 1: CORS preflight request workflow*

Alternatively, if the server doesn’t want to allow cross-origin access, then the browser responds with an error message. Depending on the nature of the requests, the cross-origin request flow can differ, as shown in the preceding figure. In the following sections, we discuss Simple CORS and Preflight CORS requests.

### **Simple CORS requests**

Simple CORS requests are the most direct type of CORS request. They are automatically generated by modern web browsers when certain conditions are met, allowing for cross-origin requests without the need for a preflight request.

To qualify as a Simple CORS request, the following conditions must be met:

* **HTTP methods**: Only HTTP methods such as GET, POST, or HEAD are allowed. If the request uses any other method, then it triggers a preflight request.
* **Content-Type header**: The Content-Type header in the request must be one of the following: application/x-www-form-urlencoded, multipart/form-data, or text/plain. If the request uses any other content type, then it triggers a preflight request.
* **Custom headers**: Custom headers can be included in the request, but only specific headers defined as [simple](https://fetch.spec.whatwg.org/#cors-safelisted-request-header)headers by the CORS specification are allowed. These simple headers include common ones such as Accept, Accept-Language, Content-Language, and Range (only with a [simple range header value](https://fetch.spec.whatwg.org/#simple-range-header-value)). Any non-simple header triggers a preflight request.

Simple CORS requests are less complex and faster to execute because they don’t involve a preflight check with the server. Instead, the browser checks if the preceding conditions mentioned are met and, if so, allows the request to proceed.

`> GET /test.html HTTP/2`

`> Host: d1234test.cloudfront.net`

`> User-Agent: curl/8.1.2`

`> Accept: */*`

`> Origin: www.example.com <----- indicates the origin that caused the request`

In this case, the server must return the [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) response header.

### **Preflight CORS requests**

Preflight CORS requests are more elaborate than Simple CORS requests and are used when a request doesn’t meet the criteria for a Simple CORS request. A preflight request is an HTTP OPTIONS request that is sent to the server before the actual request to make sure that the server supports cross-origin requests from the requesting domain.

Key factors that trigger preflight requests include:

* **Non-simple headers**: When the request includes custom headers that aren’t considered “simple” headers, a preflight request is generated.
* **Credentials**: If the request includes credentials (for example cookies, HTTP authentication), then a preflight request is typically needed.

The preflight request includes the HTTP method through the `Access-Control-Request-Method` request header and other headers that are used in the actual request through the `Access-Control-Request-Headers` header. The server must respond with appropriate CORS headers indicating whether the requested cross-origin interaction is permitted. If the server approves, then the browser proceeds with the actual request.

`> OPTIONS /test.html HTTP/2`

`> Host: d1234test.cloudfront.net`

`> User-Agent: curl/8.1.2`

`> Accept: */*`

`> Origin: www.example.com <----- indicates the origin that caused the request`

`> Access-Control-Request-Method: GET`

`> Access-Control-Request-Headers: x-custom`

`> GET /test.html HTTP/2 <----- Actual request`

`> Host: d1234test.cloudfront.net`

`> User-Agent: curl/8.1.2`

`> Accept: */*`

`> Origin: www.example.com <----- indicates the origin that caused the request`

`> x-custom: custom-value`

In this case, the server must respond with these response headers: [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin), [Access-Control-Allow-Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods), and [Access-Control-Allow-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) for preflight request.

## **Configuring CORS from the Amazon CloudFront end**

### **First option: [Response header policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.html)**

[Amazon CloudFront](https://aws.amazon.com/cloudfront/) allows you to control/customize response headers being sent back to the viewers through response header policies with little or no conditionality, as shown in the following figure. Response headers policies streamline the process of HTTP header response manipulation so that you can define CORS, security, and custom response headers as a configuration setting in CloudFront through the console or the API. By using response headers policies (RHP), you don’t need to write the code. Instead, you can use the console or API to define CORS/Security/custom headers. RHP comes free of cost and is easy to configure.

*[![Handling CORS with CloudFront](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/04/13/figure2.png)](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/04/13/figure2.png)*

*Figure 2: Handling CORS with CloudFront*

If you have a Simple CORS use-case requirement, then you can use the Simple CORS AWS Managed RHP.

If your use-case has a preflight request (also known as an OPTIONS request) as well, then you can use [CORS-With-Preflight](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-response-headers-policies.html#managed-response-headers-policies-cors-preflight) RHP.

These policies cover a wider audience, and you want specific policies where you can allow only specific origin, headers, or methods. Therefore, you can create your own RHP for a custom CORS requirement. To create RHP, you can refer to [this CloudFront developer guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/creating-response-headers-policies.html).

### **Second option: [CloudFront functions/Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html)**

If you have a requirement of handling OPTIONS directly at the CloudFront level or having a requirement of a preflight worker, then you can configure CloudFront Function on the viewer-request event. The following code is the sample code that would respond back with CORS headers for the OPTIONS method request directly from the edge without the need to forward the requests to the origin server. This decreases latency and also reduces the load on origin, thus improving the overall performance of your web application.

**Sample code:**

`function handler(event) {`

`var request = event.request;`

`var response = {`

`statusCode: 200,`

`statusDescription: 'Ok',`

`headers:``{ "access-control-allow-methods": { "value": "GET" } }`

`};`

`var headers = response.headers;`

`// If origin header is missing, set it equal to the host header.`

`if (request.method == 'OPTIONS'){`

`headers['access-control-allow-origin'] = {value: "https://example.com"};`

`headers['access-control-allow-methods']= {value: "GET"};`

`headers['access-control-allow-headers']= {value: "X-PINGOTHER"};`

`return response;`

`}`

`return request;`

`}`

For actual requests, you can use the CloudFront response header policy that allows you to configure and customize CORS headers directly at the edge.

However, there are various use-cases where the requirement is to provide CORS header values in the response based on certain conditions. For example, based on ‘access-control-allow-origin’ header values, you need to define the ‘access-control-allow-headers’ value. Then, the edge functions on the viewer/origin response events would be needed because RHP can’t perform conditional checks. The sample code can be found in [this CloudFront developer guide.](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/example-function-add-cors-header-response.html)

If the origin encounters errors such as server-side failures or the origin is unreachable, then CORS headers may not be correctly set or could be missing, which can lead to CORS errors. Proper CORS handling in these situations is vital for keeping the web applications secure and reliable. Therefore, in these cases, you can use [Lambda@Edge](https://aws.amazon.com/lambda/edge/) at the origin-response event where you can write custom code and dynamically adjust CORS headers as needed, even when the origin encounters errors.

### **Third option: CORS handling at origin**

Although CloudFront offers robust CORS handling mechanisms, the advantages of handling CORS at the origin servers are substantial. The ability to accomplish granular control, consistent CORS handling across multiple CDNs, and enhanced security through origin specific policies can significantly impact the security and performance of web applications.

When you have enabled CORS on an [Amazon S3](https://aws.amazon.com/s3/) bucket or a custom origin, you must choose specific headers to forward through [Cache policy or Origin Request policy](https://repost.aws/knowledge-center/no-access-control-allow-origin-error) to respect the CORS settings. The [headers that you must forward](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html#header-caching-web-cors) differ depending on the origin (Amazon S3 or custom origin) and whether you want to cache the OPTIONS responses.

However, you can experience inconsistent CORS issues if you configure the Managed CORS (Amazon S3 or custom origin) origin request policy to forward these headers and when you have enabled caching through the cache policy (for example, Managed [CachingOptimized](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html#managed-cache-caching-optimized) policy). In this case, if CloudFront receives a first request that doesn’t contain an ‘Origin’ header, then by default it caches the first response without the CORS response and uses this for all future requests for this object until it expires. If a user requests the same object before it expires, then they don’t get the proper CORS response headers and the browser would fail to load the asset, even if the subsequent request contains the ‘Origin’ header.

The ‘Origin’ header is added in the viewer request to CloudFront, which CloudFront forwards to the origin. Optionally, you can configure a [CloudFront Function that adds an ‘Origin’ HTTP header](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/example-function-add-cors-header-request.html) to the request if the request doesn’t already contain this header. This makes sure the ‘Origin’ header is forwarded in each request to CloudFront and then further to the origin.

## **Conclusion**

In conclusion, handling CORS in Amazon CloudFront is critical to making sure of smooth and secure interactions between web applications and resources hosted on different origin servers. The CloudFront response header policy allows a centralized and efficient way of managing CORS configurations by enabling control over allowed origins, headers, and methods.

Moreover, CloudFront Function and Lambda@Edge Function offer the necessary flexibility to implement custom CORS logic directly in the edge, and they allow for seamless integration with existing workflows. Whether it’s modifying response headers, dynamically generating CORS headers based on certain conditions, or implementing complex CORS rules, these edge functions offer a scalable and efficient option. Alongside the added benefits, there are [further costs](https://aws.amazon.com/cloudfront/pricing/#Pricing_components) incurred when using edge functions as compared to configuring the CloudFront response header policy, which comes at no extra cost. You should assess the cost-effectiveness based on specific use-cases.

However, for scenarios where extensive CORS handling requirements or fine-grained control is necessary, handling CORS directly at the origin server is a viable option. This allows you to retain full control over the CORS policy, and this could be very useful in multi-CDN architectures where you can have the CORS policy set at a single place for different CDNs.

For CORS handling, CloudFront offers a spectrum of options such as response header policy, edge functions, and the flexibility to handle CORS at the origin server. However, the choice of approach depends on certain factors such as complexity, scalability, and the requirements of the application’s architecture.

## About the authors

![Rishu Gupta.jpg](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/05/07/6b94365d12ad8a2e8082fe13c17583e5.png)

### Rishu Gupta

Rishu is a Senior Cloud Engineer at AWS, helping users enhance their applications’ performance and security. With his cloud expertise, he guides customers through technical challenges and designs secure, scalable solutions tailored to their needs. Beyond work, Rishu is a foodie who loves trying diverse cuisines and exploring new flavors. He also values spending quality time with family and friends, cherishing those precious moments together.

![Pawan Prabhu.png](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2025/05/06/gravatar.png)

### Pawan Prabhu

Pawan Prabhu is a Cloud Support Engineer at AWS and a subject matter expert in Amazon CloudFront and Amazon Simple Email Service. He specializes in providing support to enterprise users across various sectors. Outside of work, he enjoys traveling to new places and exploring their unique cultures.

TAGS: [Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/tag/amazon-cloudfront/), [Amazon CloudFront Functions](https://aws.amazon.com/blogs/networking-and-content-delivery/tag/amazon-cloudfront-functions/), [edge computing](https://aws.amazon.com/blogs/networking-and-content-delivery/tag/edge-computing/), [Lambda@Edge](https://aws.amazon.com/blogs/networking-and-content-delivery/tag/lambdaedge/)

### Resources

* [Networking Products](https://aws.amazon.com/products/networking?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)
* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)
* [Amazon CloudFront](https://aws.amazon.com/cloudfront?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=networking-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
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