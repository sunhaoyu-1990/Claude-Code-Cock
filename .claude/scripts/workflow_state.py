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
