## 🧪 测试规范

### 测试组织结构

```
tests/
├── unit/              # 单元测试 - 测试单个类/函数
│   ├── test_modules/  # 模块测试
│   ├── test_config/   # 配置测试
│   └── test_utils/    # 工具测试
├── integration/       # 集成测试 - 测试完整工作流
│   └── test_cli/      # CLI命令测试
├── benchmark/         # 性能测试
└── conftest.py        # 共享fixtures (参考 tests/conftest.py)
```

### 测试命名约定

- 文件: `test_<module_name>.py`
- 类: `Test<ClassName>`
- 函数: `test_<function_name>_<scenario>`

### 测试标记使用

```python
@pytest.mark.unit        # 单元测试
@pytest.mark.integration # 集成测试
@pytest.mark.contract    # 契约测试
def test_something():
    pass
```

### Fixtures参考

- 共享fixtures定义: `tests/conftest.py:9-18`
- Fixture使用示例: `tests/unit/test_modules/test_element_removal.py`

---