# Testing Profile – C++

本文件在 `testing-common.md` 基础上，
定义 C++ 项目的测试实现规范。

---

## 一、测试框架

- 单元测试：GoogleTest (gtest)
- Mock：GoogleMock (gmock)
- 构建系统：CMake

---

## 二、测试结构补充

- 测试目标必须是独立 target
- 测试二进制不参与正式产物构建
- 单元测试与生产代码分 target 编译

---

## 三、命名规范

- 测试文件：test_<module>.cpp
- 测试套件：TEST(<Component>, <Behavior>)

示例：

```cpp
TEST(ElementRemoval, FailsWithInvalidMask) {
    ...
}
```

---

## 四、Mock 与依赖隔离

* 优先接口隔离而非 linker hack
* Mock 只用于边界依赖
* 禁止 mock 业务核心对象

---

## 五、内存与并发安全（强烈建议）

* 启用 AddressSanitizer / UndefinedSanitizer
* 并发逻辑建议 TSAN 或专项测试

---

## 六、覆盖率与质量

* 覆盖率工具：gcov / llvm-cov
* 覆盖率用于趋势监控，不作为唯一质量指标

---

## 七、常用命令（示例）

* ctest
* ctest --output-on-failure
* sanitizer-enabled build

---

本文件为 C++ Testing Profile，
补充语言实现细节，不得弱化 Common 约束。
