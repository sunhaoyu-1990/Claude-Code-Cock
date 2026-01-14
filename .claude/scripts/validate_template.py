#!/usr/bin/env python3
"""
模板验证脚本
检查 CLAUDE.md 中的占位符是否已填写
"""

import re
import sys
from pathlib import Path

# 必填占位符列表
REQUIRED_PLACEHOLDERS = {
    "CLAUDE.md": [
        r"\{项目名称\}",
        r"\{主要语言\}",
        r"\{语言版本\}",
        r"\{主要框架\}",
        r"\{测试框架\}",
    ]
}

def check_placeholders(file_path: Path, template_name: str) -> tuple[bool, list[str]]:
    """检查文件中的必填占位符"""
    if not file_path.exists():
        return False, [f"文件不存在: {file_path}"]

    content = file_path.read_text()
    missing = []

    patterns = REQUIRED_PLACEHOLDERS.get(template_name, [])
    for pattern in patterns:
        if re.search(pattern, content):
            missing.append(f"未填写: {pattern}")

    return len(missing) == 0, missing

def main():
    # 检查 CLAUDE.md
    claude_md = Path("CLAUDE.md")
    is_valid, issues = check_placeholders(claude_md, "CLAUDE.md")

    if is_valid:
        print("✅ CLAUDE.md 模板验证通过")
    else:
        print("❌ CLAUDE.md 存在未填写的必填项:")
        for issue in issues:
            print(f"  - {issue}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
