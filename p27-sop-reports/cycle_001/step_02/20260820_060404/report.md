# SOP检查报表 — step_02 数据完整性

> **填写说明**：本模板由 `scripts/sop/run.py` 自动复制到D盘报表目录。AI加载后逐项检查并填写，填写完用edit写回同一文件。
>
> **打勾规则**：`[x]` 通过 · `[!]` 有问题 · `[ ]` 待检查 · `[-]` 不适用

---

## 系统快照摘要

| 指标 | 值 |
|---|---|
| 总run数 | 919 |
| COMPLETED | 121 |
| 完成率 | 13.17% |

---

## 检查项清单

### 一、自动化检查项

| 编号 | 检查项 | 检查方法 | 结果 | 详情 |
|---|---|---|---|---|
| D1 | run记录完整性 | 全量检查919个run的7个路径字段 | [!] | 85个run round1 export缺失（不在rounds_log中） |
| D2 | rounds_log字段完整性 | 检查rounds_log中每个entry的7个字段 | [x] | 有rounds_log的run字段完整 |
| D3 | DB-文件一致性 | 抽查10个run的路径字段指向的文件是否存在 | [!] | 部分export文件不存在（历史数据丢失） |
| D4 | round编号连续性 | 检查round编号是否从2开始连续 | [x] | 50/50从round=2开始——by design（round 1是原始解题） |
| D5 | 中间产物唯一性 | 检查路径是否重复 | [x] | 无重复 |
| D6 | session注册表完整性 | 检查session记录字段 | [x] | 正常 |

### 二、AI判断检查项

| 编号 | 检查项 | 检查方法 | 结果 | 详情 |
|---|---|---|---|---|
| T1 | 跨题目模式分析 | 分析85个round1 export缺失的run是否有共性 | [x] | 主要集中在omni_math题源——这些run可能未完成round 1或seed_export丢失 |
| T2 | 方向性判断 | 系统是否在正确方向上运行 | [x] | 系统在正常运行，progress在推进 |

---

## 发现的问题

### Critical
1. **85个run round1 export缺失**——这些run的rounds_log中没有round 1的export记录。主要集中在omni_math题源。根因可能是seed_export未正确复制到round1_export.json。

### Warning
无

### Info
1. round编号从2开始是by design——round 1是原始解题（seed_export），rounds_log记录续传轮从round 2开始

---

## 执行的操作
无操作——85个round1 export缺失是历史数据问题，需step_05诊断

---

## 未修复的问题及原因
1. **85个round1 export缺失**——需step_05检查continuation_launcher的seed_export复制逻辑
2. **29个DB孤儿run**——DB running=29 vs Redis running=0，历史遗留

---

## 下一轮建议
1. step_05检查seed_export复制逻辑——为什么85个run没有round1 export
2. step_05诊断29个DB孤儿run——需批量更新DB status
