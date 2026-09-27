"""从 round1_export.json 提取 agent step 的 reasoning_content 到纯文本文件，便于阅读。"""
import json
import sys

export_path = "/Volumes/data/math-agent-glm5.2-tmux-agents-dir/p27-continuation/p27-full-deepmath_103k_00030177/round1_export.json"
out_path = "/Volumes/data/math-agent-glm5.2-tmux-agents-dir/p27-continuation/p27-full-deepmath_103k_00030177/tmp-scripts/round1_reasoning.txt"

with open(export_path, "r", encoding="utf-8") as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]
print(f"agent step 数: {len(agent_steps)}")

for i, s in enumerate(agent_steps):
    rc = s.get("reasoning_content", "") or ""
    msg = s.get("message", "") or ""
    tc = s.get("tool_calls", []) or []
    comp = (s.get("metrics", {}) or {}).get("completion_tokens", 0)
    print(f"agent step {i}: rc={len(rc)}c msg={len(msg)}c tc={len(tc)} comp={comp}")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(rc)
    print(f"reasoning_content 写入 {out_path} ({len(rc)} chars)")
