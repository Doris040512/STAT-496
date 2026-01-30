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
