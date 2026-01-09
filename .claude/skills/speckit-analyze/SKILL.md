---
name: speckit-analyze
description: 在 tasks.md 已生成后，对 spec.md、plan.md、tasks.md 三大核心工件进行“只读、无损”的跨工件一致性与质量分析，识别冲突、重复、歧义、遗漏与宪法（constitution）违反项，并输出结构化分析报告与可选修复建议。
---

# Speckit_Analyze

## 🧠 Skill 简介

**Speckit_Analyze** 是一个“**跨工件一致性与质量审计**”的项目级 Skill。  
它在 `tasks.md` 生成完成之后运行，通过只读方式对以下三类核心工件进行联合分析：

- `spec.md`（需求与验收意图）
- `plan.md`（设计与技术约束）
- `tasks.md`（可执行任务分解）

目标是：在进入实现（implement）之前，系统性发现**高风险不一致**与**覆盖缺口**，避免后续返工。

---

## 🎯 适用场景（When to Use This Skill）

在以下情况下，应使用本 Skill：

- 已成功运行 `speckit-tasks` skill 并生成完整 `tasks.md`
- 准备进入实现阶段（`speckit-implement` skill）前，希望进行质量门禁
- 怀疑存在以下风险：
  - 需求写得很好，但任务没覆盖
  - 计划与需求冲突（术语漂移、实体不一致、架构假设不一致）
  - tasks 引入了 spec/plan 未定义的组件或范围漂移
  - 非功能需求（安全/性能/可用性）被遗漏
  - 宪法（constitution）要求未被满足

---

## 📥 输入（Input）

- **必需工件**
  - `spec.md`
  - `plan.md`
  - `tasks.md`

- **强约束来源**
  - `@.claude/constitution.md`（宪法）

- **用户补充输入（可选）**：`$ARGUMENTS`
  - 用于提供分析侧重点、风险偏好、或已知争议点（例如“重点查安全与性能”）

前提条件：
- 本 Skill 仅在 `tasks.md` 已生成后运行
- 任一必需工件缺失应终止，并提示补齐前置命令

---

## 🧭 运行约束（Operating Constraints）

### 只读、无损（Strictly Read-Only）

- **绝不修改任何文件**
- 只输出结构化分析报告
- 可提供“可选修复计划”，但必须由用户明确确认后才可通过其他命令手工执行修复

### 宪法优先（Constitution Authority）

- 宪法中的 MUST 原则在分析范围内**不可协商**
- 任何宪法冲突自动判定为 **CRITICAL**
- 不允许通过“弱化解释/忽略原则”规避冲突
- 若需要修改宪法原则，必须走独立的宪法更新流程，不属于本 Skill 范畴

---

## 🧩 Skill 核心能力

### 1️⃣ 工件最小上下文加载（Progressive Disclosure）

为保持高信噪比与可重复性，Skill 只加载必要内容：

- 从 `spec.md`：
  - Overview/Context
  - Functional Requirements
  - Non-Functional Requirements
  - User Stories
  - Edge Cases（若存在）

- 从 `plan.md`：
  - 架构/技术栈选择
  - 数据模型引用
  - 分期（phases）
  - 技术约束

- 从 `tasks.md`：
  - Task IDs
  - 任务描述与阶段分组
  - 并行标记 `[P]`
  - 文件路径引用

- 从 `constitution.md`：
  - 原则名称
  - MUST/SHOULD 的规范性约束语句

---

### 2️⃣ 语义模型构建（内部，不直接输出原文）

Skill 会构建内部语义索引，用于跨文档映射：

- **需求清单（Requirements Inventory）**
  - 为每条功能/非功能需求生成稳定 key（slug）
- **用户故事/动作清单（Story/Action Inventory）**
  - 抽取用户动作与验收意图
- **任务覆盖映射（Task Coverage Mapping）**
  - 将任务映射到需求或用户故事（基于显式引用与高置信关键词推断）
- **宪法规则集（Constitution Rule Set）**
  - 提取可判定的 MUST/SHOULD 约束点

---

### 3️⃣ 检测与发现（Findings Detection Passes）

本 Skill 仅聚焦高信号发现，最多输出 50 条 findings（超出部分汇总）。

#### A. 重复（Duplication）

- 近似重复的需求/约束
- 标注更低质量的表述，建议合并与统一表述

#### B. 歧义（Ambiguity）

- “fast / scalable / secure / intuitive / robust”等模糊词未量化
- 占位符与未决标记（TODO、TKTK、???、`<placeholder>`）

#### C. 描述不足（Underspecification）

- 有动词但缺少对象/结果/衡量标准的需求
- 用户故事缺少可对齐的验收意图
- tasks 引用 spec/plan 未定义的组件、模块或范围

#### D. 宪法对齐（Constitution Alignment）

- 任何违反 MUST 的内容
- 宪法要求的质量门禁/章节缺失（按宪法定义）

#### E. 覆盖缺口（Coverage Gaps）

- 需求没有任何任务覆盖
- 任务无法映射到任何需求/用户故事（范围漂移风险）
- 非功能需求没有在 tasks 中体现（例如安全/性能/可观测性）

#### F. 不一致（Inconsistency）

- 术语漂移（同一概念跨文件不同名称）
- 数据实体跨文件不一致（plan 有、spec 无，或反之）
- 任务顺序与依赖矛盾（例如集成先于基础设施
