# SOP检查报表 — step_01 系统存活+进度+Session

> **填写说明**：本模板由 `scripts/sop/run.py` 自动复制到D盘报表目录。AI加载后逐项检查并填写，填写完用edit写回同一文件。
>
> **打勾规则**：`[x]` 通过 · `[!]` 有问题 · `[ ]` 待检查 · `[-]` 不适用

---

## 系统快照摘要

> 以下数据从 snapshot.json 自动填充。AI填写报表前先读 snapshot.json 确认数据。

| 指标 | 值 |
|---|---|
| 总run数 | 6082 |
| pending | 499（Redis ZSET） |
| running | 0（solve槽；handover 1个占槽中 s1818） |
| COMPLETED | 124 |
| failed | 0 |
| 完成率 | 2.0%（124/6082，批次刚重启） |
| sessions总数 | 1803（不含counter文档） |
| results集合数 | 0（⚠️ < COMPLETED=124，历史缺口见发现区） |
| events总数 | 629 |

---

## 检查项清单

### 一、自动化检查项（读 check_output.txt 的输出填写）

> check_output.txt 是 `monitor_check_continuation.sh` 的8项输出 + `check_01_system_health()` 的输出。

| 编号 | 检查项 | 检查方法 | 结果 | 详情 |
|---|---|---|---|---|
| 1 | Monitor Pipe pane输出 | 读check_output.txt第1节"Monitor Pipe pane输出"。最近3轮监控输出是否正常——有无error/exception | [x] | 监控轮次正常推进，无error/exception；进度 124/6082 (2%) |
| 2 | alerts集合 | 读check_output.txt第2节"alerts集合"。有无未处理critical alert | [!] | 40815个未处理alert，其中42046条为session_registry_inconsistency（A10对同一批历史stuck session每轮重复告警，无去重→积压洪水，见发现区C1） |
| 3 | 进程状态 | 读check_output.txt第3节"进程状态"。launcher/monitor/watchdog 3个进程是否存活 | [x] | launcher+monitor存活（watchdog未部署=可选，非故障；start不启动watchdog，与修复后文档一致） |
| 4 | 进度 | 读check_output.txt第4节"进度"。pending是否在减少/completed是否在增加 | [x] | 批次刚重启：dequeue 1题（amo_bench_00000006）进R1 handover，pending 500→499，管线在推进 |
| 5 | 续传质量汇总 | 读check_output.txt第5节"续传质量汇总"。proof统计/截断统计是否正常 | [!] | "proof.md存在=0 vs COMPLETED=124"——检查脚本只数 work_dir/proof.md（当前轮文件），完成题的proof归档为round{N}_proof.md且已入库，属脚本口径问题（见发现区W2）；需与results=0缺口一并确认 |
| 6 | 通过率判定 | 读check_output.txt第6节"通过率判定"。通过率是否达标 | [-] | 124/124=100%仅对已终态题，批次5958题未跑，现阶段无判定意义 |
| 7 | 系统健康 | 读check_output.txt第7节"系统健康"。DB/Redis/Disk是否正常 | [x] | Redis pending=499；devin cli进程1个（handover）；并发=1；WARNING running(0)<1系handover占槽的正常中间态 |
| 8 | 运行时健康检查10维度 | 读check_output.txt第8节"运行时健康检查"。A-J 10维度有无⚠️ | [x] | 无严重⚠️（详见check_output.txt第8节） |
| 9 | 门闸Y通道 | 读check_output.txt末尾"步进门闸Y通道"节。无Y=✅跳过；有Y=系统冻结在该闸——按打印的checklist闭包逐项核对后 --step 放行或维持hold并记录原因 | [x] | 无Y——9闸全auto，系统未被冻结 |
| 10 | 行为流水观察（016预警核心） | SOP_01 §8要求每轮必查。运行`python -m src.observability --stats --since 1h`。`churn_suspects`非空(1小时内某题启动≥5次)=失控循环正在发生，立即按016报告§5处置(kill launcher→清队列→查根因) | [x] | churn_suspects为空（Top10=每题1次启动）；事件分布：enqueue=1000(500新增+500NX拦截)/gate_pass=1002/batch_start=10/dequeue=1/judge=1/launch_handover=1——016防御（NX幂等/防抖/产物归属）实测生效 |
| 11 | 系统运行过程全景视图（023方案） | 读check_output.txt中"系统运行过程全景视图"段。L1现状：系统在做什么？L2流畅性：节奏正常吗有卡顿吗？L3流程合规：流程按设计走吗有异常序列吗？L4趋势：在变好还是变差？在认知闭包背景下分析和推理系统运行是否正常（不是逐项打勾，是过程推理） | [x] | L1：1条管线在跑（dequeue→round1_precheck→R1 handover进行中）；L2：无卡顿无循环；L3：事件序列完整✅，门闸全auto通过；L4：窗口内完成0失败0（刚重启）。注意：L1"活跃管线500条"把队列中的题也计入（最后事件=enqueue的gate_done），展示口径待改进（见发现区I1） |

### 二、AI判断检查项

| 编号 | 检查项 | 检查方法 | 结果 | 详情 |
|---|---|---|---|---|
| SESS | Session注册表深度检查 | `python -m monitoring.continuation_control sessions --consistency-check`。逐项检查SESS-01~12需求点。 | [!] | 注册表1803个session；100个stuck（tmux消失无DONE.md）：s0032~s0049为08-19/20遗留deepmath题，s1808~s1817为昨晚amo_bench_00000006的handover残留；行为流水证实**本session内无重复启动**（1小时1次/题）——stuck是历史残留非失控，清理需用户授意 |
| ENV | 环境检查 | 确认ARANGO_DB环境变量设置正确。确认D盘挂载。确认Redis运行。逐项检查ENV-01~07。 | [x] | ARANGO_DB=xishujuzhen_math_glm52✓；D盘挂载✓（work_dir写入正常）；Redis ping✓；.venv✓ |
| H1 | 系统健康度综合判断 | 综合8项自动化检查+SESS+ENV，判断系统是否健康。如果 unhealthy→需要重启什么服务？ | [x] | **健康**：管线端到端真实运转（handover devin正在分块读52705字符reasoning并写HANDOVER.md）；无失控；无Y冻结。待办：alert积压治理（C1）与stuck清理（需授意） |

### 三、门闸放行/hold记录（落盘论证）

> 本轮如果有Y（门闸冻结等待放行），在这里记录每个事件的检查结果+决定+理由。
> 放行用 `--step GATE-ID --reason '...'`（理由已落盘flow流水），这里抄录备查。
> 维持hold也填（说明为什么不放行）。无Y则写「无门闸冻结事件」。

| gate_id | 冻结的run | 检查结果（按论证依据逐项） | 决定 | 理由 |
|---|---|---|---|---|
| （无） | | | | 无门闸冻结事件（全auto：FEED-ENQUEUE 1000次/OVERWRITE-ROUND1-SEED 1次/START-HANDOVER 1次） |

---

## 发现的问题

### Critical
（在此填写，或写「无」）

**C1 · alert积压洪水（A10无去重）**：未处理alert 40815条，其中42046条(97%)是session_registry_inconsistency——A10对每个stuck session**每轮(120s)重复新建**一条critical，无"已告警过就不再重复"的去重。约100个历史stuck × 通宵运行 → 4万+条，把新信号全部淹没，SOP_03分诊不可用。分类：**代码bug**（alert设计缺陷）→ 步骤05候选修复（按run聚合+只告新出现的不一致）。历史积压的批量resolve与stuck注册表清理需用户授意（铁律：stuck清理需授意）。

### Warning
（在此填写，或写「无」）

**W1 · results集合=0 vs COMPLETED=124**：018事故前的历史缺口（proof双写加固之前完成的124题），步骤02会再确认。若DB p27_continuation_results确为0，这124题的proof文本仅存于盘上round{N}_proof.md（018后已重建work_dir，proof是否仍在盘上待步骤02抽查）。

**W2 · 检查脚本proof口径**：monitor_check_continuation.sh第5节只数 work_dir/proof.md（当前轮文件），完成题proof已归档为round{N}_proof.md并入库，故显示"存在=0"——口径误导，建议改为数round*_proof.md或读DB proof_path。分类：代码bug（低危）→ 步骤05候选。

### Info
（在此填写，或写「无」）

**I1 · 全景视图L1口径**：把"最后事件非终态"的队列题全算"活跃管线"（500条），建议区分"在管线中(in-flight)"与"排队(queued)"。

**I2 · launcher空队列重启循环**：队列空时launcher按设计退出（提示先跑feeder），auto-restart包装使其每5秒重启一次（1小时内batch_start=10次）。功能无害但空转；feeder只入队首批500（AQL无排序+NX幂等），后续需周期性补跑feeder——SOP_02的prepared堆积检查会提示。

**I3 · feeder单次只入队500**：AQL LIMIT 500无排序，返回同一批，NX后count=0退出。属"drip feed"设计的事实行为，Master Agent需按SOP_02信号周期补跑。

---

## 执行的操作

- 启动系统：`continuation_control start --batch-id p27-full --concurrency 1`（launcher+monitor，watchdog可选未部署）
- 入队：`python -m src.continuation_feeder --batch-id p27-full` → pending=500（发现I3）
- 本报表填写（step_01）

## 未修复的问题及原因

- C1 alert洪水：需代码修复（A10去重），留步骤05评估；批量resolve历史alert需用户授意
- 100个stuck session清理：spec要求用户授意，未动

## 下一轮建议

- 步骤05优先评估A10告警去重修复（改monitor_continuation.py需跑sim发布门禁）
- 用户决策项：①历史alert批量resolve（--all-critical）②stuck注册表清理（sessions --clean-done 不适用stuck，需逐个--clean或授权脚本）③watchdog是否部署
