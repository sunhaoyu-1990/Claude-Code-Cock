# PROJECT_CLAUDE.md — Project Profile（项目画像）【模板】

> 说明：本模板用于为任意项目生成 `PROJECT_CLAUDE.md`。
> 用法：将所有 `{占位符}` 替换为项目真实信息；删除不适用章节或保留但标注 `N/A`。
> 约束：本文件必须保持"事实性上下文"，避免写成流程规范或长篇解释（流程规范应放入 `CLAUDE.md / DEVELOPMENT_GUIDE.md / TEST_GUIDE.md` 等）。

---

## 头部信息（必填）

**项目**: `{project_name}`
**适用范围**: 项目级上下文（Claude 入库必读）
**最后更新**: `{last_updated: YYYY-MM-DD}`
**当前功能分支**: `{current_branch}`

---

## 0. 使用说明（Claude 执行要点）

- 本文件提供项目的"事实性上下文"：结构、依赖、边界、配置、命令、质量门槛。
- 若本文件与 `constitution.md` / `CLAUDE.md` 冲突：以 `constitution.md` 为准，并显式说明冲突点。
- **框架核心文件引用**：
  - 组织级规范：`@.claude/BASE_CLAUDE.md`
  - 宪法文件：`@.claude/constitution.md`
  - 分支管理：`@.claude/BRANCH_GUIDE.md`
  - 命令速查：`@.claude/COMMANDS.md`
  - 错误知识库：`@.claude/knowledge/`
- 当需要修改依赖/模型/运行环境：优先更新本文件中的 **依赖与能力边界** 部分，并在 PR/提交说明中标注。
- 若项目缺少关键上下文（例如：依赖/目录/命令/质量门槛缺失），Claude 应提示"上下文不完整"，并给出最小补全清单。

---

## 1. 项目信息（Project Metadata）

| 属性 | 值 |
|------|-----|
| **项目名称** | `{project_name}` |
| **项目类型** | `{project_type}` |
| **主要语言** | `{primary_language}` |
| **语言版本** | `{language_version}` |
| **运行形态** | `{runtime_form}` |
| **入口方式** | `{entrypoint}` |
| **主要框架/运行库** | `{main_frameworks}` |
| **代码风格** | `{style_guide}` |
| **架构模式** | `{architecture_pattern}` |
| **目标平台** | `{target_platforms}` |

**补充说明（可选）**：
- 仓库类型：`{monorepo_or_single_repo}`
- 发布方式：`{release_model}`（例如：wheel/conda/docker/binary）
- 许可证：`{license}`

---

## 2. 核心能力范围（Project Scope）

### 2.1 项目聚焦（What it does）

一句话描述（必填）：
- `{one_line_description}`

核心目标（可多条）：
- `{goal_1}`
- `{goal_2}`
- `{goal_3}`

### 2.2 典型使用模式（How it is used）

- `{usage_mode_1}`（例如：单命令/HTTP API/SDK 调用/批处理）
- `{usage_mode_2}`
- `{usage_mode_3}`

### 2.3 非目标（What it does NOT do）（强烈建议）

- `{non_goal_1}`
- `{non_goal_2}`

---

## 3. 依赖与能力边界（Dependencies & Capability Boundaries）【可更新】

> 本节用于描述"项目能做什么 / 不能做什么 / 在什么条件下能做什么"。
> 当引入新模型、新硬件能力、新平台支持时，必须同步更新本节。

### 3.1 运行时依赖（Runtime）

| 依赖 | 用途 | 版本/约束 | 备注 |
|------|------|-----------|------|
| `{dep_runtime_1}` | `{purpose_1}` | `{version_constraint_1}` | `{note_1}` |
| `{dep_runtime_2}` | `{purpose_2}` | `{version_constraint_2}` | `{note_2}` |

> 约束（可选，建议保留）：
> - 运行时依赖必须可被环境管理器（pip/uv/conda/apt 等）一致安装。
> - 关键依赖升级需注明：兼容范围、验证方式、回滚方案（如适用）。

### 3.2 可选依赖（Optional / Capability Flags）

| 依赖 | 用途 | 能力开关（建议） | 降级策略 |
|------|------|------------------|----------|
| `{dep_optional_1}` | `{purpose_opt_1}` | `{feature_flag_1}` | `{fallback_policy_1}` |
| `{dep_optional_2}` | `{purpose_opt_2}` | `{feature_flag_2}` | `{fallback_policy_2}` |

约束（建议保留）：
- 未安装可选依赖时，必须提供 **清晰的降级路径**（fallback）或 **明确报错**（不允许静默失败）。
- 可选能力应通过配置/环境变量显式启用，避免"隐式启用导致运行环境不一致"。

### 3.3 平台与资源假设（Platform & Resources）

- **默认目标平台**：`{platforms}`（例如：Linux/macOS/Windows；或 Android/iOS；或 k8s）
- **资源依赖**：
  - CPU：`{cpu_requirement}`
  - 内存：`{memory_requirement}`
  - GPU：`{gpu_requirement}`（如可选，写清启用条件）
  - 存储：`{storage_requirement}`
- **CPU fallback**：`{cpu_fallback_policy}`（例如：必须可用/不支持/仅支持某些路径）
- **网络依赖**：`{network_dependency}`（例如：离线可运行/需要访问模型仓库/需要内网服务）

### 3.4 外部能力/模型边界（External Models / Services Boundary）

- 外部模型/服务属于 **外部能力依赖**（Examples）：
  - `{external_capability_1}`
  - `{external_capability_2}`
- 约束：
  - 必须有包装层隔离依赖与实现细节（例如：`{wrapper_layer_path}`）
  - 必须定义"不可用时"的行为（fallback 或 fail-fast）
  - 必须定义输入/输出契约与错误语义（contract）

---

## 4. 项目结构（Repository Layout）

> Claude 在新增/修改代码时，必须遵守模块边界，不跨层引用内部细节。

{repo_root}/
├── {path_1}/
│ ├── {path_1_file_a}
│ └── {path_1_file_b}
├── {path_2}/
│ ├── {path_2_file_a}
│ └── {path_2_file_b}
├── tests/
│ ├── unit/
│ ├── integration/
│ └── fixtures/
├── configs/ #（如适用）
├── pyproject.toml #（如适用）
└── README.md


**层级说明（可选）**：
- `{layer_explain_1}`
- `{layer_explain_2}`

---

## 5. 模块边界与职责（Module Boundaries）

| 层/目录 | 职责 | 允许依赖 | 禁止依赖 |
|---------|------|----------|----------|
| `{layer_1}` | `{responsibility_1}` | `{allowed_deps_1}` | `{forbidden_deps_1}` |
| `{layer_2}` | `{responsibility_2}` | `{allowed_deps_2}` | `{forbidden_deps_2}` |
| `{layer_3}` | `{responsibility_3}` | `{allowed_deps_3}` | `{forbidden_deps_3}` |

全局约束（建议保留）：
- 模块间交互必须通过明确接口/返回类型（避免隐式全局状态）
- 外部能力（模型/服务）必须隔离在包装层
- 核心业务逻辑不得放入入口层（CLI/UI/API），保持可复用

---

## 6. 命名约定（Naming Conventions）

| 类型 | 约定 | 示例 |
|------|------|------|
| 类名 | `{class_naming}` | `{class_example}` |
| 函数名 | `{function_naming}` | `{function_example}` |
| 变量名 | `{variable_naming}` | `{variable_example}` |
| 常量 | `{const_naming}` | `{const_example}` |
| 私有成员 | `{private_naming}` | `{private_example}` |

> 细化规范与 docstring/typing 要求见：`{conventions_profile_ref}`（例如：`@.claude/profiles/python.md` 或 language profile）。

---

## 7. 类型提示 / 接口契约（Typing & Contracts）

- 公共接口是否要求类型提示：`{typing_required: yes/no}`
- 推荐的契约形式：`{contract_form}`（例如：pydantic/dataclass/protobuf/struct）
- 常见数据结构约定（如适用）：
  - `{data_contract_1}`
  - `{data_contract_2}`

---

## 8. 配置格式（Configuration）

- 配置格式：`{config_format}`（YAML/JSON/TOML/INI/ENV/Proto）
- 配置入口：`{config_entry}`（例如：`--config` / env vars / config directory）
- 配置校验：`{config_validation}`（例如：schema/validator）

### 8.1 配置结构 Skeleton（示例）

```{config_format}
{config_skeleton_example}
```

约束（建议保留）：
- 配置加载与校验必须通过 {schema_path_or_tool}（禁止绕过校验直接读取字典/原始对象）
- 对用户可见的配置错误必须输出：字段路径 + 原因 +（可选）修复建议

## 9. 运行入口与命令（Entrypoints & Commands）

### 9.1 主入口

* 可执行入口：`{main_entry}`（例如：`smart-enhancer` / `python -m pkg` / `./bin/app`）
* 帮助命令：`{help_command}`

### 9.2 常用命令（示例）

参考 `@.claude/COMMANDS.md` 获取标准命令格式。

```bash
{command_1}
{command_2}
{command_3}
```

约束（可选，建议保留）：

* 若支持 `--dry-run` / `--log-level` / `--config`：各命令语义必须一致
* 命令行覆盖配置应可追踪（建议写入输出元数据/日志）

---

## 10. 测试与质量门槛（Testing & Quality Gates）

* 测试框架：`{test_framework}`
* 覆盖率工具：`{coverage_tool}`
* 目标覆盖率：

  * 总体：`>{coverage_total}%`
  * 核心模块：`>{coverage_core}%`（如适用）
  * 新增代码：`>{coverage_new}%`（如适用）

质量门禁（建议保留）：

* 新增功能必须带测试（unit 优先；必要时补 integration）
* 修 bug 必须先写可复现问题的测试（建议 TDD）

参考（可选）：

* 测试规范文件：`{test_guide_ref}`
* Profile：`{testing_profiles_ref}`（例如：`@.claude/profiles/testing-common.md` 和 `@.claude/profiles/testing-python.md`）

---

## 11. 日志与可观测性（Logging & Observability）

* 日志框架/库：`{logging_lib}`
* 默认日志级别：`{default_log_level}`
* 日志输出：

  * Console：`{console_logging: yes/no}`
  * File：`{file_logging: yes/no}`（路径：`{log_file_path}`）
* 监控/错误上报（如适用）：`{monitoring_tool}`（例如：Sentry/OTel/Prometheus）

约束（建议保留）：

* 关键失败必须记录 ERROR，并包含上下文（输入路径/配置摘要/模块名）
* 禁止吞掉异常；如需降级必须记录原因并返回显式状态

---

## 12. 开发工作流（High-Level）

**分支管理**：详细流程参考 `@.claude/BRANCH_GUIDE.md`

**开发模式**：
- Simple Mode：小型任务，参考 `@.claude/guides/DEV_GUIDE_SIMPLE.md`
- Complex Mode：大型功能，使用 Speckit Skill Chain（在 CLAUDE.md 中定义）

**基本流程**：
1. 创建分支：遵循分支命名规范（如 `feature/001-add-feature`）
2. 编写代码与测试
3. 运行测试：`{run_tests_command}`
4. 格式化/检查：`{format_command}` / `{lint_command}` / `{typecheck_command}`
5. 提交与推送：遵循 Conventional Commits 规范

---

## 13. 相关文档索引（Specs & Contracts）

* 规格/需求：`{spec_doc_path}`
* 实施计划：`{plan_doc_path}`
* 契约/接口：`{contracts_path}`
* 配置 schema：`{config_schema_path}`
* 快速入门：`{quickstart_path}`
* 其他：`{other_doc_1}`, `{other_doc_2}`

---

## 14. 维护要求（Maintenance）

当发生以下变更时，必须更新本文件：

* 目录结构/模块边界调整
* 依赖升级或新增（尤其涉及外部模型/硬件能力）
* 运行入口/命令新增、参数语义变更
* 配置 schema 结构变更
* 性能/质量门槛调整（并同步更新 `{nfr_file_ref}` 如适用）

更新时要求：

* 在 PR 描述或 changelog 标注变更点
* 如有 Breaking Change，必须说明迁移方式与兼容性策略

---

## 附录 A：可选"最小补全清单"（Context Minimal Checklist）

当 Claude 判断项目上下文缺失/不完整时，至少应补齐以下字段（建议保留此清单）：

* [ ] 项目名称、类型、主要语言与版本
* [ ] 主入口与常用命令
* [ ] 运行时依赖与可选依赖（含降级策略）
* [ ] 目录结构与模块边界
* [ ] 配置格式与 schema 校验位置
* [ ] 测试框架与覆盖率门槛
* [ ] 日志策略与输出位置

---

## 模板填充说明（可删除）

* 搜索并替换所有 `{...}` 占位符。
* 不适用章节可删除，但建议保留"依赖与能力边界""模块边界""测试与质量门槛"三块。
* 若项目跨语言/跨平台：为每种语言补充对应的 `@.claude/profiles/{language}.md`，并在本文件引用。
