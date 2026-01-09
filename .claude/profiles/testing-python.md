# Testing Profile – Python

本文件在 `testing-common.md` 基础上，
定义 Python 项目的测试实现规范。

---

## 一、测试框架

- 主测试框架：pytest
- Mock 工具：unittest.mock / pytest-mock
- 覆盖率：coverage.py

---

## 二、命名与结构补充

- 单元测试文件：test_<module>.py
- 集成测试：test_<feature>_integration.py
- 契约测试：test_<contract>.py

测试函数命名：

```python
def test_<behavior>_when_<condition>():
    ...
```

---

## 三、pytest markers（推荐集合）

* unit
* integration
* contract
* slow
* requires_gpu

项目必须在 pytest.ini / pyproject.toml 中显式声明。

---

## 四、Fixtures 使用规范

* Fixture 只负责环境准备，不做断言
* Fixture 作用域必须最小化
* 禁止在 fixture 中隐藏复杂逻辑

---

## 五、覆盖率约束（示例）

* 总体覆盖率 ≥ 80%
* 新增代码覆盖率 ≥ 90%
* 核心模块需单独关注

---

## 六、TDD 支持

当启用 TDD：

循环：

1. Red → 最小失败测试
2. Green → 最小实现
3. Refactor → 不改变行为

---

## 七、常用命令（示例）

* pytest
* pytest -m unit
* pytest --cov
* pytest -x / --pdb

---

本文件为 Python Testing Profile，
仅补充语言相关实现，不得覆盖 Common 规则。