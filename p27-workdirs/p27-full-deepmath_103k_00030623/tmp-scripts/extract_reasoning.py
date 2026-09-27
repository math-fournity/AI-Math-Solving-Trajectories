#!/usr/bin/env python3
"""从 round1_export.json 提取 agent step 的 reasoning_content 到文件，便于阅读。"""
import json
import sys

export_path = sys.argv[1] if len(sys.argv) > 1 else "round1_export.json"
out_path = sys.argv[2] if len(sys.argv) > 2 else "round1_reasoning.txt"

with open(export_path, "r", encoding="utf-8") as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]
print(f"Total steps: {len(steps)}, agent steps: {len(agent_steps)}")

for i, s in enumerate(agent_steps):
    rc = s.get("reasoning_content", "") or ""
    msg = s.get("message", "") or ""
    tc = s.get("tool_calls", []) or []
    comp = (s.get("metrics", {}) or {}).get("completion_tokens", 0)
    print(f"agent step {i}: rc={len(rc)}c msg={len(msg)}c tc={len(tc)} comp={comp}")
    with open(f"{out_path}.agent{i}.txt", "w", encoding="utf-8") as g:
        g.write(rc)
    print(f"  -> wrote {out_path}.agent{i}.txt ({len(rc)} chars)")
    if msg:
        with open(f"{out_path}.agent{i}.msg.txt", "w", encoding="utf-8") as g:
            g.write(msg)
        print(f"  -> wrote {out_path}.agent{i}.msg.txt ({len(msg)} chars)")
    if tc:
        with open(f"{out_path}.agent{i}.tool_calls.json", "w", encoding="utf-8") as g:
            json.dump(tc, g, ensure_ascii=False, indent=2)
        print(f"  -> wrote {out_path}.agent{i}.tool_calls.json ({len(tc)} calls)")
