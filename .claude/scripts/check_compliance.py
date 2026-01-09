#!/usr/bin/env python3
"""
规范检查脚本
用于验证 Claude 是否正确加载和遵循规范
"""

import sys
from pathlib import Path

def check_compliance(claude_dir: Path) -> tuple[bool, list[str]]:
    """检查规范合规性"""
    issues = []

    # 检查必需文件
    required_files = [
        claude_dir / "constitution.md",
        claude_dir / "BASE_CLAUDE.md",
    ]

    for file in required_files:
        if not file.exists():
            issues.append(f"缺失必需文件: {file.name}")

    # 检查项目配置
    claude_md = claude_dir.parent / "CLAUDE.md"
    if not claude_md.exists():
        issues.append("缺失项目级 CLAUDE.md")

    # 检查 Profile 引用
    if claude_md.exists():
        content = claude_md.read_text()
        if "@.claude/PROFILES/" not in content:
            issues.append("CLAUDE.md 未引用任何 Profile")

    return len(issues) == 0, issues

def main():
    claude_dir = Path(__file__).parent.parent
    is_compliant, issues = check_compliance(claude_dir)

    if is_compliant:
        print("✅ 规范检查通过")
        return 0
    else:
        print("❌ 规范检查失败")
        for issue in issues:
            print(f"  - {issue}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
