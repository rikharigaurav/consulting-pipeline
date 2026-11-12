#!/usr/bin/env python3
"""PreToolUse hook: refuse any write to a signed file. Enforces G2.

Claude Code passes the tool call as JSON on stdin. We read file_path and deny
if it matches a signed artifact. Exit 0 with a deny decision, so the refusal
carries a reason the agent can act on.
"""
import json, sys, re

SIGNED = re.compile(r"-signed\.[A-Za-z0-9]+$|/v\d+-signed\.", re.I)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)                      # unreadable input: decide nothing

    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
    if path and SIGNED.search(path.replace("\\", "/")):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"G2: {path} is a signed file and is read-only to every agent. "
                "If your work requires contradicting it, stop and write the "
                "conflict to conflicts.md (G6)."),
        }}))
    sys.exit(0)


if __name__ == "__main__":
    main()
