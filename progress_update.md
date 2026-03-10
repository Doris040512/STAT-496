
## Progress Update (Week 8)



This week we focused on stabilizing our extraction pipeline and evaluation so our experimental results are reproducible and correctly scored. We fixed a key issue where model outputs sometimes saved as raw text (e.g., code-fenced JSON) or as direct JSON objects, which previously caused incorrect parsing and accuracy flags. After updating the evaluation script to handle both formats and generating a clearer per-document scoring table, our baseline test cases now produce valid JSON outputs and correct field-level accuracy.



All experiment materials can be found in:

- `code/run_extraction.py` (runs extraction)

- `code/evaluate_results.py` (scores predictions vs. ground truth)

- `code/make_scored_table.py` (creates per-document summary table)

- `prompts/extraction_prompt.txt` (prompt template)

- `truth/ground_truth.jsonl` (ground truth labels)

- `data/documents/` (begin/middle/end documents)

- `outputs/scored_results.csv` (final scored results for current runs)

