# Lost in the Middle: Context Retrieval Accuracy

This project presents a small-scale exploratory experiment investigating whether a large language model’s ability to retrieve factual information depends on where that information appears within a long context.

Specifically, we test whether factual retrieval accuracy degrades when target information is placed in the middle of a document, compared to the beginning or the end.

## Experiment Overview

In this first-pass experiment, we generate short synthetic company-style documents describing multiple employees. Each document contains one target employee whose information appears at a controlled position (start, middle, or end). The model is prompted to extract structured information about the target employee in JSON format.

The experiment is intentionally small-scale and exploratory. Its purpose is not to produce definitive statistical results, but to:

- Validate the feasibility of the experimental setup  
- Confirm that the task produces meaningful variation in model behavior  
- Motivate future large-scale automation and statistical analysis  

## Data Source and Scaffolding

To ensure realism in document structure and language, the synthetic documents are loosely inspired by real-world company documentation patterns. Public company document text from Kaggle was used as conceptual scaffolding:

Company Documents Dataset:  
https://www.kaggle.com/datasets/ayoubcherguelaine/company-documents-dataset

No proprietary or personally identifiable information is used. All employee names and details are procedurally generated.

## Repository Contents

- Synthetic document generator
- Python scripts to run prompts through a language model
- Saved model outputs from pilot runs
- Analysis code to evaluate retrieval accuracy and result variability

This repository demonstrates a complete experimental pipeline that can be scaled to larger datasets and more rigorous statistical testing in future work.
