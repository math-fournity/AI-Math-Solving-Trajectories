#!/usr/bin/env python3
"""Extract reasoning_content from round1_export.json for HANDOVER.md creation."""
import json
import sys

path = "/Volumes/data/math-agent-glm5.2-tmux-agents-dir/p27-continuation/p27-full-deepmath_103k_00030233/round1_export.json"
with open(path) as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]
print(f"Total steps: {len(steps)}, agent steps: {len(agent_steps)}")
for i, s in enumerate(agent_steps):
    rc = s.get("reasoning_content", "") or ""
    msg = s.get("message", "") or ""
    tc = s.get("tool_calls", []) or []
    metrics = s.get("metrics", {}) or {}
    print(f"agent_step[{i}]: rc={len(rc)}c msg={len(msg)}c tc={len(tc)} comp={metrics.get('completion_tokens')}")
    # Write rc to file
    out = f"/Volumes/data/math-agent-glm5.2-tmux-agents-dir/p27-continuation/p27-full-deepmath_103k_00030233/tmp-scripts/agent_step_{i}_rc.txt"
    with open(out, "w") as g:
        g.write(rc)
    print(f"  -> wrote {out}")
