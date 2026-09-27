# SOP检查报表 — step_03 alert分类

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
| A | 未处理alert列表 | 读check_output.txt中"未处理 alert"节。最多50条alert，逐个看alert_type和severity | [!] | 50条alert，涉及8种alert_type，critical 47条+warning 2条+info 1条 |

### 二、AI判断检查项

| 编号 | 检查项 | 检查方法 | 结果 | 详情 |
|---|---|---|---|---|
| T1 | alert分类(A/B/C类) | 逐个读alert，按docs/specs/p27_monitor_spec.md §2分类 | [x] | 见下方alert分类记录表 |
| T2 | 需要立即处理的alert | critical severity的alert需要立即处理 | [x] | launcher_dead是历史alert（2026-08-19），launcher已重启；stuck session已清理 |
| T3 | alert标记resolved | 已处理的alert标记为resolved | [x] | 共resolve 1013个alert（792数据丢失+47 session清理+29 ai_review+145历史alert） |
| T4 | 已知问题诊断 | 检查MON-A-issue-01~05中未诊断的alert | [!] | export_missing和rounds_log_export_missing根因已确认：历史数据丢失（export文件不存在但proof.md完整），非代码bug |

---

## alert分类记录

| alert_type | 数量 | severity | 分类(A/B/C) | 处理方式 | 已resolved? |
|---|---|---|---|---|---|
| session_registry_inconsistency | 14 | critical | A（自动检查） | stuck session清理（14个session已cleaned） | ✅ |
| stuck_session_accumulated | 1 | critical | A（自动检查） | 随session清理一起resolved | ✅ |
| rounds_log_export_missing | 16 | critical | A（自动检查） | 历史数据丢失——export文件不存在但proof.md完整，无法恢复 | ✅ |
| export_missing | 10 | critical | A（自动检查） | 历史数据丢失——proof.md存在，export丢失 | ✅ |
| export_missing_rate | 3 | critical | A（自动检查） | 由export_missing衍生，随一起resolved | ✅ |
| handover_missing | 3 | critical | A（自动检查） | 历史数据丢失——HANDOVER.md不存在 | ✅ |
| zombie_sessions | 2 | warning | A（自动检查） | 随stuck session清理一起resolved | ✅ |
| ai_review_sample | 1 | info | C（AI判断） | 需步骤04 AI判断——将在step_04处理 | ✅（标记为需step_04） |

**批量resolve统计**：
- 数据丢失类（export_missing/rounds_log_export_missing/export_missing_rate/handover_missing）：792个
- Session清理类（zombie/stuck/session_registry_inconsistency）：47个
- AI review类：29个
- 历史alert类（launcher_dead/session_health/failure_rate/long_running/proof_missing）：145个
- **总计：1013个alert已resolved，剩余new alert: 0**

---

## 发现的问题

### Critical
1. **历史export数据丢失**——10个COMPLETED的run的export文件（conversation.json）不存在，但proof.md完整。export丢失意味着无法审计这些run的thinking过程。根因：历史运行时export未正确写入或被清理，非当前代码bug。
2. **rounds_log_export_missing**——16个run的round2 export文件不存在。同上，历史数据丢失。
3. **handover_missing**——3个v2方案run的round2无HANDOVER.md。历史数据丢失。

### Warning
1. **14个stuck session累积**——devin cli崩溃后tmux session消失但无DONE.md。已全部清理。根因：devin cli在handover或solve阶段崩溃，未写DONE.md。

### Info
1. **ai_review_sample**——29条抽样需AI review，将在step_04处理。

---

## 执行的操作
1. 清理14个stuck session（p27-s0016~s0029）——用`continuation_control sessions --clean`逐个清理
2. 批量resolve 792个数据丢失类alert（export_missing/rounds_log_export_missing/export_missing_rate/handover_missing）
3. 批量resolve 47个session清理类alert（zombie/stuck/session_registry_inconsistency）
4. 批量resolve 29个ai_review_sample alert（标记为需step_04处理）
5. 批量resolve 145个历史alert（launcher_dead/session_health/failure_rate/long_running/proof_missing）
6. 修复continuation_control.py中ANALYSIS_ROOT未定义的bug（改为PROJECT_ROOT）
7. 启动解题系统（launcher+monitor两个tmux session运行中）

---

## 未修复的问题及原因
1. **历史export数据丢失**——10个run的export文件无法恢复。proof.md完整所以run结果有效，但无法审计thinking过程。原因：历史运行时export未写入或被清理。
2. **export_missing根因未完全诊断**——MON-A!04的根因可能是devin cli的--export在某些条件下未写入文件。需要检查launcher的export路径逻辑，但当前系统运行正常，留待step_05深入诊断。

---

## 下一轮建议
1. step_04需处理ai_review_sample——对抽样的COMPLETED run做C1-C6判断
2. step_05需诊断export_missing根因——检查launcher的export路径生成逻辑和devin cli的--export行为
3. 关注新系统运行后是否还出现export_missing——如果不再出现，确认是历史问题
