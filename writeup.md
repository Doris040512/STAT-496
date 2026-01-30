# Lost in the Middle: Context Retrieval Accuracy

## 1. Overview

This project presents a small-scale exploratory experiment investigating whether a large language model’s ability to retrieve factual information depends on where that information appears within a long context.

Specifically, we test whether factual retrieval accuracy degrades when target information is placed in the middle of a document, compared to the beginning or the end. This phenomenon is often informally referred to as “lost in the middle.”

This experiment is intentionally small-scale and exploratory. Its purpose is not to draw definitive statistical conclusions, but to validate the feasibility of the experimental setup, surface meaningful variation in model behavior, and motivate future large-scale automation and analysis.

---

## 2. Experimental Design

We generate synthetic company-style documents describing multiple employees at a fictional organization. Each document contains exactly one **target employee**, whose information appears at a controlled position within the document:

- Beginning of the document  
- Middle of the document  
- End of the document  

Apart from the position of the target employee, document structure and prompt wording remain fixed across all conditions.

The model is prompted to extract structured information about the target employee and return it in JSON format.

---

## 3. Prompt Used

The same prompt is used for all experimental conditions to ensure consistency.

### System Prompt


---

## 4. Model Responses

Across all pilot runs, the model returned syntactically valid JSON outputs. However, the factual correctness of the extracted information varied depending on the position of the target employee in the document.

Common error patterns include:
- Missing fields (e.g., `location`)
- Incorrect attribution of information from nearby distractor employees
- Partial extraction when information is distributed across multiple sentences

These errors were observed more frequently when the target information appeared in the middle of the document.

---

## 5. Results (Small-Scale Pilot)

Each condition contains three synthetic documents. Performance is evaluated using:

- **Field-level accuracy**: proportion of correctly extracted fields  
- **Binary correctness**: whether all fields for a document are correct  

### Pilot Results

| Target Position | Documents | Avg. Field Accuracy | Fully Correct (%) |
|-----------------|-----------|---------------------|-------------------|
| Beginning       | 3         | 0.94                | 66.7%             |
| Middle          | 3         | 0.72                | 33.3%             |
| End             | 3         | 0.89                | 66.7%             |

Even at small scale, the results show a noticeable drop in retrieval accuracy when target information is placed in the middle of the document. This confirms that the experimental setup produces meaningful variation in model behavior.

---

## 6. How Might This Experiment Be Improved?

Several improvements are planned for future iterations:

- Increase the number of documents per condition
- Evaluate accuracy at the individual field level
- Introduce partial credit for near-miss extractions
- Vary output constraints (strict JSON vs free-form summaries)
- Compare multiple language models and decoding parameters

---

## 7. Variables to Be Varied

Future experiments will systematically vary:

- Position of target information (start, middle, end)
- Document length
- Number of distractor employees
- Information density (single paragraph vs distributed across paragraphs)
- Output format constraints
- Model choice and temperature

---

## 8. Scaling and Automation

The experiment is fully automated using a modular pipeline:

1. A document generation script creates synthetic company-style documents and corresponding ground truth.
2. A prompt execution script queries the language model and saves raw outputs.
3. An analysis script compares model outputs against ground truth and computes accuracy metrics.

This pipeline enables scalable data collection, reproducibility, and systematic evaluation across many experimental conditions.

---

## 9. Data and Ground Truth

All documents used in this experiment are synthetically generated. Employee names, roles, and attributes are fictional and do not correspond to real individuals.

Ground truth for each document is stored as a JSON object with the following fields:
- `name`
- `role`
- `department`
- `years_at_company`
- `manager`
- `location`

These values are generated at document creation time and used to compute retrieval accuracy.

---

## 10. Ethical Considerations

No real personal or proprietary data is used in this project. Public company document datasets were referenced only as conceptual scaffolding for document structure and tone. All content is fictional and used solely for research and educational purposes.

