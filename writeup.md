# Lost in the Middle: Context Retrieval Accuracy

## Overview

This project presents a small-scale exploratory experiment investigating whether a large language model’s ability to retrieve factual information depends on where that information appears within a long context.

Specifically, we test whether factual retrieval accuracy degrades when target information is placed in the middle of a document, compared to the beginning or the end.

This experiment is intentionally small-scale and serves as a first-pass validation of feasibility before scaling to larger datasets and formal statistical analysis.

---

## Experimental Design

We generate synthetic company-style documents describing multiple employees. Each document contains one target employee whose information appears at a controlled position:

- Beginning of the document  
- Middle of the document  
- End of the document  

The model is prompted to extract structured information about the target employee in JSON format. The prompt remains fixed across all conditions; only the position of the target information varies.

---

## Prompt Used

**System Prompt**
