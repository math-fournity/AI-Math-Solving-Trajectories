#!/usr/bin/env python3
"""Extract reasoning_content from round1_export.json to a text file for reading."""
import json
import sys

export_path = sys.argv[1]
out_path = sys.argv[2]

with open(export_path, 'r') as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]

with open(out_path, 'w') as f:
    for i, s in enumerate(agent_steps):
        rc = s.get("reasoning_content", "") or ""
        msg = s.get("message", "") or ""
        tc = s.get("tool_calls", []) or []
        f.write(f"=== Agent Step {i} ===\n")
        f.write(f"reasoning_content length: {len(rc)}\n")
        f.write(f"message length: {len(msg)}\n")
        f.write(f"tool_calls count: {len(tc)}\n")
        f.write(f"completion_tokens: {s.get('metrics', {}).get('completion_tokens', 'N/A')}\n")
        f.write("--- REASONING_CONTENT ---\n")
        f.write(rc)
        f.write("\n--- END REASONING_CONTENT ---\n")
        if msg:
            f.write("--- MESSAGE ---\n")
            f.write(msg)
            f.write("\n--- END MESSAGE ---\n")
        for j, t in enumerate(tc):
            f.write(f"--- TOOL_CALL {j} ---\n")
            f.write(json.dumps(t, indent=2, ensure_ascii=False))
            f.write("\n--- END TOOL_CALL ---\n")

print(f"Wrote {out_path}")
print(f"Agent steps: {len(agent_steps)}")
