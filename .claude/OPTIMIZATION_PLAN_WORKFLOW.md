# Claude Code 驾驶舱框架 - 流程保证机制补充方案

**版本**：v3.0（流程保证补充）
**日期**：2026-01-09
**补充范围**：流程触发、技能链完整性、错误管理

---

## 执行摘要

基于用户反馈，本方案补充了**6 类关键的流程保证机制**，确保：
1. ✅ 复杂开发流程能自动触发，不能跳过
2. ✅ 错误经验管理流程能自动触发，不能跳过
3. ✅ Skill Chain 能串起来，不会中断
4. ✅ 各 Skill 能找到对应的模板位置
5. ✅ 模板路径统一且跨平台兼容
6. ✅ 流程状态可追踪和恢复

---

## 一、问题诊断

### 1.1 发现的关键问题

| 问题 | 严重性 | 影响 | 位置 |
|------|--------|------|------|
| error 管理目录缺失 | P0 | 错误总结流程无法执行 | `specs/error/` 不存在 |
| Skills 命名错误 | P0 | Skill 调用失败 | `sepckit-*` 应为 `speckit-*` |
| 模板路径不统一 | P1 | 某些 Skill 找不到模板 | Windows 路径 vs Unix 路径 |
| Complex Mode 触发机制不完整 | P0 | 可能跳过复杂流程 | 缺少自动检测和强制触发 |
| Skill Chain 完整性保证缺失 | P0 | 流程可能中断 | 缺少状态检查和恢复 |
| specs/README.md 缺失 | P1 | 引用失效 | 文档引用不存在的文件 |

### 1.2 流程断点分析

```
用户请求功能
    ↓
[断点1] 是否触发 Complex Mode？ ← 缺少自动检测
    ↓
speckit-specify
    ↓
[断点2] 模板文件是否存在？ ← 缺少检查
    ↓
speckit-clarify
    ↓
speckit-plan
    ↓
[断点3] plan-template.md 能否找到？ ← 路径不统一
    ↓
speckit-checklist
    ↓
speckit-tasks
    ↓
[断点4] tasks-template.md 能否找到？ ← 路径不统一
    ↓
speckit-analyze
    ↓
speckit-implement
    ↓
[断点5] 开发过程出错 → 是否触发错误总结？ ← 缺少触发检查
    ↓
错误总结流程
    ↓
[断点6] specs/error/README.md 是否存在？ ← 目录不存在
```

---

## 二、流程保证机制（P0 级别）

### 2.1 Complex Mode 自动触发机制

**问题**：当前需要手动询问用户选择模式，可能被跳过

**解决方案**：在 BASE_CLAUDE.md 中添加自动检测和强制触发

#### 新增到 BASE_CLAUDE.md

```markdown
## 🔍 Complex Mode 自动触发检测（强制）

### 触发条件自动检查

Claude 在收到开发请求时，**必须**先执行以下检查：

#### 检查项 1：公共契约影响
- [ ] 是否影响公共 API？
- [ ] 是否影响 CLI 接口？
- [ ] 是否影响配置 Schema？
- [ ] 是否影响数据协议？
- **若任一为是 → 必须 Complex Mode**

#### 检查项 2：模块范围
- [ ] 是否涉及 ≥ 2 个核心模块？
- [ ] 是否跨层修改（Domain/Application/Infra）？
- **若任一为是 → 必须 Complex Mode**

#### 检查项 3：结构性变更
- [ ] 是否引入新依赖？
- [ ] 是否进行结构性重构？
- [ ] 是否调整目录结构？
- **若任一为是 → 必须 Complex Mode**

#### 检查项 4：风险等级
- [ ] 是否存在性能风险？
- [ ] 是否存在稳定性风险？
- [ ] 是否存在安全风险？
- [ ] 是否影响数据正确性？
- **若任一为是 → 必须 Complex Mode**

#### 检查项 5：工作量评估
- [ ] 预计新增文件 ≥ 5 个？
- [ ] 预计修改文件 ≥ 10 个？
- **若任一为是 → 建议 Complex Mode**

### 强制触发规则

**自动检测结果处理**：

| 检测结果 | 行为 |
|----------|------|
| 无任何触发条件 | 进入 Simple Mode |
| 1-2 个建议条件 | 询问用户，建议 Complex Mode |
| 1 个必须条件 | **强制进入 Complex Mode，说明原因** |
| ≥ 2 个必须条件 | **强制进入 Complex Mode，强烈警告** |

### 无法跳过保证

**以下情况禁止跳过 Complex Mode**：
- ❌ 触及公共契约（API/CLI/Schema/协议）
- ❌ 存在明确安全/性能/稳定性风险
- ❌ 涉及跨 ≥ 3 个模块的修改

**用户明确要求跳过时的处理**：
```markdown
⚠️ **警告：跳过 Complex Mode 的风险**

**检测到的风险**：
- {列出检测到的触发条件}

**可能后果**：
- 需求不完整导致返工
- 架构问题后续难以修复
- 测试覆盖不足导致上线问题
- 技术债务累积

**建议**：
- 选项 A：按 Complex Mode 执行（推荐，约增加 50% 前期时间）
- 选项 B：收缩范围后用 Simple Mode
- 选项 C：确认跳过（需要承担风险）

请选择：A / B / C
```

**若用户选择 C（跳过）**：
- 必须在输出中明确记录："⚠️ 用户选择跳过 Complex Mode，风险已告知"
- 在后续每个关键步骤前提醒风险
```

---

### 2.2 Skill Chain 完整性保证机制

**问题**：没有机制确保 Skill Chain 不会中断

**解决方案**：在每个 Skill 中添加状态检查和恢复机制

#### 2.2.1 在每个 Skill 中添加前置检查

**新增到各 SKILL.md 的"输入"部分**：

```markdown
### 前置条件检查（Pre-condition Check）

在执行本 Skill 前，**必须**验证：

1. **上游 Skill 是否已完成**
   - 检查上游产出的文件是否存在
   - 检查上游产出的文件是否完整

2. **模板文件是否可访问**
   - 检查模板文件路径是否正确
   - 检查模板文件是否可读取

3. **Feature 目录结构是否有效**
   - 检查 Feature 目录是否存在
   - 检查 specs/ 目录结构是否完整

### 检查失败处理

**若前置检查失败**：
```markdown
❌ **无法执行 {Skill Name}**

**失败原因**：{具体原因}

**可能原因**：
- 上游 Skill 未执行或执行失败
- 模板文件缺失或路径错误
- Feature 目录结构不完整

**建议操作**：
1. 检查上游 Skill 是否已完成
2. 运行 `.claude/scripts/check_workflow.py` 诊断
3. 从失败的 Skill 重新开始

需要帮助诊断吗？(yes/no)
```
```

#### 2.2.2 创建工作流状态检查脚本

创建 `.claude/scripts/check_workflow.py`：

```python
#!/usr/bin/env python3
"""
工作流状态检查脚本
检查 Skill Chain 的执行状态和完整性
"""

import sys
from pathlib import Path

def check_workflow_state(feature_dir: Path) -> dict:
    """检查工作流状态"""
    state = {
        "feature_dir": feature_dir,
        "exists": feature_dir.exists(),
        "spec": False,
        "clarify": False,
        "plan": False,
        "checklist": False,
        "tasks": False,
        "analyze": False,
        "issues": []
    }

    if not state["exists"]:
        state["issues"].append("Feature 目录不存在")
        return state

    # 检查各个阶段产物
    spec_file = feature_dir / "spec.md"
    state["spec"] = spec_file.exists()
    if not state["spec"]:
        state["issues"].append("spec.md 不存在 - 需要先运行 /speckit.specify")

    clarify_file = feature_dir / "clarify.md"
    state["clarify"] = clarify_file.exists()

    plan_file = feature_dir / "plan.md"
    state["plan"] = plan_file.exists()
    if not state["plan"]:
        state["issues"].append("plan.md 不存在 - 需要先运行 /speckit.plan")

    checklist_dir = feature_dir / "checklists"
    state["checklist"] = checklist_dir.exists() and any(checklist_dir.iterdir())

    tasks_file = feature_dir / "tasks.md"
    state["tasks"] = tasks_file.exists()
    if not state["tasks"]:
        state["issues"].append("tasks.md 不存在 - 需要先运行 /speckit.tasks")

    analyze_file = feature_dir / "cross_artifact_analysis.md"
    state["analyze"] = analyze_file.exists()

    return state

def detect_current_branch() -> str:
    """检测当前 feature 分支"""
    import subprocess
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True
        )
        branch = result.stdout.strip()
        # 提取 feature 编号和名称
        if "-" in branch:
            parts = branch.split("-", 1)
            if parts[0].isdigit():
                return f"specs/{parts[0]}-{parts[1]}"
        return ""
    except:
        return ""

def main():
    # 自动检测当前分支
    feature_dir_str = detect_current_branch()

    if not feature_dir_str:
        # 如果无法检测，尝试从命令行参数获取
        if len(sys.argv) > 1:
            feature_dir_str = sys.argv[1]
        else:
            print("❌ 无法检测 Feature 分支")
            print("请提供 Feature 目录路径作为参数，或确保在 Feature 分支上")
            return 1

    feature_dir = Path(feature_dir_str)
    state = check_workflow_state(feature_dir)

    print(f"📋 工作流状态检查: {feature_dir}")
    print("=" * 50)

    # 显示状态
    stages = [
        ("spec.md", state["spec"]),
        ("clarify.md", state["clarify"]),
        ("plan.md", state["plan"]),
        ("checklists/", state["checklist"]),
        ("tasks.md", state["tasks"]),
        ("analyze.md", state["analyze"]),
    ]

    for stage, completed in stages:
        status = "✅" if completed else "⬜"
        print(f"{status} {stage}")

    # 显示问题
    if state["issues"]:
        print("\n⚠️ 发现问题:")
        for issue in state["issues"]:
            print(f"  - {issue}")
        print("\n💡 建议操作:")
        if not state["spec"]:
            print("  → 运行: /speckit.specify")
        if state["spec"] and not state["plan"]:
            print("  → 运行: /speckit.plan")
        if state["plan"] and not state["tasks"]:
            print("  → 运行: /speckit.tasks")
        return 1
    else:
        print("\n✅ 工作流状态正常")
        return 0

if __name__ == "__main__":
    sys.exit(main())
```

---

### 2.3 模板路径统一和可访问性保证

**问题**：
1. Windows 路径风格（`\`）在 Unix 上不兼容
2. 模板引用路径不统一
3. 没有模板存在性检查

**解决方案**：

#### 2.3.1 统一模板路径规范

**新增到 `.claude/docs/TEMPLATE_PATH_CONVENTION.md`**：

```markdown
# 模板路径规范

## 模板位置

所有模板统一存放在：`specs/templates/`

## 路径引用规范

### 在 Skill 文件中引用模板

**❌ 错误（Windows 路径）**：
```markdown
- Implementation Plan 模板（@specs\templates\plan-template.md）
```

**❌ 错误（相对路径）**：
```markdown
- Implementation Plan 模板（../templates/plan-template.md）
```

**✅ 正确（跨平台相对路径）**：
```markdown
- Implementation Plan 模板（specs/templates/plan-template.md）
```

**✅ 正确（从项目根目录）**：
```markdown
- Implementation Plan 模板（specs/templates/plan-template.md）
```

## 模板文件列表

| 模板文件 | 用途 | 使用者 |
|---------|------|--------|
| spec-template.md | 功能规格说明 | speckit-specify |
| plan-template.md | 实施计划 | speckit-plan |
| checklist-template.md | 检查清单 | speckit-checklist |
| tasks-template.md | 任务清单 | speckit-tasks |
| agent-file-template.md | Agent 上下文 | speckit-plan |

## 路径解析规则

1. **绝对路径**：从项目根目录开始
2. **相对路径**：从当前文件所在目录开始
3. **@ 引用**：从项目根目录开始（Claude Code 约定）

## 验证脚本

运行：`python .claude/scripts/check_templates.py`

该脚本会：
1. 检查所有模板文件是否存在
2. 检查所有 Skills 中的模板引用是否正确
3. 报告任何缺失或不匹配
```

#### 2.3.2 创建模板检查脚本

创建 `.claude/scripts/check_templates.py`：

```python
#!/usr/bin/env python3
"""
模板文件检查脚本
检查所有模板文件是否存在并可访问
"""

import sys
import re
from pathlib import Path

# 模板文件列表
REQUIRED_TEMPLATES = {
    "spec-template.md": "specs/templates/spec-template.md",
    "plan-template.md": "specs/templates/plan-template.md",
    "checklist-template.md": "specs/templates/checklist-template.md",
    "tasks-template.md": "specs/templates/tasks-template.md",
    "agent-file-template.md": "specs/templates/agent-file-template.md",
}

# Skills 目录
SKILLS_DIR = Path(".claude/skills")

def check_template_existence() -> tuple[bool, list[str]]:
    """检查模板文件是否存在"""
    issues = []

    for template_name, template_path in REQUIRED_TEMPLATES.items():
        path = Path(template_path)
        if not path.exists():
            issues.append(f"模板文件缺失: {template_path}")

    return len(issues) == 0, issues

def check_skill_references() -> tuple[bool, list[str]]:
    """检查 Skills 中的模板引用"""
    issues = []

    if not SKILLS_DIR.exists():
        issues.append("Skills 目录不存在")
        return False, issues

    # 遍历所有 Skills
    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue

        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        content = skill_md.read_text()

        # 检查模板引用
        for template_name, template_path in REQUIRED_TEMPLATES.items():
            # 检查是否引用了该模板
            if template_name in content or template_path in content:
                # 检查路径格式
                if "\\" in template_path and template_path in content:
                    issues.append(f"{skill_dir.name}: 使用 Windows 路径风格")

                # 检查是否使用了 @specs 引用
                if "@specs\\" in content:
                    issues.append(f"{skill_dir.name}: 使用 @specs\\ (应为 specs/templates/)")

    return len(issues) == 0, issues

def main():
    print("🔍 检查模板文件和引用...")
    print("=" * 50)

    # 检查模板文件
    templates_ok, template_issues = check_template_existence()
    if templates_ok:
        print("✅ 所有模板文件存在")
    else:
        print("❌ 模板文件缺失:")
        for issue in template_issues:
            print(f"  - {issue}")

    # 检查引用
    refs_ok, ref_issues = check_skill_references()
    if refs_ok:
        print("✅ 所有 Skills 引用正确")
    else:
        print("❌ Skills 引用问题:")
        for issue in ref_issues:
            print(f"  - {issue}")

    if templates_ok and refs_ok:
        print("\n✅ 模板检查通过")
        return 0
    else:
        print("\n❌ 模板检查失败，请修复上述问题")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

---

### 2.4 错误管理流程触发保证

**问题**：
1. `specs/error/` 目录不存在
2. `specs/error/README.md` 不存在
3. 缺少自动触发机制

**解决方案**：

#### 2.4.1 创建错误管理目录结构

创建 `.claude/scripts/setup_error_workflow.py`：

```python
#!/usr/bin/env python3
"""
错误管理工作流初始化脚本
创建必要的目录结构和文件
"""

import sys
from pathlib import Path

def setup_error_workflow():
    """创建错误管理工作流目录结构"""

    # 创建目录
    dirs = [
        Path("specs/error/cases"),
        Path("specs/error/patterns"),
    ]

    for dir_path in dirs:
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ 创建目录: {dir_path}")

    # 创建 README.md
    error_readme = Path("specs/error/README.md")
    if not error_readme.exists():
        content = """# 错误管理知识库

本目录用于记录和预防开发过程中的错误模式。

## 目录结构

```
specs/
└── error/
    ├── cases/          # 具体错误案例
    │   ├── 001-*.md
    │   └── 002-*.md
    └── patterns/       # 错误模式
        ├── architecture-patterns.md
        ├── api-patterns.md
        └── performance-patterns.md
```

## 触发条件

当以下情况发生时，**必须**执行错误总结流程：
- 开发过程中出现 bug / 异常 / 非预期行为
- 用户明确指出"这里有问题 / 之前这里出过问题"
- 需要 workaround 才能继续推进
- 修复涉及非显而易见原因

## 工作流程

1. **记录错误**：在 `specs/error/cases/` 创建错误记录
2. **识别模式**：判断是否代表一类问题
3. **更新规范**：在 constitution/PROFILE 中添加约束
4. **预防检查**：后续开发优先查询 patterns/

## 模板

- 错误案例模板：`.claude/templates/error_case_template.md`
- 错误模式模板：`.claude/templates/error_pattern_template.md`
"""
        error_readme.write_text(content)
        print(f"✅ 创建文件: {error_readme}")

    print("\n✅ 错误管理工作流初始化完成")
    return 0

if __name__ == "__main__":
    sys.exit(setup_error_workflow())
```

#### 2.4.2 在 BASE_CLAUDE.md 中增强错误触发机制

**更新 BASE_CLAUDE.md 第 10 节**：

```markdown
## 🔟 错误与经验沉淀（不可跳过）

### 触发条件（强制检查）

Claude 在以下情况**必须**主动检查是否需要错误总结：

#### 自动检测触发

**开发过程中出现以下任一情况时**：
1. 代码运行失败或抛出异常
2. 测试失败且需要多次调试
3. 用户报告问题或错误
4. 需要临时方案（workaround）才能继续
5. 发现非预期的行为或结果

#### 触发检查流程

```markdown
🔍 **错误触发检查**

**当前情况**：{描述当前情况}

**检查项**：
- [ ] 是否涉及 bug / 异常？
- [ ] 是否需要 workaround？
- [ ] 根因是否非显而易见？
- [ ] 是否可能再次发生？

**判定**：
- 若 ≥ 2 个为是 → **必须执行错误总结流程**
- 若 1 个为是 → **建议执行错误总结流程**
- 若 0 个为是 → 可跳过

需要执行错误总结吗？(yes/no)
```

### 错误总结流程（强制）

当需要执行错误总结时：

1. **记录错误案例**
   - 使用 `.claude/templates/error_case_template.md`
   - 保存到 `specs/error/cases/{编号}-{错误名称}.md`

2. **识别错误模式**
   - 判断是否代表一类问题
   - 若是：创建/更新 `specs/error/patterns/` 中的模式文件

3. **更新规范（如需要）**
   - 判断是否需要更新 constitution 或 PROFILE
   - 添加预防性约束

4. **验证规范更新**
   - 确保新约束已生效
   - 在后续开发中优先查询

### 错误知识库查询（开发前必做）

在开始任何开发任务前，Claude **必须**：

```bash
# 查询相关错误模式
ls specs/error/patterns/

# 读取相关模式
cat specs/error/patterns/*relevant*
```

**若发现相关 Pattern**：
- **必须**遵循其"预防性约束"
- **不得**重复相同的错误
```

---

### 2.5 Skill Chain 状态追踪和恢复

**问题**：流程中断后无法恢复

**解决方案**：创建状态文件和恢复机制

#### 创建 `.claude/scripts/workflow_state.py`：

```python
#!/usr/bin/env python3
"""
工作流状态管理脚本
追踪和恢复 Skill Chain 执行状态
"""

import json
import sys
from datetime import datetime
from pathlib import Path

STATE_FILE = Path(".workflow_state.json")

def init_state(feature_dir: str, feature_name: str) -> dict:
    """初始化工作流状态"""
    return {
        "feature_dir": feature_dir,
        "feature_name": feature_name,
        "started_at": datetime.now().isoformat(),
        "current_stage": "init",
        "stages": {
            "specify": {"status": "pending", "completed_at": None},
            "clarify": {"status": "pending", "completed_at": None},
            "plan": {"status": "pending", "completed_at": None},
            "checklist": {"status": "pending", "completed_at": None},
            "tasks": {"status": "pending", "completed_at": None},
            "analyze": {"status": "pending", "completed_at": None},
            "implement": {"status": "pending", "completed_at": None},
        }
    }

def save_state(state: dict):
    """保存状态"""
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))

def load_state() -> dict | None:
    """加载状态"""
    if not STATE_FILE.exists():
        return None
    return json.loads(STATE_FILE.read_text())

def update_stage(stage: str, status: str):
    """更新阶段状态"""
    state = load_state()
    if state is None:
        print("❌ 工作流状态不存在")
        return False

    if stage not in state["stages"]:
        print(f"❌ 无效的阶段: {stage}")
        return False

    state["stages"][stage]["status"] = status
    if status == "completed":
        state["stages"][stage]["completed_at"] = datetime.now().isoformat()
    state["current_stage"] = stage

    save_state(state)
    print(f"✅ 更新状态: {stage} → {status}")
    return True

def get_next_stage() -> str | None:
    """获取下一个应执行的阶段"""
    state = load_state()
    if state is None:
        return None

    stages = ["specify", "clarify", "plan", "checklist", "tasks", "analyze", "implement"]

    for stage in stages:
        stage_state = state["stages"][stage]
        if stage_state["status"] == "pending":
            return stage

    return None  # 全部完成

def print_status():
    """打印当前状态"""
    state = load_state()
    if state is None:
        print("❌ 工作流状态不存在")
        return

    print(f"📋 工作流状态: {state['feature_name']}")
    print(f"📁 目录: {state['feature_dir']}")
    print(f"🕐 开始时间: {state['started_at']}")
    print("=" * 50)

    for stage_name, stage_state in state["stages"].items():
        status_icon = {
            "pending": "⬜",
            "in_progress": "🔄",
            "completed": "✅",
            "failed": "❌"
        }.get(stage_state["status"], "❓")
        print(f"{status_icon} {stage_name}: {stage_state['status']}")

    next_stage = get_next_stage()
    if next_stage:
        print(f"\n➡️  下一步: /speckit.{next_stage}")
    else:
        print("\n✅ 所有阶段已完成")

def main():
    if len(sys.argv) < 2:
        print_status()
        return 0

    command = sys.argv[1]

    if command == "init":
        if len(sys.argv) < 4:
            print("用法: python workflow_state.py init <feature_dir> <feature_name>")
            return 1
        state = init_state(sys.argv[2], sys.argv[3])
        save_state(state)
        print("✅ 工作流状态已初始化")
        return 0

    elif command == "update":
        if len(sys.argv) < 4:
            print("用法: python workflow_state.py update <stage> <status>")
            return 1
        return 1 if not update_stage(sys.argv[2], sys.argv[3]) else 0

    elif command == "next":
        next_stage = get_next_stage()
        if next_stage:
            print(f"➡️  下一步: /speckit.{next_stage}")
            return 0
        else:
            print("✅ 所有阶段已完成")
            return 0

    else:
        print(f"❌ 未知命令: {command}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

---

## 三、具体修复任务（按优先级）

### P0-1: 修复 Skills 命名（30 分钟）

**任务**：
```bash
# 重命名文件夹
mv .claude/skills/sepckit-specify .claude/skills/speckit-specify
mv .claude/skills/sepckit-implement .claude/skills/speckit-implement

# 更新所有引用
# 需要检查 commands/ 目录下的引用
```

### P0-2: 创建错误管理目录（30 分钟）

**任务**：
```bash
# 运行初始化脚本
python .claude/scripts/setup_error_workflow.py
```

### P0-3: 统一模板路径引用（1 小时）

**任务**：
1. 更新 `speckit-plan/SKILL.md` 中的路径引用
2. 更新其他 Skills 中的路径引用（如有）
3. 统一为 `specs/templates/` 格式

### P0-4: 添加 Complex Mode 自动触发（2 小时）

**任务**：
1. 在 BASE_CLAUDE.md 中添加触发检测逻辑
2. 创建触发条件检查清单
3. 添加强制触发规则

### P0-5: 添加 Skill Chain 状态检查（2 小时）

**任务**：
1. 创建 `check_workflow.py` 脚本
2. 在每个 Skill 中添加前置检查
3. 添加状态恢复机制

### P0-6: 创建模板检查脚本（1 小时）

**任务**：
1. 创建 `check_templates.py` 脚本
2. 运行检查并修复所有问题

### P0-7: 添加错误触发机制（2 小时）

**任务**：
1. 在 BASE_CLAUDE.md 中添加自动检测
2. 创建触发检查流程
3. 添加错误知识库查询要求

---

## 四、验证和测试

### 4.1 流程完整性测试

**测试场景**：创建一个新功能，走完整个流程

```bash
# 1. 开始新功能
/speckit.specify 添加用户登录

# 2. 检查工作流状态
python .claude/scripts/check_workflow.py

# 3. 继续下一步
/speckit.clarify

# 4. 检查工作流状态
python .claude/scripts/check_workflow.py

# 5. 继续直到完成
/speckit.plan
/speckit.checklist
/speckit.tasks
/speckit.analyze
/speckit.implement
```

### 4.2 恢复机制测试

**测试场景**：中断后恢复

```bash
# 1. 在 plan 阶段中断
# 2. 检查状态
python .claude/scripts/check_workflow.py
# 应该显示：plan 未完成，下一步是 /speckit.plan

# 3. 从中断处恢复
/speckit.plan
```

### 4.3 错误管理测试

**测试场景**：开发过程中出错

```bash
# 1. 模拟开发错误
# 2. Claude 应该自动检测并提示执行错误总结
# 3. 执行错误总结
# 4. 验证错误文件已创建
```

---

## 五、时间估算

| 任务 | 工作量 | 依赖 |
|------|--------|------|
| P0-1: 修复 Skills 命名 | 30 min | - |
| P0-2: 创建错误管理目录 | 30 min | - |
| P0-3: 统一模板路径 | 1 hour | P0-1 |
| P0-4: Complex Mode 触发 | 2 hours | - |
| P0-5: Skill Chain 状态 | 2 hours | - |
| P0-6: 模板检查脚本 | 1 hour | P0-3 |
| P0-7: 错误触发机制 | 2 hours | P0-2 |
| **合计** | **~9 hours** | |

---

## 六、文件清单

### 需要创建的文件

```
.claude/
├── scripts/
│   ├── check_workflow.py       # 工作流状态检查
│   ├── check_templates.py      # 模板文件检查
│   ├── setup_error_workflow.py # 错误管理初始化
│   └── workflow_state.py       # 状态管理
├── docs/
│   └── TEMPLATE_PATH_CONVENTION.md
└── templates/
    ├── error_case_template.md
    └── error_pattern_template.md

specs/
└── error/
    ├── cases/                  # 空目录，脚本会创建
    ├── patterns/               # 空目录，脚本会创建
    └── README.md               # 脚本会创建
```

### 需要修改的文件

```
.claude/
└── BASE_CLAUDE.md              # 添加触发机制和错误管理

.claude/skills/
└── speckit-plan/SKILL.md       # 修正模板路径引用
```

### 需要重命名的文件

```
.claude/skills/
├── sepckit-specify/ → speckit-specify/
└── sepckit-implement/ → speckit-implement/
```

---

## 七、后续行动

1. **立即执行 P0-1 和 P0-2**（1 小时内完成）
2. **执行 P0-3 和 P0-6**（统一路径并验证）
3. **执行 P0-4 和 P0-5**（添加触发和状态机制）
4. **执行 P0-7**（完善错误管理）
5. **端到端测试**（验证整个流程）

---

**方案结束**

*本方案确保流程不会中断，所有触发机制都能正常工作*
