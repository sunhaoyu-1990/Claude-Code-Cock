---
name: speckit-specify
description: 根据自然语言功能描述，自动创建或更新项目级功能规格说明（Feature Specification），并完成质量校验，为后续澄清与技术规划提供高质量输入。
---

# Speckit_Specify

## 🧠 Skill 简介

**Speckit_Specify** 是一个“**从自然语言到可规划规格说明**”的规范化能力 Skill。  
它用于将用户提供的**功能想法 / 需求描述**，自动转化为：

- 结构完整、无实现细节的 **功能规格说明（Spec）**
- 与 Git 分支、Spec 文件一一对应的 **可追踪 Feature 单元**
- 可直接进入 "speckit-clarify" Skill 与 "speckit-plan" Skill 的 **高质量输入**

该 Skill 专注于 **“WHAT & WHY”**，而非 **“HOW”**。

---

## 🎯 适用场景（When to Use This Skill）

当你需要做以下事情时，应使用本 Skill：

- 从一句或一段自然语言需求，生成正式的功能规格说明
- 在项目中创建一个新的 Feature 分支与对应 Spec
- 将模糊需求收敛为**可测试、可评审、可规划**的规范文档
- 在进入技术方案设计（Plan）之前，确保需求本身是“干净的”
- 避免实现细节过早污染需求阶段

---

## 📥 输入（Input）

- **用户输入内容**：  
  用户在调用 Skill 时提供的自然语言功能描述  

要求：
- 输入不能为空
- 不要求结构化
- 可以是业务语言、产品语言或技术背景描述

---

## 🧩 Skill 核心能力

### 1️⃣ Feature 标识生成（Branch & Spec Naming）

- 从功能描述中自动提取核心语义
- 生成 **2–4 个词的短名称（short-name）**
- 遵循 `动作-名词` 风格（如：`user-auth`、`analytics-dashboard`）
- 保留技术术语与缩写（OAuth2、API、JWT 等）

---

### 2️⃣ Feature 编号与唯一性校验

在创建新 Feature 前，自动完成以下检查：

- 远程分支（remote branches）
- 本地分支（local branches）
- 规格目录（specs/）

规则：
- 查找同一 short-name 下的最大编号 N
- 新 Feature 使用 `N + 1`
- 若不存在同名 Feature，则从 `1` 开始
- **每个 Feature 只允许创建一次**

---

### 3️⃣ 功能规格说明生成（Spec Generation）

基于标准 Spec 模板，自动生成完整规格说明，包含但不限于：

- 功能背景与目标
- 用户角色与使用场景
- 功能性需求（Functional Requirements）
- 成功标准（Success Criteria）
- 数据实体（如涉及）
- 假设与依赖

**核心原则**：

- 只描述「用户需要什么」「为什么需要」
- 不包含任何实现方式、技术选型、代码结构
- 面向业务与非技术干系人可读

---

### 4️⃣ 需求澄清机制（Clarification Control）

当需求存在关键不确定性时：

- 使用 `[NEEDS CLARIFICATION: ...]` 标记
- **最多允许 3 个**
- 仅在以下情况使用：
  - 明显影响功能范围
  - 存在多种合理但影响不同的解释
  - 无行业默认值可用

澄清优先级：
1. 功能范围
2. 安全 / 合规
3. 用户体验
4. 技术细节（最低优先）

---

### 5️⃣ 成功标准（Success Criteria）构建

自动生成：

- **可量化**
- **与技术无关**
- **以用户或业务结果为导向**
- **可验证**

示例：
- 用户在 3 分钟内完成核心任务
- 95% 的操作在 1 秒内得到反馈
- 任务完成率提升 40%

---

### 6️⃣ 项目相关代码参考（Specification Quality Validation）

根据确定的需求，在项目查找相关的代码内容，了解项目中的相关实现模式：

```bash
# 查看相关模块实现
ls src/modules/

# 查看类似功能的测试
ls tests/unit/test_modules/

# 阅读相关配置架构
cat src/config/schema.py
```

**关键探索点**：
- 是否有类似功能的模块可以参考？
- 是否有可复用的工具函数？
- 现有的配置模式是什么？
- 相关的测试覆盖了哪些场景？

---

### 7️⃣ 规格质量校验（Specification Quality Validation）

自动生成并维护一个独立的质量检查清单：

- 检查内容完整性
- 检查需求是否可测试
- 检查是否混入实现细节
- 检查澄清项是否已关闭

若发现问题：
- 自动修正并重新校验（最多 3 次）
- 若仍不满足，明确标注风险并告知用户

---

## 📤 输出（Output）

Skill 执行完成后，将返回：

- 新创建或更新的 **Feature 分支名**
- **Spec 文件路径**
- **需求质量检查清单路径**
- 当前 Feature 是否已具备进入下一阶段的条件：
  - "speckit-clarify" Skill

---

## 🔗 Skill 之间的协作（Handoffs）

本 Skill 通常作为 **Feature 生命周期的第一步**，并可自动衔接：

- **Clarify Spec Requirements** → "speckit-clarify" Skill

---

## 🧭 使用准则（Skill Constitution）

- 聚焦 WHAT / WHY，而非 HOW
- 不在 Spec 中嵌入 Checklist
- 不要求用户重复输入已提供的描述
- 优先做出合理假设，仅在必要时请求澄清
- 所有需求必须满足「可测试、无歧义」

---

## ✅ Skill 成功标志

当出现以下状态时，认为 Skill 执行成功：

- Spec 结构完整
- 无残留的关键澄清项
- 所有需求可测试
- 成功标准清晰可验证
- 可安全进入规划阶段

---

*This skill is designed for disciplined, large-scale, and high-quality feature development workflows.*
