# AI-Math-Solving-Trajectories

AI 数学竞赛题解题系统**当前世代**的每题运行现场归档：p27 生产续传管线、v2 递归消化链
管线（开发中）与 SOP 报表的原始运行数据。

> 分工：系统代码/架构/SOP 见
> [AI-Math-Competition-Problem-Solving-System](https://github.com/math-fournity/AI-Math-Competition-Problem-Solving-System)；
> 早期世代 5 万+ run 归档见
> [AI-Math-Solving-Trajectories-Archive](https://github.com/math-fournity/AI-Math-Solving-Trajectories-Archive)；
> 数据表见 [AI-Math-Solving-Databases](https://github.com/math-fournity/AI-Math-Solving-Databases)。

## 目录结构

| 目录 | 内容 |
|---|---|
| `p27-continuation/` | 生产续传管线每题轨迹目录：`exports/conversation.json`（含 thinking 的对话录）、`sessions_db/trajectory.jsonl`（会话轨迹事件流）、`collector/`（终端面板快照）、`session_info.json`、`tmux/`（原始终端日志） |
| `p27-workdirs/` | 每题解题工作目录：`problem.txt`（题面）、`round{N}_prompt.txt`、`round{N}_HANDOVER.md`、归档 proof 等 |
| `v2-continuation/` | v2 管线（OpenCode ACP + 观察者/解题者递归消化链）运行现场 |
| `p27-sop-reports/` | Master Agent SOP 循环的每轮报表（report.md/snapshot/check_output） |

run 目录命名：`p27-full-<problem_id>`（批次 p27-full 下的题）。早期系统曾有"DB 记录
完成但硬盘缺失产出"的教训，因此本仓库与数据表中的 `rounds_log` 记录互为对账依据：
以硬盘实物为最终真值。

## 数据说明

- 对话录（conversation.json）为 AI 解题过程的结构化导出（含 reasoning_content），
  是分析 AI 数学解题能力边界的第一手数据。
- 公开化处理：数据中出现的本地目录名（工作环境路径）已统一替换为中性名称，其余
  内容未改动；凭据模式扫描零命中。
- 本仓库数据为程序运行记录与 AI 对话，不含 API 密钥/凭据（已做凭据模式扫描）。
  mitm 代理原始流量捕获（可能含请求头凭据）未纳入上传，仅保留在本地。
- 资产保留铁律：本地原目录中的全部 run 产物（含未上传的 mitm 原始流）永不删除。

## License

MIT License，见 [LICENSE](LICENSE)。
