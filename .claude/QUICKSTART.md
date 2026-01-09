# Claude Code 驾驶舱快速开始指南

**版本**：v1.0
**适用对象**：新项目配置、现有项目接入
**预计时间**：15-30 分钟

---

## 概述

本指南将帮助你快速设置 Claude Code 驾驶舱框架，为你的项目配置完整的工程规范和开发流程。

**框架提供**：
- 📋 4 层规范体系（宪法 → BASE → CLAUDE → Profile）
- 🔄 Simple/Complex 双模式开发流程
- 🛠️ Speckit 技能链（specify → clarify → plan → checklist → tasks → analyze → implement）
- 📚 错误知识库管理
- ✅ 自动化检查脚本

---

## 步骤 1：复制框架到项目（5 分钟）

### 1.1 新项目

```bash
# 在项目根目录创建 .claude 目录
mkdir -p .claude

# 复制框架核心文件
cp -r /path/to/guide_cc/.claude/* .claude/
```

### 1.2 现有项目

```bash
# 如果已有 .claude 目录，备份配置
cp -r .claude .claude.backup

# 合并框架文件（注意保留现有配置）
cp -r /path/to/guide_cc/.claude/* .claude/
```

---

## 步骤 2：配置项目级 CLAUDE.md（5 分钟）

### 2.1 复制模板

```bash
cp .claude/templates/CLAUDE-tem.md CLAUDE.md
```

### 2.2 填写必填项

编辑 `CLAUDE.md`，替换以下占位符：

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{项目名称}` | 项目名称 | `My Awesome Project` |
| `{主要语言}` | 主要编程语言 | `Python` |
| `{语言版本}` | 语言版本 | `3.11` |
| `{主要框架}` | 主要框架（如有） | `FastAPI` |
| `{测试框架}` | 测试框架 | `pytest` |

### 2.3 配置 Profile 引用

根据项目语言，取消对应的 Profile 注释：

```markdown
@.claude/PROFILES/python.md    # Python 项目
@.claude/PROFILES/cpp.md       # C++ 项目
@.claude/PROFILES/frontend.md  # 前端项目
```

### 2.4 验证配置

```bash
python .claude/scripts/validate_template.py
```

预期输出：
```
✅ CLAUDE.md 模板验证通过
✅ PROJECT_CONTEXT.md 模板验证通过
```

---

## 步骤 3：配置项目上下文（可选，3 分钟）

### 3.1 复制模板

```bash
cp .claude/templates/PROJECT_CONTEXT-tem.md PROJECT_CONTEXT.md
```

### 3.2 填写项目信息

- 项目结构描述
- 关键模块说明
- 构建与测试命令

---

## 步骤 4：验证安装（2 分钟）

### 4.1 运行所有检查

```bash
# 检查模板文件和引用
python .claude/scripts/check_templates.py

# 检查规范合规性
python .claude/scripts/check_compliance.py

# 检查工作流状态
python .claude/scripts/check_workflow.py
```

### 4.2 预期结果

所有脚本应返回 `0` 退出码，显示 ✅ 通过信息。

---

## 步骤 5：开始使用（核心流程）

### 5.1 理解双模式开发

Claude Code 会根据任务复杂度自动选择开发模式：

#### Simple Mode（简单模式）

**适用场景**：
- 单文件修改
- 明确的 bug 修复
- 文档更新
- 配置调整

**流程**：
```
用户请求 → 直接实现 → 测试验证 → 完成
```

#### Complex Mode（复杂模式）

**适用场景**：
- 涉及 ≥ 2 个模块
- 公共 API 变更
- 引入新依赖
- 结构性重构

**流程**：
```
用户请求 → /speckit.specify → /speckit.clarify → /speckit.plan
→ /speckit.checklist → /speckit.tasks → /speckit.analyze → /speckit.implement
```

### 5.2 常用命令

```bash
# 查看命令速查
cat .claude/COMMANDS.md

# 查看工作流状态
python .claude/scripts/workflow_state.py

# 初始化功能工作流
python .claude/scripts/workflow_state.py init <feature_dir> <feature_name>
```

---

## 步骤 6：错误处理流程（按需）

当开发过程中遇到错误时：

### 6.1 错误触发检测

Claude 会自动检查是否需要记录错误：

```markdown
🔍 **错误触发检查**

**当前情况**：{描述当前情况}

**检查项**：
- [ ] 是否涉及 bug / 异常？
- [ ] 是否需要 workaround？
- [ ] 根因是否非显而易见？
- [ ] 是否可能再次发生？
```

### 6.2 创建错误案例

```bash
# 使用模板创建错误案例
cp .claude/templates/error_case_template.md .claude/knowledge/cases/001-error-name.md
```

### 6.3 参考工作流

详细流程请参考：`.claude/knowledge/ERROR_WORKFLOW.md`

---

## 常见问题

### Q1：如何切换语言 Profile？

编辑 `CLAUDE.md`，修改 Profile 引用：

```markdown
# 从 Python 切换到前端
- @.claude/PROFILES/python.md
+ @.claude/PROFILES/frontend.md
```

### Q2：如何自定义规范？

优先级：constitution > BASE > CLAUDE > Profile

- 项目级修改：编辑 `CLAUDE.md`
- 组织级修改：编辑 `.claude/BASE_CLAUDE.md`
- 宪法级修改：编辑 `.claude/constitution.md`

### Q3：如何跳过 Complex Mode？

Claude 会自动检测是否需要 Complex Mode。如果检测到强制触发条件，会警告并提供选项：

```markdown
⚠️ **警告：跳过 Complex Mode 的风险**

**检测到的风险**：
- {列出检测到的触发条件}

**建议**：
- 选项 A：按 Complex Mode 执行（推荐）
- 选项 B：收缩范围后用 Simple Mode
- 选项 C：确认跳过（需要承担风险）

请选择：A / B / C
```

### Q4：模板文件在哪里？

- 项目配置模板：`.claude/templates/`
- 规格说明模板：`specs/templates/`
- 错误处理模板：`.claude/templates/`

---

## 下一步

### 推荐阅读

- 📖 [完整框架文档](.claude/README.md)
- 📋 [命令速查](.claude/COMMANDS.md)
- 🔒 [核心宪法](.claude/constitution.md)
- 🛠️ [BASE 规范](.claude/BASE_CLAUDE.md)

### 示例项目

- 🐍 Python 项目示例：`examples/python/`
- ⚙️ C++ 项目示例：`examples/cpp/`
- 🌐 前端项目示例：`examples/frontend/`

### 进阶配置

- 自定义 Language Profile
- 扩展错误知识库
- 配置自动化脚本

---

## 检查清单

完成以下检查，确保配置正确：

- [ ] `.claude/` 目录已复制到项目
- [ ] `CLAUDE.md` 已创建并填写必填项
- [ ] 正确的 Profile 已引用
- [ ] `validate_template.py` 验证通过
- [ ] `check_templates.py` 验证通过
- [ ] `check_compliance.py` 验证通过
- [ ] 理解 Simple/Complex 双模式
- [ ] 知道如何使用 Speckit 技能链
- [ ] 了解错误处理流程

---

## 获取帮助

- 框架文档：`.claude/README.md`
- 模板检查清单：`.claude/templates/TEMPLATE_CHECKLIST.md`
- 错误处理工作流：`.claude/knowledge/ERROR_WORKFLOW.md`

---

**版本**：v1.0
**最后更新**：2026-01-09
