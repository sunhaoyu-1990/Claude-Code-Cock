# CLAUDE.md - C++ 示例项目

**项目名称**：C++ Example Project
**主要语言**：C++
**语言版本**：C++17
**主要框架**：None (Standard Library)
**测试框架**：Google Test (gtest)

---

## 项目规范引用

@.claude/BASE_CLAUDE.md
@.claude/constitution.md
@.claude/PROFILES/cpp.md

---

## 错误知识库

优先查询 @.claude/knowledge/patterns/ 中与 C++ 相关的错误模式。

---

## 项目上下文

本项目是一个简单的 C++ 库示例，展示：
- 现代 C++ 特性使用
- RAII 资源管理
- 模板编程
- 单元测试

### 项目结构

```
cpp-example/
├── include/             # 公共头文件
│   └── cpp_example/
│       └── calculator.h
├── src/                 # 源文件
│   └── calculator.cpp
├── tests/               # 测试文件
│   └── calculator_test.cpp
├── CMakeLists.txt       # CMake 构建配置
├── CLAUDE.md            # 本文件
└── README.md            # 项目说明
```

---

## 开发规范

### 代码风格

- 使用现代 C++（C++17）特性
- RAII 优先：资源获取即初始化
- const 正确性：能 const 就 const
- 头文件最小化依赖：能前置声明就前置声明

### 命名规范

- 类名：`PascalCase`
- 函数/变量：`snake_case`
- 常量：`UPPER_SNAKE_CASE`
- 成员变量：`trailing_underscore_`

### 内存管理

- 避免裸 `new/delete`
- 优先使用智能指针（`std::unique_ptr`, `std::shared_ptr`）
- 使用标准容器（`std::vector`, `std::map` 等）

### 错误处理

- 使用异常（按项目约定）
- 边界捕获，内部传播
- 异常类型语义化

### 测试

- 使用 Google Test
- 测试文件命名：`*_test.cpp`
- 每个公共函数至少一个测试

---

## 命令速查

```bash
# 配置构建（Debug）
cmake -B build -DCMAKE_BUILD_TYPE=Debug

# 构建
cmake --build build

# 运行测试
ctest --test-dir build --verbose

# 配置构建（Release）
cmake -B build -DCMAKE_BUILD_TYPE=Release

# 静态分析（如安装）
clang-tidy include/* src/* -- -I include/
```

---

## 编译器要求

- GCC ≥ 7.0
- Clang ≥ 5.0
- MSVC ≥ 2017

---

## 注意事项

1. 使用 `-Wall -Wextra` 编译选项，不引入新的编译警告
2. 公共 API 必须有声明和定义分离
3. 头文件必须包含 `#pragma once` 或 `#ifndef` 保护
4. 避免使用全局变量和静态局部变量（除非有明确理由）
