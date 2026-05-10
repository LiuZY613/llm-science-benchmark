# 代码 Debug Benchmark

## 测试场景

`buggy_project/` 是一个用 split-operator FFT 方法求解一维含时薛定谔方程的小项目（约 200 行，6 个文件）。物理设定：被弱外场驱动的谐振子势中演化的高斯波包。

**项目中恰好埋了 5 处 bug**，分布在不同文件里。bug 的种类涵盖：

- 数值因子错（缺常数 / 错算法步长）
- 算符符号错
- Python 作用域陷阱（闭包/模块级变量）
- 静默 dtype 退化

**没有任何一个 bug 是单纯的 syntax error**，所有 bug 都在运行时表现为"能跑但物理结果错"或者"产生 warning 但不报错"。

## 给被测 AI 的标准 prompt

> 你将得到一个 Python 项目，路径为 `./buggy_project/`。它本应模拟一个被外场驱动的谐振子势中高斯波包的时间演化，并输出一张 4 子图（密度热图、能量、⟨x⟩、⟨p⟩+ 模长）。
>
> 该项目当前**恰好包含 5 处 bug**，分布于不同文件，运行后结果在物理上错误（例如能量异常漂移、⟨p⟩ 与初始动量不一致、产生 ComplexWarning 等）。
>
> 你的任务：
> 1. 阅读 `buggy_project/` 下全部源码。
> 2. 定位并修复全部 5 处 bug。
> 3. 运行 `python main.py`，确保程序无 warning、无 error 完成，且输出的物理量满足下列正确性判据。
> 4. 在 `buggy_project/` 下创建 `findings.md`，**逐条**记录你找到的每个 bug：所在文件:行号、bug 简述、为何错、如何改。
>
> ### 正确性判据
>
> 修复后运行 `python main.py`，应满足：
> - **无 warning、无 error**；
> - `Initial energy` 在 `3.6` 附近（容差 ±0.05）；
> - `Initial <x>` ≈ `2.0000`（容差 ±0.001）；
> - `Initial <p>` ≈ `1.0`（容差 ±0.01）；
> - `Final norm` 在 `1.0` 附近（容差 ±1e-3）。
>
> 你可以使用任何工具（编辑文件、运行 Python、查看输出）。

## 评分细则（满分 10）

| 项 | 分值 | 说明 |
|---|------|------|
| 每修复并在 findings.md 中正确说明的 bug | 1.5 × 5 = 7.5 | 修复但未在 findings.md 描述：扣 0.5；描述了但未真正修复：扣 1 |
| `python main.py` 跑通无 error | 1.0 | 包括无 warning |
| 4 项物理判据全部满足（见上）| 1.5 | 每项 0.375 |

**满分 10 分**。

> 注：评分基于"运行结果 + findings.md"双重证据。仅修对代码但不写 findings.md 算"未完成报告"，扣分。
> 仅写 findings.md 但未修对代码（运行仍 fail）也扣分。

## 答案与参考实现

- 标准答案 + 5 个 bug 的位置和性质：`../solutions/code_debug/bugs_reference.md`
- 正确版完整代码：`../solutions/code_debug/correct_version/`
- 参考运行输出（图 + 能量数组）：`../solutions/code_debug/reference_outputs/`
