# SOP检查报表 — step_05 代码修复

| 指标 | 值 |
|---|---|
| 需修复问题 | 0（本轮无需修代码） |

## 修复记录

### 诊断1: 29个DB孤儿run
- **诊断结果**：非p27-full batch的问题。29个孤儿run属于其他batch（full-analysis-v2-r*），p27-full batch的DB running只有1个（正在运行的deepmath_103k_00000006）。
- **处理方式**：不修代码——其他batch的孤儿run不影响p27-full。

### 诊断2: 85个round1 export缺失
- **诊断结果**：非bug。85个run全部是prepared状态（还没跑过），自然没有round1_export.json。check_02的检查逻辑对prepared run也检查了round1 export，这是检查项过于严格，不是代码bug。
- **处理方式**：不修代码。可考虑在check_02中跳过prepared run的round1 export检查（优化项，非bug）。

## 发现的问题
无代码bug需修复。

## 执行的操作
无操作——本轮无需修代码

## 下一轮建议
无
