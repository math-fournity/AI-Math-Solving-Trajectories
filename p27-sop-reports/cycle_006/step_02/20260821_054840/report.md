# SOP检查报表 — step_02 数据完整性

> **填写说明**：本模板由 `scripts/sop/run.py` 自动复制到D盘报表目录。AI加载后逐项检查并填写，填写完用edit写回同一文件。
>
> **打勾规则**：`[x]` 通过 · `[!]` 有问题 · `[ ]` 待检查 · `[-]` 不适用
>
> **报表目录**：`{REPORT_DIR}/`（含本文件 + snapshot.json + snapshot_runs.json + check_output.txt）

---

## 系统快照摘要

> 以下数据从 snapshot.json 自动填充。AI填写报表前先读 snapshot.json 确认数据。

| 指标 | 值 |
|---|---|
| 总run数 | （从snapshot.json的aggregate.total_runs读取） |
| COMPLETED | （从snapshot.json的aggregate.completed读取） |
| 完成率 | （从snapshot.json的aggregate.completion_rate读取） |
| results集合 | （从snapshot.json的aggregate.results_collection_count读取） |
| events总数 | （从snapshot.json的aggregate.events_total读取） |
| sessions总数 | （从snapshot.json的aggregate.sessions_total读取） |

### 按题源完成率

> 从 snapshot.json 的 by_source 读取，填入下表。

| 题源 | 总数 | 完成 | 完成率 | 备注 |
|---|---|---|---|---|
| （src） | （total） | （completed） | （rate） | （填写：0%的写"系统性问题"，正常的留空） |

### per-run明细

> snapshot_runs.json 包含全部919条run的明细数据。每条含：
> `problem_id` / `status` / `final_status` / `rounds_count` / `current_round` / `last_method` / `last_completed` / `last_truncated` / `updated_at` / `work_dir`
>
> 需要查某道题的状态时，用 `python3 -c "import json; runs=json.load(open('snapshot_runs.json')); [print(r) for r in runs if r['problem_id']=='XXX']"` 查询。

---

## 检查项清单

### 一、自动化检查项（读 check_output.txt 的输出填写）

> check_output.txt 是 `check_02_data_integrity()` 的完整stdout输出。逐项读输出，填写结果。

| 编号 | 检查项 | 检查方法 | 结果 | 详情 |
|---|---|---|---|---|
| F1 | rounds_log 6个路径字段文件存在性 | 读check_output.txt中"数据完整性检查"节的issues列表。每个问题格式：`[pid R{N}] {输入/输出} {字段} 文件不存在: {路径}` | [!] | 200个run查出967个问题——全部为**018事故已记录的永久损失**（teardown误删生产目录，R2产物export/prompt/handover/map/prev_export/proof丢失），非新发生；重建的work_dir/problem.txt正常 |
| F2 | 文件大小检查 | 读check_output.txt中issues列表中"文件过小"的问题 | [x] | 无 |
| F3 | export JSON格式 | 读check_output.txt中issues列表中"不是JSON格式"的问题 | [x] | 无 |
| F4 | proof.md内容质量 | 读check_output.txt中issues列表中"proof.md内容过短"的问题 | [-] | 新产proof无可读样本（见Q1） |
| F5 | HANDOVER.md内容质量 | 读check_output.txt中issues列表中"HANDOVER.md内容过短"的问题 | [x] | 无（本轮新生成的round1_HANDOVER.md正常，devin cli真实产出） |
| F6 | prompt内容质量 | 读check_output.txt中issues列表中"prompt内容过短"的问题 | [x] | 无 |
| Q1 | proof.md质量统计(RUN-05) | 读check_output.txt中"proof.md 质量统计"节。关注：存在率<100%？boxed率<100%？ | [!] | proof存在=0/124——018前完成的124题盘上proof已永久丢失（018报告结论），本轮新生成proof尚未落盘（amo_bench R2解题中） |
| Q2 | results集合检查 | 读check_output.txt中"results 集合检查"节。results数<COMPLETED数→critical | [!] | results=0 < COMPLETED=124——proof双写加固(018后)之前的历史缺口，无法回补（文本已不存在）；今后新完成题会自动双写 |
| Q3 | events完整性检查 | 读check_output.txt中"events 完整性检查"节。有launched无completed/failed的run→warning | [!] | 28个run有launched无end——对应历史强制停止/崩溃（昨晚stop等），事件历史不完整但run状态已收敛，不影响后续 |
| Q4 | prepared堆积检查 | 读check_output.txt中"prepared 堆积检查"节。prepared>0但pending=0→critical | [x] | prepared=5957 vs pending=499——feeder单次只入队首批500（AQL无排序+NX），需周期补跑；非feeder故障（pending>0且在消耗） |
| Q5 | 按题源完成率统计 | 读check_output.txt中"按题源完成率统计"节。完成率=0%的题源→critical | [x] | 8源0%为**"还没跑到"**：昨晚只处理了deepmath段（124/1305=9.5%），3973道polymath等全部prepared未消费。批次刚重启，非系统性失败信号，持续观察 |
| Q6 | 标准文件检查 | 读check_output.txt中"标准文件检查"节。problem.txt/proof.md/round1 export缺失 | [x] | 100个run抽查全部正常 |
| Q7 | round编号连续性 | 读check_output.txt中"round 编号连续性检查"节。正常轮序[1,2,3..]连续（round-1补录修复后）；出现重复轮号(如[2,2,3])=旧数据或bug复发，应排查。详见SOP_02 round-1说明 | [!] | 50/50从round=2开始（018前旧数据，无R1补录）；**风险预判**：这些run被重新消费时launcher按len(rounds_log)+1算current_round会再跑R2→rounds_log出现[2,2]重复轮号→将触发rounds_log_duplicate_round告警波。建议SOP_05评估：重置此类run的rounds_log或消费前补录R1 |

### 二、AI判断检查项（需要AI主动执行检查）

| 编号 | 检查项 | 检查方法 | 结果 | 详情 |
|---|---|---|---|---|
| 2a | DB记录vs文件一致性 | 抽查几个COMPLETED的run，确认proof_path指向的文件确实存在。用snapshot_runs.json找到COMPLETED的run，读work_dir，检查proof.md。 | [!] | deep_checks_02：COMPLETED抽查5/5 proof_path不存在（018损失）；prepared抽查work_dir+problem.txt全✅（collector重建有效） |
| 2b | Redis队列vs DB status | `python3 -c "from src.continuation_redis_queue import get_redis, pending_count, running_count; r=get_redis(); print(f'pending={pending_count(r)} running={running_count(r)}')"` 对比DB中prepared数 | [x] | pending=499 running=1（amo_bench R2 solve真实占槽s1819） |
| 2c | Session注册表完整性 | `python3 -c "from src.continuation_db_schema import connect_db; from src.session_registry import list_sessions; db=connect_db(); sessions=list_sessions(db, status='running', limit=20); [print(s) for s in sessions]"` 检查running session的export_path父目录是否存在 | [x] | s1819 export父目录✅；发现小瑕疵：stuck session的notes字段每轮重复追加"tmux session消失但无DONE.md"（s1817已3+条），无上限增长 |
| 2d | 事件流完整性确认 | 读Q3中列出的有launched无end的run。用snapshot_runs.json查这些run的status——如果status=running→正常（还在跑）；如果status=completed/dead_session→异常（事件丢失） | [x] | 28个run的当前status=prepared（等待重跑）——事件断在历史强停点，状态已收敛，记录不修 |
| 2e | 跨题目模式分析 | 读Q5的按题源完成率。0%的题源：诊断原因（都是prepared没跑到？还是跑了都失败？还是都truncated？）。用snapshot_runs.json按题源分组查status分布。 | [x] | 见Q5：全部"prepared未跑到"，唯一有终态的deepmath 9.5%。真正的题源能力差异要等各源被消费后才有数据 |

---

## 发现的问题

### Critical

> 填写critical级别的问题（数据丢失/系统无法运行/系统性错误），或写「无」

**C1 · 018历史数据损失（已知，非新发）**：124个COMPLETED的proof/export/per-round产物永久丢失+results集合=0（双写加固前完成）。处置：接受损失（018报告已定论）；**新完成题自动双写**——本轮 amo_bench_00000006 R2 若完成将首次走 finalize→insert_result 双写路径，是加固有效性的首个实战样本。

### Warning

> 填写warning级别的问题（字段缺失/不一致但不影响运行），或写「无」

**W1 · 旧数据rounds_log无R1补录的重跑重复风险**：见Q7——被重新消费时会出现[2,2]重复轮号告警波。建议步骤05评估消费前清理旧rounds_log（涉及判定逻辑，需sim门禁）。

**W2 · stuck session notes无上限追加**：见2c，小瑕疵累积性污染注册表数据。

**W3 · report模板"919条run"过时**：docs/sop/templates/report_step_02.md硬编码919，应为动态数（本批6082）——步骤06顺带修。

### Info

> 填写info级别的问题（需要确认但不影响运行），或写「无」

（在此填写）

---

## 执行的操作

> 填写本轮做了什么修复/重启/重跑等操作。每个操作记录：做了什么、为什么、改了哪些文件、commit hash。或写「无操作」

（在此填写）

---

## 未修复的问题及原因

> 填写哪些问题没修，为什么没修（需要更多信息/需要用户决策/超出本轮范围）。或写「无」

（在此填写）

---

## 下一轮建议

> 填写下一轮SOP循环需要关注什么。或写「无」

（在此填写）
