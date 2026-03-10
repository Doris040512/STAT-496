from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
IN_PATH = BASE_DIR / "outputs" / "results.csv"
OUT_DIR = BASE_DIR / "outputs" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

if not IN_PATH.exists():
    raise FileNotFoundError(f"Could not find {IN_PATH}. Run evaluate_results.py first.")

df = pd.read_csv(IN_PATH)

pos_order = ["begin", "middle", "end"]

# -----------------------------
# 1) Exact match accuracy
# -----------------------------
exact_df = df[df["field"] == "ALL_FIELDS"].copy()
exact_df["position"] = pd.Categorical(exact_df["position"], categories=pos_order, ordered=True)

exact_acc = exact_df.groupby("position", observed=False)["correct"].mean().reindex(pos_order)

plt.figure(figsize=(6, 4))
plt.bar(exact_acc.index.astype(str), exact_acc.values)
plt.ylim(0, 1.05)
plt.xlabel("Position of target information")
plt.ylabel("Exact match accuracy")
plt.title("Exact Match Accuracy by Context Position")
plt.tight_layout()
plt.savefig(OUT_DIR / "exact_match_accuracy_by_position.png", dpi=200)
plt.close()

# -----------------------------
# 2) Field-level accuracy
# -----------------------------
field_df = df[df["field"] != "ALL_FIELDS"].copy()
field_df["position"] = pd.Categorical(field_df["position"], categories=pos_order, ordered=True)

field_order = [
    "job_title",
    "department",
    "years_at_company",
    "weekly_hours"
]

field_acc = (
    field_df.groupby(["position", "field"], observed=False)["correct"]
    .mean()
    .reset_index()
)

pivot_field = field_acc.pivot(index="position", columns="field", values="correct").reindex(pos_order)
pivot_field = pivot_field[field_order]

plt.figure(figsize=(8, 5))
for field in field_order:
    plt.plot(
        pivot_field.index.astype(str),
        pivot_field[field],
        marker="o",
        label=field
    )

plt.ylim(0, 1.05)
plt.xlabel("Position of target information")
plt.ylabel("Field-level accuracy")
plt.title("Field-Level Accuracy by Context Position")
plt.legend()
plt.tight_layout()
plt.savefig(OUT_DIR / "field_level_accuracy_by_position.png", dpi=200)
plt.close()

# -----------------------------
# 3) JSON validity
# -----------------------------
json_acc = exact_df.groupby("position", observed=False)["json_valid"].mean().reindex(pos_order)

plt.figure(figsize=(6, 4))
plt.bar(json_acc.index.astype(str), json_acc.values)
plt.ylim(0, 1.05)
plt.xlabel("Position of target information")
plt.ylabel("JSON validity rate")
plt.title("JSON Validity by Context Position")
plt.tight_layout()
plt.savefig(OUT_DIR / "json_validity_by_position.png", dpi=200)
plt.close()

# -----------------------------
# 4) Optional summary table
# -----------------------------
summary = pd.DataFrame({
    "position": pos_order,
    "exact_match_accuracy": exact_acc.values,
    "json_validity": json_acc.values
})

for field in field_order:
    summary[field + "_accuracy"] = pivot_field[field].values

summary.to_csv(OUT_DIR / "summary_metrics_by_position.csv", index=False)

print("Saved figures to:", OUT_DIR)
print(summary)