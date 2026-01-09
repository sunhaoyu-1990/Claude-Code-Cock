# 错误模式模板（Error Pattern Template）

**使用说明**：本模板用于定义一类错误问题的通用模式和预防措施，文件保存在 `@.claude/knowledge/patterns/` 目录。

**文件命名格式**：`{模式类别}-{模式名称}.md`
- 模式类别：如 `api`, `async`, `memory`, `type`, `config` 等
- 模式名称：简短描述模式特征

**示例**：`async-context-loss.md`, `type-implicit-any.md`

---

# {模式名称}

## 元数据（Metadata）

| 字段 | 值 |
|------|-----|
| **模式类别** | {api / async / memory / type / config / other} |
| **创建日期** | {YYYY-MM-DD} |
| **更新日期** | {YYYY-MM-DD} |
| **适用语言** | {如 Python / JavaScript / C++ / 通用} |

---

## 模式描述（Pattern Description）

### 定义

{定义这类错误的本质特征}

### 典型场景

{这类错误通常出现在什么场景}

---

## 检测特征（Detection Signs）

### 代码特征

{这类错误在代码中的常见表现}

- 特征 1：{...}
- 特征 2：{...}
- 特征 3：{...}

### 运行时特征

{这类错误在运行时的典型表现}

- 错误信息：{典型错误消息或异常类型}
- 触发条件：{什么操作会触发}
- 失败模式：{如何失败}

---

## 预防性约束（Preventive Constraints）

### 禁止行为（Must Not）

{Claude 在开发时必须避免的行为}

- ❌ {禁止行为 1}
- ❌ {禁止行为 2}
- ❌ {禁止行为 3}

### 强制行为（Must）

{Claude 在开发时必须执行的行为}

- ✅ {强制行为 1}
- ✅ {强制行为 2}
- ✅ {强制行为 3}

### 推荐行为（Should）

{推荐但非强制的最佳实践}

- 💡 {推荐行为 1}
- 💡 {推荐行为 2}

---

## 检查清单（Pre-Commit Checklist）

在提交代码前，Claude 必须检查：

- [ ] {检查项 1}
- [ ] {检查项 2}
- [ ] {检查项 3}
- [ ] {检查项 4}

---

## 代码示例（Code Examples）

### 反模式（Anti-Pattern）

\`\`\`{language}
{展示容易导致此类问题的错误代码}
\`\`\`

**问题**：{说明这段代码的问题}

### 正确模式（Correct Pattern）

\`\`\`{language}
{展示正确的实现方式}
\`\`\`

**优势**：{说明为什么这样更好}

---

## 关联案例（Related Cases）

| 案例编号 | 案例名称 | 严重程度 | 日期 |
|----------|----------|----------|------|
| {编号} | [{案例名称}](@.claude/knowledge/cases/{case_file}.md) | {🔴/🟡/🟢} | {YYYY-MM-DD} |
| {编号} | [{案例名称}](@.claude/knowledge/cases/{case_file}.md) | {🔴/🟡/🟢} | {YYYY-MM-DD} |

---

## 自动化检测建议（Automated Detection）

### 静态分析

{可以通过静态分析工具检测的特征}

- 工具：{如 ESLint / mypy / clang-tidy}
- 规则：{具体的规则或配置}

### 测试策略

{如何通过测试发现此类问题}

- 单元测试：{...}
- 集成测试：{...}
- 回归测试：{...}

---

## 相关规范链接（Related Specifications）

- {宪法或规范中的相关条款}
- {Language Profile 中的相关规则}

---

## 修订历史（Revision History）

| 日期 | 版本 | 变更说明 |
|------|------|----------|
| {YYYY-MM-DD} | 1.0 | 初始版本 |
| {YYYY-MM-DD} | 1.1 | {变更内容} |
