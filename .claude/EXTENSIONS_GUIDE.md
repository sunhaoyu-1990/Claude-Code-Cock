# Extension 启用指南（Extension Usage Guide）

**版本**：v1.0
**适用对象**：需要额外约束的项目
**目的**：说明何时启用哪些 Extension，以及如何集成到项目

---

## 概述

Extension 是框架的可选重型约束模块，用于特定类型的项目。

**与 Profile 的区别**：
- **Profile**：语言/框架的基础规范（必选）
- **Extension**：特定场景的额外约束（可选）

**启用方式**：在项目级 `CLAUDE.md` 中引用

---

## 可用 Extension

### 1. architecture-heavy.md（架构强约束）

**用途**：架构强约束项目，需要严格的架构分层和依赖管理。

**适用项目**：
- 大型企业应用
- 微服务架构
- 需要长期演进的项目
- 多团队协作项目

**约束内容**：
- 严格的分层架构（Domain/Application/Infrastructure）
- 禁止跨层依赖
- 依赖方向控制
- 模块化边界

**启用方式**：

```markdown
# 在 CLAUDE.md 中添加

@.claude/EXTENSIONS/architecture-heavy.md
```

**检查清单**：
- [ ] 项目是否需要严格的分层架构？
- [ ] 是否有多个模块/服务？
- [ ] 是否需要长期演进（≥ 1 年）？
- [ ] 是否有多团队协作？

**示例项目**：
- 电商系统（订单、库存、支付分离）
- SaaS 平台（多租户、多服务）
- 企业 ERP 系统

---

### 2. ai-workflow-advanced.md（重型 AI 协作流）

**用途**：深度集成 AI 辅助开发的高级工作流。

**适用项目**：
- 高度依赖 AI 辅助开发的项目
- 需要 AI 代码审查的项目
- 需要 AI 生成测试的项目
- AI Agent 参与的开发流程

**约束内容**：
- AI 代码审查强制要求
- AI 测试生成覆盖率要求
- AI 辅助重构流程
- AI Agent 协作规范

**启用方式**：

```markdown
# 在 CLAUDE.md 中添加

@.claude/EXTENSIONS/ai-workflow-advanced.md
```

**检查清单**：
- [ ] 项目是否大量使用 AI 辅助开发？
- [ ] 是否需要 AI 代码审查？
- [ ] 是否有 AI Agent 参与开发？
- [ ] 团队是否熟悉 AI 工具链？

**示例项目**：
- 快速原型开发项目
- AI 辅助的遗留系统重构
- 自动化测试生成项目

---

### 3. safety-critical.md（高风险系统）

**用途**：安全攸关系统的额外约束。

**适用项目**：
- 医疗设备软件
- 金融交易系统
- 航空/汽车控制软件
- 任何涉及人身安全的系统

**约束内容**：
- 强制安全审查
- 故障模式分析（FMEA）
- 冗余和容错要求
- 安全认证要求

**启用方式**：

```markdown
# 在 CLAUDE.md 中添加

@.claude/EXTENSIONS/safety-critical.md
```

**检查清单**：
- [ ] 系统故障是否会导致人身伤害？
- [ ] 是否有安全认证要求？
- [ ] 是否需要故障容错？
- [ ] 是否有监管合规要求？

**示例项目**：
- 医疗影像诊断系统
- 自动驾驶控制模块
- 金融高频交易系统

---

### 4. data-pipeline.md（数据工程专用）

**用途**：数据管道和数据工程的专用约束。

**适用项目**：
- ETL/ELT 数据管道
- 数据仓库项目
- 实时数据处理
- 大数据处理项目

**约束内容**：
- 数据质量标准
- 数据血缘追踪
- 数据版本管理
- 数据安全与隐私

**启用方式**：

```markdown
# 在 CLAUDE.md 中添加

@.claude/EXTENSIONS/data-pipeline.md
```

**检查清单**：
- [ ] 项目是否涉及大量数据处理？
- [ ] 是否需要数据质量保证？
- [ ] 是否需要数据血缘追踪？
- [ ] 是否有数据隐私要求？

**示例项目**：
- 日志分析系统
- 用户行为分析平台
- 实时推荐系统

---

## Extension 启用决策树

```
项目是否需要额外约束？
    ↓
是否为大型企业应用或多服务架构？
    ├─ 是 → 启用 architecture-heavy.md
    └─ 否 → 是否为安全攸关系统？
        ├─ 是 → 启用 safety-critical.md
        └─ 否 → 是否为数据工程项目？
            ├─ 是 → 启用 data-pipeline.md
            └─ 否 → 是否重度使用 AI 开发？
                ├─ 是 → 启用 ai-workflow-advanced.md
                └─ 否 → 不需要 Extension
```

## Extension 组合

某些项目可能需要多个 Extension：

| 组合 | 适用场景 |
|------|---------|
| `architecture-heavy` + `data-pipeline` | 大型数据分析平台 |
| `safety-critical` + `architecture-heavy` | 安全攸关的企业系统 |
| `ai-workflow-advanced` + `data-pipeline` | AI 驱动的数据处理项目 |

**注意**：Extension 越多，约束越严格，开发效率可能降低。请按需启用。

---

## Extension 与 CLAUDE.md 的集成

### 完整示例

```markdown
# {项目名称} 项目级规范

## 1️⃣ 组织级规范导入（不可删除）

@.claude/BASE_CLAUDE.md
@.claude/constitution.md

## 2️⃣ 语言/框架 Profile

@.claude/PROFILES/common.md
@.claude/PROFILES/python.md
@.claude/PROFILES/testing-python.md

## 3️⃣ Extension（按需启用）

@.claude/EXTENSIONS/architecture-heavy.md
@.claude/EXTENSIONS/data-pipeline.md

## 4️⃣ 项目特定内容...
```

### 启用顺序

建议按以下顺序引用：
1. constitution.md
2. BASE_CLAUDE.md
3. Profile（common + 语言/框架 + 测试）
4. Extension（按需）

---

## Extension 验证

启用 Extension 后，检查配置：

- 确认 Extension 引用路径正确
- 验证 Extension 文件存在
- 检查 CLAUDE.md 中的引用格式

---

## 常见问题

### Q1：可以创建自定义 Extension 吗？

**A**：可以。在 `.claude/EXTENSIONS/` 目录下创建新的 `.md` 文件，并在项目中引用。

### Q2：Extension 会覆盖 Profile 规则吗？

**A**：不会。Extension 是补充约束，与 Profile 共同生效。冲突时按决策优先级裁决（constitution > BASE > Extension > Profile）。

### Q3：如何判断项目是否需要 Extension？

**A**：参考各 Extension 的检查清单。如果 ≥ 2 项为"是"，建议启用。

### Q4：可以中途启用/禁用 Extension 吗？

**A**：可以。在 `CLAUDE.md` 中添加/删除 Extension 引用即可。建议在项目初期决定，避免中途变更导致的不一致。

---

## 相关文档

- [Profile 选择指南](QUICKSTART.md#23-配置-profile-引用)
- [BASE_CLAUDE.md](BASE_CLAUDE.md)
- [constitution.md](constitution.md)

---

**版本**：v1.0
**最后更新**：2026-01-14
