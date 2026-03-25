# Lost in the Middle: Context Retrieval Accuracy in Large Language Models

STAT 496 Final Project  
University of Washington  
Authors: Yijing Chen, Shuozishan Wang, Chenyi Wang  

---

## Overview

Large language models are often used to extract structured information from long documents.  
However, recent research suggests that models may not use all parts of a long context equally well.  
In particular, retrieval performance may decrease when relevant information appears in the middle of the input sequence.

This project studies whether structured extraction accuracy depends on the position of the relevant information inside a document.

We design a controlled experiment where the same type of information appears at different positions:

- Beginning  
- Middle  
- End  

We then measure whether extraction accuracy changes across positions.

This experiment is inspired by the **Lost in the Middle** phenomenon in long-context LLM research.

---

## Research Question

Does the accuracy of structured extraction decrease when the target information appears in the middle of a long document rather than at the beginning or end?

---

## Task Description

Each document describes multiple fictional employees.

The model must extract information about one target employee:

- job_title  
- department  
- years_at_company  
- weekly_hours  

The model must return valid JSON only.

Example output:

```json
{
  "job_title": "Data Analyst",
  "department": "Finance Analytics",
  "years_at_company": 3,
  "weekly_hours": 40
}
