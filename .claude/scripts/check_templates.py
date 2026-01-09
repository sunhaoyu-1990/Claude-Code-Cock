#!/usr/bin/env python3
"""
模板文件检查脚本
检查所有模板文件是否存在并可访问
"""

import sys
from pathlib import Path

# 模板文件列表
REQUIRED_TEMPLATES = {
    "spec-template.md": "specs/templates/spec-template.md",
    "plan-template.md": "specs/templates/plan-template.md",
    "checklist-template.md": "specs/templates/checklist-template.md",
    "tasks-template.md": "specs/templates/tasks-template.md",
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

        # 检查 Windows 路径风格
        if "\\" in content:
            issues.append(f"{skill_dir.name}: 使用 Windows 路径风格 (\\)")

        # 检查是否使用了错误的 @specs 引用
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
