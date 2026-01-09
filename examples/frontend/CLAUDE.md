# CLAUDE.md - Frontend 示例项目

**项目名称**：Frontend Example Project
**主要语言**：TypeScript
**语言版本**：5.x
**主要框架**：React 18
**测试框架**：Vitest + Testing Library

---

## 项目规范引用

@.claude/BASE_CLAUDE.md
@.claude/constitution.md
@.claude/PROFILES/frontend.md

---

## 错误知识库

优先查询 @.claude/knowledge/patterns/ 中与前端相关的错误模式。

---

## 项目上下文

本项目是一个简单的 React 应用示例，展示：
- 函数组件和 Hooks
- TypeScript 类型定义
- 状态管理
- 组件测试

### 项目结构

```
frontend-example/
├── src/
│   ├── components/      # React 组件
│   ├── hooks/           # 自定义 Hooks
│   ├── types/           # TypeScript 类型定义
│   ├── utils/           # 工具函数
│   ├── App.tsx          # 主应用组件
│   └── main.tsx         # 入口文件
├── tests/               # 测试文件
├── CLAUDE.md            # 本文件
├── package.json         # 项目配置
├── tsconfig.json        # TypeScript 配置
└── vite.config.ts       # Vite 配置
```

---

## 开发规范

### 命名规范

- 组件文件：`PascalCase.tsx`
- 工具文件：`kebab-case.ts`
- 变量/函数：`camelCase`
- 类型/接口：`PascalCase`
- 常量：`UPPER_SNAKE_CASE`

### TypeScript

- 所有组件必须有类型定义
- 避免 `any`，优先使用 `unknown` 或具体类型
- 公共 API 使用显式类型注解

### 组件规范

- 优先使用函数组件
- Hooks 遵循 Rules of Hooks
- Props 使用接口定义
- 样式使用 CSS Modules 或 Tailwind

### 状态管理

- 本地状态：`useState`, `useReducer`
- 全局状态：Context API（小型项目）
- 表单：受控组件

### 错误处理

- 使用 Error Boundary
- API 错误统一处理
- 表单验证错误用户友好

### 性能

- 大列表使用虚拟滚动
- 图片懒加载
- 代码分割（路由级别）
- 合理使用 `memo`, `useMemo`, `useCallback`

---

## 命令速查

```bash
# 安装依赖
npm install

# 开发服务器
npm run dev

# 构建
npm run build

# 预览构建
npm run preview

# 运行测试
npm run test

# 类型检查
npm run type-check

# Lint
npm run lint

# 格式化
npm run format
```

---

## 测试策略

- 单元测试：Vitest + Testing Library
- 组件测试：渲染、交互、快照
- 避免测试实现细节
- 专注用户行为

---

## 样式规范

- 遵循项目约定（CSS Modules / Tailwind / styled-components）
- 响应式优先移动端
- 语义化 HTML
- ARIA 属性（如需要）

---

## 安全

- 避免 `dangerouslySetInnerHTML`
- API 密钥不存储在客户端
- 用户输入验证和转义
- HTTPS 生产环境

---

## 注意事项

1. 所有公共组件必须有 Props 类型定义
2. 使用 ESLint 和 Prettier
3. 提交前运行类型检查和测试
4. 不在生产环境使用 console.log
