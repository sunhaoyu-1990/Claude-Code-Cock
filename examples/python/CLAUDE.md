# CLAUDE.md - Python 示例项目

**项目名称**：Python Example Project
**主要语言**：Python
**语言版本**：3.11
**主要框架**：FastAPI
**测试框架**：pytest

---

## 项目规范引用

@.claude/BASE_CLAUDE.md
@.claude/constitution.md
@.claude/PROFILES/python.md

---

## 错误知识库

优先查询 @.claude/knowledge/patterns/ 中与 Python 相关的错误模式。

---

## 项目上下文

本项目是一个简单的 FastAPI 服务示例，展示：
- RESTful API 设计
- 异步编程
- 依赖注入
- 测试策略

### 项目结构

```
python-example/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI 应用入口
│   ├── api/             # API 路由
│   ├── models/          # Pydantic 模型
│   ├── services/        # 业务逻辑
│   └── utils/           # 工具函数
├── tests/               # 测试文件
├── CLAUDE.md            # 本文件
└── requirements.txt     # 依赖列表
```

---

## 开发规范

### 代码风格

- 遵循 PEP 8
- 使用 black 格式化
- 使用 flake8 静态检查
- 使用 mypy 类型检查

### 类型提示

- 所有公共 API 必须有类型注解
- 复杂类型使用 TypedDict 或 Pydantic 模型

### 测试

- 使用 pytest
- 测试文件命名：`test_*.py`
- 覆盖率目标：≥ 80%

---

## 命令速查

```bash
# 安装依赖
pip install -r requirements.txt

# 运行服务
uvicorn app.main:app --reload

# 运行测试
pytest

# 类型检查
mypy app/

# 格式化代码
black app/

# 静态检查
flake8 app/
```

---

## 注意事项

1. 所有 API 端点必须有类型提示和文档字符串
2. 异步操作使用 `async/await`
3. 数据验证使用 Pydantic
4. 错误处理遵循项目统一的异常层级
