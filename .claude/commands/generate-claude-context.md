---
description: 分析现有项目并生成项目的 CLAUDE.md 文件
argument-hint: []
model: opus
allowed-tools: Bash, Read, Glob, Grep, Write
---

你现在是一个项目分析专家，你的任务是：

> **分析当前项目的代码内容，并基于模板生成项目的 CLAUDE.md 文件**

请严格按照下面步骤执行，通过工具分析项目并生成配置。

---

## 执行步骤

### 步骤 1：检测项目基本信息

1. 检查是否在 Git 仓库中：
   ```bash
   git status
   ```

2. 获取项目名称（使用目录名或 Git 仓库名）：
   ```bash
   git remote -v | head -1 | sed 's/.*:\(.*\)\.git/\1/' | xargs basename
   # 或使用当前目录名
   basename $(pwd)
   ```

3. 检测项目类型和技术栈：

   检测以下文件的存在性：
   - `package.json` / `package-lock.json` / `yarn.lock` → JavaScript/TypeScript 项目
   - `requirements.txt` / `pyproject.toml` / `setup.py` / `poetry.lock` → Python 项目
   - `Cargo.toml` / `Cargo.lock` → Rust 项目
   - `go.mod` / `go.sum` → Go 项目
   - `pom.xml` / `build.gradle` → Java 项目
   - `composer.json` → PHP 项目
   - `Gemfile` → Ruby 项目
   - `*.csproj` / `*.sln` → C# 项目
   - `CMakeLists.txt` / `Makefile` → C/C++ 项目

---

### 步骤 2：分析项目结构

1. 探索目录结构：
   ```bash
   ls -la
   find . -maxdepth 2 -type d | head -20
   ```

2. 识别关键目录：
   - `src/` 或 `source/` → 源代码目录
   - `tests/` 或 `test/` → 测试目录
   - `docs/` → 文档目录
   - `config/` 或 `.config/` → 配置目录
   - `lib/` → 库目录
   - `dist/` 或 `build/` → 构建输出目录

3. 识别入口文件：
   - JavaScript/TypeScript：`index.js`, `index.ts`, `main.js`, `src/index.ts`
   - Python：`__main__.py`, `main.py`, `app.py`
   - Go：`main.go`, `cmd/*/main.go`
   - Rust：`src/main.rs`

---

### 步骤 3：分析依赖和框架

根据检测到的包管理文件，提取关键信息：

#### Python 项目

从 `pyproject.toml`, `requirements.txt`, `setup.py` 中提取：
- 主要语言：Python
- 语言版本：`python_requires` 或 `.python-version`
- 主要框架：fastapi, django, flask, sqlalchemy, pytest 等
- 包管理器：pip / poetry / uv / conda

#### JavaScript/TypeScript 项目

从 `package.json` 中提取：
- 主要语言：TypeScript / JavaScript
- 语言版本：`engines.node`
- 主要框架：react, vue, angular, express, next.js 等
- 包管理器：npm / pnpm / yarn
- 测试框架：jest, vitest, mocha, jasmine 等

#### 其他语言

类似地分析对应语言的配置文件。

#### 语言偏好推断（新增）

检测项目主要文档和代码的语言：
1. 检查 README.md 的主要语言
2. 抽样检查代码注释的语言
3. 检查文档目录（docs/）的语言

推断规则：
- 中文内容 > 70% → 使用"中文（简体）"
- 英文内容 > 70% → 使用"English"
- 混合内容 → 使用"灵活模式"
- 无法判断 → 使用默认值"中文（简体）"

---

### 步骤 4：分析代码规范

检测以下文件：
- `.eslintrc.*` / `eslint.config.*` → ESLint 规范
- `.prettierrc.*` / `prettier.config.*` → Prettier 规范
- `.pylintrc` / `pyproject.toml` (pylint section) → Pylint 规范
- `.flake8` → Flake8 规范
- `pyproject.toml` (black section) → Black 规范
- `.editorconfig` → 编辑器配置
- `tsconfig.json` → TypeScript 配置

---

### 步骤 5：分析测试配置

检测测试框架和配置：
- Python：`pytest.ini`, `tox.ini`, `pyproject.toml` (pytest section)
- JavaScript：`jest.config.*`, `vitest.config.*`
- 测试目录结构：`tests/`, `test/`, `__tests__/`, `*.test.*`, `*.spec.*`

---

### 步骤 6：分析 CI/CD 配置

检测 CI/CD 配置文件：
- `.github/workflows/*` → GitHub Actions
- `.gitlab-ci.yml` → GitLab CI
- `Jenkinsfile` → Jenkins
- `.travis.yml` → Travis CI
- `azure-pipelines.yml` → Azure Pipelines

---

### 步骤 7：读取模板并生成 CLAUDE.md

1. 读取模板文件：
   ```
   .claude/templates/CLAUDE-tem.md
   ```

2. 基于分析结果，填充模板中的占位符：

   **必填占位符**：
   - `{项目名称}` → 从 Git 仓库名或目录名
   - `{项目类型}` → web 应用 / CLI 工具 / 库 / API 服务 / 桌面应用等
   - `{主要语言}` → Python / TypeScript / JavaScript / Go / Rust 等
   - `{语言版本}` → 3.11 / 18 / 1.21 等
   - `{主要框架}` → FastAPI / React / Vue / Express 等
   - `{测试框架}` → pytest / Jest / Vitest 等
   - `{维护者}` → 从 Git 获取或使用占位符
   - `{last_updated}` → 当前日期

   **可选占位符**（根据项目实际情况填写或删除）：
   - `{runtime_form}` → Web 服务 / CLI 工具 / 桌面应用 / 库
   - `{entrypoint}` → main.py / index.ts / src/index.ts
   - `{style_guide}` → PEP 8 / ESLint + Prettier / Google Style Guide
   - `{架构模式}` → MVC / 分层架构 / 微服务 / 单体应用
   - `{目标平台}` → Web / Linux / Windows / macOS / 跨平台
   - `{包管理器}` → npm / pnpm / yarn / pip / poetry / uv / cargo
   - `{monorepo_or_single_repo}` → monorepo / single repo
   - `{release_model}` → npm / Docker / wheel / binary
   - `{license}` → MIT / Apache 2.0 / GPL / 专有

3. 填充其他章节：

   **第 2️⃣ 节：项目角色设定**
   - 根据主要语言设定角色
   - 添加语言偏好字段：
     ```markdown
     ### 主语言偏好（Language Preference）

     - **默认**：中文（简体）（遵循 constitution.md 第 0.1 节）
     - **项目覆盖**：{language_preference: 默认中文}

     > 推断逻辑：
     > - README.md / 文档主要为中文 → 使用"中文（简体）"
     > - README.md / 文档主要为英文 → 使用"English"
     > - 代码注释主要为中文 → 使用"中文（简体）"
     > - 无法判断 → 使用默认值"中文（简体）"
     ```

   **第 4️⃣ 节：核心能力范围（Project Scope）**
   - 基于项目描述或 README.md 填写

   **第 5️⃣ 节：依赖与能力边界**
   - 列出主要外部依赖
   - 说明项目的能力边界（做什么，不做什么）

   **第 6️⃣ 节：项目结构（Repository Layout）**
   - 基于步骤 2 的分析结果
   - 使用表格或列表形式
   - 说明各目录的用途

   **第 7️⃣ 节：模块边界与职责**
   - 如果项目有明确的模块划分，说明各模块的职责

   **第 8️⃣ 节：语言/框架 Profile**
   - 根据主要语言选择对应的 Profile：
     - Python → `@.claude/profiles/python.md`
     - C++ → `@.claude/profiles/cpp.md`
     - 前端 → `@.claude/profiles/frontend.md`
   - 根据测试框架选择对应的测试 Profile：
     - pytest → `@.claude/profiles/testing-python.md`
     - gtest/catch2 → `@.claude/profiles/testing-cpp.md`
     - Jest/Vitest → `@.claude/profiles/testing-common.md`

   **第 1️⃣4️⃣ 节：运行入口与命令**
   - 列出常用命令：
     - 安装依赖
     - 运行开发服务器
     - 运行测试
     - 构建项目
   - 参考 COMMANDS.md 中的格式

   **第 1️⃣5️⃣ 节：测试与质量门槛**
   - 说明测试要求（覆盖率、测试类型）
   - 说明质量检查工具（linting、格式化、类型检查）

   **第 1️⃣7️⃣ 节：项目特定约定**
   - 说明项目的特殊约定（如果有）
   - 命名规范、文件组织规范等

---

### 步骤 8：选择合适的 Profile 和 Extension

根据项目特点，建议启用以下 Profile 和 Extension：

#### 语言 Profile（必选）

| 主要语言 | Profile 引用 |
|---------|-------------|
| Python | `@.claude/profiles/python.md` |
| C/C++ | `@.claude/profiles/cpp.md` |
| JavaScript/TypeScript | `@.claude/profiles/frontend.md` |
| Go | 使用 `@.claude/profiles/common.md`（暂无 Go 专用 Profile） |

#### 测试 Profile（推荐）

| 测试框架 | Profile 引用 |
|---------|-------------|
| pytest | `@.claude/profiles/testing-python.md` |
| gtest/catch2 | `@.claude/profiles/testing-cpp.md` |
| Jest/Vitest | `@.claude/profiles/testing-common.md` |

#### Extension（按需）

| 项目特征 | 建议启用 |
|---------|---------|
| 大型企业应用、微服务 | `@.claude/extensions/architecture-heavy.md` |
| 医疗、金融、安全攸关 | `@.claude/extensions/safety-critical.md` |
| 大数据处理、ETL | `@.claude/extensions/data-pipeline.md` |

---

### 步骤 9：生成 CLAUDE.md 文件

1. 将生成的内容写入 `CLAUDE.md` 文件

2. 检查生成的配置是否符合项目实际情况

---

### 步骤 10：输出总结报告

向用户输出以下信息：

```markdown
## ✅ CLAUDE.md 生成完成

### 项目分析结果

- **项目名称**：{项目名称}
- **项目类型**：{项目类型}
- **主要语言**：{主要语言} {语言版本}
- **主要框架**：{主要框架}
- **包管理器**：{包管理器}
- **测试框架**：{测试框架}

### 生成的文件

- **文件路径**：CLAUDE.md
- **Profile**：{选择的 Profile}
- **Extension**：{选择的 Extension（如有）}

### 下一步操作

1. 检查生成的 CLAUDE.md 文件
2. 根据项目实际情况调整内容
3. 如需启用 Extension，参考：
   - [Extension 启用指南](.claude/EXTENSIONS_GUIDE.md)

### 自动化检测总结

- 检测到的主要文件：{列表}
- 检测到的目录结构：{列表}
- 检测到的代码规范：{列表}
- 检测到的 CI/CD：{列表}

### 需要手动填写的内容

以下内容需要根据项目实际情况手动填写：

- [ ] 项目核心能力范围（第 4️⃣ 节）
- [ ] 依赖与能力边界（第 5️⃣ 节）
- [ ] 模块边界与职责（第 7️⃣ 节，如有）
- [ ] 项目特定约定（第 1️⃣7️⃣ 节）
- [ ] 其他项目特定内容
```

---

## 注意事项

1. **准确性优先**：基于实际分析结果填充，不要猜测
2. **保守估计**：不确定的内容使用占位符或注释标注
3. **保持模板结构**：不要改变模板的基本结构
4. **可读性**：使用清晰的格式和说明
5. **完整性**：确保所有必填占位符都已填充

---

## 错误处理

如果遇到以下错误，请按说明处理：

### 错误 1：无法检测项目类型

**原因**：未找到常见的包管理文件

**处理**：
- 提示用户手动指定项目类型
- 根据文件扩展名推断语言类型

### 错误 2：模板文件不存在

**原因**：`.claude/templates/CLAUDE-tem.md` 不存在

**处理**：
- 检查框架是否正确安装
- 提示用户先运行框架初始化脚本

### 错误 3：无法写入文件

**原因**：权限不足或文件已存在

**处理**：
- 检查文件权限
- 如果文件已存在，询问用户是否覆盖

---

## 相关文档

- [快速开始指南](.claude/QUICKSTART.md)
- [Profile 选择指南](.claude/QUICKSTART.md#23-配置-profile-引用)
- [Extension 启用指南](.claude/EXTENSIONS_GUIDE.md)
- [模板检查清单](.claude/templates/TEMPLATE_CHECKLIST.md)
