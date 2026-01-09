# 🔧 常用命令速查（Command Cheat Sheet）

本文件用于指导 Claude 与开发者在本仓库中执行一致的命令操作。
规则：当需要建议或执行命令时，优先从本文件选择；若缺失则补充并归类。

**多包管理器支持**：Python (uv/pip) + JavaScript (npm/pnpm/yarn) + System (apt/brew/choco)

---

## 目录

- [0) 平台与运行时快速识别](#0-平台与运行时快速识别)
- [1) Python 生态](#1-python-生态)
- [2) JavaScript/TypeScript 生态](#2-javascripttypescript-生态)
- [3) 系统包管理](#3-系统包管理)
- [4) Git 常用命令](#4-git-常用命令)
- [5) 常见排障命令](#5-常见排障命令)
- [6) 命令输出规范](#6-命令输出规范)

---

## 0) 平台与运行时快速识别

### Python 解释器（Windows / PowerShell）
```powershell
# 直接调用指定 Python
powershell -Command "D:\Users\sunha\anaconda3\python.exe -V"
powershell -Command "D:\Users\sunha\anaconda3\python.exe -c ""import sys; print(sys.executable)"""
````

### Python 解释器（Linux / macOS）

```bash
python -V
python3 -V
which python
which python3
```

### uv 环境确认

```bash
uv --version
uv pip --version
uv run python -V
```

---

## 1) Python 生态

> **包管理器**：uv（推荐）/ pip
> **适用项目**：Python 后端服务、脚本、数据处理等

### 1.1 安装与环境

#### 安装项目依赖（推荐）

```bash
# 使用 uv（推荐）
uv pip install -e ".[dev]"

# 使用 pip（传统方式）
pip install -e ".[dev]"
```

#### 锁定与同步（如项目使用 lock）

```bash
# uv 锁文件
uv lock
uv sync

# pip 使用 requirements.txt
pip freeze > requirements.txt
pip install -r requirements.txt
```

#### 快速健康检查

```bash
uv run python -c "import sys; print(sys.version)"
uv run pytest -q
```

---

### 1.2 测试（pytest）

#### 运行全部测试

```bash
uv run pytest
```

### 详细输出 / 快速失败

```bash
uv run pytest -v
uv run pytest -vv
uv run pytest -x          # 第一个失败即停止
uv run pytest --maxfail=1 # 最多失败 1 个
```

### 运行单文件 / 单用例

```bash
uv run pytest tests/unit/test_modules/test_element_removal.py
uv run pytest tests/unit/test_modules/test_element_removal.py::TestElementRemoval::test_process_with_valid_mask
```

### 关键词筛选

```bash
uv run pytest -k "element_removal"
uv run pytest -k "remove and not integration"
```

### 按 marker 运行

```bash
uv run pytest -m unit
uv run pytest -m integration
uv run pytest -m "not slow"
uv run pytest -m "integration or contract"
```

### 输出与调试

```bash
uv run pytest -s                  # 保留 print 输出
uv run pytest --pdb               # 失败进入调试器
uv run pytest -vv -s              # 常用组合
uv run pytest --lf                # 只跑上次失败
uv run pytest --ff                # 先跑上次失败，再跑剩余
```

### 并行测试（需要 pytest-xdist）

```bash
uv run pytest -n auto
```

### 列出可用 markers / fixtures

```bash
uv run pytest --markers
uv run pytest --fixtures
uv run pytest --fixtures-per-test tests/unit/test_modules/test_element_removal.py
```

---

### 1.3 覆盖率（coverage）

#### 终端报告 / HTML 报告

```bash
uv run pytest --cov={项目包名} --cov-report=term-missing
uv run pytest --cov={项目包名} --cov-report=html
```

### XML 报告（CI 常用）

```bash
uv run pytest --cov={项目包名} --cov-report=xml
```

### 打开 HTML 报告

```bash
# macOS
open htmlcov/index.html

# Windows
start htmlcov/index.html

# Linux（视发行版）
xdg-open htmlcov/index.html
```

---

### 1.4 代码质量（格式化 / Lint / 类型）

#### black（格式化）

```bash
black .
black --check .
black --diff .
```

### flake8（静态检查）

```bash
flake8
flake8 src/
```

### mypy（类型检查）

```bash
mypy src/
mypy --show-error-codes src/
```

### 组合式质量门禁（推荐在提交前执行）

```bash
uv run pytest
black --check .
flake8
mypy src/
```

> 建议：如果项目已配置 pre-commit，则以 pre-commit 为准（见下节）

---

### 1.5 pre-commit（若项目启用）

```bash
pre-commit --version
pre-commit install
pre-commit run --all-files
pre-commit run <hook_id> --all-files
```

---

## 2) JavaScript/TypeScript 生态

> **包管理器**：npm / pnpm / yarn
> **适用项目**：React/Vue/Angular 应用、Node.js 服务、前端工具库等

### 2.1 安装与环境

#### 安装项目依赖

```bash
# npm（默认）
npm install

# pnpm（快速，节省磁盘空间）
pnpm install

# yarn（传统）
yarn install
```

#### 安装特定依赖

```bash
# npm
npm install <package>
npm install -D <package>        # 开发依赖
npm install -g <package>        # 全局安装

# pnpm
pnpm add <package>
pnpm add -D <package>
pnpm add -g <package>

# yarn
yarn add <package>
yarn add -D <package>
yarn global add <package>
```

#### 锁文件管理

```bash
# npm 生成 package-lock.json
npm install

# pnpm 生成 pnpm-lock.yaml
pnpm install

# yarn 生成 yarn.lock
yarn install
```

#### 快速健康检查

```bash
# npm
npm run --help
npm test
npm run build

# pnpm
pnpm run --help
pnpm test
pnpm build

# yarn
yarn run --help
yarn test
yarn build
```

---

### 2.2 测试（Jest / Vitest / Mocha）

#### 运行全部测试

```bash
# npm
npm test

# pnpm
pnpm test

# yarn
yarn test
```

#### 详细输出 / 单个测试

```bash
# Jest
npm test -- --verbose
npm test -- path/to/test.test.ts
npm test -- -t "test name"

# Vitest
npm test -- --reporter=verbose
npm test -- path/to/test.test.ts
npm test -- -t "test name"
```

#### Watch 模式（开发时常用）

```bash
npm test -- --watch
pnpm test -- --watch
yarn test --watch
```

---

### 2.3 代码质量

#### ESLint（代码检查）

```bash
# npm
npm run lint
npm run lint:fix

# pnpm
pnpm lint
pnpm lint:fix

# yarn
yarn lint
yarn lint:fix
```

#### Prettier（格式化）

```bash
# npm
npm run format
npm run format:check

# pnpm
pnpm format
pnpm format:check

# yarn
yarn format
yarn format:check
```

#### TypeScript 类型检查

```bash
# npm
npm run type-check

# pnpm
pnpm type-check

# yarn
yarn type-check
```

---

### 2.4 构建与开发

#### 开发服务器

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev
```

#### 生产构建

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build
```

#### 预览构建结果

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview
```

---

## 3) 系统包管理

> **包管理器**：apt (Ubuntu/Debian) / brew (macOS/Linux) / choco (Windows)
> **适用场景**：安装系统级依赖、工具、运行时等

### 3.1 apt (Ubuntu/Debian)

#### 更新包索引

```bash
sudo apt update
```

#### 安装软件包

```bash
sudo apt install <package>
sudo apt install python3 python3-pip nodejs npm
```

#### 搜索包

```bash
apt search <keyword>
apt show <package>
```

#### 升级系统

```bash
sudo apt upgrade
sudo apt full-upgrade
```

#### 清理

```bash
sudo apt autoremove
sudo apt clean
```

---

### 3.2 brew (macOS/Linux)

#### 安装 Homebrew（如未安装）

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 安装软件包

```brew install <package>
brew install python node go
```

#### 搜索包

```bash
brew search <keyword>
brew info <package>
```

#### 更新与升级

```bash
brew update          # 更新 Homebrew 自身
brew upgrade         # 升级所有已安装的包
brew upgrade <package>  # 升级特定包
```

#### 清理

```bash
brew cleanup
brew cleanup --prune=all
```

---

### 3.3 choco (Windows)

#### 安装 Chocolatey（如未安装）

```powershell
# 以管理员身份运行 PowerShell
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

#### 安装软件包

```powershell
choco install <package>
choco install python nodejs git
```

#### 搜索包

```powershell
choco search <keyword>
choco info <package>
```

#### 更新与升级

```powershell
choco upgrade all
choco upgrade <package>
```

#### 列出已安装包

```powershell
choco list
choco list --local-only
```

---

### 3.4 系统包选择指南

| 平台 | 推荐包管理器 | 使用场景 |
|------|-------------|----------|
| Ubuntu/Debian | apt | 系统包、运行时、开发工具 |
| macOS | brew | 开发工具、运行时、GUI 应用 |
| Windows | choco | 开发工具、运行时、系统工具 |
| 跨平台 | scoop (Windows) | 用户空间工具（可选） |

---

## 4) Git 常用命令

> **通用命令**：适用于所有平台和项目类型

### 4.1 基本状态与差异

```bash
git status
git diff
git diff --staged
git log --oneline --decorate -n 20
```

### 4.2 分支

```bash
git branch
git branch -vv
git checkout -b feature/<name>
git switch -c feature/<name>
```

### 4.3 提交与推送

```bash
git add -A
git commit -m "feat: ..."
git push -u origin feature/<name>
```

### 4.4 Rebase / 合并常用（谨慎使用）

```bash
git fetch --all --prune
git rebase origin/<base-branch>
git merge --no-ff feature/<name>
```

---

## 5) 常见排障命令

> **通用命令**：适用于所有平台和项目类型

### 5.1 查看端口占用

#### Windows

```powershell
netstat -ano | findstr :<port>
tasklist | findstr <pid>
```

#### Linux/macOS

```bash
lsof -i :<port>
ss -ltnp | grep <port>
```

### 5.2 查看日志 / 文件

#### Linux/macOS

```bash
tail -n 200 <logfile>
tail -f <logfile>
```

#### Windows PowerShell

```powershell
Get-Content <logfile> -Tail 200
Get-Content <logfile> -Wait
```

### 5.3 搜索（ripgrep 推荐）

```bash
rg "keyword"
rg "keyword" -n
rg "keyword" -S              # 智能大小写
rg "pattern" src/ tests/
rg -g "*.py" "keyword"
```

---

## 6) 命令输出规范

### Claude 必须遵守

当 Claude 建议运行命令时，必须输出：

* **用途**：这条命令用来验证什么
* **预期输出**：成功/失败大致长什么样
* **成功判定**：看到什么算通过
* **最小集合**：默认不超过 3 条命令（除非用户要求完整诊断脚本）

---

## 7) 待项目填充项（必须在项目落地时补齐）

* Python 项目包名（用于 coverage）：`{项目包名}`
* 基础分支名：`{主分支}`
* CLI 名称（如适用）：`{cli_name}`
* 常用配置目录：`{configs_dir}`
