# 变更日志

本项目的所有重要变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### 待发布
- 添加示例项目
- 完善测试覆盖
- 添加 CI/CD 配置

## [1.1.0] - 2026-01-14

### 新增

- **主语言限定**：constitution.md v2.2 新增第 0.1 节
  - 默认使用中文（简体）
  - 支持项目级和会话级覆盖
  - 添加技术术语处理规范
- **语言偏好检查**：BASE_CLAUDE.md v1.1 新增第 1.1.1 节
- **命令更新**：
  - `init-claude-context` 支持语言偏好询问
  - `generate-claude-context` 自动推断语言偏好
- **GitHub 配置**：
  - Issue 模板（Bug 反馈、功能建议、文档改进）
  - PR 模板
  - 贡献指南
  - MIT 许可证

### 变更
- 更新 README.md，添加主语言限定说明
- 更新 CLAUDE-tem.md 模板，添加语言偏好字段

### 文档
- 完善 README.md 结构和内容
- 添加贡献指南（CONTRIBUTING.md）
- 添加变更日志（CHANGELOG.md）

## [1.0.0] - 2026-01-09

### 新增

- **核心规范**：
  - constitution.md v2.1 - 核心宪法
  - BASE_CLAUDE.md v1.0 - 组织级基础规范
- **快速上手**：
  - QUICKSTART.md - 5 分钟配置指南
  - NEW_PROJECT_GUIDE.md - 新项目完整指南
  - EXISTING_PROJECT_GUIDE.md - 现有项目接入指南
- **开发流程**：
  - DEV_GUIDE_SIMPLE.md - 简单开发模式
  - DEVELOPMENT_GUIDE_COMPLEX.md - Speckit 技能链
  - CODE_REVIEW_GUIDE.md - 代码审查流程
  - TEST_GUIDE.md - 测试规范
- **Profile 系统**：
  - common.md - 通用工程规范
  - python.md - Python 项目规范
  - cpp.md - C++ 项目规范
  - frontend.md - 前端项目规范
  - testing-common.md - 通用测试规范
  - testing-python.md - Python 测试规范
  - testing-cpp.md - C++ 测试规范
- **Extension 系统**：
  - architecture-heavy.md - 架构强约束项目
  - ai-workflow-advanced.md - 重型 AI 协作流
  - safety-critical.md - 高风险系统
  - data-pipeline.md - 数据工程专用
- **命令系统**：
  - init-claude-context - 新项目初始化命令
  - generate-claude-context - 现有项目分析命令
- **配置指南**：
  - EXTENSIONS_GUIDE.md - Extension 启用指南
  - BRANCH_GUIDE.md - 分支管理指南
  - COMMANDS.md - 多生态命令速查
- **模板系统**：
  - CLAUDE-tem.md - CLAUDE.md 项目模板
  - error_case_template.md - 错误案例模板
  - error_pattern_template.md - 错误模式模板
- **错误知识库**：
  - knowledge/patterns/ - 错误模式存储
  - knowledge/cases/ - 错误案例存储
  - ERROR_WORKFLOW.md - 错误处理工作流
- **辅助脚本**：
  - PowerShell 脚本（新建功能分支、设置计划、前置检查）

### 特性

- 四层规范体系（宪法 → BASE → Profile → Extension）
- Simple/Complex 双模式开发流程
- Speckit 技能链（7 步完整流程）
- MCU 原则（最小可合并单元）
- 确定性等级标注（已验证/推断/假设）
- 多语言支持（Python、JS/TS、Go、Rust、C/C++）
- 错误知识库自动管理

### 文档

- 完整的 README.md（框架内部说明）
- FRAMEWORK_TODO.md - 待完善事项跟踪

## 版本说明

### 版本号格式

`<主版本>.<次版本>.<修订版本>`

- **主版本**：不兼容的 API 变更
- **次版本**：向后兼容的功能性新增
- **修订版本**：向后兼容的问题修正

### 变更类型

- **新增** - 新增功能
- **变更** - 现有功能的变更
- **弃用** - 即将移除的功能
- **移除** - 已移除的功能
- **修复** - Bug 修复
- **安全** - 安全相关的修复或改进

---

## 链接

- [当前版本](https://github.com/your-username/guide_cc/releases/latest)
- [所有版本](https://github.com/your-username/guide_cc/releases)
- [贡献指南](CONTRIBUTING.md)
