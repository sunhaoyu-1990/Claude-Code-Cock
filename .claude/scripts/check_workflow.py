#!/usr/bin/env python3
"""
工作流状态检查脚本
检查 Skill Chain 的执行状态和完整性
"""

import sys
import subprocess
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
