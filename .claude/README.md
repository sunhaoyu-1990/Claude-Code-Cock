# 本地 Claude Code 的驾驶舱搭建框架

本项目是一个专门为各项目生成 Claude Code 驾驶舱的搭建框架。它提供了完整的模板体系、规范文件和技能链条，帮助团队建立统一的 AI 辅助开发规范。

---

## 目录结构

```
.claude/
├─ BASE_CLAUDE.md                  # 组织级基础规范（不可修改）
├─ constitution.md                 # 核心宪法（最高优先级）
├─ COMMANDS.md                     # 常用命令速查
│
├─ PROFILES/                       # Layer 2: 语言/框架工程直觉
│  ├─ common.md                    # 通用工程规范
│  ├─ python.md                    # Python 项目规范
│  ├─ cpp.md                       # C++ 项目规范
│  ├─ frontend.md                  # 前端项目规范
│  ├─ testing-common.md            # 通用测试规范
│  ├─ testing-python.md            # Python 测试规范
│  └─ testing-cpp.md               # C++ 测试规范
│
├─ EXTENSIONS/                     # Layer 3: 可选重型约束
│  ├─ architecture-heavy.md        # 架构强约束项目
│  ├─ ai-workflow-advanced.md      # 重型 AI 协作流
│  ├─ safety-critical.md           # 高风险系统
│  └─ data-pipeline.md             # 数据工程专用
│
├─ GUIDES/                         # 开发指南
│  ├─ DEV_GUIDE_SIMPLE.md          # 简单开发模式指南
│  ├─ DEVELOPMENT_GUIDE_COMPLEX.md # 复杂开发模式指南
│  └─ TEST_GUIDE.md                # 测试规范指南
│
├─ SKILLS/                         # Speckit 技能链条
│  ├─ speckit-specify/             # 需求规格化
│  ├─ speckit-clarify/             # 需求澄清
│  ├─ speckit-plan/                # 技术规划
│  ├─ speckit-checklist/           # 完整性检查
│  ├─ speckit-tasks/               # 任务拆解
│  ├─ speckit-analyze/             # 一致性分析
│  └─ speckit-implement/           # 实施执行
│
├─ COMMANDS/                       # 自定义命令定义
│  ├─ speckit.specify.md
│  ├─ speckit.clarify.md
│  ├─ speckit.plan.md
│  ├─ speckit.checklist.md
│  ├─ speckit.tasks.md
│  ├─ speckit.analyze.md
│  ├─ speckit.implement.md
│  ├─ speckit.constitution.md
│  └─ merge-current-branch.md
│
├─ AGENTS/                         # 专用代理
│  ├─ python-code-security-reviewer.md
│  ├─ python-test-reviewer.md
│  └─ performance-optimizer.md
│
├─ SCRIPTS/                        # PowerShell 辅助脚本
│  └─ powershell/
│     ├─ create-new-feature.ps1
│     ├─ setup-plan.ps1
│     └─ check-prerequisites.ps1
│
├─ SETTINGS/                       # Claude Code 配置
│  ├─ settings.json                # 权限与沙箱配置
│  └─ settings.local.json          # 本地覆盖配置
│
└─ templates/                      # 文档模板
   └─ CLAUDE-tem.md                # 项目级 CLAUDE.md 模板（包含规范与上下文）
```

---

## 核心概念

### 1. 分层规范体系

框架采用四层规范体系，优先级从高到低：

| 层级 | 文件 | 作用 | 可修改性 |
|------|------|------|----------|
| Layer 0 | `constitution.md` | 核心宪法，最高优先级 | 不可削弱 |
| Layer 1 | `BASE_CLAUDE.md` | 组织级基础规范 | 不可修改 |
| Layer 2 | `PROFILES/*.md` | 语言/框架工程直觉 | 可扩展 |
| Layer 3 | `EXTENSIONS/*.md` | 可选重型约束 | 按需启用 |
| Layer 4 | `CLAUDE.md` | 项目级规范 | 项目定制 |

### 2. 决策优先级

当多个信息源存在冲突时，Claude 必须严格按照以下顺序裁决：

1. `constitution.md`
2. `BASE_CLAUDE.md`
3. 项目级 `CLAUDE.md`（包含规范与上下文）
4. Language Profile
5. specs / design / ADR 等需求文档
6. README / 说明文档
7. 现有代码实现（允许被修正）

---

## 两种开发模式

### Simple Development Mode（简单开发模式）

**适用场景：**
- 小功能开发（< 5 个新文件）
- Bug 修复
- 快速迭代
- 不涉及公共契约变更

**工作流程：**
1. Light Plan（5-10 行轻量计划）
2. 选择是否启用 TDD
3. 开发与验证
4. 质量门禁检查
5. 错误总结（如有问题）

**参考指南：** `@.claude/GUIDES/DEV_GUIDE_SIMPLE.md`

### Complex Development Mode（复杂开发模式）

**适用场景（满足任一即启用）：**
- 影响 **公共 API / CLI / 配置 Schema / 数据协议**
- 跨模块、跨层修改（≥ 2 个核心模块）
- 引入新依赖或结构性重构
- 新增文件 ≥ 5 个
- 存在明确性能/稳定性/安全风险

**Skill Chain（强制执行顺序）：**

```
speckit-specify  →  需求规格化
       ↓
speckit-clarify →  澄清不确定性
       ↓
speckit-plan     →  技术实现计划
       ↓
speckit-checklist → 完整性检查
       ↓
speckit-tasks    →  任务拆解
       ↓
speckit-analyze  →  实现前分析
       ↓
speckit-implement → 实施与验证
```

**参考指南：** `@.claude/GUIDES/DEVELOPMENT_GUIDE_COMPLEX.md`

---

## Speckit 技能链条详解

### speckit-specify（需求规格化）

**目标：** 将模糊需求转化为明确、可验证的规格

**产出：** `specs/<feature_name>/spec.md`
- 功能目标
- 非目标（明确不做什么）
- 使用场景
- 成功判定标准

### speckit-clarify（需求澄清）

**目标：** 消除所有影响实现决策的不确定点

**产出：** `specs/<feature_name>/clarify.md`
- 澄清问题清单（最多 5 个高价值问题）
- 用户确认的答案
- 被否决的方案

### speckit-plan（技术规划）

**目标：** 形成可执行、可评估的实现方案

**产出：**
- `research.md` - 技术决策记录
- `data-model.md` - 数据模型文档
- `contracts/` - 接口契约
- `quickstart.md` - 快速上手文档

### speckit-checklist（完整性检查）

**目标：** 确保方案在实现前已被系统性检查

**产出：** `specs/<feature_name>/checklists/`
- 兼容性检查清单
- 测试策略检查清单
- 性能影响检查清单
- 可维护性检查清单

### speckit-tasks（任务拆解）

**目标：** 将计划拆解为可跟踪、可验证的最小任务单元

**产出：** `specs/<feature_name>/tasks.md`
- 按 Phase 组织的任务清单
- 任务依赖关系
- 并行执行标记
- 用户故事映射

### speckit-analyze（一致性分析）

**目标：** 在编码前发现跨工件不一致问题

**产出：** `specs/<feature_name>/cross_artifact_analysis.md`
- spec.md / plan.md / tasks.md 一致性检查
- 覆盖缺口识别
- 冲突与歧义分析
- 修复建议

### speckit-implement（实施执行）

**目标：** 按既定方案完成实现，并通过测试与验证

**能力：**
- 执行前门禁检查
- 阶段化任务执行
- 进度跟踪与状态回写
- 完成验证

---

## 语言 Profile（工程直觉）

### common.md（通用工程规范）

**核心原则：**
- MCU（最小可合并单元）原则
- 确定性等级标注（已验证/推断/假设）
- 接口契约要求
- 测试分类要求

### python.md（Python 项目规范）

**代码风格：**
- PEP 8
- snake_case / PascalCase / UPPER_SNAKE_CASE
- Google 风格 docstring
- typing 类型提示

**测试策略：**
- pytest 首选
- test_*.py + TestClass/test_function 命名
- 回归测试优先

**工具链：**
- black（格式化）
- flake8/ruff（静态检查）
- mypy（类型检查）

### cpp.md（C++ 项目规范）

**代码风格：**
- 优先现代 C++（C++17/20/23）
- RAII 优先
- const 正确性
- 头文件最小化依赖

**测试策略：**
- gtest/catch2
- 边界条件优先

---

## 核心宪法原则

### 不可违反条款

1. **单一职责原则** - 一个模块只负责一类明确职责
2. **清晰边界原则** - 模块之间通过明确接口交互
3. **接口优先原则** - 实现前明确输入/输出/错误语义
4. **可测试性优先** - 设计阶段即考虑测试
5. **自动化优先** - 能自动化的流程不得依赖人工
6. **可演进性优先** - 禁止为方便牺牲结构清晰度
7. **显式优于隐式** - 行为、依赖、假设必须清晰表达

### 确定性等级标注

- ✅ **【已验证】** - 已验证、可复现、无歧义
- ⚠️ **【推断】** - 基于充分经验或共识
- ❓ **【假设】** - 需要验证、试验或进一步澄清

### 最小可合并单元（MCU）

每次变更必须：
- 逻辑自洽
- 职责单一
- 可测试
- 可回滚

---

## 专用代理（Agents）

### python-code-security-reviewer

**用途：** 识别、分类和修复 Python 代码中的安全风险

**检查领域：**
- 输入验证与信任边界
- 文件系统与路径安全
- 命令执行与注入
- 反序列化与代码执行
- 网络、SSRF 与外部调用
- 密钥与敏感数据处理
- 依赖与供应链安全
- DoS 与资源安全
- 并发与竞态条件

### python-test-reviewer

**用途：** 审查测试覆盖率与测试质量

### performance-optimizer

**用途：** 性能优化分析与建议

---

## 命令速查

### 基本命令

```bash
# 安装依赖
uv pip install -e ".[dev]"

# 运行测试
uv run pytest
uv run pytest -v
uv run pytest -k "keyword"

# 代码质量
black .
black --check .
flake8
mypy src/

# Git 操作
git status
git diff
git log --oneline -n 20
```

### 项目特定命令

需要在 `COMMANDS.md` 中补充：
- 项目包名（用于 coverage）
- 基础分支名
- CLI 名称
- 常用配置目录

---

## 配置说明

### settings.json

Claude Code 的权限与沙箱配置：

```json
{
  "permissions": {
    "allow": [...],  // 允许的操作
    "deny": [...],   // 禁止的操作
    "ask": [...]     // 需要询问的操作
  },
  "sandbox": {
    "autoAllowBashIfSandboxed": true,
    "enabled": true
  }
}
```

---

## 快速开始

### 1. 为新项目创建驾驶舱

```bash
# 复制模板
cp .claude/templates/CLAUDE-tem.md <your-project>/CLAUDE.md
```

### 2. 填写项目信息

在 `CLAUDE.md` 中替换占位符：
- `{项目名称}`
- `{主要语言}`
- `{语言版本}`
- `{主要框架}`
- 等等...

### 3. 选择适用的 Profile

在 `CLAUDE.md` 中导入：
- `@.claude/PROFILES/common.md`（必选）
- `@.claude/PROFILES/python.md` 或 `cpp.md` 或 `frontend.md`
- `@.claude/PROFILES/testing-*.md`
- `@.claude/EXTENSIONS/architecture-heavy.md`（如需要）

### 4. 使用 Speckit 技能链

对于复杂功能：
```bash
# 使用 Claude Code 命令
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.checklist
/speckit.tasks
/speckit.analyze
/speckit.implement
```

---

## 维护指南

### 什么时候更新规范？

**constitution.md：**
- 仅当组织级工程原则发生变化
- 必须明确版本号和变更原因

**BASE_CLAUDE.md：**
- 组织级流程变更
- 新增通用约束

**PROFILES：**
- 新语言/框架支持
- 工具链迁移

**CLAUDE.md（项目级）：**
- 依赖变更
- 架构调整
- 新增项目特定约定

---

## 常见问题

### Q: 如何选择 Simple vs Complex Mode？

**A:** 使用决策树：
1. 用户是否明确指定？→ 按指定执行
2. 是否影响公共契约？→ Complex
3. 是否跨模块/跨层？→ 建议 Complex
4. 是否结构性重构？→ Complex
5. 是否有高风险？→ Complex
6. 工作量是否超标？→ 建议 Complex
7. 否则 → Simple

### Q: 可以跳过 Skill Chain 吗？

**A:** 可以，但必须：
- 用户**明确声明**跳过
- Claude 说明跳过的风险
- 记录偏离决定

### Q: 如何自定义命令？

**A:** 编辑 `COMMANDS.md`：
- 按类别组织（安装/测试/质量/部署）
- 每条命令包含：用途/预期输出/成功判定
- 注意 Windows/Linux 差异

---

## 版本信息

- **框架版本：** v1.0
- **最后更新：** 2026-01-09
- **维护者：** shy

---

## 参考资料

- Claude Code 官方文档：https://docs.anthropic.com/claude-code
- Speckit 方法论：本项目 `.claude/SKILLS/` 目录
- 测试规范：`.claude/GUIDES/TEST_GUIDE.md`
- 复杂开发流程：`.claude/GUIDES/DEVELOPMENT_GUIDE_COMPLEX.md`
