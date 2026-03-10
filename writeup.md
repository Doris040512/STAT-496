# Middle Matters: Measuring Information Loss in Large Language Models

## Project Update

Over the past week, we implemented an end-to-end extraction pipeline for evaluating positional effects in long-context structured retrieval. We constructed synthetic employee documents with controlled placement of target facts (begin, middle, end), implemented prompt templates for JSON-based extraction, and built scripts to run model inference and evaluate outputs against ground truth. All documents, prompts, model outputs, and evaluation scripts are stored in this repository under `data/`, `prompts/`, `code/`, and `outputs/`. Initial baseline experiments were conducted using `gpt-4o-mini` with temperature set to zero. These results establish our experimental framework, which we plan to scale with additional documents and repeated trials in the coming week.

## 1. Introduction
Large language models (LLMs) are increasingly used for information extraction tasks such as summarizing long reports, answering questions from policy documents, and extracting structured fields from unstructured text in enterprise analytics pipelines. For example, organizations now rely on LLMs to extract employee attributes, compliance indicators, or financial metrics from lengthy internal documents. In many of these real-world settings, the user’s question depends on a small number of critical facts that may appear anywhere in a long input.

Our project investigates the “lost in the middle” phenomenon: the hypothesis that LLMs tend to perform better when relevant information appears near the beginning or the end of the context than when it appears in the middle. Prior work has documented positional effects in transformer-based models and observed performance drops for information located in the middle of long contexts. This behavior is important for deployment because many enterprise and scientific workflows rely on LLMs to extract specific attributes from lengthy documents, where key details are often embedded among irrelevant or distracting content.

In our experiments, we design controlled documents where the same target facts are placed at different positions (beginning, middle, end) while holding all other content constant. We then measure extraction accuracy across positions using a structured JSON output format. This approach provides a reproducible way to quantify positional retrieval biases and to evaluate whether prompt constraints and output formatting improve reliability.

## 2. Experimental Design

### 2.1 Task and Data

We use a structured extraction task: given a document describing several employees, the model must extract attributes about a target employee (Alex Chen). The required fields are:
- `job_title`
- `department`
- `years_at_company`
- `weekly_hours`

We create three versions of the same document where the relevant facts about Alex Chen are placed at different locations:
- **begin**: relevant sentence appears near the beginning of the document
- **middle**: relevant sentence appears in the middle
- **end**: relevant sentence appears near the end

The documents are stored in `data/documents/` with filenames:
- `about_us_begin_01.txt`
- `about_us_middle_01.txt`
- `about_us_end_01.txt`

Ground truth labels for each document are stored in `truth/ground_truth.jsonl`, keyed by `doc_id`.

### 2.2 Prompting and Output Format

We prompt the model using a fixed template in `prompts/extraction_prompt.txt`. The prompt instructs the model to only use information explicitly stated in the document, avoid guessing, and return valid JSON with exactly the required keys. The document text is inserted via the placeholder `{{DOCUMENT}}`.

The extraction script (`code/run_extraction.py`) loads each document, fills the prompt template, and queries the model. We set temperature to 0 to reduce randomness. Model outputs are saved per document as JSON files in `outputs/model_outputs/`.

### 2.3 Models and Runs

Our baseline runs use the OpenAI chat completion endpoint with model:
- `gpt-4o-mini`

For each document version (begin/middle/end), we run one extraction trial per document file. (In later stages we will scale up the number of documents and trials to estimate variability and positional effects more robustly.)

In subsequent experiments, we plan to increase both the number of documents and repeated runs per position to enable statistical analysis of positional effects.

### 2.4 Evaluation

We score predictions by comparing model outputs against the ground truth in `truth/ground_truth.jsonl`. Evaluation is performed by `code/evaluate_results.py`, which:
1. Loads ground truth by `doc_id`
2. Loads model outputs from `outputs/model_outputs/`
3. Parses outputs that may be saved either as direct JSON objects or wrapped as raw strings
4. Computes field-level correctness and an overall `ALL_FIELDS` indicator

To make results easier to interpret, we also generate a per-document summary table using `code/make_scored_table.py`, saved as `outputs/scored_results.csv`. Each row corresponds to one document and includes ground truth values, predicted values, per-field accuracy, and overall accuracy (`acc_all`). These metrics allow us to quantify both partial extraction failures and complete retrieval breakdowns across different positional conditions.

## 3. References

1. Liu, Nelson F., Lin, Kevin, Hewitt, John, Paranjape, Ashwin, Bevilacqua, Michele, Petroni, Fabio, & Liang, Percy. (2023). Lost in the middle: How language models use long contexts.
2. Vaswani, Ashish, Shazeer, Noam, Parmar, Niki, Uszkoreit, Jakob, Jones, Llion, Gomez, Aidan N., Kaiser, Lukasz, & Polosukhin, Illia. (2017). Attention is all you need. 


