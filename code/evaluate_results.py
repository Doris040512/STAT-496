import json
import csv
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PRED_DIR = BASE_DIR / "outputs" / "model_outputs"
TRUTH_PATH = BASE_DIR / "Truth" / "ground_truth.jsonl"
OUT_CSV = BASE_DIR / "outputs" / "results.csv"

def extract_json_from_raw(raw):
    if raw is None:
        return None

    s = str(raw)


    s = s.replace("```json", "").replace("```", "")


    s = s.replace("\\n", "\n")


    start = s.find("{")
    end = s.rfind("}")
    if start == -1 or end == -1:
        return None

    candidate = s[start:end+1]

    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        print("JSON parse failed for:", candidate)
        return None

def norm_num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return int(x)
    m = re.search(r"\d+", str(x))
    return int(m.group()) if m else None

def norm_str(x):
    if x is None:
        return None
    return " ".join(str(x).strip().lower().split())

def field_equal(field, pred_val, true_val):
    if field in ["weekly_hours", "years_at_company"]:
        return norm_num(pred_val) == norm_num(true_val)
    return norm_str(pred_val) == norm_str(true_val)

truth = {}
target_names = {}

with open(TRUTH_PATH, "r", encoding="utf-8") as f:
    for line in f:
        row = json.loads(line)
        truth[row["doc_id"]] = row["ground_truth"]
        target_names[row["doc_id"]] = row.get("target_name")



rows = []

for pred_file in PRED_DIR.glob("*.json"):
    doc_id = pred_file.stem

    if "begin" in doc_id:
        position = "begin"
    elif "middle" in doc_id:
        position = "middle"
    else:
        position = "end"

    with open(pred_file, "r", encoding="utf-8") as f:
        wrapper = json.load(f)

    pred_obj = wrapper if isinstance(wrapper, dict) and any(k in wrapper for k in ("job_title","department","years_at_company","weekly_hours")) else extract_json_from_raw((wrapper.get("_raw") or wrapper.get("raw")) if isinstance(wrapper, dict) else None)
    json_valid = pred_obj is not None

    all_correct = True

    for field, true_val in truth[doc_id].items():
        pred_val = pred_obj.get(field) if json_valid else None

        ok = field_equal(field, pred_val, true_val)
        if not ok:
            all_correct = False

        rows.append({
            "doc_id": doc_id,
            "position": position,
            "field": field,
            "predicted": pred_val,
            "truth": true_val,
            "correct": int(ok),
            "json_valid": int(json_valid)
        })

    rows.append({
        "doc_id": doc_id,
        "position": position,
        "field": "ALL_FIELDS",
        "predicted": "",
        "truth": "",
        "correct": int(all_correct),
        "json_valid": int(json_valid)
    })

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "doc_id","position","field",
            "predicted","truth",
            "correct","json_valid"
        ]
    )
    writer.writeheader()
    writer.writerows(rows)

print("Saved", OUT_CSV)
