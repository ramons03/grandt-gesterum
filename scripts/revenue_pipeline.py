#!/usr/bin/env python3
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "templates" / "growth_weekly_dashboard.csv"
OUT = BASE / "reports"
OUT.mkdir(parents=True, exist_ok=True)

rows = []
with DATA.open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

summary = {
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "weeks": len(rows),
    "totals": {
        "leads_new": 0,
        "meetings_booked": 0,
        "demos_done": 0,
        "proposals_sent": 0,
        "won": 0,
        "lost": 0,
        "mrr_new": 0.0
    },
    "rates": {}
}

def to_int(v):
    try:
        return int(v)
    except Exception:
        return 0

def to_float(v):
    try:
        return float(v)
    except Exception:
        return 0.0

for r in rows:
    summary["totals"]["leads_new"] += to_int(r.get("leads_new"))
    summary["totals"]["meetings_booked"] += to_int(r.get("meetings_booked"))
    summary["totals"]["demos_done"] += to_int(r.get("demos_done"))
    summary["totals"]["proposals_sent"] += to_int(r.get("proposals_sent"))
    summary["totals"]["won"] += to_int(r.get("won"))
    summary["totals"]["lost"] += to_int(r.get("lost"))
    summary["totals"]["mrr_new"] += to_float(r.get("mrr_new"))

won = summary["totals"]["won"]
props = summary["totals"]["proposals_sent"]
demos = summary["totals"]["demos_done"]
meetings = summary["totals"]["meetings_booked"]

summary["rates"]["proposal_to_win"] = (won / props) if props else 0.0
summary["rates"]["demo_to_proposal"] = (props / demos) if demos else 0.0
summary["rates"]["meeting_to_demo"] = (demos / meetings) if meetings else 0.0

out_json = OUT / "revenue_summary.json"
out_md = OUT / "revenue_summary.md"

with out_json.open("w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

with out_md.open("w", encoding="utf-8") as f:
    f.write("# Revenue Summary\n\n")
    f.write(f"Generated at UTC: {summary['generated_at_utc']}\n\n")
    f.write("## Totals\n")
    for k, v in summary["totals"].items():
        f.write(f"- {k}: {v}\n")
    f.write("\n## Rates\n")
    for k, v in summary["rates"].items():
        f.write(f"- {k}: {v:.4f}\n")

print(str(out_json))
print(str(out_md))
