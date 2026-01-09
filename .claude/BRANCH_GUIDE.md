# 分支管理指南（Branch Management Guide）

**版本**：v1.0
**适用对象**：所有使用 Claude Code 的项目
**目的**：建立清晰的 Git 分支规范和工作流程

---

## 分支策略概览

本项目采用 **Feature Branch Workflow** + **Semantic Branch Naming**：

```
main (主分支)
  ├─ feature/001-add-user-login     (功能分支)
  ├─ feature/002-fix-memory-leak    (修复分支)
  ├─ feature/003-refactor-api       (重构分支)
  └─ hotfix/001-critical-bug       (热修复分支)
```

---

## 分支类型与命名规范

### 1. 功能分支（feature/）

**用途**：新功能开发
**命名格式**：`feature/<id>-<short-name>`

**示例**：
```
feature/001-add-user-authentication
feature/002-implement-dashboard
feature/003-add-export-functionality
```

**生命周期**：
1. 从 `main` 分支创建
2. 完整的 Speckit Skill Chain（specify → clarify → plan → checklist → tasks → analyze → implement）
3. 测试验证通过
4. 合并回 `main` 并删除

---

### 2. 修复分支（feature/）

**用途**：bug 修复、问题解决
**命名格式**：`feature/<id>-fix-<short-name>` 或 `feature/<id>-<short-name>`

**示例**：
```
feature/004-fix-login-bug
feature/005-resolve-memory-leak
feature/006-fix-type-error
```

**生命周期**：
1. 从 `main` 分支创建
2. 使用 Simple Mode 或 Complex Mode（根据复杂度）
3. 修复验证和回归测试
4. 合并回 `main` 并删除

---

### 3. 热修复分支（hotfix/）

**用途**：生产环境紧急修复
**命名格式**：`hotfix/<id>-<short-name>`

**示例**：
```
hotfix/001-fix-crash-on-startup
hotfix/002-security-patch
```

**生命周期**：
1. 从 `main` 或生产标签创建
2. 快速修复（可跳过部分 Complex Mode 流程）
3. 紧急测试验证
4. 合并回 `main` 和生产分支

---

### 4. 重构分支（feature/）

**用途**：代码重构、架构调整
**命名格式**：`feature/<id>-refactor-<short-name>`

**示例**：
```
feature/007-refactor-database-layer
feature/008-migrate-to-new-api
```

**生命周期**：
1. 从 `main` 分支创建
2. **必须使用 Complex Mode**
3. 完整的测试覆盖
4. 合并回 `main` 并删除

---

## 分支创建工作流程

### 步骤 1：开始新功能

```bash
# 1. 确保在 main 分支且是最新的
git checkout main
git pull origin main

# 2. 创建新的功能分支
git checkout -b feature/001-add-user-authentication

# 3. 初始化 Speckit 工作流（可选）
python .claude/scripts/workflow_state.py init specs/001-add-user-authentication "Add User Authentication"
```

### 步骤 2：执行 Speckit Skill Chain

使用 Skill 而非命令来执行工作流：

```bash
# 1. 运行 speckit-specify skill
# 在 Claude Code 中输入：
# /skill speckit-specify 添加用户认证功能

# 2. 检查工作流状态
python .claude/scripts/check_workflow.py
# 应显示：spec.md ✅

# 3. 继续后续 skills
# /skill speckit-clarify
# /skill speckit-plan
# /skill speckit-checklist
# /skill speckit-tasks
# /skill speckit-analyze
# /skill speckit-implement
```

**可用的 Speckit Skills**：
- `speckit-specify`：创建功能规格说明
- `speckit-clarify`：澄清需求中的歧义
- `speckit-plan`：创建实施计划
- `speckit-checklist`：生成检查清单
- `speckit-tasks`：创建可执行任务列表
- `speckit-analyze`：跨工件一致性分析
- `speckit-implement`：执行实现

### 步骤 3：提交与推送

```bash
# 1. 提交代码
git add -A
git commit -m "feat: implement user authentication

- Add login endpoint
- Add JWT token validation
- Add user registration

Co-Authored-By: Claude <noreply@anthropic.com>"

# 2. 推送到远程
git push -u origin feature/001-add-user-authentication
```

### 步骤 4：代码审查与合并

```bash
# 1. 创建 Pull Request
# 使用 GitHub CLI 或 Web UI

# 2. 等待审查通过后，合并到 main
# 建议：使用 Squash and Merge 保持历史清洁

# 3. 删除本地和远程分支
git branch -d feature/001-add-user-authentication
git push origin --delete feature/001-add-user-authentication
```

---

## 分支命名规范

### 编号规则

使用递增的三位数字编号：

```
001, 002, 003, ..., 010, 011, ..., 100, 101, ...
```

**获取下一个编号**：
```bash
# 查看现有分支的最大编号
git branch -a | grep -E "feature/[0-9]+" | sort -t/ -k2 -n | tail -1

# 或使用脚本
git branch -a | grep -E "feature/[0-9]+" | sed 's/.*feature\/\([0-9]*\).*/\1/' | sort -n | tail -1
```

### 名称规则

- 使用小写字母
- 使用连字符（`-`）分隔单词
- 简短但描述性强
- 避免使用特殊字符

**好的示例**：
```
feature/001-add-user-login
feature/002-fix-memory-leak
feature/003-refactor-api-layer
```

**不好的示例**：
```
feature/001   # 太简单
feature/001-AddUserLogin  # 大写字母
feature/001/add_user_login # 使用下划线
feature/001-添加用户登录 # 使用中文
```

---

## 与 Speckit Skill Chain 集成

### 目录结构

分支命名应与 Feature 目录对应：

```
分支名：feature/001-add-user-authentication
目录：specs/001-add-user-authentication/
```

### 自动检测

工作流状态检查脚本会自动检测当前分支：

```bash
# 如果在 feature/001-add-user-authentication 分支上
python .claude/scripts/check_workflow.py

# 自动检测 Feature 目录为 specs/001-add-user-authentication
```

### 手动指定

如果自动检测失败，可以手动指定：

```bash
python .claude/scripts/check_workflow.py specs/001-add-user-authentication
```

---

## 分支保护规则

### 主分支（main）保护

建议在 GitHub/GitLab 设置中启用：

- ✅ **要求代码审查**：至少 1 人批准
- ✅ **要求状态检查通过**：CI/CD 必须通过
- ✅ **限制推送权限**：只有管理员可推送
- ❌ **不允许直接推送**

### 功能分支

- 允许强制推送（谨慎使用）
- 不需要代码审查（可选）
- 推送前建议运行：`python .claude/scripts/check_compliance.py`

---

## 常用工作流程

### 功能开发流程（完整 Skill Chain）

```bash
# 1. 创建功能分支
git checkout -b feature/001-add-feature

# 2. 执行完整 Speckit Skill Chain
# 在 Claude Code 中依次调用：
# /skill speckit-specify 添加功能
# /skill speckit-clarify
# /skill speckit-plan
# /skill speckit-checklist
# /skill speckit-tasks
# /skill speckit-analyze
# /skill speckit-implement

# 3. 提交并推送
git add -A
git commit -m "feat: add feature"
git push -u origin feature/001-add-feature

# 4. 创建 PR，审查后合并

# 5. 清理分支
git checkout main
git pull
git branch -d feature/001-add-feature
```

### Bug 修复流程（Simple Mode）

```bash
# 1. 创建修复分支
git checkout -b feature/002-fix-bug

# 2. 直接使用 implement skill（小修复）
# /skill speckit-implement 修复 bug

# 3. 提交并推送
git add -A
git commit -m "fix: resolve bug in..."
git push -u origin feature/002-fix-bug

# 4. 创建 PR，审查后合并

# 5. 清理分支
```

### 热修复流程

```bash
# 1. 从 main 或生产标签创建热修复分支
git checkout main
git pull
git checkout -b hotfix/001-critical-fix

# 2. 快速修复
# 可跳过部分 Skill Chain，但必须：
# - 记录问题
# - 添加测试
# - 验证修复
# /skill speckit-implement 紧急修复

# 3. 提交并推送
git add -A
git commit -m "hotfix: critical fix"
git push -u origin hotfix/001-critical-fix

# 4. 紧急审查并合并

# 5. 清理分支
```

---

## 分支管理最佳实践

### 1. 保持分支小而聚焦

- ✅ 一个分支只做一件事
- ❌ 一个分支混合多个不相关的改动
- ✅ 分支生命周期短（1-3 天）
- ❌ 长期存在的功能分支

### 2. 频繁提交，保持同步

```bash
# 频繁提交小改动
git commit -m "progress: add authentication logic"

# 定期同步 main 分支的变更
git fetch origin main
git rebase origin/main  # 或 git merge origin/main
```

### 3. 清晰的提交信息

遵循 Conventional Commits 规范：

```
feat: add user authentication
fix: resolve memory leak
refactor: simplify API layer
docs: update README
test: add unit tests for auth
chore: update dependencies
```

### 4. 分支清理

```bash
# 删除已合并的本地分支
git branch --merged | grep -v "\*" | xargs git branch -d

# 删除已合并的远程分支
git fetch --prune

# 或使用 GitHub CLI
gh repo prune
```

---

## 故障排除

### 问题：分支命名冲突

**症状**：分支已存在

```bash
# 检查是否已存在
git branch -a | grep feature/001

# 解决方案 1：使用新编号
git checkout -b feature/002-add-feature

# 解决方案 2：删除旧分支（如果未使用）
git branch -D feature/001-add-feature
```

### 问题：rebase 冲突

```bash
# 1. 开始 rebase
git rebase origin/main

# 2. 解决冲突
# 编辑冲突文件，解决标记

# 3. 标记冲突已解决
git add <resolved-file>
git rebase --continue

# 4. 如果需要取消 rebase
git rebase --abort
```

### 问题：大文件合并困难

```bash
# 使用 squash merge 保持历史清洁
# 在 GitHub/GitLab Web UI 中选择 "Squash and merge"

# 或使用命令行
git merge --squash feature/001-add-feature
git commit -m "feat: add feature"
```

---

## 分支与 Feature 目录映射表

| 分支名 | Feature 目录 | Speckit 工作流状态 |
|--------|-------------|-------------------|
| `feature/001-add-auth` | `specs/001-add-auth/` | 追踪此分支 |
| `feature/002-fix-bug` | `specs/002-fix-bug/` | 追踪此分支 |
| `main` | - | 无 |

---

## 自动化脚本

### 创建功能分支脚本

```bash
#!/bin/bash
# create-feature-branch.sh

# 获取下一个编号
NEXT_ID=$(git branch -a | grep -E "feature/[0-9]+" | sed 's/.*feature\/\([0-9]*\).*/\1/' | sort -n | tail -1)
NEXT_ID=$(printf "%03d" $((10#$NEXT_ID + 1)))

# 获取功能名称
FEATURE_NAME=$1

if [ -z "$FEATURE_NAME" ]; then
    echo "用法: ./create-feature-branch.sh <feature-name>"
    exit 1
fi

BRANCH_NAME="feature/${NEXT_ID}-${FEATURE_NAME}"
FEATURE_DIR="specs/${NEXT_ID}-${FEATURE_NAME}"

# 创建分支
git checkout main
git pull
git checkout -b $BRANCH_NAME

# 创建 Feature 目录
mkdir -p $FEATURE_DIR

# 初始化工作流状态
python .claude/scripts/workflow_state.py init $FEATURE_DIR "${FEATURE_NAME}"

echo "✅ 分支创建成功: $BRANCH_NAME"
echo "✅ Feature 目录创建成功: $FEATURE_DIR"
echo "➡️  下一步: 在 Claude Code 中调用 /skill speckit-specify ${FEATURE_NAME}"
```

---

## Skill 调用示例

### 完整功能开发

```bash
# 在 Claude Code 中依次调用以下 skills：

# 1. 创建功能规格
/skill speckit-specify 添加用户认证功能

# 2. 澄清需求（如有歧义）
/skill speckit-clarify

# 3. 创建实施计划
/skill speckit-plan

# 4. 生成检查清单
/skill speckit-checklist

# 5. 创建任务列表
/skill speckit-tasks

# 6. 分析一致性
/skill speckit-analyze

# 7. 执行实现
/skill speckit-implement
```

### 快速 Bug 修复

```bash
# 对于简单修复，可以直接调用 implement skill：

/skill speckit-implement 修复登录页面的验证错误
```

### 使用代码审查 Skill

```bash
# 审查 C++ 代码
/skill c-code-reviewer 审查 src/auth.cpp
```

---

**相关文档**：
- [命令速查](COMMANDS.md)
- [快速开始指南](QUICKSTART.md)
- [故障排除指南](TROUBLESHOOTING.md)
- [Speckit Skills](skills/)

---

**版本**：v1.0
**最后更新**：2026-01-09
