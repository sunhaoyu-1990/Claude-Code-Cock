# Python 示例项目

这是一个展示如何使用 Claude Code 驾驶舱框架的 Python 示例项目。

## 项目特点

- ✅ 配置了完整的 Claude Code 规范
- ✅ 使用 FastAPI 框架
- ✅ 包含测试策略
- ✅ 遵循 PEP 8 代码风格

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 运行服务
uvicorn app.main:app --reload

# 运行测试
pytest
```

## Claude Code 使用

本项目的 Claude Code 配置位于 `CLAUDE.md`，包含：

- 代码风格规范
- 类型提示要求
- 测试策略
- 命令速查

## 项目结构

```
python-example/
├── app/               # 应用代码
├── tests/             # 测试文件
├── CLAUDE.md          # Claude Code 配置
├── README.md          # 本文件
└── requirements.txt   # 依赖列表
```
