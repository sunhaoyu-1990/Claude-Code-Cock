# Profile: python

**层级**：Profile  
**适用**：Python 项目（脚本 / 服务端 / 数据处理 / 工具链）  
**依赖**：建议同时导入 `common.md`  
**禁止**：不定义项目工作流与技能链；不引入业务约束。

---

## 代码风格与结构（默认偏好）

- 命名：函数/变量 `snake_case`，类 `PascalCase`，常量 `UPPER_SNAKE_CASE`。
- 类型：公共 API 优先添加 `typing` 标注；复杂结构用 `TypedDict`/`dataclass`（按项目习惯）。
- 文档：公共函数/类建议提供 docstring（简短、描述输入输出与异常）。
- 风格：PEP8

---

## 类型提示与返回类型（Typing & Contracts）

- 所有模块对外输出必须使用 明确返回类型（例如 ModuleResult / Result[T]）
- 禁止返回“裸 dict”作为跨层契约（允许内部使用）

建议：
- 跨模块/跨层接口使用 pydantic 或 dataclasses 定义结构
- 对 np.ndarray 需明确：
-- dtype（若关键）
-- 形状约束（例如 (H, W, C) / (H, W)）
-- 通道顺序（BGR/RGB）

---

## 依赖与环境（默认直觉）

- 优先避免新增依赖；如新增依赖，必须说明用途与替代方案（遵循 BASE）。
- 若项目使用 lock（poetry.lock / requirements.txt / uv.lock），保持锁文件一致。
- 依赖管理：uv / pip

---

## 错误处理（Python 默认）

- 使用异常表达失败，不用“返回 None/False”混淆语义（除非项目约定如此）。
- 对外边界（IO、网络、解析）：
  - 捕获底层异常并抛出更有语义的异常（保留 cause）
  - 错误信息包含：资源标识、关键参数、重试建议（如适用）

---

## 测试（Python 默认）

- 首选 `pytest`（若项目已有其他框架，遵循项目约定）。
- 测试命名：`test_*.py` + `TestClass`/`test_function`。
- 对缺陷修复：优先补充回归测试（先失败、后修复）。
- 对时间/随机性：使用固定 seed、冻结时间工具（若项目已有）。

---

## 性能（Python 默认）

- 不提前优化；若性能是目标：
  1) 先 profile（cProfile/py-spy 等）
  2) 再做局部优化
- 数据处理：优先批处理、避免 N^2 循环；必要时使用向量化/缓存。

---

## 日志规范（Logging）

- 使用项目统一 logger（例如 utils/logging.py 提供的封装）
- 日志必须包含：
-- module_name
-- image_id 或 image_path
-- config_name 或关键参数摘要（避免打印整份配置）

---

## Docstring 规范（统一风格）

- 本项目默认采用 **Google 风格 docstring**
- 所有 public API（公开函数/类/方法）必须写 docstring
- 私有方法可省略，但复杂逻辑建议补充

### 推荐模板（Google Style）

```python
def func(arg1: str, arg2: int | None = None) -> str:
    """一句话说明函数做什么。

    Args:
        arg1: 参数说明
        arg2: 可选参数说明

    Returns:
        返回值说明

    Raises:
        ValueError: 触发条件
        RuntimeError: 触发条件
    """
```

### NumPy 数组约定（强烈建议写进 docstring）

- 图像：np.ndarray 形状 (H, W, C)，默认 BGR
- 掩码：np.ndarray 形状 (H, W)，值域 0-255 或 bool（必须在契约中明确）

---

## 错误处理（Error Handling Policy,详细规则）
### 原则

- 错误必须：
-- 可定位（包含模块名、输入路径、关键配置项）
-- 可分类（ValueError / RuntimeError / 自定义错误）
-- 可追踪（日志 + 可选元数据输出）

### 推荐错误类型分层

- ValueError：输入参数/配置不合法（可恢复：用户修配置）
- FileNotFoundError / OSError：I/O 层面失败（可能可恢复）
- RuntimeError：模型推理/执行引擎失败（需记录上下文）
- 自定义错误（可选）：ConfigError, ModelUnavailableError, PipelineExecutionError

### 禁止行为

- ❌ 吞异常（except: pass）
- ❌ 用 print 替代日志
- ❌ 返回 None 表示失败（除非契约明确允许）

---

## 代码风格与工具（Tooling）

推荐工具链（可按项目实际落地）：
- 格式化：black
- 静态检查：flake8 或 ruff（二选一）
- 类型检查：mypy
- 测试：pytest

约束：
- 允许迁移工具，但必须在 CLAUDE/指南中统一，并更新命令速查

---

## 测试编写约定（Python）

- 测试命名遵循：test_<unit>_<scenario>()
- 一个测试函数尽量只验证一个核心行为（避免巨石测试）
- 通过 fixtures 管理共享资源，避免重复样板代码
- 对外部依赖（模型/网络/大文件）使用 mock 或标记为 slow / requires_gpu

---

## 配置与 schema 约定（Pydantic）

- 所有配置字段必须在 schema 中显式声明
- 所有约束（范围、枚举、必填）必须在 schema 或 validator 中表达
- schema 错误信息必须可读：字段路径 + 原因 + 示例（如可能）

---

## 最小可合并单元（MMU）在 Python 项目中的落地

每次提交应满足：
- 单一目标（feature/fix/refactor 之一）
- 对应测试（新增或更新）
- 不引入无关格式/重排（除非专门的格式化提交）
