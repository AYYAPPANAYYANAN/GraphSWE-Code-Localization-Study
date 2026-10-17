#!/usr/bin/env python3
"""Compute descriptive localization metrics from a per-task target-rank CSV.

Required columns: task_id,baseline_rank,fixed_rank,conservative_rank
Ranks are positive integers. Blank/0/NA means target not ranked in the evaluated
list. Missing ranks contribute zero to MRR. This script does not rebuild graphs.
"""
import argparse, csv
from pathlib import Path

POLICIES = ("baseline", "fixed", "conservative")
COLUMNS = {"baseline": "baseline_rank", "fixed": "fixed_rank", "conservative": "conservative_rank"}

def parse_rank(value):
    value = (value or "").strip()
    if value.upper() in {"", "NA", "N/A", "NONE", "NULL", "0"}:
        return None
    rank = int(value)
    if rank < 1:
        raise ValueError(f"Ranks must be positive or blank/0/NA, got {value!r}")
    return rank

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("csv_path", help="Path to task-level rank CSV")
    args = ap.parse_args()
    with Path(args.csv_path).open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        required = {"task_id", *COLUMNS.values()}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"Missing columns: {sorted(missing)}")
        rows, seen = [], set()
        for line, raw in enumerate(reader, start=2):
            task = (raw.get("task_id") or "").strip()
            if not task or task in seen:
                raise SystemExit(f"Line {line}: blank or duplicate task_id {task!r}")
            seen.add(task)
            rows.append({"task_id": task, **{p: parse_rank(raw.get(c)) for p, c in COLUMNS.items()}})
    if not rows:
        raise SystemExit("CSV has no task rows; add verified rank data first.")
    n = len(rows)
    print(f"Tasks: {n}\n")
    print(f"{'policy':<16}{'MRR':>10}{'Hit@1':>10}{'Hit@5':>10}{'Hit@10':>10}{'Hit@20':>10}")
    for policy in POLICIES:
        ranks = [r[policy] for r in rows]
        mrr = sum(1 / rank if rank else 0 for rank in ranks) / n
        hits = [sum(rank is not None and rank <= k for rank in ranks) / n for k in (1, 5, 10, 20)]
        print(f"{policy:<16}{mrr:>10.6f}" + "".join(f"{h:>10.6f}" for h in hits))
    print("\nTarget-rank movement vs baseline (both ranks available only):")
    for policy in ("fixed", "conservative"):
        pairs = [(r["baseline"], r[policy]) for r in rows if r["baseline"] is not None and r[policy] is not None]
        improved = sum(after < before for before, after in pairs)
        worsened = sum(after > before for before, after in pairs)
        unchanged = sum(after == before for before, after in pairs)
        print(f"{policy}: comparable={len(pairs)}, improved={improved}, worsened={worsened}, unchanged={unchanged}")
    print("\nAudit task eligibility and source/graph provenance separately; these metrics do not validate either.")

if __name__ == "__main__":
    main()
