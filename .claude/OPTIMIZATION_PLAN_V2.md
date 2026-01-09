# Claude Code 驾驶舱框架优化方案（用户定制版）

**版本**：v2.0（基于用户反馈调整）
**日期**：2026-01-09
**维护者**：shy
**目标**：1 周内完成关键优化，聚焦规范严谨性

---

## 用户画像与约束

### 使用场景
- **团队类型**：小团队协作（2-10 人）
- **技术栈**：Python + C++ + 前端（TS/JS）多语言
- **项目状态**：全新开始（无需向后兼容）
- **时间预算**：1 周（约 30 小时）

### 关键需求
1. **规范严谨性**：确保 Claude 不能绕过规范
2. **多包管理器支持**：uv/pip + npm/pnpm/yarn + apt/brew/choco
3. **完整文档**：快速参考 + 详细教程都要
4. **Skill 恢复**：必须支持断点恢复
5. **错误处理**：必须完善错误总结流程

### 规范执行机制（用户要求）
- ✅ 任务启动检查
- ✅ 关键操作门禁
- ✅ 过程回顾
- ✅ 完成验证
- ⚠️ 违规处理：警告后继续（非强制中止）

---

## 优化后的优先级排序

基于用户反馈，重新排序优先级：

### P0 - 紧急核心（1 周内必须完成，约 20 小时）

| ID | 任务 | 工作量 | 依赖 |
|----|------|--------|------|
| P0-1 | 修复文件夹命名错误（sepckit → speckit） | 30 min | - |
| P0-2 | 修复路径引用不一致 | 15 min | - |
| P0-3 | 创建核心模板（spec/plan/checklist） | 4 hours | - |
| P0-4 | **增强规范执行机制**（4 道门禁） | 4 hours| P0-2 |
| P0-5 | 创建前端 Profile（frontend.md） | 2 hours | - |
| P0-6 | 创建错误总结模板和流程 | 3 hours | - |
| P0-7 | 创建模板验证脚本 | 2 hours | P0-3 |
| P0-8 | 创建快速开始文档 | 2 hours | P0-3 |
| P0-9 | 创建项目示例（Python + C++ + 前端） | 3 hours | P0-8 |
| **合计** | | **~20.5 hours** | |

### P1 - 重要补充（后续完成，约 10 小时）

| ID | 任务 | 工作量 | 备注 |
|----|------|--------|------|
| P1-1 | Skill Chain 恢复机制 | 6 hours | 用户要求必须实现 |
| P1-2 | 更新 COMMANDS.md 支持多包管理器 | 1 hour | - |
| P1-3 | 创建故障排除指南 | 1 hour | - |
| P1-4 | 创建分支管理指南 | 2 hours | - |
| **合计** | | **~10 hours** | |

### P2 - 延后处理（按需进行）

| 任务 | 工作量 | 备注 |
|------|--------|------|
| EXTENSIONS 文件创建 | 10 hours | 用户暂不需要 |
| CI/CD 集成指南 | 3 hours | 用户有但不急 |
| 设置向导脚本 | 4 hours | 可后续添加 |

---

## 详细实施计划

### P0-1: 修复文件夹命名错误（30 分钟）

**问题**：
- `skills/sepckit-specify/` → 应为 `speckit-specify/`
- `skills/sepckit-implement/` → 应为 `speckit-implement/`

**操作**：
```bash
# 重命名文件夹
mv skills/sepckit-specify skills/speckit-specify
mv skills/sepckit-implement skills/speckit-implement

# 更新所有引用（需要手动检查 commands/ 目录）
```

---

### P0-2: 修复路径引用不一致（15 分钟）

**问题**：`CLAUDE-tem.md` 中引用 `@.specify/memory/constitution.md` 应为 `@.claude/constitution.md`

**修复**：
```diff
- @.specify/memory/constitution.md
+ @.claude/constitution.md
```

---

### P0-3: 创建核心模板（4 小时）

#### 3.1 spec-template.md（1.5 小时）

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

#### 3.2 plan-template.md（1.5 小时）

创建 `.claude/templates/plan-template.md`：

```markdown
# Implementation Plan: {Feature Name}

**Feature**: {Link to spec.md}
**Created**: {Date}
**Author**: {Author}

---

## Technical Context
{Technical background and implications}

## Constitution Check
{Check against constitution.md}

## Architecture Overview
{High-level architecture}

## Data Model
{Core entities and relationships}

## Interface Contracts
{APIs, schemas, protocols}

## Implementation Strategy
{How we will build this}

## Risk Assessment
{Technical risks and mitigations}

## Success Criteria
{How we know this is done}
```

#### 3.3 checklist-template.md（1 小时）

创建 `.claude/templates/checklist-template.md`：

```markdown
# Checklist: {Category}

**Feature**: {Link to spec.md}
**Created**: {Date}
**Purpose**: {What this checklist validates}

---

## Requirement Completeness
- [ ] CHK001 All requirements are testable
- [ ] CHK002 Success criteria are measurable
- [ ] ...

## Requirement Clarity
- [ ] CHK003 No ambiguous language
- [ ] ...

[... more categories]
```

---

### P0-4: 增强规范执行机制（4 小时）⭐ **核心需求**

这是用户最关心的部分：**确保 Claude 不能绕过规范**。

#### 4.1 在 BASE_CLAUDE.md 中添加规范执行门禁

在 `BASE_CLAUDE.md` 的开头添加：

```markdown
## 🔒 规范执行门禁（强制）

Claude 在执行任何任务前，必须按顺序通过以下 4 道门禁：

### 门禁 1：任务启动检查
当用户请求任何任务时，Claude 必须：
1. 检查是否已加载 `constitution.md`
2. 检查是否已加载适用的 `PROFILES/*.md`
3. 检查项目级 `CLAUDE.md` 是否存在
4. ❌ 若缺失任何一项：**必须先提示用户补全，不得开始任务**

### 门禁 2：关键操作门禁
以下操作前必须显式检查：
- [ ] 修改公共 API
- [ ] 引入新依赖
- [ ] 修改目录结构
- [ ] 跳过测试/文档

对于每项操作：
1. 检查是否违反 constitution
2. 检查是否有相关规范
3. ✅ 若符合：说明符合的条款
4. ⚠️ 若违反或缺失：警告用户，说明风险，请求确认

### 门禁 3：过程回顾
在任务执行过程中：
- 每完成一个阶段，回顾是否偏离规范
- 若发现偏离：立即提醒用户
- 建议纠正措施

### 门禁 4：完成验证
任务完成后：
- 对照规范检查所有变更
- 报告是否符合规范
- ⚠️ 若有偏差：说明偏差点和影响

### 违规处理策略

当检测到可能的违规行为时：

**分级处理**：
- 🟢 **轻微偏差**（命名风格、注释格式）：警告，允许继续
- 🟡 **中等偏差**（局部重构、新增工具函数）：警告 + 说明风险，请求确认
- 🔴 **严重偏差**（违反宪法、破坏架构）：**必须中止**，请求用户明确指示

**警告格式**：
```markdown
⚠️ **规范检查警告**

**检测到的偏差**：{描述偏差}

**涉及规范**：{引用相关规范条款}

**影响**：{说明可能的风险}

**建议**：
- 选项 A：按照规范调整（推荐）
- 选项 B：继续执行（确认风险）

请选择：A / B
```

### 自动检查清单

Claude 在任务启动时必须自动运行：

```markdown
## 规范预检清单

- [ ] constitution.md 已加载
- [ ] 语言 Profile 已加载
- [ ] 项目 CLAUDE.md 已加载
- [ ] 当前操作符合宪法原则
- [ ] 不存在已知冲突的规范

✅ 所有检查通过，开始任务
❌ 发现问题，需要先处理：{列出问题}
```
```

#### 4.2 在 constitution.md 中强化执行条款

添加新的宪法条款：

```markdown
## 10. 规范执行强制要求（新增）

### 10.1 禁止绕过规范

以下行为被视为**违规**，Claude **不得**执行：
- ❌ 明知违反宪法但继续执行
- ❌ 跳过必需的规范检查
- ❌ 忽略规范冲突警告而继续
- ❌ 在用户未确认的情况下继续高风险操作

### 10.2 规范缺失的处理

当发现规范缺失或不完整时：
1. **必须**明确告知用户
2. **不得**自行推断或假设
3. **建议**补充规范后再继续

### 10.3 规范冲突的裁决

当多个规范存在冲突时：
1. **必须**按优先级裁决（constitution > BASE > CLAUDE > Profile）
2. **必须**显式说明冲突点
3. **不得**自行调和
```

#### 4.3 创建规范检查工具

创建 `.claude/scripts/check_compliance.py`：

```python
#!/usr/bin/env python3
"""
规范检查脚本
用于验证 Claude 是否正确加载和遵循规范
"""

import sys
from pathlib import Path

def check_compliance(claude_dir: Path) -> tuple[bool, list[str]]:
    """检查规范合规性"""
    issues = []

    # 检查必需文件
    required_files = [
        claude_dir / "constitution.md",
        claude_dir / "BASE_CLAUDE.md",
    ]

    for file in required_files:
        if not file.exists():
            issues.append(f"缺失必需文件: {file.name}")

    # 检查项目配置
    claude_md = claude_dir.parent / "CLAUDE.md"
    if not claude_md.exists():
        issues.append("缺失项目级 CLAUDE.md")

    # 检查 Profile 引用
    if claude_md.exists():
        content = claude_md.read_text()
        if "@.claude/PROFILES/" not in content:
            issues.append("CLAUDE.md 未引用任何 Profile")

    return len(issues) == 0, issues

def main():
    claude_dir = Path(__file__).parent.parent
    is_compliant, issues = check_compliance(claude_dir)

    if is_compliant:
        print("✅ 规范检查通过")
        return 0
    else:
        print("❌ 规范检查失败")
        for issue in issues:
            print(f"  - {issue}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

---

### P0-5: 创建前端 Profile（2 小时）

创建 `.claude/profiles/frontend.md`：

```markdown
# Profile: frontend

**层级**：Profile
**适用**：前端项目（React / Vue / Angular / Svelte）
**依赖**：建议同时导入 `common.md`
**禁止**：不定义项目工作流；不引入业务规则。

---

## 代码风格与结构

### 命名约定
- 组件：PascalCase（`UserProfile.tsx`）
- 工具函数：camelCase（`formatDate.ts`）
- 常量：UPPER_SNAKE_CASE（`API_BASE_URL`）
- 类型/接口：PascalCase（`UserData`, `APIResponse`）
- Hooks：camelCase，use 前缀（`useUserData`）

### 目录结构
```
src/
├── components/     # 可复用组件
├── pages/          # 页面组件
├── hooks/          # 自定义 Hooks
├── utils/          # 工具函数
├── types/          # TypeScript 类型定义
├── api/            # API 调用
├── stores/         # 状态管理
└── styles/         # 全局样式
```

---

## 类型提示（TypeScript）

- **强制**：公共 API 必须有类型定义
- **推荐**：所有组件使用 Props 接口
- **禁止**：使用 `any`（除非有明确注释说明原因）

### 示例
```typescript
interface UserProfileProps {
  userId: string;
  onUpdate?: () => void;
}

export function UserProfile({ userId, onUpdate }: UserProfileProps) {
  // ...
}
```

---

## 测试

### 测试框架
- 主框架：Jest / Vitest
- 组件测试：Testing Library
- E2E：Playwright / Cypress

### 测试原则
- **用户行为优先**：测试用户如何使用组件，而非实现细节
- **可访问性**：重要组件应包含 a11y 测试

### 命名
- 测试文件：`ComponentName.test.tsx`
- 测试描述：`should {expected behavior} when {state}`

### 示例
```typescript
describe('UserProfile', () => {
  it('should render user name when data is loaded', () => {
    // ...
  });

  it('should call onUpdate when save button is clicked', () => {
    // ...
  });
});
```

---

## 样式

### 推荐方式（按项目选择其一）
- CSS Modules
- styled-components
- Tailwind CSS

### 约束
- **禁止**：内联样式（除动态计算值）
- **推荐**：使用设计系统的 tokens
- **注意**：响应式设计，移动优先

---

## 性能

### 代码分割
- 路由级别懒加载
- 大型组件动态导入

### 优化
- React.memo() 适当使用
- useMemo/useCallback 避免过度优化
- 图片懒加载

---

## 安全

### 必须注意
- XSS 防护（避免 dangerouslySetInnerHTML）
- CSRF token 处理
- 敏感数据不存 localStorage
- 环境变量使用 .env

---

## 工具链

### 包管理器
- npm / pnpm / yarn（按项目选择）

### 代码质量
- ESLint（必选）
- Prettier（推荐）
- TypeScript strict mode（推荐）

### 构建
- Vite（推荐）
- Next.js / Nuxt.js（SSR 项目）
- Webpack（遗留项目）

---

本文件为 Frontend Profile，仅补充前端相关实现，不得覆盖 Common 规则。
```

---

### P0-6: 创建错误总结模板和流程（3 小时）

#### 6.1 创建错误总结模板

创建 `.claude/templates/error_case_template.md`：

```markdown
# Error Case: {错误标题}

**Date**: {YYYY-MM-DD}
**Severity**: Critical / High / Medium / Low
**Status**: Open | Resolved | Verified

---

## 症状（Symptoms）

{描述用户可见的错误现象}

## 根因（Root Cause）

{分析错误发生的根本原因}

## 修复（Fix）

{如何修复这个问题}

## 预防（Prevention）

{如何防止类似问题再次发生}

## 相关规范更新

{是否需要更新 constitution/PROFILE/CLAUDE.md}

## 相关 Pattern

{如果这个问题代表了一类问题，创建 Pattern}
```

#### 6.2 创建 Pattern 模板

创建 `.claude/templates/error_pattern_template.md`：

```markdown
# Error Pattern: {模式名称}

**Created**: {YYYY-MM-DD}
**Category**: {类别：架构/API/性能/安全等}

---

## 描述

{这类错误的通用描述}

## 典型症状

{如何识别这类错误}

## 典型根因

{这类错误的常见原因}

## 预防性约束

{在 constitution/PROFILE 中应该添加什么约束来防止}

## 检查清单

- [ ] {检查项 1}
- [ ] {检查项 2}

## 相关 Cases

- [Case 1]({link})
- [Case 2]({link})
```

#### 6.3 定义错误处理工作流

创建 `.claude/docs/ERROR_WORKFLOW.md`：

```markdown
# 错误总结工作流

## 触发条件

当以下任一情况发生时，**必须**执行错误总结流程：
- 开发过程中出现 bug / 异常 / 非预期行为
- 用户明确指出"这里有问题"
- 需要 workaround 才能继续推进
- 修复涉及非显而易见的原因

## 工作流程

### 1. 记录错误

在 `specs/error/cases/` 目录创建错误记录：
1. 使用 `error_case_template.md` 模板
2. 填写症状、根因、修复、预防

### 2. 识别模式

判断这个错误是否代表了一类问题：
- 如果是：在 `specs/error/patterns/` 创建 Pattern
- 更新相关规范（constitution/PROFILE）

### 3. 更新规范

如果需要更新规范：
1. 在 `constitution.md` 或相关 Profile 中添加约束
2. 在 Pattern 中引用规范条款

### 4. 验证

在后续开发中：
- 优先查询 `specs/error/patterns/`
- 若存在相关 Pattern，必须遵循其"预防性约束"

## 目录结构

```
specs/
└── error/
    ├── cases/              # 具体错误案例
    │   ├── 001-error-name.md
    │   └── 002-error-name.md
    └── patterns/           # 错误模式
        ├── architecture-patterns.md
        ├── api-patterns.md
        └── performance-patterns.md
```
```

---

### P0-7: 创建模板验证脚本（2 小时）

创建 `.claude/scripts/validate_template.py`：

```python
#!/usr/bin/env python3
"""
模板验证脚本
检查 CLAUDE.md 和 PROJECT_CONTEXT.md 中的占位符是否已填写
"""

import re
import sys
from pathlib import Path

# 必填占位符列表
REQUIRED_PLACEHOLDERS = {
    "CLAUDE.md": [
        r"\{项目名称\}",
        r"\{主要语言\}",
        r"\{语言版本\}",
        r"\{主要框架\}",
        r"\{测试框架\}",
    ],
    "PROJECT_CONTEXT.md": [
        r"\{project_name\}",
        r"\{project_type\}",
        r"\{primary_language\}",
        r"\{language_version\}",
    ]
}

def check_placeholders(file_path: Path, template_name: str) -> tuple[bool, list[str]]:
    """检查文件中的必填占位符"""
    if not file_path.exists():
        return False, [f"文件不存在: {file_path}"]

    content = file_path.read_text()
    missing = []

    patterns = REQUIRED_PLACEHOLDERS.get(template_name, [])
    for pattern in patterns:
        if re.search(pattern, content):
            missing.append(f"未填写: {pattern}")

    return len(missing) == 0, missing

def main():
    # 检查 CLAUDE.md
    claude_md = Path("CLAUDE.md")
    is_valid, issues = check_placeholders(claude_md, "CLAUDE.md")

    if is_valid:
        print("✅ CLAUDE.md 模板验证通过")
    else:
        print("❌ CLAUDE.md 存在未填写的必填项:")
        for issue in issues:
            print(f"  - {issue}")

    # 检查 PROJECT_CONTEXT.md
    project_ctx = Path("PROJECT_CONTEXT.md")
    is_valid, issues = check_placeholders(project_ctx, "PROJECT_CONTEXT.md")

    if is_valid:
        print("✅ PROJECT_CONTEXT.md 模板验证通过")
    else:
        print("❌ PROJECT_CONTEXT.md 存在未填写的必填项:")
        for issue in issues:
            print(f"  - {issue}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
```

同时创建手动检查清单 `.claude/docs/TEMPLATE_CHECKLIST.md`：

```markdown
# 模板填写检查清单

使用本清单在自动脚本验证后进行人工确认。

## CLAUDE.md 必填项

- [ ] {项目名称}
- [ ] {主要语言}
- [ ] {语言版本}
- [ ] {主要框架}
- [ ] {测试框架}
- [ ] @.claude/constitution.md 已引用
- [ ] @.claude/PROFILES/common.md 已引用
- [ ] 语言 Profile 已引用（python/cpp/frontend）
- [ ] testing Profile 已引用

## PROJECT_CONTEXT.md 必填项

- [ ] {project_name}
- [ ] {project_type}
- [ ] {primary_language}
- [ ] {language_version}
- [ ] 项目目录结构已填写
- [ ] 依赖列表已填写
- [ ] 运行命令已填写

## 人工确认项

- [ ] 所有占位符已替换为实际内容
- [ ] 不适用的章节已删除
- [ ] 文档路径引用正确
- [ ] 命令在当前环境可执行
```

---

### P0-8: 创建快速开始文档（2 小时）

创建 `.claude/docs/QUICKSTART.md`：

```markdown
# 快速开始指南

本指南帮助你在 15 分钟内为项目配置 Claude Code 驾驶舱。

---

## 第一步：准备项目

确保你的项目满足以下条件：
- [ ] 是 Git 仓库
- [ ] 有明确的主要语言（Python/C++/前端等）
- [ ] 知道项目的框架和测试工具

---

## 第二步：复制模板

```bash
# 在项目根目录执行
mkdir -p .claude

# 复制模板（从框架目录）
cp /path/to/guide_cc/.claude/templates/CLAUDE-tem.md .claude/CLAUDE.md
cp /path/to/guide_cc/.claude/templates/PROJECT_CLAUDE-tem.md PROJECT_CONTEXT.md
```

---

## 第三步：填写 CLAUDE.md

打开 `.claude/CLAUDE.md`，填写以下必填项：

### 3.1 头部信息

```markdown
**项目**：my-awesome-project
**类型**：Web 应用
**主要语言**：Python
**维护者**：your-name
```

### 3.2 技术栈

填写表格：

| 项目 | 内容 |
|----|----|
| 语言版本 | Python 3.11 |
| 框架 | FastAPI |
| 架构模式 | 分层架构 |
| 包管理 | uv |
| 测试框架 | pytest |

### 3.3 选择 Profile

取消注释并保留你需要的：

```markdown
@.claude/PROFILES/python.md   # Python 项目
@.claude/PROFILES/testing-python.md
```

---

## 第四步：填写 PROJECT_CONTEXT.md

打开 `PROJECT_CONTEXT.md`，填写：

### 4.1 项目信息

```markdown
| **项目名称** | my-awesome-project |
| **项目类型** | Web API |
| **主要语言** | Python |
| **语言版本** | 3.11 |
```

### 4.2 项目结构

填写你的实际目录结构：

```
my-awesome-project/
├── src/
│   ├── api/
│   ├── services/
│   └── models/
├── tests/
└── pyproject.toml
```

### 4.3 常用命令

填写实际可用的命令：

```bash
# 安装依赖
uv pip install -e ".[dev]"

# 运行测试
uv run pytest

# 启动服务
uv run python -m src.main
```

---

## 第五步：验证配置

运行验证脚本：

```bash
python .claude/scripts/validate_template.py
python .claude/scripts/check_compliance.py
```

应该看到：
```
✅ CLAUDE.md 模板验证通过
✅ PROJECT_CONTEXT.md 模板验证通过
✅ 规范检查通过
```

---

## 第六步：测试

在 Claude Code 中测试：

1. 打开项目
2. 询问："请检查项目配置是否正确"
3. Claude 应该能正确加载所有规范

---

## 常见问题

### Q: Claude 说找不到 constitution.md

**A**: 检查 `.claude/CLAUDE.md` 中的路径是否正确：
```markdown
@.claude/constitution.md  # 注意路径是相对路径
```

### Q: 不知道填什么框架

**A**: 参考 `.claude/examples/` 中的示例项目

### Q: 验证脚本报错

**A**:
1. 确保使用了绝对路径或从项目根目录运行
2. 检查 Python 版本（需要 Python 3.10+）

---

## 下一步

配置完成后，你可以：
- 阅读 [完整指南](GUIDE.md) 了解更多
- 查看 [示例项目](examples/) 学习最佳实践
- 开始第一个功能：`/speckit.specify 添加用户登录`
```

---

### P0-9: 创建项目示例（3 小时）

创建三个示例项目，展示最佳实践。

#### 9.1 Python 项目示例

创建 `.claude/examples/python/CLAUDE.md`（简化版完整示例）

#### 9.2 C++ 项目示例

创建 `.claude/examples/cpp/CLAUDE.md`（简化版完整示例）

#### 9.3 前端项目示例

创建 `.claude/examples/frontend/CLAUDE.md`（简化版完整示例）

---

## 时间进度安排

| 天数 | 任务 | 累计工作量 |
|------|------|-----------|
| Day 1 | P0-1, P0-2, P0-4（规范执行机制） | ~5 hours |
| Day 2 | P0-3（核心模板） | ~4 hours |
| Day 3 | P0-5（前端 Profile）, P0-6（错误处理） | ~5 hours |
| Day 4 | P0-7（验证脚本）, P0-8（快速开始） | ~4 hours |
| Day 5 | P0-9（项目示例） | ~3 hours |
| Day 6-7 | 缓冲时间 + P1 任务 | ~6 hours |

---

## 验收标准

完成 P0 所有任务后，应该能够：

1. ✅ 文件夹命名正确，路径引用一致
2. ✅ 创建新功能时使用标准模板
3. ✅ Claude 不会绕过规范（4 道门禁生效）
4. ✅ 前端项目有专门的 Profile 支持
5. ✅ 错误有标准记录和预防流程
6. ✅ 模板可自动验证 + 人工检查
7. ✅ 新项目可在 15 分钟内完成配置
8. ✅ 有完整的项目示例参考

---

## 附录：文件清单

### 需要创建的文件（P0）

```
.claude/
├── templates/
│   ├── spec-template.md
│   ├── plan-template.md
│   ├── checklist-template.md
│   ├── error_case_template.md
│   └── error_pattern_template.md
├── docs/
│   ├── ERROR_WORKFLOW.md
│   ├── QUICKSTART.md
│   └── TEMPLATE_CHECKLIST.md
├── scripts/
│   ├── check_compliance.py
│   └── validate_template.py
├── profiles/
│   └── frontend.md
└── examples/
    ├── python/
    ├── cpp/
    └── frontend/
```

### 需要修改的文件（P0）

```
.claude/
├── BASE_CLAUDE.md         # 添加规范执行门禁
├── constitution.md        # 添加执行强制要求
└── templates/
    └── CLAUDE-tem.md      # 修复路径引用
```

---

**方案结束**

*本方案基于用户实际需求定制，聚焦 1 周内可完成的关键优化*
