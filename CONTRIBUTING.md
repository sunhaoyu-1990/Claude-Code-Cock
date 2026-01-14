# 贡献指南

感谢你有兴趣为 Claude Code 驾驶舱框架做出贡献！

## 🤝 如何贡献

### 报告 Bug

如果你发现了 bug，请：

1. 检查 [Issues](https://github.com/your-username/guide_cc/issues) 中是否已有相同问题
2. 如果没有，创建新的 Issue，使用 **Bug 反馈** 模板
3. 提供详细的信息：
   - 复现步骤
   - 预期行为 vs 实际行为
   - 环境信息
   - 错误日志

### 提出新功能

1. 先检查是否已有类似的功能建议
2. 使用 **功能建议** 模板创建 Issue
3. 说明功能的使用场景和预期效果
4. 讨论实现方案后再开始开发

### 改进文档

1. 使用 **文档改进** 模板创建 Issue
2. 说明需要改进的文档位置
3. 提供改进建议或具体内容

## 🛠️ 开发流程

### 准备工作

1. **Fork 仓库**
   ```bash
   # 在 GitHub 上点击 Fork 按钮
   ```

2. **克隆到本地**
   ```bash
   git clone https://github.com/your-username/guide_cc.git
   cd guide_cc
   ```

3. **添加上游仓库**
   ```bash
   git remote add upstream https://github.com/original-owner/guide_cc.git
   ```

4. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   ```

### 分支命名规范

遵循以下分支命名规范：

| 类型 | 前缀 | 示例 |
|------|------|------|
| 新功能 | `feature/` | `feature/add-rust-profile` |
| Bug 修复 | `fix/` | `fix/typo-in-constitution` |
| 文档更新 | `docs/` | `docs/update-readme` |
| 重构 | `refactor/` | `refactor/profiles-structure` |
| 测试 | `test/` | `test/add-validation-tests` |
| 性能优化 | `perf/` | `perf/optimize-loading` |

### 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<类型>(<范围>): <简短描述>

<详细描述>

<关闭的 Issue>
```

**类型**：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建/工具相关

**示例**：
```
feat(profiles): add Rust language profile

- 添加 Rust 专用 Profile
- 包含 Cargo 工作流规范
- 添加测试策略说明

Closes #42
```

### 开发建议

1. **保持提交原子性**
   - 每个提交只做一件事
   - 遵循 MCU 原则（最小可合并单元）

2. **编写清晰的提交信息**
   - 简短描述不超过 50 字符
   - 详细描述说明"为什么"而不是"做了什么"

3. **及时同步上游**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

4. **本地测试**
   - 确保修改不会破坏现有功能
   - 测试新生成的配置文件

## 📝 提交 Pull Request

### PR 标题格式

使用与提交信息相同的格式：

```
[类型] 简短描述
```

**示例**：
- `[feat] 添加 Go 语言 Profile`
- `[fix] 修正 QUICKSTART.md 中的错误链接`
- `[docs] 更新贡献指南`

### PR 描述

使用项目提供的 PR 模板，包含：

1. **变更描述** - 清晰说明做了什么
2. **变更类型** - 选择合适的类型
3. **影响范围** - 列出受影响的文件
4. **测试情况** - 说明如何测试
5. **检查清单** - 确保所有项都已完成
6. **相关 Issue** - 关联的 Issue 编号

### PR 审查流程

1. **自动检查**
   - CI/CD 自动运行（如果配置）
   - 检查代码格式和规范

2. **人工审查**
   - 维护者会审查代码
   - 提出修改建议
   - 确认后合并

3. **修改反馈**
   - 根据反馈修改代码
   - 在 PR 中回复说明
   - 标记为"已修改"

## 🏗️ 项目结构

了解项目结构有助于你做出更好的贡献：

```
guide_cc/
├── .claude/                 # 核心框架
│   ├── constitution.md      # 宪法（最高优先级）
│   ├── BASE_CLAUDE.md       # 基础规范
│   ├── profiles/            # 语言/框架 Profile
│   ├── extensions/          # 可选扩展
│   ├── guides/              # 开发指南
│   ├── commands/            # Claude Code 命令
│   ├── templates/           # 文档模板
│   └── knowledge/           # 错误知识库
├── .github/                 # GitHub 配置
│   ├── ISSUE_TEMPLATE/      # Issue 模板
│   └── pull_request_template.md
├── examples/                # 示例项目
├── specs/                   # 功能规格
├── README.md                # 项目说明
├── LICENSE                  # MIT 许可证
└── CONTRIBUTING.md          # 本文件
```

## ✅ 代码规范

### Markdown 文件规范

- 使用中文标点（中文内容）
- 代码块标注语言
- 标题层级清晰
- 列表对齐整齐
- 链接使用相对路径

### 配置文件规范

- 遵循宪法原则
- 保持与 BASE_CLAUDE.md 一致
- 使用确定性等级标注
- 清晰的职责边界

## 🎯 贡献方向

我们欢迎以下类型的贡献：

### 高优先级

- **新语言 Profile**：Go、Rust、Java 等
- **新 Extension**：特定场景的扩展
- **示例项目**：完整的使用示例
- **测试用例**：验证框架功能

### 中优先级

- **文档改进**：更清晰的说明
- **Bug 修复**：修复已知问题
- **性能优化**：提升加载效率

### 低优先级

- **UI 改进**：更好的排版
- **翻译**：英文版文档
- **工具集成**：与其他工具的集成

## 📜 行为准则

### 我们的承诺

为了营造开放和友好的环境，我们承诺：

- 尊重不同的观点和经验
- 优雅地接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

### 不可接受的行为

- 使用性化的语言或图像
- 人身攻击或政治攻击
- 公开或私下骚扰
- 未经许可发布他人私人信息
- 其他在专业场合可能被认为不合适的行为

## 📧 联系方式

如有任何问题，请通过以下方式联系：

- **GitHub Issues**: [提交问题](https://github.com/your-username/guide_cc/issues)
- **GitHub Discussions**: [参与讨论](https://github.com/your-username/guide_cc/discussions)
- **Email**: your-email@example.com

## 🙏 致谢

感谢所有为本项目做出贡献的开发者！

---

<p align="center">
  <sub>再次感谢你的贡献！🎉</sub>
</p>
