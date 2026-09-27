#!/usr/bin/env python3
"""Extract the problem text from round1_export.json."""
import json

path = "/Volumes/data/math-agent-glm5.2-tmux-agents-dir/p27-continuation/p27-full-deepmath_103k_00030233/round1_export.json"
with open(path) as f:
    data = json.load(f)

steps = data.get("steps", [])
# Look for the problem in all steps' messages
for i, s in enumerate(steps):
    msg = s.get("message", "") or ""
    if "Iwah" in msg or "non-archimedean" in msg or "Problem" in msg:
        print(f"=== steps[{i}] source={s.get('source')} (len={len(msg)}) ===")
        # Find the problem section
        idx = msg.find("Problem")
        if idx >= 0:
            print(msg[idx:idx+3000])
        else:
            idx = msg.find("Iwah")
            if idx >= 0:
                print(msg[max(0,idx-500):idx+2500])
        print("---END---")
