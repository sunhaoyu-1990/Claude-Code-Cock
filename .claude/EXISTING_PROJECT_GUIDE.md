# 现有项目接入指南（Existing Project Onboarding Guide）

**版本**：v1.0
**适用对象**：已有代码的项目
**目的**：快速将现有项目接入 Claude Code 框架

---

## 概述

本指南针对**已有代码的项目**，提供快速接入 Claude Code 框架的方法。

**核心命令**：`/generate-claude-context`

**命令功能**：
- 自动分析项目技术栈
- 识别项目结构和依赖
- 检测代码规范和测试配置
- 基于模板生成 CLAUDE.md
- 提供配置建议

---

## 快速开始（3 分钟）

### 前置条件

1. **项目必须是 Git 仓库**
   ```bash
   # 如果还不是 Git 仓库，先初始化
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **安装 Claude Code 框架**
   ```bash
   # 在项目根目录创建 .claude 目录
   mkdir -p .claude

   # 复制框架核心文件
   # 假设框架在 /path/to/guide_cc/.claude/
   cp -r /path/to/guide_cc/.claude/* .claude/
   ```

### 使用自动化命令

**在 Claude Code 中调用**：
```
/generate-claude-context
```

**命令会自动执行**：

1. ✅ 检测项目类型（Python/JavaScript/Go/Rust 等）
2. ✅ 识别主要框架（Django/React/FastAPI 等）
3. ✅ 分析项目结构（src/tests/docs 等）
4. ✅ 提取依赖信息（requirements.txt/package.json 等）
5. ✅ 检测代码规范（ESLint/Pylint/Black 等）
6. ✅ 识别测试框架（pytest/Jest/Vitest 等）
7. ✅ 检测 CI/CD 配置（GitHub Actions/GitLab CI 等）
8. ✅ 生成 CLAUDE.md 文件
9. ✅ 验证生成的配置

---

## 支持的项目类型

### Python 项目

**检测特征**：
- `requirements.txt`, `pyproject.toml`, `setup.py`, `poetry.lock`
- 文件扩展名：`.py`

**自动识别**：
- 主要框架：Django, FastAPI, Flask, SQLAlchemy 等
- 测试框架：pytest, unittest, nose
- 代码规范：PEP 8, Black, Flake8, Pylint, mypy
- 包管理器：pip, poetry, uv, conda

**示例输出**：
```markdown
## 项目分析结果

- **项目名称**：my-awesome-project
- **项目类型**：Web API
- **主要语言**：Python 3.11
- **主要框架**：FastAPI
- **包管理器**：poetry
- **测试框架**：pytest
```

### JavaScript/TypeScript 项目

**检测特征**：
- `package.json`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
- 文件扩展名：`.js`, `.ts`, `.jsx`, `.tsx`

**自动识别**：
- 主要框架：React, Vue, Angular, Express, Next.js 等
- 测试框架：Jest, Vitest, Mocha, Jasmine
- 代码规范：ESLint, Prettier, TypeScript
- 包管理器：npm, pnpm, yarn

**示例输出**：
```markdown
## 项目分析结果

- **项目名称**：react-dashboard
- **项目类型**：Web 应用
- **主要语言**：TypeScript 5.0
- **主要框架**：React 18 + Next.js 14
- **包管理器**：pnpm
- **测试框架**：Jest + React Testing Library
```

### Go 项目

**检测特征**：
- `go.mod`, `go.sum`
- 文件扩展名：`.go`

**自动识别**：
- 主要框架：Gin, Echo, Fiber, gRPC 等
- 测试框架：testing, testify
- 包管理器：go modules

### Rust 项目

**检测特征**：
- `Cargo.toml`, `Cargo.lock`
- 文件扩展名：`.rs`

**自动识别**：
- 主要框架：Actix, Rocket, Tokio 等
- 测试框架：built-in testing
- 包管理器：cargo

### C/C++ 项目

**检测特征**：
- `CMakeLists.txt`, `Makefile`, `meson.build`
- 文件扩展名：`.c`, `.cpp`, `.h`, `.hpp`

**自动识别**：
- 主要框架：Boost, Qt, STL 等
- 测试框架：gtest, catch2
- 构建系统：CMake, Make, Meson

---

## 命令执行流程

### 步骤 1：项目分析

命令会执行以下检测：

```bash
# Git 仓库检查
git status

# 项目类型检测（按优先级）
ls package.json pyproject.toml Cargo.toml go.mod 2>/dev/null

# 目录结构分析
find . -maxdepth 2 -type d

# 入口文件检测
ls index.ts main.py src/main.rs 2>/dev/null

# 配置文件检测
find . -maxdepth 1 -name ".*rc*" -o -name "*.config.*"
```

### 步骤 2：信息提取

**从配置文件中提取**：

| 文件类型 | 提取内容 |
|---------|---------|
| `package.json` | name, version, dependencies, devDependencies, scripts |
| `pyproject.toml` | name, version, dependencies, requires-python |
| `Cargo.toml` | name, version, dependencies |
| `go.mod` | module name, go version |
| `tsconfig.json` | compiler options, paths |
| `.eslintrc.*` | rules, parser options |
| `pytest.ini` | test paths, markers |

### 步骤 3：Profile 和 Extension 选择

**自动推荐 Profile**：

| 项目特征 | 推荐 Profile |
|---------|-------------|
| Python + pytest | `@.claude/profiles/python.md` + `@.claude/profiles/testing-python.md` |
| TypeScript + React | `@.claude/profiles/frontend.md` + `@.claude/profiles/testing-common.md` |
| C++ + gtest | `@.claude/profiles/cpp.md` + `@.claude/profiles/testing-cpp.md` |

**自动推荐 Extension**（可选）：

| 项目特征 | 推荐 Extension |
|---------|---------------|
| 大型企业应用 | `@.claude/extensions/architecture-heavy.md` |
| 数据处理项目 | `@.claude/extensions/data-pipeline.md` |
| 金融/医疗项目 | `@.claude/extensions/safety-critical.md` |

### 步骤 4：生成 CLAUDE.md

**生成的文件包含**：

```markdown
# CLAUDE.md（项目级规范与上下文）

## 0️⃣ 使用说明
## 1️⃣ 组织级规范导入
## 2️⃣ 项目角色设定
## 3️⃣ 项目信息（自动填充）
## 4️⃣ 核心能力范围
## 5️⃣ 依赖与能力边界（自动填充）
## 6️⃣ 项目结构（自动填充）
## 7️⃣ 模块边界与职责
## 8️⃣ 语言/框架 Profile（自动选择）
## 9️⃣ 开发模式
## 🔟 命名约定
## 1️⃣1️⃣ 类型提示/接口契约
## 1️⃣2️⃣ 配置格式
## 1️⃣3️⃣ Git 与提交规范
## 1️⃣4️⃣ 运行入口与命令（自动填充）
## 1️⃣5️⃣ 测试与质量门槛（自动填充）
## 1️⃣6️⃣ 日志与可观测性
## 1️⃣7️⃣ 项目特定约定
## 1️⃣8️⃣ 项目级补充约束
## 1️⃣9️⃣ 错误知识库
## 2️⃣0️⃣ 相关文档索引
## 2️⃣1️⃣ 维护要求
## 2️⃣2️⃣ 架构参考
```

### 步骤 5：验证和调整

**自动验证**：
```bash
python .claude/scripts/validate_template.py
```

**如果验证通过**：
```
✅ CLAUDE.md 模板验证通过
```

**如果验证失败**：
```
❌ CLAUDE.md 存在未填写的必填项:
  - 未填写: {项目名称}
```

**手动调整**：
1. 检查生成的 CLAUDE.md
2. 填充自动分析无法识别的内容
3. 根据项目实际情况调整
4. 重新验证

---

## 手动调整指南

### 必须手动填写的内容

以下内容命令无法自动识别，需要手动填写：

#### 1. 核心能力范围（第 4️⃣ 节）

**示例**：
```markdown
## 核心能力范围

本项目是一个用户认证和授权系统，提供以下功能：
- 用户注册、登录、登出
- JWT Token 认证
- 基于角色的访问控制（RBAC）
- 密码重置和邮箱验证

**非目标**：
- 社交登录集成
- 多因素认证（MFA）
- SSO 单点登录
```

#### 2. 依赖与能力边界（第 5️⃣ 节）

**示例**：
```markdown
## 依赖与能力边界

### 外部依赖
- PostgreSQL 14+（数据存储）
- Redis 6+（缓存和会话）
- SendGrid（邮件服务）

### 能力边界
**包含**：
- 用户认证 API
- Token 管理和验证
- 权限检查中间件

**不包含**：
- 前端 UI（由前端团队负责）
- 用户管理界面
- 审计日志（未来版本考虑）
```

#### 3. 模块边界与职责（第 7️⃣ 节）

**示例**：
```markdown
## 模块边界与职责

| 模块 | 职责 | 接口 |
|------|------|------|
| auth | 认证逻辑 | `authenticate()`, `login()`, `logout()` |
| user | 用户管理 | `create_user()`, `update_user()` |
| token | Token 管理 | `generate_token()`, `validate_token()` |
| permission | 权限检查 | `check_permission()`, `require_role()` |
```

#### 4. 项目特定约定（第 1️⃣7️⃣ 节）

**示例**：
```markdown
## 项目特定约定

### 命名约定
- API 路由使用 kebab-case：`/api/v1/user-profile`
- 数据库表名使用 snake_case：`user_profiles`
- Python 变量使用 snake_case：`user_profile`

### 文件组织
- 每个 FastAPI router 独立文件：`routers/auth.py`
- 数据库模型集中管理：`models/`
- 工具函数统一存放：`utils/`

### Git 提交规范
- 遵循 Conventional Commits
- feat: 新功能
- fix: Bug 修复
- refactor: 重构
```

---

## 常见问题

### Q1：命令检测不到项目类型怎么办？

**A**：命令基于常见配置文件检测。如果检测失败：

1. 检查是否有包管理文件：
   ```bash
   ls package.json pyproject.toml Cargo.toml go.mod
   ```

2. 如果没有，手动指定项目类型：
   - 编辑生成的 CLAUDE.md
   - 手动填写项目信息

3. 如果有但不常见，提交 issue 让我们添加支持

### Q2：生成的 Profile 不合适怎么办？

**A**：命令根据主要语言推荐 Profile。如果不合适：

1. 查看 QUICKSTART.md 中的 Profile 选择表
2. 手动修改 Profile 引用
3. 参考 EXTENSIONS_GUIDE.md

### Q3：如何确认生成的配置正确？

**A**：运行验证脚本：

```bash
# 验证模板填写
python .claude/scripts/validate_template.py

# 检查模板文件
python .claude/scripts/check_templates.py

# 检查规范合规性
python .claude/scripts/check_compliance.py
```

### Q4：Monorepo 项目如何处理？

**A**：对于 Monorepo 项目：

1. 在根目录运行命令生成主 CLAUDE.md
2. 为每个子项目生成独立的配置
3. 在主 CLAUDE.md 中引用子项目配置

### Q5：多语言项目如何处理？

**A**：对于多语言项目：

1. 命令会识别主要语言
2. 手动添加其他语言的 Profile
3. 在 CLAUDE.md 中说明各语言的用途

---

## 完整示例

### 示例 1：Python FastAPI 项目

**项目结构**：
```
my-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes/
│   ├── models/
│   └── services/
├── tests/
├── pyproject.toml
└── README.md
```

**命令输出**：
```markdown
## ✅ CLAUDE.md 生成完成

### 项目分析结果

- **项目名称**：my-api
- **项目类型**：Web API
- **主要语言**：Python 3.11
- **主要框架**：FastAPI
- **包管理器**：poetry
- **测试框架**：pytest

### 生成的文件

- **文件路径**：CLAUDE.md
- **Profile**：@.claude/profiles/python.md
- **测试 Profile**：@.claude/profiles/testing-python.md

### 下一步操作

1. 检查生成的 CLAUDE.md
2. 填写核心能力范围（第 4️⃣ 节）
3. 填写模块边界与职责（第 7️⃣ 节）
4. 运行验证脚本
```

### 示例 2：TypeScript React 项目

**项目结构**：
```
my-app/
├── src/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   └── utils/
├── public/
├── package.json
├── tsconfig.json
└── vite.config.ts
```

**命令输出**：
```markdown
## ✅ CLAUDE.md 生成完成

### 项目分析结果

- **项目名称**：my-app
- **项目类型**：Web 应用
- **主要语言**：TypeScript 5.0
- **主要框架**：React 18 + Vite
- **包管理器**：pnpm
- **测试框架**：Vitest

### 生成的文件

- **文件路径**：CLAUDE.md
- **Profile**：@.claude/profiles/frontend.md
- **测试 Profile**：@.claude/profiles/testing-common.md

### 下一步操作

1. 检查生成的 CLAUDE.md
2. 填写核心能力范围（第 4️⃣ 节）
3. 填写项目特定约定（第 1️⃣7️⃣ 节）
4. 运行验证脚本
```

---

## 相关文档

- [快速开始指南](QUICKSTART.md)
- [Profile 选择指南](QUICKSTART.md#23-配置-profile-引用)
- [Extension 启用指南](EXTENSIONS_GUIDE.md)
- [命令参考](COMMANDS.md#claude-code-自定义命令)

---

**版本**：v1.0
**最后更新**：2026-01-14
