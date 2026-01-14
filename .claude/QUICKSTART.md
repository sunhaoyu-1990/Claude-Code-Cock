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
```

---

## 步骤 3：验证安装（2 分钟）

### 3.1 运行所有检查

```bash
# 检查模板文件和引用
python .claude/scripts/check_templates.py

# 检查规范合规性
python .claude/scripts/check_compliance.py

# 检查工作流状态
python .claude/scripts/check_workflow.py
```

### 3.2 预期结果

所有脚本应返回 `0` 退出码，显示 ✅ 通过信息。

---

## 步骤 4：开始使用（核心流程）

### 4.1 理解双模式开发

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

- 项目配置模板：`.claude/templates/CLAUDE-tem.md`
- 规格说明模板：`specs/templates/`
- 错误处理模板：`.claude/templates/`

---

## 故障排除（Troubleshooting）

当配置框架时遇到问题，按以下流程快速诊断：

### 快速诊断流程

```
遇到问题
    ↓
是否为 Claude 执行问题？
    ├─ 是 → Claude 执行问题（见下方）
    └─ 否 → 是否为配置/环境问题？
        ├─ 是 → 配置/环境问题（见下方）
        └─ 否 → 运行完整诊断脚本
```

### Claude 执行问题

#### 问题 1：Claude 说找不到 constitution.md

**症状**：`错误：无法找到 @.claude/constitution.md`

**原因**：路径引用错误、文件不存在、使用了错误的路径分隔符

**解决方案**：
```bash
# 检查文件是否存在
ls .claude/constitution.md

# 检查 CLAUDE.md 中的引用
grep "constitution.md" CLAUDE.md

# 正确的引用格式：@.claude/constitution.md（使用 / 而非 \）
```

**错误代码**：E001

---

#### 问题 2：Claude 不遵循规范

**症状**：Claude 跳过了 Complex Mode、没有执行错误总结流程、违反了宪法条款

**原因**：规范执行门禁未生效、BASE_CLAUDE.md 未正确加载

**解决方案**：
```bash
# 检查 BASE_CLAUDE.md 是否包含规范执行门禁
head -n 100 .claude/BASE_CLAUDE.md | grep "规范执行门禁"

# 检查 constitution.md 是否包含强制要求
tail -n 50 .claude/constitution.md | grep "规范执行强制要求"

# 重新加载 Claude Code
```

---

#### 问题 3：Skill Chain 执行中断

**症状**：`错误：无法执行 /speckit.plan，原因：上游产物不存在`

**原因**：上游 Skill 未执行、Feature 目录不存在、文件命名不正确

**解决方案**：
```bash
# 检查工作流状态
python .claude/scripts/check_workflow.py

# 检查 Feature 目录和必需文件
ls specs/<feature_dir>/
ls specs/<feature_dir>/spec.md
ls specs/<feature_dir>/clarify.md
```

**错误代码**：E004

---

#### 问题 4：模板文件找不到

**症状**：`错误：无法找到模板文件 specs/templates/plan-template.md`

**原因**：模板文件不存在、路径引用格式错误、Windows 路径风格（`\`）不兼容

**解决方案**：
```bash
# 检查模板文件是否存在
ls specs/templates/

# 正确引用格式：specs/templates/plan-template.md（使用 /）
# 错误格式：@specs\templates\plan-template.md

# 运行模板检查
python .claude/scripts/check_templates.py
```

**错误代码**：E002

---

### 配置/环境问题

#### 问题 5：CLAUDE.md 模板验证失败

**症状**：
```
❌ CLAUDE.md 存在未填写的必填项:
  - 未填写: {项目名称}
  - 未填写: {主要语言}
```

**原因**：复制模板后未填写必填项、占位符未被替换

**解决方案**：
```bash
# 运行验证脚本
python .claude/scripts/validate_template.py

# 编辑 CLAUDE.md，替换所有占位符
# {项目名称} → My Awesome Project
# {主要语言} → Python
# {语言版本} → 3.11
# {主要框架} → FastAPI
# {测试框架} → pytest
```

**错误代码**：E003

---

#### 问题 6：Python 脚本无法运行

**症状**：`错误：找不到模块 'pathlib'` 或 `语法错误：f-string`

**原因**：Python 版本过低（需要 Python 3.10+）

**解决方案**：
```bash
# 检查 Python 版本
python --version

# 使用 uv 管理 Python 环境
uv run python .claude/scripts/check_compliance.py
```

**错误代码**：E006

---

#### 问题 7：Profile 不生效

**症状**：Claude 没有遵循语言特定的规范（如类型检查被忽略）

**原因**：CLAUDE.md 未引用 Profile、Profile 路径错误、Profile 文件不存在

**解决方案**：
```bash
# 检查 Profile 引用
grep "PROFILES" CLAUDE.md

# 正确格式：@.claude/PROFILES/python.md
# 错误格式：.claude/profiles/python.md

# 检查可用的 Profile
ls .claude/PROFILES/
```

**错误代码**：E005

---

### 完整诊断脚本

当遇到问题时，首先运行完整诊断：

```bash
# 运行所有检查脚本
python .claude/scripts/check_compliance.py && \
python .claude/scripts/check_templates.py && \
python .claude/scripts/check_workflow.py && \
python .claude/scripts/validate_template.py
```

### 手动检查清单

- [ ] `.claude/constitution.md` 存在
- [ ] `.claude/BASE_CLAUDE.md` 存在
- [ ] `CLAUDE.md` 存在且必填项已填写
- [ ] Profile 引用正确（`@.claude/PROFILES/*.md`）
- [ ] 模板文件存在
- [ ] Python 版本 >= 3.10
- [ ] 在 Git 仓库中

### 错误代码速查表

| 错误代码 | 错误信息 | 解决方案 |
|----------|----------|----------|
| E001 | 找不到 constitution.md | 检查路径引用，运行 check_compliance.py |
| E002 | 模板文件不存在 | 运行 check_templates.py |
| E003 | 必填项未填写 | 运行 validate_template.py |
| E004 | 上游产物不存在 | 检查工作流状态，按顺序执行 Skills |
| E005 | Profile 未引用 | 在 CLAUDE.md 中添加 Profile 引用 |
| E006 | Python 版本过低 | 升级到 Python 3.10+ |

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
