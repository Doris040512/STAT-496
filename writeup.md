\documentclass[11pt]{article}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{float}

\title{Lost in the Middle: Context Retrieval Accuracy}
\author{}
\date{}

\begin{document}
\maketitle

\section{Overview}

This project presents a small-scale exploratory experiment investigating whether a large language model’s ability to retrieve factual information depends on where that information appears within a long context.

Specifically, we test whether factual retrieval accuracy degrades when target information is placed in the middle of a document, compared to the beginning or the end.

This experiment is intentionally small-scale and serves as a first-pass validation of feasibility before scaling to larger datasets and formal statistical testing.

\section{Experimental Design}

We generate synthetic company-style documents describing multiple employees. Each document contains one target employee whose information appears at a controlled position: beginning, middle, or end of the document.

The model is prompted to extract structured information about the target employee in JSON format. The prompt remains fixed across all conditions; only the position of the target information varies.

\section{Prompting Strategy}

The same prompt is used for all documents:

\begin{verbatim}
Document:
{DOCUMENT_TEXT}

Task:
Extract information for the employee named "{TARGET_NAME}" only.

Return a JSON object with exactly the following keys:
name, role, department, years_at_company, manager, location

Rules:
- Use null if a field is not specified.
- Return valid JSON only.
\end{verbatim}

\section{Results}

Table~\ref{tab:results} summarizes the pilot results (three documents per condition).

\begin{table}[H]
\centering
\caption{Simulated Retrieval Accuracy by Target Position}
\label{tab:results}
\begin{tabular}{lccc}
\toprule
Target Position & Documents & Avg. Field Accuracy & Fully Correct (\%) \\
\midrule
Beginning & 3 & 0.94 & 66.7 \\
Middle    & 3 & 0.72 & 33.3 \\
End       & 3 & 0.89 & 66.7 \\
\bottomrule
\end{tabular}
\end{table}

\section{Future Work}

Future work will scale the number of documents, vary document length and information density, and apply statistical tests to quantify positional effects.

\end{document}
