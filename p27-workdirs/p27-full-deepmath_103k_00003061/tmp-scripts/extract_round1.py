#!/usr/bin/env python3
"""Extract agent step content from round1_export.json for HANDOVER.md production."""
import json
import sys

EXPORT = "/Volumes/data/math-agent-glm5.2-tmux-agents-dir/p27-continuation/p27-full-deepmath_103k_00003061/round1_export.json"
OUT_DIR = "/Volumes/data/math-agent-glm5.2-tmux-agents-dir/p27-continuation/p27-full-deepmath_103k_00003061/tmp-scripts"

with open(EXPORT) as f:
    data = json.load(f)

# Find agent steps
agent_steps = [s for s in data.get("steps", []) if s.get("source") == "agent"]
print(f"Total steps: {len(data['steps'])}")
print(f"Agent steps: {len(agent_steps)}")

for i, s in enumerate(agent_steps):
    msg = s.get("message", "") or ""
    rc = s.get("reasoning_content", "") or ""
    tc = s.get("tool_calls", []) or []
    metrics = s.get("metrics", {}) or {}
    print(f"\n=== Agent step {i} ===")
    print(f"  message len: {len(msg)}")
    print(f"  reasoning_content len: {len(rc)}")
    print(f"  tool_calls: {len(tc)}")
    print(f"  completion_tokens: {metrics.get('completion_tokens')}")
    print(f"  prompt_tokens: {metrics.get('prompt_tokens')}")

    # Write message
    with open(f"{OUT_DIR}/agent_msg_{i}.txt", "w") as out:
        out.write(msg)
    # Write reasoning_content
    with open(f"{OUT_DIR}/agent_rc_{i}.txt", "w") as out:
        out.write(rc)
    # Write tool_calls
    with open(f"{OUT_DIR}/agent_tc_{i}.json", "w") as out:
        json.dump(tc, out, ensure_ascii=False, indent=2)

print("\nDone. Files written to tmp-scripts/")
