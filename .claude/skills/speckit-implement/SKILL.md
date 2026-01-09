---
name: speckit-implement
description: 基于 tasks.md 执行项目级实施流程，在遵循计划、检查清单与依赖约束的前提下，按阶段推进实现、跟踪进度并完成最终交付。
---

# Speckit_Implement

## 🧠 Skill 简介

**Speckit_Implement** 是一个“**从任务清单到实际实现**”的项目级执行 Skill。  
它以 `tasks.md` 作为**唯一执行蓝图**，在满足质量门禁（checklists）与技术计划（plan.md）的前提下，**有序、可控、可追踪地推进实现工作**，并将执行结果实时反映回任务状态。

该 Skill 的核心目标是：

- 确保实现严格遵循既定计划与需求规格
- 防止“跳任务”“越阶段”“无依赖约束的并行执行”
- 在执行阶段引入清晰的质量门禁与中断机制
- 让 tasks.md 成为**真实的执行账本（execution ledger）**

---

## 🎯 适用场景（When to Use This Skill）

在以下条件满足时，应使用本 Skill：

- 已成功生成 `tasks.md`（来自 `speckit-tasks`）
- 设计与一致性分析已完成，可能已成功生成`cross_artifact_analysis.md`（通常已运行 `speckit-analyze`）
- 需要正式进入实现阶段，而非继续设计或拆解
- 希望在执行前：
  - 明确哪些质量检查项已完成
  - 对“是否允许带缺口推进”做出显式决策
- 需要在实现过程中：
  - 严格按阶段推进
  - 自动更新任务完成状态
  - 对失败进行中断与诊断

---

## 📥 输入（Input）

- **必需工件**
  - `tasks.md`（完整、结构正确的任务清单）
  - `plan.md`（技术栈、架构、目录结构）
- **可选工件**
  - `spec.md`（用于最终对齐验证）
  - `data-model.md`
  - `contracts/`
  - `research.md`
  - `quickstart.md`
- **质量门禁**
  - `checklists/` 目录（若存在，将作为执行前门禁）
- **用户补充输入（可选）**：`$ARGUMENTS`
  - 例如是否允许在部分 checklist 未完成的情况下继续推进

前提条件：
- Feature 目录存在
- `tasks.md` 已生成且可解析
- 所有路径必须可解析为绝对路径

---

## 🧭 执行前门禁（Pre-Execution Gates）

### 1️⃣ Checklist 状态检查（若存在）

若 `FEATURE_DIR/checklists/` 存在，Skill 会：

- 扫描所有 checklist 文件
- 统计每个清单：
  - 总条目数
  - 已完成项（`[X] / [x]`）
  - 未完成项（`[ ]`）
- 生成状态汇总表：

| Checklist | Total | Completed | Incomplete | Status |
|----------|-------|-----------|------------|--------|
| ux.md | 12 | 12 | 0 | ✓ PASS |
| security.md | 6 | 6 | 0 | ✓ PASS |
| test.md | 8 | 5 | 3 | ✗ FAIL |

#### 决策规则

- **全部 PASS** → 自动进入实现阶段
- **存在 FAIL** → 必须暂停并询问用户是否继续
  - 用户明确同意（yes / proceed）才能继续
  - 否则立即中止执行

> 该机制确保“带风险推进”是**显式决策**，而非默认行为。

---

## 🧩 Skill 核心能力

### 2️⃣ 实施上下文加载（Implementation Context）

在通过门禁后，Skill 会加载并整合实施所需上下文：

- `tasks.md`：任务阶段、依赖、并行标记、文件路径
- `plan.md`：技术栈、架构约束、目录结构
- 可选工件（若存在）：
  - 数据模型、接口契约、研究结论、快速上手场景

这些信息共同构成**实施执行的约束空间**。

---

### 3️⃣ 项目基础设施校验（Project Hygiene）

Skill 会根据实际项目形态，自动检测并创建/校验必要的忽略文件（只在需要时）：

- `.gitignore`
- `.dockerignore`
- `.eslintignore` / ESLint ignores
- `.prettierignore`
- `.npmignore`
- `.terraformignore`
- `.helmignore`

校验原则：

- 若文件已存在：仅补充缺失的**关键模式**
- 若文件不存在：基于 plan.md 中的技术栈创建最小完整版本
- 永不删除用户已有规则

目的在于防止：
- 构建产物被误提交
- 密钥/配置文件泄漏
- 工具链产生噪声文件

---

### 4️⃣ 任务解析与执行计划构建

Skill 会解析 `tasks.md`，提取：

- 阶段结构（Setup / Tests / Core / Integration / Polish 等）
- 任务 ID、描述、文件路径
- 并行标记 `[P]`
- 隐含依赖关系（同文件 → 顺序执行）

并构建一个**可执行的任务流**：

- 阶段内按依赖顺序执行
- 标记为 `[P]` 且无文件冲突的任务可并行
- 跨阶段不得提前执行

---

### 5️⃣ 实施执行规则（Execution Semantics）

执行过程中严格遵循以下规则：

- **阶段优先**：当前阶段未完成，不进入下一阶段
- **依赖优先**：有依赖的任务必须顺序完成
- **测试优先（若适用）**：测试任务先于对应实现
- **文件互斥**：修改同一文件的任务不得并行
- **失败即停（非并行）**：顺序任务失败即中断
- **并行容错**：并行任务部分失败需汇总报告

---

### 6️⃣ 进度跟踪与状态回写

- 每完成一个任务，立即：
  - 输出进度反馈
  - 将 `tasks.md` 中对应条目标记为 `[X]`
- 任务失败时：
  - 输出明确的失败上下文
  - 给出可能的下一步建议
- Skill 不会“跳过失败”，除非用户明确介入

---

## 📤 完成验证（Completion Validation）

在所有任务执行结束后，Skill 会进行最终核验：

- 所有必需任务是否完成
- 实现是否覆盖 spec.md 中的功能与约束
- 测试是否通过，覆盖率是否满足要求（若定义）
- 实现是否符合 plan.md 的技术与架构约束

并输出最终总结：

- 完成任务数 / 总任务数
- 已完成阶段列表
- 遗留问题（若有）
- 是否可进入发布或下一阶段

---

## 🧭 行为与约束原则（Skill Constitution）

- `tasks.md` 是唯一执行真源（single source of truth）
- 不允许脱离任务清单的“即兴实现”
- 不允许跳过阶段或忽略依赖
- Checklist 未通过时，必须显式决策
- 已完成任务必须同步反映为 `[X]`
- 若 tasks.md 不完整，应建议先运行 `speckit-tasks`

---

## ✅ Skill 成功标志

当满足以下条件时，认为 Skill 成功：

- 所有必需任务均标记为完成
- 实现结果与 spec/plan 保持一致
- 质量门禁未被无意绕过
- 任务执行过程可回溯、可审计
- 项目可安全进入交付/发布阶段

---

*This skill turns a task list into a disciplined, auditable execution process rather than an ad-hoc coding session.*
