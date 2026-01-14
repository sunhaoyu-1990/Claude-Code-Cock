# 新项目快速指南（New Project Quick Start）

**版本**：v1.0
**适用对象**：从零开始的新项目
**目的**：快速为新项目初始化 Claude Code 配置

---

## 概述

本指南针对**从零开始的新项目**，提供快速初始化 Claude Code 框架的方法。

**核心命令**：`/init-claude-context`

**命令功能**：
- 自动检测需求文件
- 支持两种生成模式：
  - **自动模式**：基于需求文件自动推断并生成
  - **互动模式**：逐步引导用户填写配置
- 智能选择 Profile 和 Extension
- 生成规范的 CLAUDE.md 文件

---

## 快速开始（2 分钟）

### 前置条件

1. **创建项目目录**
   ```bash
   mkdir my-new-project
   cd my-new-project
   ```

2. **初始化 Git 仓库**
   ```bash
   git init
   ```

3. **安装框架**
   ```bash
   # 复制框架文件到项目
   # 假设框架在 /path/to/guide_cc/.claude/
   cp -r /path/to/guide_cc/.claude/* .claude/
   ```

### 使用命令初始化

**方式一：有需求文档（自动模式）**

如果项目有需求文档（README.md、SPEC.md、PRD.md 等）：

```bash
# 在 Claude Code 中调用
/init-claude-context --auto
```

**命令会自动**：
1. ✅ 读取需求文件
2. ✅ 提取项目信息
3. ✅ 推断技术栈
4. ✅ 选择合适的 Profile
5. ✅ 生成 CLAUDE.md
6. ✅ 验证配置

**方式二：无需求文档（互动模式）**

如果项目还没有需求文档：

```bash
# 在 Claude Code 中调用
/init-claude-context --interactive
```

**命令会引导您**：
1. 📝 逐步询问项目信息
2. 🎯 帮助明确项目范围
3. 🔧 推荐合适的 Profile
4. ✅ 生成完整的 CLAUDE.md

---

## 命令详解

### 自动模式（--auto）

**适用场景**：
- ✅ 有完整的需求文档
- ✅ 项目目标明确
- ✅ 希望快速开始

**执行流程**：

```
检测需求文件
    ↓
读取并分析需求文件
    ↓
提取关键信息
    ↓
自动推断配置
    ↓
生成 CLAUDE.md
    ↓
验证配置
    ↓
完成
```

**自动推断内容**：

| 信息项 | 推断方式 |
|--------|---------|
| 项目名称 | 需求文件标题 / Git 仓库名 |
| 项目类型 | 需求描述关键词（API/应用/库等） |
| 主要语言 | 需求中提到的语言 |
| 主要框架 | 需求中提到的框架 |
| 测试框架 | 语言对应的默认框架 |
| 代码风格 | 语言对应的默认风格 |
| 项目结构 | 项目类型对应的默认结构 |

**输出示例**：
```markdown
## ✅ CLAUDE.md 生成完成（自动模式）

### 项目信息
- **项目名称**：user-auth-service
- **项目类型**：Web API
- **主要语言**：Python 3.11
- **主要框架**：FastAPI

### 需求文件来源
- **文件**：SPEC.md
- **提取信息**：用户认证、JWT Token、RBAC

### 占位符内容
以下内容使用了占位符，建议后续完善：
- [ ] 入口文件路径
- [ ] 模块职责详细说明

### 下一步
1. 检查 CLAUDE.md
2. 修改占位符
3. 运行验证
```

### 互动模式（--interactive）

**适用场景**：
- ✅ 需求文档不完整
- ✅ 需要逐步明确项目细节
- ✅ 希望完全控制配置过程

**执行流程**：

```
需求文件检测
    ↓
逐步引导（22个章节）
    ↓
每个章节确认
    ↓
累积生成内容
    ↓
完成并验证
```

**引导章节**：

1. **项目信息**（必填）
   - 项目名称
   - 项目类型
   - 主要语言
   - 语言版本
   - 主要框架
   - 测试框架
   - 包管理器

2. **核心能力范围**（建议填写）
   - 项目功能描述
   - 非目标说明

3. **依赖与能力边界**（建议填写）
   - 外部依赖
   - 功能边界

4. **项目结构**（可选）
   - 目录结构说明

5. **Profile 选择**（必填）
   - 语言 Profile
   - 测试 Profile
   - Extension（可选）

6. **其他章节**（可使用默认值）
   - 开发模式
   - 运行命令
   - 测试配置

**对话示例**：
```markdown
## 新项目初始化 - 互动模式

### 步骤 1/22：项目基本信息

**项目名称**：请输入项目名称
> my-awesome-api

**项目类型**：请选择项目类型
> A. Web API / 后端服务
> B. Web 应用 / 前端
> ...
> A

**主要语言**：请选择主要编程语言
> A. Python
> B. JavaScript / TypeScript
> ...
> A

**语言版本**：Python 常用版本：3.9 / 3.10 / 3.11 / 3.12
> 3.11

[...]

✅ 22 个章节引导完成
```

---

## 需求文件格式支持

### 支持的文件名

命令会按以下优先级查找需求文件：

1. `SPEC.md` / `spec.md`
2. `PRD.md` / `prd.md`
3. `README.md`
4. `docs/SPEC.md`
5. `docs/requirements.md`
6. `REQUIREMENTS.md`
7. `.claude/SPECS/*/spec.md`

### 文件格式要求

#### Markdown 格式（推荐）

```markdown
# {项目名称} 需求文档

## 项目概述

{项目描述}

## 功能需求

### 核心功能

1. {功能1}
2. {功能2}
3. {功能3}

## 技术需求

### 后端技术栈
- 语言：Python 3.11
- 框架：FastAPI
- 数据库：PostgreSQL 14

### 前端技术栈
- 框架：React 18
- 语言：TypeScript 5

## 非功能需求

### 性能要求
- API 响应时间 < 100ms
- 支持并发用户数 > 1000

### 安全要求
- 使用 JWT Token 认证
- 支持基于角色的访问控制（RBAC）
```

#### 关键词映射

命令会根据关键词推断项目信息：

| 关键词 | 推断结果 |
|--------|---------|
| **项目类型关键词** |
| "API" / "后端" / "服务" / "Service" | Web API / 后端服务 |
| "Web 应用" / "前端" / "UI" / "界面" | Web 应用 / 前端 |
| "CLI" / "命令行" / "工具" | CLI 工具 |
| "库" / "框架" / "SDK" / "Library" | 库 / 框架 |
| **语言关键词** |
| "Python" / "Django" / "FastAPI" | Python |
| "JavaScript" / "TypeScript" / "Node" | JavaScript / TypeScript |
| "Go" / "Golang" | Go |
| "Rust" | Rust |
| "C++" / "C plus plus" | C/C++ |
| "Java" / "Spring" | Java |
| **框架关键词** |
| "React" | React（前端） |
| "Vue" | Vue（前端） |
| "Angular" | Angular（前端） |
| "Django" | Django（Python Web） |
| "FastAPI" | FastAPI（Python API） |
| "Flask" | Flask（Python Web） |
| "Express" | Express（Node.js） |
| **测试关键词** |
| "pytest" / "PyTest" | pytest（Python 测试） |
| "Jest" / "jest" | Jest（JS 测试） |
| "Vitest" / "vitest" | Vitest（JS 测试） |
| "unittest" | unittest（Python 测试） |

---

## 项目类型模板

命令内置了常见项目类型的默认配置：

### Web API（Python）

```python
{
    "项目类型": "Web API",
    "主要语言": "Python",
    "语言版本": "3.11",
    "主要框架": "FastAPI",
    "包管理器": "poetry",
    "测试框架": "pytest",
    "代码风格": "Black + Flake8 + mypy",
    "架构模式": "分层架构",
    "目标平台": "Linux / Docker",
    "目录结构": """
app/
├── api/          # API 路由
├── models/       # 数据模型
├── services/     # 业务逻辑
├── schemas/      # 数据验证
├── main.py       # 应用入口
tests/            # 测试代码
alembic/           # 数据库迁移
    """,
}
```

### Web 应用（TypeScript）

```python
{
    "项目类型": "Web 应用",
    "主要语言": "TypeScript",
    "语言版本": "5.0",
    "主要框架": "React 18 + Next.js 14",
    "包管理器": "pnpm",
    "测试框架": "Vitest + Testing Library",
    "代码风格": "ESLint + Prettier",
    "架构模式": "组件化架构",
    "目标平台": "Web 浏览器",
    "目录结构": """
src/
├── app/         # 页面组件
├── components/  # 可复用组件
├── lib/         # 工具函数
├── styles/      # 样式文件
└── main.tsx     # 应用入口
public/          # 静态资源
tests/           # 测试代码
    """,
}
```

### CLI 工具（Python）

```python
{
    "项目类型": "CLI 工具",
    "主要语言": "Python",
    "语言版本": "3.11",
    "主要框架": "Click / Typer",
    "包管理器": "poetry",
    "测试框架": "pytest",
    "代码风格": "Black + Flake8",
    "架构模式": "命令模式",
    "目标平台": "跨平台",
    "目录结构": """
src/
├── __main__.py  # 入口点
├── cli/         # 命令定义
├── core/        # 核心逻辑
└── utils/       # 工具函数
tests/           # 测试代码
    """,
}
```

### 库/框架（Python）

```python
{
    "项目类型": "库 / SDK",
    "主要语言": "Python",
    "语言版本": "3.8+",
    "主要框架": "无（纯库）",
    "包管理器": "poetry / setuptools",
    "测试框架": "pytest + tox",
    "代码风格": "Black + Flake8 + mypy",
    "架构模式": "模块化架构",
    "目标平台": "跨平台",
    "目录结构": """
src/
├── {package_name}/  # 主要代码
├── __init__.py
tests/                # 测试代码
docs/                 # 文档
examples/             # 示例代码
    """,
}
```

---

## 完整使用示例

### 示例 1：有需求文档的自动模式

**需求文件（SPEC.md）**：
```markdown
# 用户认证服务 API

## 项目概述

开发一个用户认证和授权的 Web API 服务。

## 功能需求

### 核心功能
1. 用户注册和登录
2. JWT Token 认证
3. 基于角色的访问控制（RBAC）
4. 密码重置和邮箱验证

## 技术需求

### 后端技术栈
- 语言：Python 3.11
- 框架：FastAPI
- 数据库：PostgreSQL 14
- 缓存：Redis 6

### 测试
- 使用 pytest 进行单元测试和集成测试
- 测试覆盖率 > 80%
```

**执行命令**：
```bash
/init-claude-context --auto
```

**命令输出**：
```markdown
## ✅ CLAUDE.md 生成完成（自动模式）

### 需求文件分析结果

**文件**：SPEC.md

### 提取的信息

**项目基本信息**：
- 项目名称：用户认证服务 API
- 项目类型：Web API
- 主要语言：Python
- 主要框架：FastAPI

**核心功能**：
1. 用户注册和登录
2. JWT Token 认证
3. 基于角色的访问控制（RBAC）
4. 密码重置和邮箱验证

**技术栈**：
- 后端：Python 3.11 + FastAPI
- 数据库：PostgreSQL 14
- 缓存：Redis 6
- 测试：pytest

### 自动推断的配置

- **项目类型**：Web API
- **主要语言**：Python 3.11
- **主要框架**：FastAPI
- **包管理器**：poetry
- **测试框架**：pytest
- **代码风格**：Black + Flake8 + mypy
- **架构模式**：分层架构
- **目标平台**：Linux / Docker

### Profile 配置

- **语言 Profile**：@.claude/profiles/python.md
- **测试 Profile**：@.claude/profiles/testing-python.md

### 占位符内容

以下内容使用了占位符，建议后续完善：
- [ ] 入口文件路径（默认：app/main.py）
- [ ] 数据库连接配置
- [ ] Redis 连接配置
- [ ] JWT Secret 配置
- [ ] 邮件服务配置

### 下一步操作

1. 检查生成的 CLAUDE.md
2. 根据项目实际情况调整占位符内容
3. 运行验证：
   ```bash
   python .claude/scripts/validate_template.py
   ```
4. 开始开发：
   ```bash
   # 创建功能分支
   /branch feature/001-user-registration

   # 或使用 Speckit Skill Chain
   /speckit-specify 实现用户注册功能
   ```

### 推荐的 Extension

根据项目特点，建议考虑以下 Extension：

- [ ] architecture-heavy.md（大型企业应用）
- [ ] safety-critical.md（涉及安全认证）

参考：[Extension 启用指南](.claude/EXTENSIONS_GUIDE.md)
```

### 示例 2：无需求文档的互动模式

**项目状态**：
- 新建项目目录
- 没有 README.md 或需求文档
- 项目想法还在构思中

**执行命令**：
```bash
/init-claude-context --interactive
```

**互动过程**（简化版）：
```markdown
## 新项目初始化 - 互动模式

### 步骤 1/22：项目基本信息

**项目名称**：请输入项目名称
> task-manager-api

**项目类型**：请选择项目类型
> A. Web API / 后端服务
> B. Web 应用 / 前端
> C. CLI 工具 / 命令行应用
> D. 库 / 框架 / SDK
> E. 桌面应用
> F. 移动应用
> G. 其他
> A

**主要语言**：请选择主要编程语言
> A. Python
> B. JavaScript / TypeScript
> C. Go
> D. Rust
> E. C / C++
> F. Java
> G. 其他
> A

**语言版本**：Python 常用版本：3.9 / 3.10 / 3.11 / 3.12
> 3.11

**主要框架**：请选择主要框架（可选）
> A. FastAPI
> B. Django
> C. Flask
> D. 其他
> A

**测试框架**：选择测试框架
> A. pytest（推荐）
> B. unittest
> C. 其他
> A

**包管理器**：选择包管理器
> A. poetry（推荐）
> B. pip
> C. uv
> A

### 步骤 2/22：核心功能范围

**项目功能描述**：请描述项目的核心功能（1-3 句话）
> 一个任务管理 API 服务，提供任务的创建、更新、删除和查询功能。
> 支持任务的优先级设置、到期提醒和任务分配。

**项目非目标**（可选）：请说明项目不做什么
> 不包含前端 UI，不包含用户管理，不包含实时通知。

[... 继续其他步骤 ...]

### 步骤 22/22：确认生成

**所有信息收集完成，即将生成 CLAUDE.md**

**项目信息摘要**：
- 项目名称：task-manager-api
- 项目类型：Web API
- 主要语言：Python 3.11
- 主要框架：FastAPI
- 测试框架：pytest
- 包管理器：poetry

**是否确认生成？**
- A. 确认生成
- B. 返回修改
> A

✅ 生成 CLAUDE.md...
✅ 验证配置...

## ✅ CLAUDE.md 生成完成（互动模式）

### 生成统计
- 总章节数：22
- 填写章节数：18
- 跳过章节数：4
- 使用默认值章节数：5

### Profile 配置
- 语言 Profile：@.claude/profiles/python.md
- 测试 Profile：@.claude/profiles/testing-python.md

### 下一步
1. 检查 CLAUDE.md
2. 运行验证：python .claude/scripts/validate_template.py
3. 开始开发
```

---

## 命令参数详解

### 语法

```bash
/init-claude-context [模式]
```

### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--auto` / `-a` | 自动模式 | 无 |
| `--interactive` / `-i` | 互动模式 | 无 |
| 无参数 | 自动检测需求文件，找到则自动模式，否则互动模式 | - |

### 使用场景对照表

| 场景 | 推荐参数 | 说明 |
|------|----------|------|
| 有完整需求文档 | `--auto` | 快速生成，无需交互 |
| 有需求文档但需调整 | `--auto` + 手动编辑 | 先自动生成，再手动调整 |
| 需求文档不完整 | `--interactive` | 补充缺失信息 |
| 无需求文档 | `--interactive` | 从头开始引导 |
| 不确定 | 无参数 | 命令会自动检测并推荐 |

---

## 与现有项目命令的对比

| 特性 | init-claude-context | generate-claude-context |
|------|-------------------|------------------------|
| **适用对象** | 新项目 | 现有项目 |
| **需求文件** | 读取并分析 | 不读取 |
| **代码分析** | 不分析代码 | 分析现有代码 |
| **模式选择** | 自动/互动两种 | 仅自动 |
| **Profile 选择** | 引导用户选择 | 自动推荐 |
| **配置复杂度** | 简单（默认值为主） | 详细（基于实际代码） |

---

## 常见问题

### Q1：两种模式如何选择？

**A**：
- **选择自动模式**：如果你有完整的需求文档，希望快速开始
- **选择互动模式**：如果你需要逐步明确项目细节，希望完全控制配置过程

### Q2：自动模式生成的配置可以修改吗？

**A**：可以。自动模式只是快速生成初始配置，你可以：
1. 直接编辑生成的 CLAUDE.md
2. 使用互动模式重新生成
3. 手动添加 Extension

### Q3：互动模式会很耗时吗？

**A**：不会。互动模式：
- 必填章节约 8 个
- 可选章节约 14 个（可跳过或使用默认值）
- 大部分章节可以使用默认值
- 预计 3-5 分钟完成

### Q4：可以中途退出吗？

**A**：可以。在任何步骤选择：
- 输入 `quit` 或 `exit` 退出
- 命令会保存已收集的信息
- 下次可以继续

### Q5：生成的 CLAUDE.md 不满意怎么办？

**A**：有三种方式：
1. **手动编辑**：直接修改 CLAUDE.md
2. **重新生成**：删除 CLAUDE.md 后重新运行命令
3. **补充生成**：使用互动模式补充缺失章节

---

## 完整工作流

### 新项目完整流程

```
1. 创建项目目录
   mkdir my-project
   cd my-project

2. 初始化 Git
   git init

3. 安装框架
   cp -r /path/to/guide_cc/.claude/* .claude/

4. （可选）创建需求文档
   # 方式 A：使用模板
   cp .claude/templates/spec-template.md SPEC.md
   # 编辑 SPEC.md

   # 方式 B：直接写 README.md
   # 编辑 README.md

5. 运行初始化命令
   /init-claude-context

6. 验证配置
   python .claude/scripts/validate_template.py

7. 开始开发
   /branch feature/001-initial-feature
   /speckit-specify 添加第一个功能
```

---

## 相关文档

- [快速开始指南](QUICKSTART.md)
- [现有项目接入指南](EXISTING_PROJECT_GUIDE.md)
- [Profile 选择指南](QUICKSTART.md#23-配置-profile-引用)
- [Extension 启用指南](EXTENSIONS_GUIDE.md)
- [分支管理指南](BRANCH_GUIDE.md)
- [模板检查清单](templates/TEMPLATE_CHECKLIST.md)

---

**版本**：v1.0
**最后更新**：2026-01-14
