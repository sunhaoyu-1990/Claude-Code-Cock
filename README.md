# Claude Code 规范框架

> 通过配置规范体系，让 Claude Code 按照团队既定方式进行 AI 辅助开发

本项目是一套**纯文档规范框架**，通过分层配置定义 Claude Code 的工作行为，无需任何自动化程序，完全依赖 Claude Code 对规范的理解和执行。

[![Framework Version](https://img.shields.io/badge/framework-v1.1-blue)](.claude/)
[![Constitution](https://img.shields.io/badge/constitution-v2.2-green)](.claude/constitution.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Language](https://img.shields.io/badge/lang-中文--简体-red)](.claude/constitution.md)

---

## 📖 简介

**Claude Code 驾驶舱框架** 是一套完整的 Claude Code 配置规范体系，帮助你建立统一的 AI 辅助开发工作流。通过本框架，你可以：

- ✅ **快速配置** - 2-3 分钟完成新项目或现有项目的驾驶舱配置
- ✅ **规范工作流** - Simple/Complex 双模式开发流程，适配不同规模需求
- ✅ **Speckit 技能链** - 完整的需求→实现闭环工作流
- ✅ **多语言支持** - Python、JavaScript/TypeScript、Go、Rust、C/C++
- ✅ **可扩展架构** - 四层规范体系，灵活适应项目需求
- ✅ **中文优先** - 默认中文环境，符合国内开发习惯

---

## 🚀 快速开始

### 方式一：新项目（从零开始）

```bash
# 1. 将框架克隆到你的项目
git clone https://github.com/sunhaoyu-1990/Claude-Code-Cock.git my-project
cd my-project

# 2. 在 Claude Code 中运行
/init-claude-context --auto        # 自动模式：基于需求文件生成
# 或
/init-claude-context --interactive # 互动模式：逐步引导填写

# 3. 完成！开始使用 Claude Code 辅助开发
```

### 方式二：现有项目（已有代码）

```bash
# 1. 将框架复制到你的项目
cp -r /path/to/guide_cc/.claude /path/to/your-project/

# 2. 在 Claude Code 中运行
/generate-claude-context

# 3. 根据分析结果调整生成的 CLAUDE.md
```

### 方式三：直接复制模板

```bash
# 1. 复制模板
cp .claude/templates/CLAUDE-tem.md <your-project>/CLAUDE.md

# 2. 填写项目信息
# 搜索并替换所有 {...} 占位符

# 3. 选择适用的 Profile
# 编辑 CLAUDE.md，导入对应的 profile
```

---

## 🎯 核心功能

### 1. 分层规范体系

```
Layer 0: constitution.md     ← 最高优先级（不可违反）
Layer 1: BASE_CLAUDE.md      ← 组织级基础规范
Layer 2: PROFILES/*.md       ← 语言/框架工程直觉
Layer 3: EXTENSIONS/*.md     ← 可选重型约束
Layer 4: CLAUDE.md           ← 项目级规范（你的配置）
```

### 2. 双模式开发流程

| 模式 | 适用场景 | 流程 |
|------|---------|------|
| **Simple Mode** | 小功能、Bug 修复、快速迭代 | Light Plan → 开发 → 验证 |
| **Complex Mode** | 公共 API 变更、跨模块修改、结构性重构 | Speckit 技能链（7 步完整流程） |

### 3. Speckit 技能链

```
specify → clarify → plan → checklist → tasks → analyze → implement
  ↓         ↓         ↓          ↓        ↓        ↓        ↓
 需求规格化  需求澄清   技术规划   完整性检查  任务拆解   一致性分析   实施执行
```

### 4. 支持的语言与框架

| 语言 | Profile | 测试框架 |
|------|---------|---------|
| Python | `@.claude/profiles/python.md` | pytest |
| JavaScript/TypeScript | `@.claude/profiles/frontend.md` | Jest, Vitest |
| C/C++ | `@.claude/profiles/cpp.md` | gtest, catch2 |
| Go | `@.claude/profiles/common.md` | testing |
| Rust | `@.claude/profiles/common.md` | built-in |

---

## ✨ 核心亮点

### 1️⃣ 错误知识库 - 让 AI 自动学习避坑

**🎯 使用场景**
- 项目中重复出现相同类型的 Bug
- 新成员总是踩同样的坑
- 团队经验难以传承

**❌ 传统困难**
```
同样的错误重复出现 → 浪费时间排查
老成员离职后经验流失 → 新人重蹈覆辙
错误解决方案散落在聊天记录 → 难以查找
```

**✅ 框架解决方案**
```
错误发生 → 自动检测 → 生成案例 → 识别模式 → 更新规范 → 预防再发生
```

**🚀 如何开启**
```bash
# 无需额外配置，自动工作
# 1. 开发时遇到错误，Claude 自动生成案例
# 2. 存储在 .claude/knowledge/cases/
# 3. 同类错误不再重复出现

# 手动添加错误案例（可选）
cp .claude/templates/error_case_template.md .claude/knowledge/cases/my-error.md
```

**💡 工作原理**
- Claude 遇到错误时按照规范记录案例
- 形成可复用的错误经验库
- 后续遇到类似错误时可参考历史处理方案

---

### 2️⃣ 一键初始化 - 2 分钟搭建项目规范

**🎯 使用场景**
- 新项目启动，不知道如何配置 Claude Code
- 现有项目想接入 AI 辅助开发
- 多个项目需要统一规范

**❌ 传统困难**
```
手动编写 CLAUDE.md → 不知道写什么、写多全
每个项目重复配置 → 浪费 1-2 小时
配置不统一 → AI 行为不一致，效果打折扣
```

**✅ 框架解决方案**
```bash
# 新项目：自动生成完整配置
/init-claude-context --auto        # 30 秒完成
/init-claude-context --interactive # 引导式填写（2-3 分钟）

# 现有项目：智能分析并生成
/generate-claude-context           # 自动分析项目结构
```

**💡 工作原理**
- Claude Code 读取需求文件，智能推断项目配置
- 自动填充模板，大幅减少手动配置时间
- 支持 Python/JS/Go/Rust/C++ 等多种语言检测

---

### 3️⃣ Speckit 技能链 - 完整的需求→实现闭环

**🎯 使用场景**
- 开发大型功能（影响多个模块）
- 需求不明确，容易遗漏场景
- 实现后返工，需求理解偏差

**❌ 传统困难**
```
需求理解不透彻 → 边做边改 → 返工率高
缺少技术规划 → 架构不清晰 → 后期重构成本高
任务拆解粗糙 -> 开发遗漏边界情况 -> 测试不全面
```

**✅ 框架解决方案**
```
7 步完整流程：
specify → clarify → plan → checklist → tasks → analyze → implement
  需求      澄清     规划     检查      任务     分析     实现
```

**🚀 如何使用**
```bash
# 完整流程（大型功能）
/speckit.specify    # 1. 需求规格化
/speckit.clarify    # 2. 需求澄清（如有疑问）
/speckit.plan       # 3. 技术规划
/speckit.checklist  # 4. 完整性检查
/speckit.tasks      # 5. 任务拆解
/speckit.analyze    # 6. 一致性分析
/speckit.implement  # 7. 实施执行

# 小功能可用 Simple Mode（见下一条）
```

**💡 工作原理**
- 每个技能是 Claude Code 的规范定义
- 通过结构化流程帮助减少需求理解偏差
- 完整规划和检查清单有助于降低返工风险

---

### 4️⃣ 双模式开发 - 灵活适配不同需求

**🎯 使用场景**
- 小改动也要走完整流程？太重了！
- 大型功能没有规范？容易混乱！

**❌ 传统困难**
```
所有任务统一流程 → 小改动也被拖慢
大功能没有规范 → 遗漏场景、架构混乱
不知道何时用哪种流程 → 主观判断，标准不一
```

**✅ 框架解决方案**

| 模式 | 触发条件 | 流程 | 耗时 |
|------|---------|------|------|
| **Simple Mode** | ✅ 修改 < 5 个文件<br>✅ Bug 修复<br>✅ 小功能迭代 | Light Plan → 开发 → 验证 | 5-15 分钟 |
| **Complex Mode** | ✅ 修改 ≥ 5 个文件<br>✅ 公共 API 变更<br>✅ 跨模块修改<br>✅ 结构性重构 | Speckit 技能链（7 步） | 30-60 分钟 |

**🚀 如何使用**
```bash
# Claude 自动检测并选择合适的模式
# 你只需正常提出需求，无需手动选择

# 强制指定模式（可选）
"用 Simple Mode 快速修复这个 Bug"
"用 Complex Mode 开发这个支付功能"
```

**💡 工作原理**
- 小改动使用 Simple Mode 快速完成
- 大功能使用 Complex Mode 确保规范
- Claude 根据改动规模自动选择合适模式

---

### 5️⃣ MCU 原则 + 分支管理 - 规范的 Git 工作流

**🎯 使用场景**
- 代码提交混乱，一个 PR 包含多个不相关的改动
- Code Review 困难，改动太大难以审查
- 回滚麻烦，一个提交包含多个功能

**❌ 传统困难**
```
大而全的提交 → Code Review 困难 → 质量难保证
多个功能混在一起 → 难以回滚 → 牵一发而动全身
提交信息不规范 → 不知道改了什么 → Git 历史混乱
```

**✅ 框架解决方案**

**MCU 原则（最小可合并单元）**：
每次提交必须：
- ✅ 逻辑自洽（一个完整的改动）
- ✅ 职责单一（只做一件事）
- ✅ 可测试（能独立验证）
- ✅ 可回滚（出问题能快速回退）

**分支管理**：
```bash
# 创建功能分支
git checkout -b feature/your-feature-name

# 开发完成后合并
/merge-current-branch
```

**💡 工作原理**
- 每次提交职责单一，便于 Code Review
- MCU 原则确保可快速回滚
- 语义化提交信息使 Git 历史清晰可追溯

---

## 📚 文档导航

### 快速上手
- **[快速开始指南](.claude/QUICKSTART.md)** - 5 分钟完成配置
- **[新项目指南](.claude/NEW_PROJECT_GUIDE.md)** - 从零开始项目
- **[现有项目指南](.claude/EXISTING_PROJECT_GUIDE.md)** - 已有代码项目接入

### 核心规范
- **[核心宪法](.claude/constitution.md)** - 最高优先级规范（v2.2）
- **[BASE 规范](.claude/BASE_CLAUDE.md)** - 组织级基础规范（v1.1）
- **[分支管理指南](.claude/BRANCH_GUIDE.md)** - Git 工作流规范

### 开发流程
- **[简单开发模式](.claude/guides/DEV_GUIDE_SIMPLE.md)** - 小功能开发
- **[复杂开发模式](.claude/guides/DEVELOPMENT_GUIDE_COMPLEX.md)** - Speckit 技能链
- **[代码审查流程](.claude/guides/CODE_REVIEW_GUIDE.md)** - 人工审查规范
- **[测试规范](.claude/guides/TEST_GUIDE.md)** - 测试策略与质量门槛

### 配置参考
- **[命令速查](.claude/COMMANDS.md)** - 多生态命令参考
- **[Extension 启用指南](.claude/EXTENSIONS_GUIDE.md)** - 何时启用哪些 Extension
- **[Profile 选择指南](.claude/QUICKSTART.md#23-配置-profile-引用)** - 语言/框架 Profile

---

## 🏗️ 项目结构

```
.claude/
├── constitution.md              # 核心宪法（最高优先级）
├── BASE_CLAUDE.md               # 组织级基础规范
├── QUICKSTART.md                # 快速开始指南
├── NEW_PROJECT_GUIDE.md         # 新项目指南
├── EXISTING_PROJECT_GUIDE.md    # 现有项目指南
├── BRANCH_GUIDE.md              # 分支管理指南
├── COMMANDS.md                  # 命令速查
├── EXTENSIONS_GUIDE.md          # Extension 启用指南
├── FRAMEWORK_TODO.md            # 框架待完善事项
│
├── profiles/                    # 语言/框架 Profile
│   ├── common.md                # 通用工程规范
│   ├── python.md                # Python 项目规范
│   ├── cpp.md                   # C++ 项目规范
│   ├── frontend.md              # 前端项目规范
│   ├── testing-common.md        # 通用测试规范
│   ├── testing-python.md        # Python 测试规范
│   └── testing-cpp.md           # C++ 测试规范
│
├── extensions/                  # 可选重型约束
│   ├── architecture-heavy.md    # 架构强约束项目
│   ├── ai-workflow-advanced.md  # 重型 AI 协作流
│   ├── safety-critical.md       # 高风险系统
│   └── data-pipeline.md         # 数据工程专用
│
├── guides/                      # 开发指南
│   ├── DEV_GUIDE_SIMPLE.md      # 简单开发模式
│   ├── DEVELOPMENT_GUIDE_COMPLEX.md # 复杂开发模式
│   ├── TEST_GUIDE.md            # 测试规范
│   └── CODE_REVIEW_GUIDE.md     # 代码审查流程
│
├── commands/                    # Claude Code 命令
│   ├── init-claude-context.md   # 新项目初始化
│   └── generate-claude-context.md # 现有项目分析
│
├── templates/                   # 文档模板
│   ├── CLAUDE-tem.md            # CLAUDE.md 模板
│   └── error_case_template.md   # 错误案例模板
│
├── knowledge/                   # 错误知识库
│   ├── patterns/                # 错误模式
│   └── cases/                   # 错误案例
```

---

## ⚠️ 重要说明

### 项目定位

本项目是 **Claude Code 的配置规范框架**，通过文档定义引导 Claude Code 的工作行为。

**工作原理**：
```
你定义规范 → Claude Code 读取配置 → Claude 按规范执行
```

### 核心组件说明

| 组件 | 类型 | 说明 |
|------|------|------|
| **Commands** | Claude Code 命令 | `/init-claude-context`、`/generate-claude-context` 等 |
| **Skills** | Claude Code 技能 | Speckit 技能链（7个技能）等 |
| **Profiles** | 语言/框架规范 | Python、C++、Frontend 等 |
| **Extensions** | 可选重型约束 | 架构、安全、数据工程等 |
| **Knowledge** | 错误知识库 | 错误案例和模式管理 |

### 效果说明

**效果取决于**：
- Claude Code 对规范的理解程度
- 规范定义的清晰程度
- 具体任务的复杂度

**不同于传统工具**：
- ❌ 不是自动化脚本或程序
- ❌ 不是独立运行的服务
- ✅ 通过规范文档引导 AI 行为
- ✅ 灵活可扩展，通过定义规范调整行为

---

## 💡 典型使用场景

### 场景 1：开始一个新项目

```bash
# 创建新项目
mkdir my-api && cd my-api
git init

# 复制框架
cp -r /path/to/guide_cc/.claude .

# 创建需求文件
cat > SPEC.md << EOF
# 用户认证 API

## 功能目标
- 用户注册、登录、登出
- JWT Token 认证
- 基于角色的访问控制

## 技术栈
- Python 3.11
- FastAPI
- PostgreSQL
EOF

# 在 Claude Code 中运行
/init-claude-context --auto

# 开始开发
```

### 场景 2：现有项目接入

```bash
# 在你的项目目录
cd /path/to/your-project

# 复制框架
cp -r /path/to/guide_cc/.claude .

# 在 Claude Code 中运行
/generate-claude-context

# 检查生成的 CLAUDE.md
# 根据项目实际情况调整
```

### 场景 3：使用 Speckit 技能链开发新功能

```bash
# 1. 需求规格化
/speckit.specify

# 2. 需求澄清（如有疑问）
/speckit.clarify

# 3. 技术规划
/speckit.plan

# 4. 完整性检查
/speckit.checklist

# 5. 任务拆解
/speckit.tasks

# 6. 一致性分析
/speckit.analyze

# 7. 实施执行
/speckit.implement
```

---

## 🌟 其他特性

### 主语言限定

**默认中文环境，符合国内开发习惯**

- **默认语言**：中文（简体）
- **适用范围**：代码注释、文档、提交信息、错误提示
- **项目覆盖**：国际化项目可在 CLAUDE.md 中声明使用英文
- **优先级**：项目级覆盖 > 宪法默认 > 会话级指定

**技术术语处理**：
- 保留原文：API、HTTP、JSON、RESTful 等
- 中英混用：`RESTful API（Representational State Transfer）`

### 确定性等级标注

**信息可信度一目了然**

| 等级 | 符号 | 说明 | 使用场景 |
|------|------|------|---------|
| 已验证 | ✅ | 已验证、可复现、无歧义 | 已测试的代码、已验证的配置 |
| 推断 | ⚠️ | 基于充分经验或共识 | 最佳实践、常见模式 |
| 假设 | ❓ | 需要验证、试验或澄清 | 未测试的代码、待验证的想法 |

**价值**：快速识别哪些是经过验证的，哪些是基于经验的推断，哪些还需要进一步验证。

---

## 🤝 贡献指南

欢迎贡献！以下是一些贡献方式：

### 报告问题
在 [Issues](https://github.com/sunhaoyu-1990/Claude-Code-Cock/issues) 中报告 bug 或提出新功能建议。

### 提交代码
1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'feat: add some amazing feature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

### 添加新的 Profile 或 Extension
- 新增语言 Profile：在 `.claude/profiles/` 中创建
- 新增 Extension：在 `.claude/extensions/` 中创建
- 更新文档：在相关指南中引用

---

## 📋 待办事项

查看 [FRAMEWORK_TODO.md](.claude/FRAMEWORK_TODO.md) 了解框架的待完善事项。

**当前优先级**：
- P1：secrets 管理、CI/CD 指南
- P2：已完成（Profile 指南、Extension 指南、代码审查指南）
- P3：知识库维护、性能测试、安全审查

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---

## 🔗 相关资源

### 官方资源
- [Claude Code 官方文档](https://docs.anthropic.com/claude-code)
- [Anthropic Claude API](https://docs.anthropic.com/claude/reference)

### 社区
- [GitHub Issues](https://github.com/sunhaoyu-1990/Claude-Code-Cock/issues)
- [GitHub Discussions](https://github.com/sunhaoyu-1990/Claude-Code-Cock/discussions)

### 示例项目
- [examples/python-fastapi](examples/python-fastapi) - Python FastAPI 示例
- [examples/frontend-react](examples/frontend-react) - React 前端示例

---

## 📊 版本信息

| 组件 | 版本 | 最后更新 |
|------|------|---------|
| **框架** | v1.1 | 2026-01-14 |
| **宪法** | v2.2 | 2026-01-14 |
| **BASE 规范** | v1.1 | 2026-01-14 |

---

## ⭐ Star History

如果这个项目对你有帮助，请给个 Star 支持一下！

[![Star History Chart](https://api.star-history.com/svg?repos=sunhaoyu-1990/Claude-Code-Cock&type=Date)](https://star-history.com/#sunhaoyu-1990/Claude-Code-Cock&Date)

---

## 📞 联系方式

- **维护者**：shy
- **邮箱**：your-email@example.com
- **GitHub**：[@sunhaoyu-1990](https://github.com/sunhaoyu-1990)

---

<p align="center">
  <b>让 Claude Code 成为你的得力助手 🚀</b>
</p>

<p align="center">
  <sub>Built with ❤️ by the Claude Code community</sub>
</p>
