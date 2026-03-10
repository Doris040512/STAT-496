import csv
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
IN_CSV = BASE_DIR / "outputs" / "results.csv"
OUT_CSV = BASE_DIR / "outputs" / "scored_results.csv"

FIELDS = ["job_title", "department", "years_at_company", "weekly_hours"]

by_doc = defaultdict(lambda: {
    "doc_id": "",
    "position": "",
    "json_valid": 0,
    "acc_all": 0,
    **{f"truth_{k}": "" for k in FIELDS},
    **{f"pred_{k}": "" for k in FIELDS},
    **{f"acc_{k}": "" for k in FIELDS},
})

with open(IN_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        doc_id = r["doc_id"]
        field = r["field"]

        rec = by_doc[doc_id]
        rec["doc_id"] = doc_id
        rec["position"] = r["position"]
        rec["json_valid"] = r.get("json_valid", "0")

        if field == "ALL_FIELDS":
            rec["acc_all"] = r["correct"]
            continue

        if field in FIELDS:
            rec[f"truth_{field}"] = r["truth"]
            rec[f"pred_{field}"] = r["predicted"]
            rec[f"acc_{field}"] = r["correct"]


cols = (
    ["doc_id", "position", "json_valid"]
    + [f"truth_{k}" for k in FIELDS]
    + [f"pred_{k}" for k in FIELDS]
    + [f"acc_{k}" for k in FIELDS]
    + ["acc_all"]
)

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for doc_id in sorted(by_doc.keys()):
        w.writerow(by_doc[doc_id])

print("Wrote", OUT_CSV)
