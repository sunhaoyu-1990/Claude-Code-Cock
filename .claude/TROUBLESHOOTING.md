# 故障排除指南（Troubleshooting Guide）

**版本**：v1.0
**适用对象**：Claude Code 用户、项目维护者
**目的**：帮助诊断和解决常见问题

---

## 快速诊断流程

```
遇到问题
    ↓
是否为 Claude 执行问题？
    ├─ 是 → [Claude 执行问题](#claude-执行问题)
    └─ 否 → 是否为配置/环境问题？
        ├─ 是 → [配置/环境问题](#配置环境问题)
        └─ 否 → [其他问题](#其他问题)
```

---

## Claude 执行问题

### 问题 1：Claude 说找不到 constitution.md

**症状**：
```
错误：无法找到 @.claude/constitution.md
```

**可能原因**：
1. CLAUDE.md 中路径引用错误
2. constitution.md 文件不存在
3. 使用了错误的路径分隔符

**解决方案**：
```bash
# 1. 检查文件是否存在
ls .claude/constitution.md

# 2. 检查 CLAUDE.md 中的引用
grep "constitution.md" CLAUDE.md

# 3. 正确的引用格式应该是：
# @.claude/constitution.md  # 使用 / 而非 \
```

**预防**：
- 运行 `python .claude/scripts/check_compliance.py`
- 运行 `python .claude/scripts/check_templates.py`

---

### 问题 2：Claude 不遵循规范

**症状**：
- Claude 跳过了 Complex Mode
- Claude 没有执行错误总结流程
- Claude 违反了宪法条款

**可能原因**：
1. 规范执行门禁未生效
2. BASE_CLAUDE.md 未正确加载
3. 用户明确要求跳过（已记录风险）

**解决方案**：
```bash
# 1. 检查 BASE_CLAUDE.md 是否包含规范执行门禁
head -n 100 .claude/BASE_CLAUDE.md | grep "规范执行门禁"

# 2. 检查 constitution.md 是否包含强制要求
tail -n 50 .claude/constitution.md | grep "规范执行强制要求"

# 3. 重新加载 Claude Code
```

**预防**：
- 确保使用最新版本的框架文件
- 检查 `.claude/BASE_CLAUDE.md` 版本

---

### 问题 3：Skill Chain 执行中断

**症状**：
```
错误：无法执行 /speckit.plan
原因：上游产物不存在
```

**可能原因**：
1. 上游 Skill 未执行
2. Feature 目录不存在
3. 文件命名不正确

**解决方案**：
```bash
# 1. 检查工作流状态
python .claude/scripts/check_workflow.py

# 2. 检查 Feature 目录是否存在
ls specs/<feature_dir>/

# 3. 检查必需的文件
ls specs/<feature_dir>/spec.md
ls specs/<feature_dir>/clarify.md
```

**预防**：
- 按照 Skill Chain 顺序执行
- 使用 `python .claude/scripts/workflow_state.py` 追踪状态

---

### 问题 4：模板文件找不到

**症状**：
```
错误：无法找到模板文件 specs/templates/plan-template.md
```

**可能原因**：
1. 模板文件不存在
2. 路径引用格式错误
3. Windows 路径风格（`\`）不兼容

**解决方案**：
```bash
# 1. 检查模板文件是否存在
ls specs/templates/

# 2. 检查路径引用格式（应使用 /）
# 错误：@specs\templates\plan-template.md
# 正确：specs/templates/plan-template.md

# 3. 运行模板检查
python .claude/scripts/check_templates.py
```

**预防**：
- 遵循模板路径规范（见 TEMPLATE_PATH_CONVENTION.md）
- 定期运行检查脚本

---

## 配置/环境问题

### 问题 5：CLAUDE.md 模板验证失败

**症状**：
```
❌ CLAUDE.md 存在未填写的必填项:
  - 未填写: {项目名称}
  - 未填写: {主要语言}
```

**可能原因**：
1. 复制模板后未填写必填项
2. 占位符未被替换

**解决方案**：
```bash
# 1. 运行验证脚本
python .claude/scripts/validate_template.py

# 2. 编辑 CLAUDE.md，替换所有占位符
# {项目名称} → My Awesome Project
# {主要语言} → Python
# {语言版本} → 3.11
# {主要框架} → FastAPI
# {测试框架} → pytest

# 3. 确保引用了正确的 Profile
# @.claude/PROFILES/python.md
```

**预防**：
- 使用 QUICKSTART.md 作为配置指南
- 配置完成后运行验证脚本

---

### 问题 6：Python 脚本无法运行

**症状**：
```
错误：找不到模块 'pathlib'（Python < 3.4）
语法错误：f-string（Python < 3.6）
```

**可能原因**：
1. Python 版本过低
2. 脚本使用了不兼容的语法

**解决方案**：
```bash
# 1. 检查 Python 版本
python --version
# 需要 Python 3.10+

# 2. 使用正确的 Python
python3 .claude/scripts/check_compliance.py

# 3. 或使用 uv
uv run python .claude/scripts/check_compliance.py
```

**预防**：
- 确保系统 Python 版本 >= 3.10
- 或使用 uv 管理项目 Python 环境

---

### 问题 7：Git 分支相关错误

**症状**：
```
错误：无法检测 Feature 分支
```

**可能原因**：
1. 不在 Git 仓库中
2. 不在 Feature 分支上
3. 分支命名不符合规范

**解决方案**：
```bash
# 1. 检查是否在 Git 仓库中
git status

# 2. 检查当前分支
git branch --show-current

# 3. 分支命名应符合规范：feature/<id>-<name>
git checkout -b feature/001-add-user-login

# 4. 手动指定 Feature 目录
python .claude/scripts/check_workflow.py specs/001-add-user-login
```

**预防**：
- 遵循分支命名规范
- 参考 [分支管理指南](BRANCH_GUIDE.md)

---

## 其他问题

### 问题 8：错误知识库目录不存在

**症状**：
```
错误：.claude/knowledge/cases/ 目录不存在
```

**可能原因**：
1. 目录未创建
2. 使用了旧的路径（specs/error/）

**解决方案**：
```bash
# 1. 创建目录结构
mkdir -p .claude/knowledge/cases
mkdir -p .claude/knowledge/patterns

# 2. 检查路径是否正确
# 旧路径：specs/error/
# 新路径：.claude/knowledge/

# 3. 更新引用
# 查找并替换所有 specs/error/ → .claude/knowledge/
```

**预防**：
- 遵循最新的目录结构规范
- 参考 ERROR_WORKFLOW.md

---

### 问题 9：Profile 不生效

**症状**：
- Claude 没有遵循语言特定的规范
- TypeScript 类型提示被忽略
- Python 类型检查被跳过

**可能原因**：
1. CLAUDE.md 未引用 Profile
2. Profile 路径错误
3. Profile 文件不存在

**解决方案**：
```bash
# 1. 检查 CLAUDE.md 中的 Profile 引用
grep "PROFILES" CLAUDE.md

# 2. 确保路径格式正确
# 正确：@.claude/PROFILES/python.md
# 错误：.claude/profiles/python.md

# 3. 检查 Profile 文件是否存在
ls .claude/PROFILES/

# 4. 可用的 Profile：
# - common.md
# - python.md
# - cpp.md
# - frontend.md
# - testing-*.md
```

**预防**：
- 配置时选择正确的 Profile
- 运行 `python .claude/scripts/check_compliance.py`

---

### 问题 10：权限问题（Linux/macOS）

**症状**：
```
错误：权限被拒绝 (Permission denied)
```

**可能原因**：
1. 脚本没有执行权限
2. 目录权限不正确

**解决方案**：
```bash
# 1. 添加执行权限
chmod +x .claude/scripts/*.py

# 2. 检查目录权限
ls -la .claude/

# 3. 使用 python 运行（替代直接执行）
python .claude/scripts/check_compliance.py
```

**预防**：
- 设置脚本时添加执行权限
- 或直接使用 `python script.py` 运行

---

## 诊断工具

### 自动诊断脚本

运行以下命令进行全面诊断：

```bash
# 完整诊断
python .claude/scripts/check_compliance.py && \
python .claude/scripts/check_templates.py && \
python .claude/scripts/check_workflow.py && \
python .claude/scripts/validate_template.py
```

### 手动检查清单

- [ ] `.claude/constitution.md` 存在
- [ ] `.claude/BASE_CLAUDE.md` 存在
- [ ] `CLAUDE.md` 存在且必填项已填写
- [ ] Profile 引用正确
- [ ] 模板文件存在
- [ ] 错误知识库目录存在
- [ ] Python 版本 >= 3.10
- [ ] 在 Git 仓库中

---

## 获取帮助

### 文档资源

- [快速开始指南](.claude/QUICKSTART.md)
- [完整框架文档](.claude/README.md)
- [模板检查清单](.claude/templates/TEMPLATE_CHECKLIST.md)
- [错误处理工作流](.claude/knowledge/ERROR_WORKFLOW.md)

### 验证脚本

```bash
# 检查规范合规性
python .claude/scripts/check_compliance.py

# 检查模板文件
python .claude/scripts/check_templates.py

# 检查工作流状态
python .claude/scripts/check_workflow.py

# 验证模板填写
python .claude/scripts/validate_template.py
```

---

## 常见错误代码

| 错误信息 | 错误代码 | 解决方案 |
|----------|----------|----------|
| `找不到 constitution.md` | E001 | 检查路径引用，运行 check_compliance.py |
| `模板文件不存在` | E002 | 运行 check_templates.py |
| `必填项未填写` | E003 | 运行 validate_template.py |
| `上游产物不存在` | E004 | 检查工作流状态，按顺序执行 Skills |
| `Profile 未引用` | E005 | 在 CLAUDE.md 中添加 Profile 引用 |
| `Python 版本过低` | E006 | 升级到 Python 3.10+ |

---

**版本**：v1.0
**最后更新**：2026-01-09
