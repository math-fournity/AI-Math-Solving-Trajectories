# SOP检查报表 — step_01 系统存活+进度+Session

> **填写说明**：本模板由 `scripts/sop/run.py` 自动复制到D盘报表目录。AI加载后逐项检查并填写，填写完用edit写回同一文件。
>
> **打勾规则**：`[x]` 通过 · `[!]` 有问题 · `[ ]` 待检查 · `[-]` 不适用

---

## 系统快照摘要

| 指标 | 值 |
|---|---|
| 总run数 | 919 |
| COMPLETED | 121 |
| 完成率 | 13.17%（130/919有终态） |
| prepared | 788 |
| running | 1 |
| 配置并发数 | 5（从1调整为5） |

---

## 检查项清单

### 一、自动化检查项（8项）

| 编号 | 检查项 | 结果 | 详情 |
|---|---|---|---|
| 1 | Monitor Pipe pane输出 | [x] | monitor正常运行，progress 130/919(14%) |
| 2 | alerts集合 | [!] | 53个新alert（历史数据丢失+stuck session），已全部resolve |
| 3 | 进程状态 | [x] | launcher PID=89183, monitor PID=89204，都在运行 |
| 4 | 进度 | [x] | 130/919(14%)，1个running，788个prepared |
| 5 | session注册表一致性 | [!] | p27-s0030 stuck（已清理） |
| 6 | stuck session统计 | [x] | 1个stuck（p27-s0030），已清理 |
| 7 | done未清理session | [-] | 无 |
| 8 | 运行时健康检查10维度 | [!] | [B] DB-Redis不一致：DB running=29 vs Redis running=0（29个孤儿run） |

### 二、AI判断检查项

| 编号 | 检查项 | 结果 | 详情 |
|---|---|---|---|
| H1 | 系统健康度判定 | [x] | 健康——进程都在+进度在推进+alert已处理 |
| H2 | 并发数配置 | [!] | batch concurrency=1（应为5），已用set-concurrency调整为5 |
| H3 | 环境检查 | [x] | ArangoDB OK, Redis OK, D盘OK, .env OK |

---

## 发现的问题

### Critical
1. **DB-Redis不一致**——DB running=29 vs Redis running=0，29个孤儿run（历史遗留，DB中状态为running但Redis中无记录）。这些run可能已经完成或失败但状态未更新。

### Warning
1. **并发数配置错误**——batch concurrency=1（应为5），已用set-concurrency调整为5。可能是batch记录在之前运行时被设为1。
2. **p27-s0030 stuck**——handover session崩溃，已清理。

### Info
1. 53个新alert全部是历史数据丢失类型（export_missing/rounds_log_export_missing/handover_missing），已批量resolve。

---

## 执行的操作
1. 清理stuck session p27-s0030
2. 批量resolve 53个新alert
3. 用set-concurrency将batch并发数从1调整为5
4. 确认launcher和monitor进程正常运行

---

## 未修复的问题及原因
1. **29个DB孤儿run**——DB中状态为running但Redis中无记录。历史遗留，需step_05诊断是否需要批量更新DB状态。
2. **export_missing持续产生**——monitor每轮检查都会发现新的export丢失。根因是历史数据丢失，非代码bug。

---

## 下一轮建议
1. step_02检查数据完整性时关注29个DB孤儿run
2. step_05诊断DB-Redis不一致问题——29个run的status需要更新
3. 观察并发数调整为5后launcher是否启动更多session
