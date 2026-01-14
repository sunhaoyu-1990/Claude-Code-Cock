# Claude Code 驾驶舱框架

> 为你的项目快速搭建 Claude Code AI 辅助开发规范与工作流

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
git clone https://github.com/your-username/guide_cc.git my-project
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
│
└── scripts/                     # 辅助脚本
    └── powershell/              # PowerShell 脚本
```

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

## 🌟 核心特性

### 主语言限定

- **默认语言**：中文（简体）
- **适用范围**：代码注释、文档、提交信息、错误提示
- **项目覆盖**：可在 CLAUDE.md 中声明使用英文
- **优先级**：项目级覆盖 > 宪法默认 > 会话级指定

### MCU 原则（最小可合并单元）

每次变更必须：
- 逻辑自洽
- 职责单一
- 可测试
- 可回滚

### 确定性等级标注

- ✅ **【已验证】** - 已验证、可复现、无歧义
- ⚠️ **【推断】** - 基于充分经验或共识
- ❓ **【假设】** - 需要验证、试验或进一步澄清

### 错误知识库

- 自动检测开发过程中的错误
- 生成错误案例文档
- 识别错误模式
- 更新规范预防同类错误

---

## 🤝 贡献指南

欢迎贡献！以下是一些贡献方式：

### 报告问题
在 [Issues](https://github.com/your-username/guide_cc/issues) 中报告 bug 或提出新功能建议。

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
- [GitHub Issues](https://github.com/your-username/guide_cc/issues)
- [GitHub Discussions](https://github.com/your-username/guide_cc/discussions)

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

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/guide_cc&type=Date)](https://star-history.com/#your-username/guide_cc&Date)

---

## 📞 联系方式

- **维护者**：shy
- **邮箱**：your-email@example.com
- **GitHub**：[@your-username](https://github.com/your-username)

---

<p align="center">
  <b>让 Claude Code 成为你的得力助手 🚀</b>
</p>

<p align="center">
  <sub>Built with ❤️ by the Claude Code community</sub>
</p>
