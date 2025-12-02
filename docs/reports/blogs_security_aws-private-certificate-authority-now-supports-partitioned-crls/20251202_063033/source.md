# AWS Private Certificate Authority now supports partitioned CRLs

by Kartik Bhatnagar on 26 NOV 2025 in AWS Private Certificate Authority, Intermediate (200), Security, Identity, & Compliance Permalink  Comments   Share

[Public Key Infrastructure (PKI)](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-pki) is essential for securing and establishing trust in digital communications. As you scale your digital operations, you’ll issue and revoke certificates. Revoking certificates is useful especially when employees leave, migrate to a new certificate authority hierarchy, meet compliance, and respond to security incidents. Use the [Certificate Revocation List (CRL)](https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html) or [Online Certificate Status Protocol (OCSP)](https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html) method to track revoked certificates. You can use Amazon Web Services ([AWS) Private Certificate Authority (AWS Private CA)](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) to create a [certificate authority](https://docs.aws.amazon.com/privateca/latest/userguide/PcaTerms.html#terms-ca) (CA), which publishes revocation information through these methods so that systems can verify certificate validity.

As enterprises continue to scale their operations, they face limitations when using [complete CRLs](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html) to issue and revoke more than 1 million certificates. The workaround of increasing CRL file sizes isn’t viable, because many applications can’t process large CRL files (with some needing a 1 MB maximum). Furthermore, alternative solutions like OCSP may be rejected by major trust stores and browser vendors due to privacy concerns and compliance requirements. These constraints significantly impact your ability to scale PKI infrastructure efficiently while maintaining security and compliance standards.

## Feature release: Addressing challenges

AWS Private CA addresses these challenges with [partitioned CRLs](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html), which enable the issuance and revocation of up to 100 million certificates per CA. This feature distributes revocation information across multiple smaller, manageable CRL partitions, each maintaining a maximum size of 1 MB for more effective application compatibility. At the time of issuance, certificates are automatically bound to specific CRL partitions through a critical [Issuer Distribution Point (IDP)](https://datatracker.ietf.org/doc/html/rfc5280#section-5.2.5) extension, which contains a unique URI identifying the partition. Validation works by comparing the CRL URI in the certificate’s [CRL Distribution Point (CDP)](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#crl-url) extension against the CRL’s IDP extension, which provides accurate certificate validation.

Partitioned CRL provides automatic scaling of certificate issuance limits from 1M to 100M certificates per CA, support for both new and existing CAs, flexible configuration options for CRL naming and paths, backward compatibility by preserving existing complete CRL functionality while offering partitioned CRL as an optional feature, and compliance with industry standards such as [RFC5280](https://datatracker.ietf.org/doc/html/rfc5280) while maintaining security and operational efficiency.

## Configuring Partitioned CRLs in AWS Private CA

You can configure Partitioned CRLs for existing CAs in AWS Private CA by using the following steps.

1. Choose **Private certificate authorities** in the left navigation bar.
2. Choose the hyperlink in the **Subject** column that is your CA to go into its details.

> **Note:** Verify that you are in the correct AWS Region.

![Figure 1: Certificate Authority selection](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/24/AWS_Private-Certificate_Authority_partitioned-CRLs-1.png)

Figure 1: Certificate Authority selection
3. Choose the **Revocation configuration** tab and you should observe the CRL distribution **enabled** or **disabled**. If it is **disabled**, then you should enable it in the next steps.

![Figure 2: Certification Authority general configuration information](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/24/AWS_Private-Certificate_Authority_partitioned-CRLs-2.png)

Figure 2: Certification Authority general configuration information
4. Choose **Edit**.
5. Check the checkbox of **Activate** [**CRL distribution**](https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html).

If CRL distribution was **enabled** already, then skip to step 7.
6. Under **S3 bucket URI**, choose an existing bucket from the list. You can observe detailed steps listed in Step 6 of the instructions in [Create a private CA in AWS Private CA.](https://docs.aws.amazon.com/privateca/latest/userguide/create-CA.html#PcaCreateRevocation)

You must verify that BPA is disabled for the account and for the bucket, and you must manually attach a policy to it before you can begin generating CRLs. Use one of the policy patterns described in [Access policies for CRLs in Amazon S3](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies). For more information, go to [Adding a bucket policy using the Amazon S3 console.](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-bucket-policy.html)
7. Expand **CRL settings** for more configuration options.
8. Check the **Enable partitioning** checkbox to enable partitioning of CRLs. This creates a [partitioned CRL](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#crl-type).

If you don’t enable partitioning, then a [complete CRL](https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html) is created and your CA is subject to the limit of 1M issued or revoked certificates. For more information, go to [AWS Private CA quotas](https://docs.aws.amazon.com/general/latest/gr/pca.html#limits_pca).

![Figure 3: Certificate revocation options](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/24/AWS_Private-Certificate_Authority_partitioned-CRLs-3.png)

Figure 3: Certificate revocation options
9. Choose **Save changes**.
10. CRL distribution shows as **enabled** with partitioned CRLs. The limit of 1M automatically updates to 100M per CA.

![Figure 4: Certificate revocation configuration](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/24/AWS_Private-Certificate_Authority_partitioned-CRLs-4.png)

Figure 4: Certificate revocation configuration

## Conclusion

The AWS Private CA partitioned CRLs can deliver substantial benefits across multiple dimensions. From a security perspective, the feature maintains certificate validation while supporting comprehensive revocation capabilities for up to 100M certificates per CA. Therefore, you can respond effectively to security incidents or key compromises. Operationally, it reduces CA rotation, lessening administrative overhead and streamlining PKI management. Furthermore, maintaining CRL partition sizes at 1 MB provides broad compatibility with applications while supporting automated partition management. Moreover, this makes it particularly valuable when you need scalable, standards-compliant certificate management. Regarding compliance, you can use the feature to comply with multiple industry requirements: it supports [WebTrust principles and criteria](https://www.cpacanada.ca/business-and-accounting-resources/audit-and-assurance/Overview-of-WebTrust-services/Principles-and-criteria) and [ETSI TSP standards](https://www.etsi.org/standards#Pre-defined%20Collections), maintains compatibility with [RFC5280](https://datatracker.ietf.org/doc/html/rfc5280), aligns with browser trust store requirements for both CRL and OCSP support, and provides the flexibility needed for emerging standards such as Matter.

Lastly, you can maximize the value of your [general purpose](https://docs.aws.amazon.com/privateca/latest/userguide/short-lived-certificates.html#standard) or [short-lived](https://docs.aws.amazon.com/privateca/latest/userguide/short-lived-certificates.html#short) CA while all certificates remain revocable by enabling Partitioned CRL for no added charge on top of AWS Private CA and Amazon Simple Storage Service (Amazon S3).

Start creating your CA in [AWS Private CA using AWS Management Console](https://console.aws.amazon.com/acm-pca/).

If you have feedback about this post, submit comments in the **Comments** section below.

![Kartik Bhatnagar](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/24/Author.png)

### Kartik Bhatnagar

Kartik is a San Francisco-based Solutions Architect at AWS, specializing in data security. With experience serving both startups and enterprises across fintech, healthcare, and media industries as a DevOps Engineer and Systems Architect, he helps customers design secure, scalable AWS solutions. Off-duty, he enjoys cricket, tennis, food hopping, and hiking.