# 科研大模型实测对比 Benchmark

五款大语言模型在 **3 项科研任务** 上的客观对比评测，覆盖数学推理、代码调试、引用核查。

## 参评模型

| 模型 | API 端点 | 上下文 | 备注 |
|------|----------|--------|------|
| Claude Opus 4.7 | Anthropic 官方 | 1M token | OAuth Max 订阅 |
| DeepSeek V4 Pro | api.deepseek.com | 1M token | ¥3 / ¥6 每百万 token |
| MiMo V2.5 Pro | Xiaomi Token Plan | 1M token | 订阅制 |
| Kimi K2.6 | api.moonshot.cn | 262k token | ¥6.5 / ¥27 每百万 token |
| 磐石100 (S1-671B) | uni-api.cstcloud.cn | 32k token | 中科院内部部署 |

## 结果摘要

| 模型 | 01 数学推理 | 02 代码调试 | 03 引用核查 | 加权均分 |
|------|:----------:|:----------:|:----------:|:--------:|
| deepseek | 60/60 | 10.0/10 | 8.5/10 | **96.3** |
| opus | 60/60 | 10.0/10 | 5.75/10 | **94.7** |
| kimi | 60/60 | 10.0/10 | 6.25/10 | **92.5** |
| MiMo | 50/60 | 10.0/10 | 6.9/10 | **83.7** |
| 磐石100 | 25/60 | 0.4/10 | 0.0/10 | **30.9** |

> 加权：01 占 60%，02/03 各占 20%。报告详见 `report/index.html`。

## 3 项 Benchmark

### 01 · 数学推理
6 道数学题（代数·几何·数论·组合·极限·概率），难度清北强基~Putnam 中段。
- **评分**：每题 10 分（答案错误即 0，答案对再评推导思路），满分 60
- **运行**：每模型每题独立采样 **3 次**，best-of-3 计分
- **模式**：单轮推理，无工具调用（opus/kimi/mimo 通过 `claude -p`，ds/磐石 HTTP 流式）

### 02 · 代码调试
量子谐振子仿真项目含 **5 处 Bug**，需在沙盒中定位修复并通过物理验证。
- **评分**：5 Bug × 1.2 分 + 4 判据 × 1 分 = 10 分
- **运行**：每模型 **1 次** agent 运行（sandbox 隔离，防答案泄漏）
- **模式**：Agent loop（Read/Edit/Bash），沙盒位于 `%TEMP%` 树外

### 03 · 引用核查
LaTeX 论文 23 条引用含 **8 处人为注入错误**（2 完全捏造 + 2 字段篡改 + 2 领域伪造 + 2 位置错误）。
- **评分**：TP 识别 0.625×8 + 分类正确 0.625×8，假阳性 −0.5/条，满分 10
- **运行**：每模型 **1 次** agent 运行（沙盒隔离）
- **模式**：Agent loop（WebSearch/WebFetch/Bash/Python 调用 Crossref/arXiv API）

## 前置条件

### 1. Claude Code CLI
所有 agent 模式运行依赖 `claude.exe`，安装位置：
```
%USERPROFILE%\.local\bin\claude.exe
```

### 2. API Key 配置
```bash
cp .env.example .env
# 编辑 .env 填入你的 API Key
```

| 变量 | 用途 |
|------|------|
| `BENCH_DS_KEY` | DeepSeek API |
| `BENCH_CST_KEY` | 中科院磐石 |
| `BENCH_KIMI_TOKEN` | Kimi K2.6 |
| `BENCH_MIMO_TOKEN` | MiMo V2.5 |

opus 无需额外 Key——`claude.exe` 自动使用 OAuth Max 订阅。

### 3. Python 环境
Python 3.10+，标准库即可（无额外依赖）。

## 使用方式

### 运行全部

```bash
# Benchmark 01 — 数学推理（每模型 6 题 × 3 次 = 18 次调用）
python run_benchmark.py opus
python run_benchmark.py deepseek
python run_benchmark.py mimo
python run_benchmark.py kimi
python run_benchmark.py panshi100

# Benchmark 02 — 代码调试（每模型 1 次 agent 运行）
python run_codedebug.py opus
python run_codedebug.py deepseek
python run_codedebug.py mimo
python run_codedebug.py kimi
python run_codedebug.py panshi100

# Benchmark 03 — 引用核查（每模型 1 次 agent 运行）
python run_citation.py opus
python run_citation.py deepseek
python run_citation.py mimo
python run_citation.py kimi
python run_citation.py panshi100
```

### 单题 / 单次运行

```bash
# 01: 指定题目和跑次
python run_benchmark.py opus problem_5       # 题 5 × 3 次
python run_benchmark.py opus problem_5 2     # 题 5 run2 only

# 02: 指定跑次
python run_codedebug.py opus 2               # opus run2

# 03: 指定跑次
python run_citation.py kimi 2                # kimi run2
```

### 评分

评分基准在 `solutions/` 目录：
- `solutions/math/solutions.md` — 6 题标准答案
- `solutions/code_debug/bugs_reference.md` — 5 Bug 标准答案 + 评分细则
- `solutions/citation/bugs_reference.md` — 8 处引用错误标准答案 + 评分细则

结果输出在 `<model>-answer/` 目录，对照评分基准手工打分。完整报告见 `report/index.html`。

## 项目结构

```
benchmark/
├── config.py                 # API Key 管理（从 .env 读取）
├── .env.example              # 环境变量模板
├── .gitignore
├── run_benchmark.py          # 01 数学推理 runner
├── run_codedebug.py          # 02 代码调试 runner
├── run_citation.py           # 03 引用核查 runner
├── 01_math_reasoning/        # 6 道数学题 (problem_1.md ~ problem_6.md)
├── 02_code_debug/            # 含 Bug 的量子谐振子项目
│   └── buggy_project/
├── 03_citation_check/        # LaTeX 论文 + 引用真值对照
│   ├── paper_buggy.tex
│   ├── answer_key.md
│   └── references_truth.md
├── solutions/                # 评分基准（标准答案 + 验证脚本）
│   ├── math/
│   ├── code_debug/
│   └── citation/
├── opus-answer/              # opus 原始输出
├── deepseek-answer/          # deepseek 原始输出
├── mimo-answer/              # MiMo 原始输出
├── kimi-answer/              # kimi 原始输出
├── panshi100-answer/         # 磐石100 原始输出
└── report/                   # HTML 对比报告
    ├── index.html
    ├── benchmark01.html
    ├── benchmark02.html
    └── benchmark03.html
```

## 设计要点

- **沙盒隔离**：02/03 agent 任务运行在 `%TEMP%` 下，模型无法通过 `..` 访问 `solutions/` 或答案文件
- **可复现**：每条评分有原始输出支撑，评分基准公开，任何人用相同环境可重跑验证
- **统一 harness**：所有模型通过同一套 `claude -p --output-format json` 协议调用（HTTP 模式除外），消除测试工具偏差
- **3 次采样**：01 每模型每题独立采样 3 次，避免单次运气影响结论
