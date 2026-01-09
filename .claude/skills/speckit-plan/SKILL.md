---
name: speckit-plan
description: 基于既有功能规格说明（Spec）与计划模板，执行项目级实施方案规划流程，生成 research、数据模型、接口契约与快速上手文档等设计工件，并在宪法（constitution）约束下完成门禁校验，为任务拆解与交付检查清单提供高质量输入。
---

# Speckit_Plan

## 🧠 Skill 简介

**Speckit_Plan** 是一个“从规格说明到可实施设计工件”的项目级规划 Skill。  
它在 Spec 已稳定（或已完成澄清）的前提下，使用统一的 **Implementation Plan 模板**与项目 **宪法（constitution）**约束，输出一套可交付、可评审、可拆解任务的设计与规划产物。

该 Skill 的核心目标是：

- 把“需求规格”转化为“可实施的方案与工件”
- 让关键技术决策可追溯、可论证、可替代
- 让接口与数据模型形成可验证契约
- 让后续任务拆解（tasks）与检查清单（checklist）有坚实依据

---

## 🎯 适用场景（When to Use This Skill）

当你需要做以下事情时，应使用本 Skill：

- 已有 Feature Spec（通常来自 "speckit-specify" skill / "speckit-clarify" Skill）
- 需要进入实施方案设计阶段，产出设计文档与契约
- 需要将不确定点收敛为“明确决策 + 依据 + 替代方案”
- 需要为后续的 "speckit-tasks" skill 任务拆解提供结构化输入
- 需要为 "speckit-checklist" skill 生成交付前检查项提供依据

---

## 📥 输入（Input）

- **必需上下文**：
  - Feature Spec（当前分支对应的规格说明文件）
  - 项目宪法（`.claude\constitution.md`）
  - Implementation Plan 模板（@specs\templates\plan-template.md）

- **用户补充输入（可选）**：`$ARGUMENTS`
  - 用于强调优先级、已有技术栈约束、目标环境、特殊合规要求等

前提条件：
- Spec 文件存在且可读取
- Plan 模板已初始化并可定位
- Feature 分支与目录结构有效

---

## 🧩 Skill 核心能力

### 1️⃣ 规划初始化与上下文装载（Setup & Context Loading）

- 定位并读取：
  - Feature Spec 路径
  - Implementation Plan 路径（IMPL_PLAN）
  - specs 根目录、分支信息等
- 载入宪法（constitution）作为“硬约束”来源
- 准备规划模板所需的章节结构与门禁规则

---

### 2️⃣ 按模板生成实施规划（Plan Authoring）

严格按照 IMPL_PLAN 模板结构填写，重点产出：

- **Technical Context（技术背景）**
  - 对需求的技术含义进行澄清与归纳
  - 未知项必须显式标注为 `NEEDS CLARIFICATION`

- **Constitution Check（宪法检查）**
  - 将宪法要求转为当前 Feature 的可执行约束项
  - 对潜在违反项给出理由、缓解策略或直接门禁失败

- **Gates（门禁评估）**
  - 若存在无法合理解释的宪法违反或关键未知未解决，应终止并报错
  - 门禁通过才进入后续阶段产物生成

---

### 3️⃣ 了解现有实现

必须先了解项目中的相关实现模式：
可以查看@README.md @CLAUDE.md @PROJECT_CONTEXT.md来快速了解项目框架

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

## 📦 分阶段产物（Phases & Artifacts）

### Phase 0：研究与决策收敛（Outline & Research）

目标：消除技术规划中的关键未知项，形成可追溯决策记录。

做法：
- 从 Technical Context 中提取：
  - 每一个 `NEEDS CLARIFICATION` → 研究任务
  - 每一个依赖项 → 最佳实践任务
  - 每一个集成点 → 典型模式任务

输出工件：`research.md`  
标准结构（必须包含）：
- Decision：选择了什么
- Rationale：为什么这样选
- Alternatives considered：评估过哪些替代方案

验收条件：
- 所有 `NEEDS CLARIFICATION` 必须在 research.md 中被解决
- 关键决策具备理由与可替代性说明

---

### Phase 1：设计与契约（Design & Contracts）

前置条件：`research.md` 完整且未知项已清零。

产出内容：

1) **数据模型文档：`data-model.md`**
- 从 Spec 抽取实体（Entities）
- 字段（Fields）、关系（Relationships）
- 关键校验规则与唯一性约束
- 生命周期 / 状态迁移（如适用）

2) **接口契约：`/contracts/*`**
- 从功能需求映射用户动作到接口能力
- 产出可验证的接口定义（如 OpenAPI / GraphQL Schema）
- 同时明确失败模式与输入输出约束（契约层）

3) **快速上手：`quickstart.md`**
- 说明如何在标准环境下跑通最小闭环
- 对外依赖、配置项、运行路径、验证方式清晰可复现

4) **Agent Context 更新（可选但推荐）**
- 根据当前计划新增的技术信息，更新 agent context 文件
- 保持人工编辑区不被覆盖，仅在标记区间内增量写入

验收条件：
- 数据模型与契约与 Spec 一致，不得引入不在 Spec 中的新增范围
- 契约可用于测试用例设计与联调对齐
- quickstart 能指导实现最小可行闭环

---

## 🔗 Skill 协作关系（Handoffs）

本 Skill 通常下游衔接：

- **Create Tasks → "speckit-tasks" skill**
  - 将计划拆成可执行任务与里程碑
- **Create Checklist → "speckit-checklist" skill**
  - 为交付与验收生成检查清单（质量、风险、合规等）

---

## 🧭 行为与约束原则（Skill Constitution）

- 必须遵循宪法（constitution）约束；门禁失败必须停止
- 必须使用绝对路径（当涉及引用/输出路径时）
- 不允许遗留未解决的 `NEEDS CLARIFICATION` 进入 Phase 1
- 产物必须可审计：决策、理由、替代方案清晰可追溯
- 规划阶段以“设计工件”为中心，不在此处完成任务拆解

---

## 📤 输出（Output）

Skill 完成后，输出应包含：

- Feature 分支信息
- IMPL_PLAN 文件路径
- 已生成工件列表与路径：
  - research.md
  - data-model.md
  - contracts/
  - quickstart.md
  - agent context 文件（如有）
- 门禁检查结论（通过 / 失败原因）
- 下一步推荐命令：
  - "speckit-tasks" skill（任务拆解）
  - "speckit-checklist" skill（交付检查清单）

---

## ✅ Skill 成功标志

当满足以下条件时，认为 Skill 成功：

- 宪法门禁通过
- `research.md` 解决所有关键未知项
- 已生成一致的数据模型与契约工件
- quickstart 可支持最小闭环验证
- 可安全进入任务拆解与交付检查阶段

---

*This skill is designed to turn a stable spec into auditable design artifacts and a plan that can be executed with minimal rework.*
