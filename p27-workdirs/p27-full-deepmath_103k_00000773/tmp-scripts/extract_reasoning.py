#!/usr/bin/env python3
"""从round1_export.json提取agent step的reasoning_content到独立文件，便于分段阅读。"""
import json
import sys

export_path = sys.argv[1] if len(sys.argv) > 1 else "round1_export.json"
out_path = sys.argv[2] if len(sys.argv) > 2 else "round1_reasoning.txt"

with open(export_path, "r", encoding="utf-8") as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]

with open(out_path, "w", encoding="utf-8") as f:
    for i, s in enumerate(agent_steps):
        rc = s.get("reasoning_content", "") or ""
        msg = s.get("message", "") or ""
        tc = s.get("tool_calls", []) or []
        metrics = s.get("metrics", {}) or {}
        f.write(f"=== AGENT STEP {i} ===\n")
        f.write(f"step_id={s.get('step_id')} timestamp={s.get('timestamp')}\n")
        f.write(f"message_len={len(msg)} reasoning_len={len(rc)} tool_calls={len(tc)}\n")
        f.write(f"metrics={json.dumps(metrics)}\n")
        f.write(f"--- REASONING_CONTENT ---\n")
        f.write(rc)
        f.write(f"\n--- END REASONING_CONTENT ---\n")
        if msg:
            f.write(f"--- MESSAGE ---\n{msg}\n--- END MESSAGE ---\n")
        if tc:
            f.write(f"--- TOOL_CALLS ---\n{json.dumps(tc, ensure_ascii=False, indent=2)}\n--- END TOOL_CALLS ---\n")
        f.write("\n")

print(f"Extracted {len(agent_steps)} agent step(s) to {out_path}")
