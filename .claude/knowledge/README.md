# 错误知识库使用说明（Claude 指南）

本目录用于沉淀可复用的错误经验。

Claude 在以下情况下必须记录错误：
- 修复 bug
- 引入 workaround
- 用户指出历史问题
- 出现非预期行为

## Claude 操作流程（强制）

1. 判断问题是否属于已有 Pattern
2. 如果是：
   - 新增一个 Case
   - 更新 Pattern 的“关联案例”
3. 如果不是：
   - 创建新的 Case
   - 若具备通用性，创建新的 Pattern
4. 更新 index.md（如有新增 Pattern）

## 写入规则

- Case 写入：.claude/knowledge/cases/
- Pattern 写入：.claude/knowledge/patterns/
- 不允许覆盖历史内容
- 允许在 Pattern 中合并总结

## 输出要求

- 结构必须严格遵循模板
- 语言偏工程化，避免情绪化描述
- 必须包含“改进动作”
