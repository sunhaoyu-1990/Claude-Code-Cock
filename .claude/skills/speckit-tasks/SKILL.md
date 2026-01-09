---
name: speckit-tasks
description: 基于已有的功能规格与设计工件，生成可直接执行、按依赖关系排序、以用户故事为中心的 tasks.md，实现从“设计方案”到“可实施任务列表”的系统化转化。
---

# Speckit_Tasks

## 🧠 Skill 简介

**Speckit_Tasks** 是一个**项目级任务生成（Task Decomposition）Skill**。  
它在功能规格说明与设计工件已经就绪的前提下，将抽象的设计成果转化为：

- **可执行的任务清单（tasks.md）**
- **严格格式化、可并行标注的 Checklist**
- **以用户故事为中心、可独立测试的交付单元**
- **显式的任务依赖关系与 MVP 实施路径**

该 Skill 的目标是：

> 让任务列表本身成为“可执行说明书”，而不是待解释的 TODO 列表。

---

## 🎯 适用场景（When to Use This Skill）

在以下情况下，应使用本 Skill：

- 已完成实施规划（通常来自 `speckit-plan` skill）
- 已具备 Spec、Plan、数据模型、接口契约等设计工件（可部分缺失）
- 需要生成一份 **LLM 或人类工程师可直接执行的任务清单**
- 希望明确：
  - 任务顺序
  - 并行机会
  - 用户故事级交付边界
  - MVP 最小实现范围
- 准备进入实现阶段（`speckit-implement` skill）

---

## 📥 输入（Input）

- **必需上下文**
  - Feature 目录（当前分支）
  - `spec.md`（用户故事与优先级）
  - `plan.md`（技术栈、结构与实现策略）

- **可选设计工件（自动识别）**
  - `data-model.md`
  - `contracts/`
  - `research.md`
  - `quickstart.md`

- **用户补充输入（可选）**：`$ARGUMENTS`
  - 用于指定特殊实施策略（如 TDD、阶段性交付、性能优先等）

前提条件：
- Feature 目录存在
- Spec 与 Plan 可被正确加载
- 所有路径可解析为绝对路径

---

## 📤 输出（Output）

Skill 执行完成后，将返回：

- 严格可执行的任务Checklist
- tasks.md文档
- 在进入实现（implement）之前，系统性发现spec.md、plan.md、tasks.md 三大核心工件存在**高风险不一致**与**覆盖缺口**，避免后续返工：
  - "speckit-analyze" Skill

---

## 🧩 Skill 核心能力

### 1️⃣ 设计工件感知与抽取（Artifact-Aware）

Skill 会自动识别并解析当前 Feature 中的设计工件：

- 从 **spec.md** 抽取：
  - 用户故事（US1, US2, …）
  - 优先级（P1, P2, P3…）
- 从 **plan.md** 抽取：
  - 技术栈
  - 项目结构
  - 关键实现约束
- 从可选文档中抽取：
  - 实体 → 任务
  - 接口 → 任务
  - 决策 → 初始化 / 配置任务
  - 验证场景 → 测试或验收任务

文档缺失不会阻断 Skill，但会影响任务粒度与覆盖面。

---

### 2️⃣ 以用户故事为核心的任务拆解（Story-Centric）

**用户故事是任务组织的第一原则**：

- 每个用户故事形成一个独立 Phase
- 每个 Phase 都是一个 **可独立实现、可独立测试的增量**
- 共享能力前移，故事专属能力后置

阶段结构固定为：

1. **Phase 1：Setup**
   - 项目初始化、目录结构、基础配置

2. **Phase 2：Foundational**
   - 所有用户故事的公共前置条件
   - 未完成前，不允许进入故事实现

3. **Phase 3+：User Stories**
   - 按 spec.md 中优先级排序
   - 每个用户故事一个 Phase（US1、US2、…）

4. **Final Phase：Polish & Cross-Cutting**
   - 性能、日志、异常处理、文档补全等

---

### 3️⃣ 严格可执行的任务格式（Checklist Contract）

所有任务 **必须** 使用统一 Checklist 格式：

```text
- [ ] [TaskID] [P?] [Story?] 清晰动作描述 + 精确文件路径
