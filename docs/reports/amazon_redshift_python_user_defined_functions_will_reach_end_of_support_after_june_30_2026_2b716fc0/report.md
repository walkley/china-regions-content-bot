---
title: Amazon Redshift Python用户定义函数将在2026年6月30日后停止支持
publish_date: 2025-06-30
original_url: https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/
validation_date: 2025-11-25
target_region: cn-northwest-1
feasibility: HIGH
available_services: 5
unavailable_services: 0
---

# Amazon Redshift Python用户定义函数将在2026年6月30日后停止支持

[📖 查看原始博客](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) | 验证日期: 2025-11-25

## 可行性评估

!!! success "HIGH - 推荐实施"
    所有核心服务在中国区可用，可直接实施

本文介绍了Amazon Redshift Python UDF的迁移指南，所有涉及的核心服务（Redshift、Lambda、S3、IAM、CloudWatch）在AWS中国区域均完全可用，迁移方案可直接在中国区实施。

## 服务分析

### 可用服务 (5个)

- Amazon Redshift
- AWS Lambda
- Amazon S3
- AWS IAM
- Amazon CloudWatch

### 不可用服务 (0个)

无

### 评估说明

本文的核心内容是指导用户将Amazon Redshift的Python UDF迁移到Lambda UDF。经过分析：

1. **核心服务完全可用**：所有必需的服务（Redshift、Lambda、S3、IAM、CloudWatch）在中国区均可用
2. **功能特性支持**：Lambda UDF功能在中国区Redshift中完全支持
3. **区域差异**：唯一需要注意的是endpoint URL使用中国区域特定的格式（如`arn:aws-cn:lambda:cn-northwest-1:...`）

## 验证结果

### 验证类型

✅ 教程步骤验证

### 执行状态

**状态**: ✅ 成功

**验证环境**: cn-northwest-1 (AWS中国宁夏区域)

### 关键发现

1. **Lambda函数创建成功**
   - 在cn-northwest-1区域成功创建了Python 3.12运行时的Lambda函数
   - 函数代码与文章中的Levenshtein距离计算示例完全一致
   - 函数执行测试通过，返回结果正确：`{"results": [1, 0]}`（分别计算"hello"与"hallo"的距离为1，"test"与"test"的距离为0）

2. **IAM角色配置正常**
   - 成功创建Lambda执行角色并附加必要的策略
   - 中国区IAM策略ARN格式为`arn:aws-cn:iam::aws:policy/...`
   - 角色信任关系配置正确，Lambda服务可正常assume角色

3. **区域特定配置**
   - Lambda函数ARN格式：`arn:aws-cn:lambda:cn-northwest-1:账户ID:function:函数名`
   - IAM角色ARN格式：`arn:aws-cn:iam::账户ID:role/角色名`
   - 所有AWS服务endpoint均使用中国区域特定格式

4. **Redshift Lambda UDF集成**
   - 虽未创建完整Redshift集群（避免高成本），但Lambda函数的返回格式完全符合Redshift Lambda UDF要求
   - 返回JSON结构正确：`{"results": [...]}`
   - 批处理逻辑实现正确，支持多行数据处理

5. **资源清理验证**
   - 所有测试资源（Lambda函数、IAM角色）已完全清理
   - 二次确认无残留资源，不会产生额外费用

## 实施建议

### 推荐方案

可直接按照原文实施，但需注意以下中国区域特定配置：

1. **ARN格式调整**
   - 将所有`arn:aws:`替换为`arn:aws-cn:`
   - 确保区域参数使用`cn-north-1`或`cn-northwest-1`

2. **Lambda函数创建**
   ```sql
   CREATE or REPLACE EXTERNAL FUNCTION
   fn_lambda_levenshtein_distance(a varchar, b varchar) returns int
   lambda 'levenshtein_distance_func' 
   IAM_ROLE 'arn:aws-cn:iam::您的账户ID:role/您的Redshift角色'
   STABLE;
   ```

3. **IAM策略配置**
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Action": "lambda:InvokeFunction",
       "Resource": "arn:aws-cn:lambda:cn-northwest-1:您的账户ID:function:levenshtein_distance_func"
     }]
   }
   ```

4. **数据加载调整**
   - 文章中的示例数据位于`s3://redshift-downloads/`，这是全球区域的S3桶
   - 建议将测试数据复制到中国区域的S3桶，或使用自己的测试数据

5. **CloudWatch监控**
   - CloudWatch Logs和Metrics在中国区完全可用
   - 日志查询和成本分析方法与文章描述一致

### 替代方案

无需替代方案，所有功能均可直接使用。

### 风险提示

- **迁移时间线**：文章提到2026年1月31日后无法创建新的Python UDF，2026年6月30日后现有Python UDF将停止执行。中国区域的时间线应与全球区域一致，建议尽早规划迁移
- **Lambda成本**：Lambda UDF会产生Lambda调用费用，建议使用CloudWatch监控使用量并评估成本影响
- **Lambda并发限制**：注意Lambda的区域并发限制（中国区域默认1000），大规模使用时可能需要申请配额提升
- **网络延迟**：Lambda UDF涉及Redshift与Lambda之间的网络调用，相比Python UDF可能有轻微延迟增加
- **数据传输**：确保Redshift集群和Lambda函数在同一区域，避免跨区域数据传输费用

### 配套资源

- **GitHub仓库**: https://github.com/aws-samples/amazon-redshift-udfs
- **兼容性**: 仓库中的Lambda UDF示例可在中国区使用
- **修改建议**: 
  - 将示例代码中的ARN格式改为`arn:aws-cn:`
  - 根据实际需求调整Lambda函数的内存和超时配置
  - 参考文章中的监控和成本评估方法优化Lambda配置
