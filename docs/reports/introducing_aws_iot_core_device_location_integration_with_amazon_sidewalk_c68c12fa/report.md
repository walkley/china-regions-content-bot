---
title: Introducing AWS IoT Core Device Location integration with Amazon Sidewalk
original_url: https://aws.amazon.com/blogs/aws/introducing-aws-iot-core-device-location-integration-with-amazon-sidewalk/
validation_date: 2025-11-24
target_region: cn-northwest-1
feasibility: LOW
available_services: 6
unavailable_services: 1
---

# Introducing AWS IoT Core Device Location integration with Amazon Sidewalk

[📖 查看原始博客](https://aws.amazon.com/blogs/aws/introducing-aws-iot-core-device-location-integration-with-amazon-sidewalk/) | 验证日期: 2025-11-24

## 可行性评估

!!! danger "LOW - 不建议实施"
    核心服务不可用，需要重大修改或无法实施

Amazon Sidewalk是本方案的核心依赖服务，在中国区域不可用且依赖美国物理网络基础设施，无法通过技术手段替代。

## 服务分析

### 可用服务 (6个)

- AWS IoT Core
- AWS IoT Core Device Location
- AWS IoT Wireless
- Amazon CloudWatch Logs
- AWS IoT Rules
- MQTT

### 不可用服务 (1个)

- **Amazon Sidewalk** - 核心服务

### 评估说明

虽然服务可用性比例达到85.7%（6/7），但Amazon Sidewalk是整个解决方案的核心基础服务，存在以下关键限制：

1. **核心服务不可用**：Amazon Sidewalk是本文介绍的核心技术，整篇博客围绕AWS IoT Core Device Location与Amazon Sidewalk的集成展开。

2. **地理和网络限制**：
   - Amazon Sidewalk是一个社区共享网络，依赖Amazon Echo和Ring设备作为网关（Sidewalk Bridge）
   - 博客明确指出该网络覆盖美国90%以上的人口
   - 该功能仅在US East (N. Virginia)区域可用
   - 中国区域既没有Sidewalk网络基础设施，也没有相应的服务支持

3. **无替代方案**：Amazon Sidewalk是一个专有的低功耗广域网络（LPWAN），使用BLE、LoRa和FSK协议，无法通过其他AWS服务替代。

4. **设备生态系统依赖**：该方案需要Sidewalk兼容的硬件设备和开发套件，这些设备针对美国市场设计。

## 验证结果

### 验证类型

- ⏭️ 已跳过（可行性等级为LOW）

### 执行状态

**状态**: ⏭️ 已跳过

**原因**: 核心服务Amazon Sidewalk在中国区域不可用，且依赖美国物理网络基础设施，无法进行实际部署验证。

## 实施建议

### 推荐方案

**不建议在中国区域实施此方案**

该博客介绍的解决方案完全依赖Amazon Sidewalk网络，而该网络在中国区域不存在且不可用。即使AWS IoT Core和Device Location服务在中国区域可用，没有Sidewalk网络作为连接层，整个方案无法运作。

### 替代方案

如果您需要在中国区域实现类似的IoT设备定位和资产追踪功能，可以考虑以下替代方案：

1. **使用LoRaWAN网络**
   - 实施方式：通过AWS IoT Core for LoRaWAN连接设备，结合AWS IoT Core Device Location服务解析位置
   - 复杂度：中
   - 适用场景：需要低功耗广域网络覆盖的资产追踪应用
   - 注意事项：需要自建或使用第三方LoRaWAN网络基础设施

2. **使用蜂窝网络（NB-IoT/LTE-M）**
   - 实施方式：通过蜂窝网络连接IoT设备到AWS IoT Core，使用Device Location服务或设备内置GPS
   - 复杂度：中
   - 适用场景：需要广域覆盖且对功耗要求相对宽松的场景
   - 注意事项：需要SIM卡和运营商网络支持

3. **使用Wi-Fi/蓝牙定位**
   - 实施方式：设备通过Wi-Fi或蓝牙连接，使用AWS IoT Core Device Location的Wi-Fi/BLE定位功能
   - 复杂度：低
   - 适用场景：室内或Wi-Fi覆盖区域的资产追踪
   - 注意事项：覆盖范围受限于Wi-Fi网络

4. **使用MQTT over 4G/5G**
   - 实施方式：设备通过蜂窝网络使用MQTT协议直接连接AWS IoT Core
   - 复杂度：低
   - 适用场景：对实时性要求高、功耗限制较宽松的应用
   - 注意事项：需要考虑数据流量成本

### 风险提示

- **服务不可用风险**：Amazon Sidewalk在中国区域完全不可用，无任何技术手段可以启用
- **网络基础设施缺失**：即使未来服务开放，也需要大量Echo和Ring设备部署形成网络覆盖
- **设备兼容性风险**：Sidewalk设备和开发套件主要面向美国市场，在中国可能面临认证和合规问题
- **区域限制风险**：该功能明确仅在US East (N. Virginia)区域可用，短期内不太可能扩展到中国区域

### 配套资源

- **GitHub仓库**: 无
- **兼容性**: 不适用
- **修改建议**: 不适用

## 总结

本博客介绍的AWS IoT Core Device Location与Amazon Sidewalk集成方案在中国区域不可行。建议根据实际业务需求，选择上述替代方案中的LoRaWAN、蜂窝网络或Wi-Fi/蓝牙定位方案来实现类似的IoT设备定位和资产追踪功能。
