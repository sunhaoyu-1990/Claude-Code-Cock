# Profile: frontend

**层级**：Profile
**适用**：前端项目（React / Vue / Angular / 原生 JS/TS / Node.js 工具链）
**依赖**：建议同时导入 `common.md`
**禁止**：不定义项目工作流与技能链；不引入业务约束。

---

## 代码风格与结构（默认偏好）

### 命名规范

- 变量/函数：`camelCase`
- 类/组件/类型：`PascalCase`
- 常量：`UPPER_SNAKE_CASE`
- 文件名：`kebab-case` 或 `PascalCase`（组件）
- 私有成员：`_prefix`（若语言/框架支持）

### TypeScript 优先

- 项目默认使用 TypeScript（除非项目明确使用纯 JS）
- 所有公共 API 必须有类型定义
- 避免 `any`：优先使用 `unknown` 或具体类型
- 复杂类型使用 `type` 或 `interface`（按项目约定）

### 组件结构（React/Vue 通用）

- 组件文件保持单一职责
- 相关类型定义与组件同文件或就近
- 样式方案与项目保持一致（CSS Modules / Tailwind / styled-components / 等）

---

## 类型与接口契约（TypeScript 默认）

### 接口定义

- 所有公共 API 必须显式声明输入输出类型
- 跨组件通信使用明确的 Props 接口定义
- API 响应类型集中定义（types/ 或 @/types/）

### 类型工具

- 优先使用工具类型（`Partial<T>`, `Pick<T>`, `Omit<T>`, `Record<K,V>`）
- 复杂类型定义需附带注释说明用途
- 避免类型断言（`as`），除非绝对必要且已注释

---

## 依赖与包管理（默认直觉）

- 优先避免新增依赖；新增依赖必须说明用途、大小、替代方案
- 遵循项目锁文件策略（package-lock.json / pnpm-lock.yaml / yarn.lock）
- 包管理器：npm / pnpm / yarn（按项目约定）

### 依赖分类

- `dependencies`：运行时必需
- `devDependencies`：开发时工具、类型定义
- 避免将大型库作为生产依赖（除非项目核心依赖）

---

## 状态管理（默认直觉）

### 本地状态

- 优先使用框架内置方案（useState / ref / reactive）
- 简单表单使用受控组件

### 全局状态

- 小型项目：Context API / Provide-Inject
- 中大型项目：按项目约定（Redux / Zustand / Pinia / 等）
- 避免过度设计：能用本地解决的不要上全局

---

## 错误处理（前端默认）

### 用户输入验证

- 表单提交前验证，提供清晰错误提示
- 验证规则集中管理或使用 schema（zod / yup / 等）

### 网络请求

- 统一错误处理（axios interceptor / fetch wrapper）
- 错误信息用户友好（避免直接暴露技术栈）
- 关键操作提供重试机制

### 边界错误

- 使用 Error Boundary（React）或等效机制
- 避免白屏崩溃

---

## 性能（前端默认）

### 不提前优化

- 性能目标明确时再优化
- 使用 Lighthouse / Performance API 测量

### 常见优化点

- 大列表：虚拟滚动（react-window / virtual-scroller）
- 图片：懒加载、现代格式、响应式
- 代码分割：按路由 / 功能动态导入
- 缓存：合理使用 memo / useMemo / computed

---

## 测试（前端默认）

### 测试框架

- 优先使用项目既有框架（Jest / Vitest / Playwright / Cypress）
- 无框架时：Vitest（现代）或 Jest

### 测试分层

- **单元测试**：组件逻辑、工具函数
- **集成测试**：页面交互流程
- **E2E 测试**：关键用户路径（可选，按项目需求）

### 测试原则

- 新功能：至少一个测试覆盖核心路径
- 缺陷修复：优先回归用例
- 外部依赖（API、第三方库）：mock 或 stub

---

## 样式规范（默认直觉）

### 遵循项目约定

- 若项目已有设计系统：优先使用组件库
- 若项目使用原子化 CSS：遵循约定（Tailwind / UnoCSS）

### 通用原则

- 响应式：优先移动端或按产品需求
- 可访问性：语义化 HTML、ARIA 属性（如需要）
- 主题色：使用 CSS 变量或设计 token

---

## 构建与工具链（默认）

### 构建工具

- 遵循项目既有配置（Vite / Webpack / esbuild / Next.js / Nuxt）
- 不引入额外的构建步骤，除非必要

### 代码质量

- 格式化：Prettier（若项目配置）
- 静态检查：ESLint（必需）
- 类型检查：tsc（TypeScript 项目）

### Git Hooks（可选）

- 若项目配置：pre-commit（lint-staged）、commitlint
- 不强制新增，但建议保持一致

---

## 安全（前端默认）

### XSS 防护

- 框架默认转义：避免 `dangerouslySetInnerHTML` / `v-html`
- 必须使用时：内容 sanitized 或来自可信源

### 敏感数据

- 不在客户端存储敏感信息（localStorage / sessionStorage）
- API 密钥、token 通过安全渠道获取
- 日志不泄露用户隐私

---

## 最小可合并单元（MMU）在前端项目中的落地

每次提交应满足：
- 单一目标（feature / fix / refactor / ui-adjustment 之一）
- 对应测试或手工验证步骤
- 不引入无关格式/重排（除非专门的格式化提交）

---

## 日志与调试（前端默认）

### 开发环境

- 使用 console.error / console.warn 标记问题
- 避免生产环境 console 泄露（或使用可配置 logger）

### 生产环境

- 错误上报：Sentry / 自建（按项目约定）
- 性能监控：Core Web Vitals（按项目需求）
