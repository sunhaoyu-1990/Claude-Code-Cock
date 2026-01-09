# C++ 示例项目

这是一个展示如何使用 Claude Code 驾驶舱框架的 C++ 示例项目。

## 项目特点

- ✅ 配置了完整的 Claude Code 规范
- ✅ 使用 C++17 标准
- ✅ 包含单元测试
- ✅ 使用 CMake 构建系统

## 快速开始

```bash
# 配置构建
cmake -B build

# 构建
cmake --build build

# 运行测试
ctest --test-dir build --verbose
```

## Claude Code 使用

本项目的 Claude Code 配置位于 `CLAUDE.md`，包含：

- 现代 C++ 特性使用指南
- RAII 资源管理规范
- 命名和代码风格
- 测试策略

## 项目结构

```
cpp-example/
├── include/           # 公共头文件
├── src/               # 源文件
├── tests/             # 测试文件
├── CMakeLists.txt     # CMake 构建配置
├── CLAUDE.md          # Claude Code 配置
└── README.md          # 本文件
```
