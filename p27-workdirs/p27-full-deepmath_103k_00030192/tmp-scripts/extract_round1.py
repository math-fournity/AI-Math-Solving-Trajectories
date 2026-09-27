#!/usr/bin/env python3
"""Extract reasoning_content and message from round1_export.json for HANDOVER.md authoring."""
import json

src = "/Volumes/data/math-agent-glm5.2-tmux-agents-dir/p27-continuation/p27-full-deepmath_103k_00030192/round1_export.json"
with open(src) as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]
print(f"Total steps: {len(steps)}, agent steps: {len(agent_steps)}")

for i, s in enumerate(agent_steps):
    rc = s.get("reasoning_content", "") or ""
    msg = s.get("message", "") or ""
    tc = s.get("tool_calls", []) or []
    comp = (s.get("metrics", {}) or {}).get("completion_tokens", 0)
    print(f"agent_step[{i}]: rc_len={len(rc)} msg_len={len(msg)} tc_len={len(tc)} comp={comp}")
    # write reasoning_content
    with open("round1_reasoning.txt", "w") as f:
        f.write(rc)
    # write message
    with open("round1_message.txt", "w") as f:
        f.write(msg)
    print("Wrote round1_reasoning.txt and round1_message.txt")
