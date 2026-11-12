"""CLI for offline jailbreak evaluations and localhost financial API tests."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .evals import run_evaluations
from .finance import ScopeError, finance_scan, load_scope


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="financial-redteam", description="Authorized synthetic AI red teaming and finance API lab checks")
    cmd = p.add_subparsers(dest="command", required=True)
    e = cmd.add_parser("eval", help="Evaluate instruction boundaries for selected OpenCode models")
    e.add_argument("--model", action="append", required=True, dest="models", help="provider/model-id, repeat up to 5 times")
    e.add_argument("--cases", type=int, default=6, help="1 to 6 safe synthetic scenarios")
    e.add_argument("--timeout", type=int, default=120, help="timeout in seconds for one model call (5–300)")
    e.add_argument("--output", type=Path, default=Path("eval-report.json"))
    s = cmd.add_parser("scan-lab", help="Read-only tests exclusively against the local synthetic API")
    s.add_argument("--scope", type=Path, default=Path("engagement.example.json"))
    s.add_argument("--target", default="http://127.0.0.1:8765")
    s.add_argument("--output", type=Path, default=Path("finance-report.json"))
    a = p.parse_args(argv)
    try:
        if a.command == "eval":
            report = run_evaluations(a.models, a.cases, a.timeout)
        else:
            report = finance_scan(load_scope(a.scope), a.target)
        a.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps({"report": str(a.output), "summary": report.get("summary", report.get("counts"))}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, ScopeError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
