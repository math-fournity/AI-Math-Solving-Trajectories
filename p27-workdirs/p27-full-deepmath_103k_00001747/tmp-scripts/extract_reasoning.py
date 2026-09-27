#!/usr/bin/env python3
"""从round1_export.json提取agent step的reasoning_content到文本文件，便于分段阅读。"""
import json
import sys

export_path = sys.argv[1] if len(sys.argv) > 1 else "round1_export.json"
out_path = sys.argv[2] if len(sys.argv) > 2 else "round1_reasoning.txt"

with open(export_path, "r", encoding="utf-8") as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]

with open(out_path, "w", encoding="utf-8") as out:
    for i, s in enumerate(agent_steps):
        rc = s.get("reasoning_content", "") or ""
        msg = s.get("message", "") or ""
        tc = s.get("tool_calls", []) or []
        out.write(f"===== AGENT STEP {i} =====\n")
        out.write(f"step_id={s.get('step_id')} message_len={len(msg)} tool_calls={len(tc)}\n")
        out.write(f"reasoning_content_len={len(rc)}\n")
        out.write("----- REASONING_CONTENT -----\n")
        out.write(rc)
        out.write("\n----- END REASONING_CONTENT -----\n")
        if msg:
            out.write("----- MESSAGE -----\n")
            out.write(msg)
            out.write("\n----- END MESSAGE -----\n")
        if tc:
            out.write("----- TOOL_CALLS -----\n")
            out.write(json.dumps(tc, ensure_ascii=False, indent=2))
            out.write("\n----- END TOOL_CALLS -----\n")

print(f"提取完成: {out_path}")
print(f"agent step数: {len(agent_steps)}")
