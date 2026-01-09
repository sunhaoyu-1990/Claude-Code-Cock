# Claude Code 驾驶舱框架优化方案

**版本**：v1.0
**日期**：2026-01-09
**维护者**：shy

---

## 执行摘要

本方案基于对整个框架的系统性检查，识别了 **6 大类共 28 项优化点**，按优先级分为 P0（紧急）、P1（重要）、P2（建议）三个等级。

---

## 问题分类汇总

| 类别 | P0 | P1 | P2 | 合计 |
|------|----|----|----|------|
| 文件完整性缺失 | 3 | 4 | 2 | 9 |
| 内容一致性问题 | 2 | 1 | 3 | 6 |
| 模板可用性问题 | 1 | 2 | 1 | 4 |
| 工作流完整性 | 2 | 2 | 0 | 4 |
| 文档质量问题 | 0 | 1 | 2 | 3 |
| 配置与集成 | 0 | 2 | 0 | 2 |
| **合计** | **8** | **12** | **8** | **28** |

---

## 一、文件完整性缺失（9 项）

### P0 - 严重缺失（3 项）

#### 1.1 缺失 frontend.md Profile

**问题描述**：
- README 中声明支持前端项目，但 `PROFILES/` 目录下缺少 `frontend.md`
- 导致前端项目无法获得针对性的工程直觉指导

**影响**：
- 前端项目（React/Vue/Angular 等）无法使用框架
- 强制使用通用 profile，丢失前端最佳实践

**建议内容**：
```markdown
# Profile: frontend

**层级**：Profile
**适用**：前端项目（React / Vue / Angular / Svelte 等）
**依赖**：建议同时导入 `common.md`
**禁止**：不定义项目工作流；不引入业务规则。

## 代码风格与结构
- 组件命名：PascalCase
- 工具函数：camelCase
- 常量：UPPER_SNAKE_CASE
- 样式：CSS Modules / styled-components / Tailwind（按项目）

## 类型提示
- TypeScript 优先
- Props 接口定义
- 严格的类型检查（noImplicitAny）

## 测试
- Jest / Vitest / Testing Library
- 组件测试 + 用户行为测试

## 构建
- Webpack / Vite / esbuild
- 环境变量管理
```

**优先级**：P0
**工作量**：2-3 小时

---

#### 1.2 缺失 EXTENSIONS 目录下的关键扩展

**问题描述**：
- README 中声明存在以下扩展，但实际缺失：
  - `ai-workflow-advanced.md` - 重型 AI 协作流
  - `safety-critical.md` - 高风险系统
  - `data-pipeline.md` - 数据工程专用

**影响**：
- 高风险项目（医疗/金融/安全关键）无法获得额外保障
- 数据密集型项目缺少专门指导

**建议创建**：

**ai-workflow-advanced.md** - 用于需要 AI 大模型协作的复杂项目
**safety-critical.md** - 用于安全关键系统
**data-pipeline.md** - 用于数据处理管道

**优先级**：P0
**工作量**：每个扩展 3-4 小时

---

#### 1.3 Skills 与 Commands 名称不一致

**问题描述**：
- 技能文件夹命名存在拼写错误：
  - `skills/sepckit-specify/` → 应为 `speckit-specify/`
  - `skills/sepckit-implement/` → 应为 `speckit-implement/`
- 导致命名混乱，不利于维护

**修复方案**：
1. 重命名文件夹
2. 更新所有引用路径

**优先级**：P0
**工作量**：30 分钟

---

### P1 - 重要缺失（4 项）

#### 1.4 缺失 spec-template.md

**问题描述**：
- `speckit.specify` 命令引用 `.specify/templates/spec-template.md`
- 但该模板不存在于框架中

**影响**：
- `/speckit.specify` 命令无法正常工作
- 用户无法创建新功能规格

**解决方案**：
创建 `.claude/templates/spec-template.md`：

```markdown
# Feature Specification: {Feature Name}

**Feature ID**: {ID}
**Status**: Draft | In Review | Approved
**Created**: {Date}
**Author**: {Author}

---

## Overview

{One-line description}

## Background & Motivation

{Why this feature is needed}

## Goals

{What this feature achieves}

## Non-Goals

{What this feature explicitly does NOT address}

## User Stories

| Story ID | As a | I want to | So that | Priority |
|----------|-----|----------|--------|----------|
| US1 | ... | ... | ... | P1 |

## Functional Requirements

{Detailed functional requirements}

## Success Criteria

{Measurable outcomes}

## Key Entities

{Core data entities (if applicable)}

## Assumptions & Dependencies

{What we assume to be true}

## Open Questions

{[NEEDS CLARIFICATION] items}

## Risks & Mitigations

{Potential risks and how to address them}
```

**优先级**：P1
**工作量**：1 小时

---

#### 1.5 缺失 plan-template.md

**问题描述**：
- `speckit-plan` skill 引用 `@specs\templates\plan-template.md`
- 但该模板不存在

**解决方案**：
创建 `.claude/templates/plan-template.md`

**优先级**：P1
**工作量**：2 小时

---

#### 1.6 缺失 checklist-template.md

**问题描述**：
- `speckit-checklist` skill 需要检查清单模板
- 但缺少标准模板

**解决方案**：
创建 `.claude/templates/checklist-template.md`

**优先级**：P1
**工作量**：1 小时

---

#### 1.7 缺失 CLAUDE.md 中的占位符说明文档

**问题描述**：
- `CLAUDE-tem.md` 模板中存在大量占位符
- 缺少"如何填写"的指导文档

**解决方案**：
创建 `.claude/docs/CLAUDE_FILL_GUIDE.md`，详细说明每个占位符的含义和填写方式

**优先级**：P1
**工作量**：2 小时

---

### P2 - 建议补充（2 项）

#### 1.8 缺失 testing-frontend.md

**问题描述**：
- 缺少前端项目专用测试 profile

**解决方案**：
创建 `profiles/testing-frontend.md`，包含：
- Testing Library 最佳实践
- 组件测试策略
- 可访问性测试

**优先级**：P2
**工作量**：2 小时

---

#### 1.9 缺失 testing-go.md

**问题描述**：
- 如支持 Go 语言，需要对应测试 profile

**解决方案**：
创建 `profiles/testing-go.md`（如需要）

**优先级**：P2
**工作量**：2 小时

---

## 二、内容一致性问题（6 项）

### P0 - 严重不一致（2 项）

#### 2.1 路径引用不一致

**问题描述**：
- `CLAUDE-tem.md` 中引用 `@.specify/memory/constitution.md`
- 实际文件位于 `.claude/constitution.md`

**影响**：
- Claude 无法正确加载宪法文件
- 导致规范层级混乱

**修复方案**：
```diff
- @.specify/memory/constitution.md
+ @.claude/constitution.md
```

**优先级**：P0
**工作量**：15 分钟

---

#### 2.2 开发指南文件名不一致

**问题描述**：
- README 中引用 `DEVELOPMENT_GUIDE.md`
- 实际文件名为 `DEV_GUIDE_SIMPLE.md`

**影响**：
- 用户找不到正确的指南文件

**修复方案**：
统一使用 `DEV_GUIDE_SIMPLE.md` 或创建别名

**优先级**：P0
**工作量**：15 分钟

---

### P1 - 重要不一致（1 项）

#### 2.3 模板与实际目录结构不一致

**问题描述**：
- 模板中引用的目录结构可能与实际项目不匹配
- 例如 `specs/error/patterns/` 目录在模板中被引用但未说明如何创建

**解决方案**：
1. 在 `.claude/docs/` 中创建标准目录结构说明
2. 更新模板，添加目录结构验证步骤

**优先级**：P1
**工作量**：2 小时

---

### P2 - 轻微不一致（3 项）

#### 2.4 命令速查与实际工具不一致

**问题描述**：
- `COMMANDS.md` 中假设使用 `uv`
- 但项目可能使用 `pip` 或其他包管理器

**解决方案**：
添加多种包管理器的命令变体

**优先级**：P2
**工作量**：1 小时

---

#### 2.5 Git 分支策略未定义

**问题描述**：
- 模板中要求填写"分支策略"
- 但缺少可选策略的说明和推荐

**解决方案**：
创建 `.claude/docs/GIT_STRATEGY_GUIDE.md`，提供常见分支策略选项

**优先级**：P2
**工作量**：2 小时

---

#### 2.6 测试覆盖率目标未明确定义

**问题描述**：
- 各 profile 中提到覆盖率目标但数值不统一

**解决方案**：
统一覆盖率目标定义：
- 总体：≥ 80%
- 核心模块：≥ 90%
- 新增代码：≥ 95%

**优先级**：P2
**工作量**：30 分钟

---

## 三、模板可用性问题（4 项）

### P0 - 严重问题（1 项）

#### 3.1 模板占位符过多且缺少验证

**问题描述**：
- `CLAUDE-tem.md` 和 `PROJECT_CLAUDE-tem.md` 包含 50+ 占位符
- 用户容易遗漏关键占位符
- 缺少完成性验证

**解决方案**：
1. 将占位符分为"必填"和"可选"两类
2. 创建 `.claude/scripts/validate_template.py` 脚本
3. 在模板顶部添加"必填项清单"

**优先级**：P0
**工作量**：3 小时

---

### P1 - 重要问题（2 项）

#### 3.2 缺少快速开始示例

**问题描述**：
- 用户不知道如何从零开始使用框架
- 缺少端到端示例

**解决方案**：
创建 `.claude/docs/QUICKSTART.md`，包含：
1. 新项目初始化步骤
2. 第一个功能的完整流程
3. 常见问题解决方法

**优先级**：P1
**工作量**：3 小时

---

#### 3.3 缺少项目示例

**问题描述**：
- 没有"好"的 CLAUDE.md 和 PROJECT_CONTEXT.md 示例
- 用户参考困难

**解决方案**：
创建 `.claude/examples/` 目录，包含：
1. Python 项目示例
2. C++ 项目示例
3. 前端项目示例

**优先级**：P1
**工作量**：4 小时

---

### P2 - 建议改进（1 项）

#### 3.4 模板缺乏交互式填写工具

**问题描述**：
- 手动填写模板容易出错
- 缺少交互式引导

**解决方案**：
创建 `.claude/scripts/setup_wizard.py`，交互式引导用户填写模板

**优先级**：P2
**工作量**：4 小时

---

## 四、工作流完整性（4 项）

### P0 - 严重缺失（2 项）

#### 4.1 错误总结流程缺少模板

**问题描述**：
- `BASE_CLAUDE.md` 要求执行错误总结
- 但缺少错误总结模板和存放位置说明

**解决方案**：
1. 创建 `.claude/templates/error_summary_template.md`
2. 定义 `specs/error/cases/` 和 `specs/error/patterns/` 目录结构
3. 在 `.claude/docs/ERROR_WORKFLOW.md` 中说明完整流程

**优先级**：P0
**工作量**：3 小时

---

#### 4.2 Skill Chain 缺少回退机制

**问题描述**：
- Complex Mode 的 7 个 skill 必须顺序执行
- 缺少"部分完成"或"回退"的处理机制

**解决方案**：
在每个 skill 中添加"恢复执行"逻辑：
1. 检查当前进度
2. 支持从中间步骤恢复
3. 记录每个阶段的完成状态

**优先级**：P0
**工作量**：6 小时

---

### P1 - 重要补充（2 项）

#### 4.3 缺少 feature 分支管理指南

**问题描述**：
- `/speckit.specify` 会创建分支
- 缺少分支命名、合并、清理的完整指南

**解决方案**：
创建 `.claude/docs/BRANCH_MANAGEMENT.md`：
- 分支命名规范
- 分支生命周期管理
- 合并策略

**优先级**：P1
**工作量**：2 小时

---

#### 4.4 缺少 PR 描述模板

**问题描述**：
- 完成功能后需要创建 PR
- 缺少标准 PR 描述模板

**解决方案**：
创建 `.claude/templates/pr_description_template.md`：

```markdown
## Summary
{Brief description}

## Related Feature
- Feature: #{ID}
- Spec: [Link]

## Changes
{List of changes}

## Testing
{How this was tested}

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Error summary created (if applicable)
```

**优先级**：P1
**工作量**：1 小时

---

## 五、文档质量问题（3 项）

### P1 - 重要改进（1 项）

#### 5.1 缺少故障排除指南

**问题描述**：
- 用户遇到问题无处查询
- 缺少常见问题解决方案

**解决方案**：
创建 `.claude/docs/TROUBLESHOOTING.md`，包含：
- Claude 无法加载规范文件
- Skill 执行失败
- Git 操作问题
- 模板填写问题

**优先级**：P1
**工作量**：2 小时

---

### P2 - 建议改进（2 项）

#### 5.2 文档缺少版本兼容性说明

**问题描述**：
- 未说明框架与 Claude Code 版本的兼容性

**解决方案**：
在 README 中添加"版本兼容性"章节

**优先级**：P2
**工作量**：30 分钟

---

#### 5.3 缺少变更日志

**问题描述**：
- 无法追踪框架的演进历史

**解决方案**：
创建 `.claude/CHANGELOG.md`，使用语义化版本

**优先级**：P2
**工作量**：1 小时

---

## 六、配置与集成（2 项）

### P1 - 重要改进（2 项）

#### 6.1 settings.json 权限配置需要扩展

**问题描述**：
- 当前 `settings.json` 配置较为保守
- 某些操作需要频繁确认

**解决方案**：
根据实际使用场景，优化权限配置：
- 添加常用的写权限
- 完善沙箱规则

**优先级**：P1
**工作量**：1 小时

---

#### 6.2 缺少 CI/CD 集成指南

**问题描述**：
- 如何将规范检查集成到 CI/CD 流程

**解决方案**：
创建 `.claude/docs/CI_INTEGRATION.md`，包含：
- GitHub Actions 示例
- GitLab CI 示例
- Jenkins 集成示例

**优先级**：P1
**工作量**：3 小时

---

## 优化实施计划

### 第一阶段（紧急修复，1-2 天）

**目标**：修复 P0 级别问题，确保框架基本可用

| 任务 | 工作量 | 负责人 |
|------|--------|--------|
| 修复文件夹命名错误 | 30 min | - |
| 修复路径引用不一致 | 15 min | - |
| 修复开发指南文件名 | 15 min | - |
| 创建 spec-template.md | 1 hour | - |
| 优化模板占位符验证 | 3 hours | - |
| 创建错误总结流程 | 3 hours | - |
| 添加 Skill Chain 恢复机制 | 6 hours | - |
| 创建 frontend.md | 2-3 hours | - |
| **合计** | **~16 hours** | |

---

### 第二阶段（重要补充，3-5 天）

**目标**：完善 P1 级别功能，提升可用性

| 任务 | 工作量 |
|------|--------|
| 创建 plan-template.md | 2 hours |
| 创建 checklist-template.md | 1 hour |
| 创建 CLAUDE 填写指南 | 2 hours |
| 创建快速开始文档 | 3 hours |
| 创建项目示例 | 4 hours |
| 创建扩展（ai-workflow/safety/data） | 10 hours |
| 创建错误总结模板 | 3 hours |
| 创建分支管理指南 | 2 hours |
| 创建 PR 描述模板 | 1 hour |
| 创建故障排除指南 | 2 hours |
| 创建 CI 集成指南 | 3 hours |
| 优化 settings.json | 1 hour |
| **合计** | **~34 hours** |

---

### 第三阶段（持续改进，按需进行）

**目标**：完成 P2 级别优化

| 任务 | 工作量 |
|------|--------|
| 创建 testing-frontend.md | 2 hours |
| 添加多包管理器支持 | 1 hour |
| 创建 Git 策略指南 | 2 hours |
| 统一覆盖率目标 | 30 min |
| 创建设置向导 | 4 hours |
| 添加版本兼容性说明 | 30 min |
| 创建变更日志 | 1 hour |
| **合计** | **~11 hours** |

---

## 总工作量估算

| 优先级 | 任务数 | 工作量 | 建议完成时间 |
|--------|--------|--------|--------------|
| P0 | 8 | ~16 hours | 1-2 天 |
| P1 | 12 | ~34 hours | 3-5 天 |
| P2 | 8 | ~11 hours | 按需进行 |
| **合计** | **28** | **~61 hours** | **~1-2 周** |

---

## 风险与建议

### 主要风险

1. **工作量可能低估**：某些任务可能比预期复杂
2. **优先级判断主观**：不同项目可能需要调整优先级
3. **向后兼容性**：修改模板可能影响已有项目

### 建议

1. **按阶段执行**：先完成 P0，验证后再进行 P1
2. **保持向后兼容**：新模板应考虑已有项目的迁移路径
3. **收集用户反馈**：实际使用后可能发现新的优化点
4. **版本管理**：框架本身也需要版本管理和变更日志

---

## 附录：文件清单

### 需要创建的文件（按优先级）

#### P0 文件
```
.claude/
├── PROFILES/frontend.md
├── templates/
│   ├── spec-template.md
│   └── error_summary_template.md
├── docs/
│   ├── ERROR_WORKFLOW.md
│   └── BRANCH_MANAGEMENT.md
└── EXTENSIONS/
    ├── ai-workflow-advanced.md
    ├── safety-critical.md
    └── data-pipeline.md
```

#### P1 文件
```
.claude/
├── templates/
│   ├── plan-template.md
│   ├── checklist-template.md
│   ├── pr_description_template.md
│   └── CLAUDE_FILL_GUIDE.md
├── docs/
│   ├── QUICKSTART.md
│   ├── TROUBLESHOOTING.md
│   └── CI_INTEGRATION.md
├── examples/
│   ├── python/
│   ├── cpp/
│   └── frontend/
└── scripts/
    └── validate_template.py
```

#### P2 文件
```
.claude/
├── PROFILES/testing-frontend.md
├── docs/
│   ├── GIT_STRATEGY_GUIDE.md
│   └── VERSION_COMPATIBILITY.md
├── CHANGELOG.md
└── scripts/
    └── setup_wizard.py
```

### 需要修改的文件

1. `.claude/templates/CLAUDE-tem.md` - 修复路径引用
2. `.claude/README.md` - 统一文件名引用
3. `.claude/COMMANDS.md` - 添加多包管理器支持
4. `.claude/settings.json` - 优化权限配置
5. `.claude/profiles/*.md` - 统一覆盖率目标

---

**方案结束**

*本方案应随框架演进持续更新*
