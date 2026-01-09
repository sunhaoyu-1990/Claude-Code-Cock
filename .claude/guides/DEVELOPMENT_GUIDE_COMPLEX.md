# 复杂开发规范（Complex Development Mode）

本文件定义 **复杂开发模式（Complex Development Mode）** 下的  
**强制协作流程、技能链条（Skill Chain）与文档产出规范**。

本规范用于：
- 中大型功能开发
- 架构调整
- 公共接口 / 配置 / 协议变更
- 高风险、高影响范围的工程任务

---

## 一、复杂开发模式的强制适用条件

当满足以下任一条件时，**必须启用 Complex Development Mode**：

- 新功能影响 **公共 API / CLI / 配置 Schema / 数据协议**
- 涉及跨模块、跨层（Domain / Application / Infra）修改
- 引入新依赖或进行结构性重构
- 需要新增较多文件（建议阈值 ≥ 5）
- 存在明确的性能 / 稳定性 / 安全风险
- 用户明确指定“复杂开发 / 完整设计 / 可扩展方案”

---

## 二、AI 协作指令（强制执行）

### 1️⃣ 新功能请求的处理规则

**当被要求添加新功能时，Claude 必须首先询问用户：**

> 是否启用：
> - **简单开发模式（simple code）**
> - **复杂开发模式（complex code）**

#### 用户选择说明

- **simple code**  
  → 按照 Simple Development Mode 工作  
  → 参考：`@.claude/DEVELOPMENT_GUIDE.md`

- **complex code**  
  → **必须**启用完整 Skill Chain  
  → 严格遵循本文件

---

### 2️⃣ 测试开发指令（模式无关）

当被要求 **编写或补充测试** 时，Claude 必须：

- 遵循统一测试规范  
- 参考：`@.claude/TEST_GUIDE.md`

测试是复杂开发的**强制组成部分**，不可省略。

---

### 3️⃣ 错误总结指令（开发闭环）

**每一次 Complex Mode 开发结束时，Claude 必须执行错误总结流程**：
- 错误回顾
- Pattern 抽象（如适用）
- 即使开发过程“看起来很顺利”
- 也必须进行一次错误回顾（哪怕结论是“无新错误模式”）

错误总结规范参考：
@specs/README.md

---

## 三、复杂开发的 Skill Chain（不可跳过）

### 🔗 完整技能链条（强制顺序）
speckit-specify
→ speckit-clarify
→ speckit-plan
→ speckit-checklist
→ speckit-tasks
→ speckit-analyze
→ speckit-implement

### ⚠️ 不可违反条款

- ❌ 不允许跳过任意一个 Skill
- ❌ 不允许合并 Skill 阶段
- ❌ 不允许在未完成上一步时进入下一步
- ✅ **仅当用户明确声明“跳过某步骤”时，才允许例外**

---

## 四、各 Skill 阶段的职责与产出（核心）

### 1️⃣ speckit-specify —— 需求规格化

**目标**：将模糊需求转化为明确、可验证的规格

**必须输出**：
- 功能目标
- 非目标（明确不做什么）
- 使用场景
- 成功判定标准

**文档位置**：
specs/<feature_name>/spec.md

---

### 2️⃣ speckit-clarify —— 澄清不确定性

**目标**：消除所有影响实现决策的不确定点

**必须输出**：
- 澄清问题清单
- 用户确认的答案
- 被否决的方案（如有）

**文档位置**：
specs/<feature_name>/clarify.md

---

### 3️⃣ speckit-plan —— 技术实现计划

**目标**：形成可执行、可评估的实现方案

**必须包含**：
- 架构方案
- 涉及模块 / 文件
- 技术选型理由
- 风险点与权衡

**文档位置**：
specs/<feature_name>/plan.md

---

### 4️⃣ speckit-checklist —— 完整性检查

**目标**：确保方案在实现前已被系统性检查

**必须覆盖**：
- 兼容性
- 测试策略
- 性能影响
- 可维护性

**文档位置**：
specs/<feature_name>/checklist.md

---

### 5️⃣ speckit-tasks —— 任务拆解

**目标**：将计划拆解为可跟踪、可验证的最小任务单元

**要求**：
- 任务具备明确输入 / 输出
- 任务之间依赖关系清晰
- 支持并行与回滚

**文档位置**：
specs/<feature_name>/tasks.md

---

### 6️⃣ speckit-analyze —— 实现前分析

**目标**：在编码前发现潜在问题，避免返工

**关注点**：
- 性能瓶颈
- 错误模式（参考错误知识库）
- 边界条件
- 测试可行性

**文档位置**：
specs/<feature_name>/analyze.md

---

### 7️⃣ speckit-implement —— 实现与验证

**目标**：按既定方案完成实现，并通过测试与验证

**强制要求**：
- 实现必须严格对齐 plan / tasks
- 测试必须覆盖核心路径
- 不允许“边写边改规格”

---

## 五、文档与目录规范（Complex Mode 专属）

### 统一文档根目录
specs/
└── <feature_name>/
├── spec.md
├── clarify.md
├── plan.md
├── checklist.md
├── tasks.md
├── analyze.md
└── notes.md # 可选

---

## 六、与其他规范的关系

| 模块 | 关系 |
|----|----|
| BASE_CLAUDE.md | 定义是否进入 Complex Mode |
| Simple Mode | 不适用于本流程 |
| Testing Guide | 提供测试实现规范 |
| Error KB | 提供错误模式与总结闭环 |
| Architecture-heavy | 作为 plan / analyze 的参考 |

---

## 七、复杂开发的最终闭环（必须完成）

Complex Development Mode **只有在以下全部完成后才算结束**：

- [ ] 所有 Skill 阶段完成或被用户明确跳过
- [ ] 所有任务完成并验证
- [ ] 测试通过
- [ ] 错误总结已记录（Case / Pattern）
- [ ] 文档齐全并存入 `specs/`

---

## 八、关键原则总结（必须牢记）

> **复杂开发的目标不是“写代码”，而是“降低未来变化的成本”。**  
> **Skill Chain 的存在，是为了防止一次性思维和隐性决策。**

---

**适用模式**：Complex Development Mode  
**规范级别**：强制  
**维护者**：shy  
**最后更新**：2026-01-08
