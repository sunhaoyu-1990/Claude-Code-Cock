# 错误知识库（Error Knowledge Base）

## 🚨 快速入口

**当用户说"总结到知识库"时，立即执行：**

```bash
# 1. 读取工作流文件
Read @.claude/knowledge/ERROR_WORKFLOW.md

# 2. 查询现有 Pattern
ls @.claude/knowledge/patterns/

# 3. 按工作流程创建 Case/Pattern
```

---

## 目录结构

```
.claude/knowledge/
├── ERROR_WORKFLOW.md      # 🔴 必读：错误处理工作流
├── README.md              # 本文件：知识库入口
├── patterns/              # 错误模式（可复用的错误类型）
│   ├── algorithm-scenario-assumption.md
│   ├── cuda-memory-out-of-bounds.md
│   └── ...
└── cases/                 # 错误案例（具体实例）
    ├── 005-curved-road-boundary-error.md
    ├── 006-retrograde-detection-jitter-filter.md
    └── ...
```

---

## 核心文件

### 1. ERROR_WORKFLOW.md（必读）

定义了完整的错误处理流程，包括：
- 触发条件
- 工作流程
- Case/Pattern 模板
- 最佳实践

### 2. patterns/（错误模式）

定义一类错误的通用模式和预防措施。

### 3. cases/（错误案例）

记录具体的错误实例，关联到对应的 Pattern。

---

## 使用流程

### 当用户提到错误相关词汇时：

1. **触发**：用户说"总结到知识库"、"有什么经验教训"
2. **读取**：立即读取 `ERROR_WORKFLOW.md`
3. **查询**：查询现有 Pattern
4. **创建**：根据模板创建 Case/Pattern
5. **验证**：执行完成检查

### 禁止行为

- ❌ 不得跳过 ERROR_WORKFLOW.md 的读取
- ❌ 不得在未查询现有 Pattern 的情况下创建新 Pattern
- ❌ 不得直接创建文件而未执行完整流程

---

## 相关文档

- **主规范**：`CLAUDE.md` 第 19 节
- **模板目录**：`.claude/templates/`
- **规格说明**：`specs/README.md`
