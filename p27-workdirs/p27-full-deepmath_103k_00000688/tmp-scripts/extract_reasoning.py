#!/usr/bin/env python3
"""临时脚本：从round1_export.json提取agent step的reasoning_content到文本文件。
用途：为编写HANDOVER.md提供原始thinking内容。
用法：python tmp-scripts/extract_reasoning.py
"""
import json
import sys
from pathlib import Path

export_path = Path(__file__).parent.parent / "round1_export.json"
out_path = Path(__file__).parent.parent / "round1_reasoning.txt"

with open(export_path, "r", encoding="utf-8") as f:
    data = json.load(f)

steps = data.get("steps", [])
agent_steps = [s for s in steps if s.get("source") == "agent"]
print(f"Found {len(agent_steps)} agent steps")

for i, s in enumerate(agent_steps):
    rc = s.get("reasoning_content", "") or ""
    msg = s.get("message", "") or ""
    tc = s.get("tool_calls", []) or []
    metrics = s.get("metrics", {}) or {}
    comp = metrics.get("completion_tokens", 0)
    print(f"agent_step[{i}]: rc_len={len(rc)} msg_len={len(msg)} tc={len(tc)} comp={comp}")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(rc)
    print(f"Wrote reasoning_content to {out_path} ({len(rc)} chars)")
