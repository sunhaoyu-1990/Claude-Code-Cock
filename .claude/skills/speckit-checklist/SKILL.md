---
name: speckit-checklist
description: 基于用户需求与当前功能上下文（spec/plan/tasks 等），生成“需求写作质量单元测试”式的自定义检查清单，聚焦规格说明的完整性、清晰度、一致性与可验证性，而非实现/测试行为。
---

# Speckit_Checklist

## 🧠 Skill 简介

**Speckit_Checklist** 是一个“**需求质量检查清单生成**”的项目级 Skill。  
它的核心理念是：

> **Checklist 是“英文需求的单元测试（Unit Tests for Requirements Writing）”。**  
> 用于验证规格说明（requirements/spec）是否写得足够好、足够清楚、足够完整、足够一致、足够可验收。  
> **不是**用于验证按钮能否点击、接口是否返回 200、实现是否正确。

---

## 🎯 适用场景（When to Use This Skill）

在以下场景中，应使用本 Skill：

- 你需要为某个 Feature 建立“需求写作质量门禁（质量关卡）”
- 规格说明已初步完成，但你希望系统化发现：
  - 缺失的需求点
  - 模糊/不可度量的表述
  - 章节之间的矛盾与术语不一致
  - 缺少异常/恢复/非功能等场景覆盖
- 需要为评审者（PR Review）、产品/研发协作、发布前评估提供统一检查依据
- 希望生成多份领域清单（如 `ux.md` / `api.md` / `security.md`），分别覆盖不同质量维度

---

## 📥 输入（Input）

- **用户输入（可选）**：`$ARGUMENTS`
  - 描述你希望清单聚焦的领域、使用人群、严格程度、风险侧重点等  
  - 例如：“面向发布门禁，重点安全与回滚”“给 PR reviewer 用，偏轻量”等

- **Feature 上下文（自动加载）**
  - `spec.md`：需求、范围、验收/成功标准
  - `plan.md`（若存在）：技术背景与依赖（用于识别需求缺口，不写实现检查）
  - `tasks.md`（若存在）：用于反向发现需求未覆盖的场景类别（仍然只写需求质量项）

前提条件：
- Feature 目录与 spec.md 至少存在
- 所有文件路径解析为绝对路径

---

## 🧩 Skill 核心能力

### 1️⃣ 意图与焦点校准（最多 3 个动态澄清问题）

Skill 会从 `$ARGUMENTS` + 当前文档信号中动态生成最多 3 个澄清问题（Q1–Q3），用于确定：

- 清单**范围**（scope）：只看 spec 还是要覆盖 plan/tasks 的“需求质量影子”
- 清单**深度**（depth）：轻量预检查 vs 发布门禁
- 清单**受众**（audience）：作者自检 vs 同行评审/QA/发布评审
- 清单**风险重点**（risk emphasis）：安全/性能/可用性/可访问性/合规 等
- 清单**边界排除**（exclusions）：明确不在本轮关注的维度

规则：
- 不要求用户重复已提供信息
- 问题必须对清单内容产生实质影响
- 如仍存在关键场景类别不明确，可追加最多 2 个追问（Q4–Q5），但总问题数 ≤ 5

默认策略（无法交互时）：
- 深度：Standard
- 受众：若偏代码/工程 → Reviewer（PR），否则 Author
- 焦点：最高相关的前 2 个聚类方向

---

### 2️⃣ 上下文读取与“最小必要”提取

Skill 会从 spec/plan/tasks 中读取**与焦点相关的部分**，并采用“渐进式披露”策略：

- 不做全文转储
- 长段落先摘要为要点，再判断是否需要继续深挖
- 仅提取用于构建“需求质量检查项”的信息
- 严禁臆造未出现的需求内容（不 hallucinate）

---

### 3️⃣ 生成“需求写作单元测试”式检查项

所有检查项必须符合以下原则：

- **测试对象**：需求文本本身（written requirements）
- **测试维度**：完整性/清晰度/一致性/可度量性/覆盖面/可追溯性
- **禁止**：任何实现验证、测试用例、QA 操作步骤、代码行为检查

#### 明确禁止（会把清单变成实现测试）

- 以 “Verify / Test / Confirm / Check（验证/测试/确认/检查）+ 行为” 开头
- 任何“点击/跳转/渲染/加载/执行”等实现行为描述
- 引用框架、算法、API 调用细节来当作检查项本体
- 输出测试计划或测试步骤

#### 允许且推荐（需求质量提问模式）

- “是否已定义/指定/说明……？”
- “是否对模糊词进行了量化……？”
- “是否在 A 节与 B 节之间保持一致……？”
- “是否可被客观验证……？”
- “是否覆盖主流程/备选/异常/恢复/非功能场景……？”

---

## 🧱 清单结构（Categories）

生成的 checklist 按“需求质量维度”分组（可按焦点裁剪）：

- Requirement Completeness（完整性）
- Requirement Clarity（清晰度）
- Requirement Consistency（一致性）
- Acceptance Criteria Quality（验收标准质量）
- Scenario Coverage（场景覆盖）
- Edge Case Coverage（边界情况覆盖）
- Non-Functional Requirements（非功能：性能/安全/可用性/可访问性/合规等）
- Dependencies & Assumptions（依赖与假设）
- Ambiguities & Conflicts（歧义与冲突）

---

## 🧾 输出工件（Output）

### 1) Checklist 文件

- 输出目录：`FEATURE_DIR/checklists/`
- 文件名规则：
  - 使用短领域名：`ux.md` / `api.md` / `security.md` / `performance.md` 等
  - 若同名文件已存在：采取追加策略
- 每次运行必须生成“新的文件或在既有文件中追加”，**不得覆盖历史清单**
- 条目编号：`CHK001` 起连续递增（单文件内递增）

### 2) 条目格式（Checklist Item Contract）

每条检查项必须符合：

```text
- [ ] CHK### <以问题形式表述的需求质量检查项> [维度标签, 可追溯引用]
