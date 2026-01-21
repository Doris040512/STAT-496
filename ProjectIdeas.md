## 1. The "Sycophancy" Effect: Do LLMs Bow to Authority?
**The Concept:** We want to investigate if LLMs prioritize being "agreeable" over being factually correct. Does the model's error rate change depending on the user's authoritative tone?
**Experimental Design:**
* **Treatment Groups:** 1. Control (Neutral Tone)
    2. Treatment A (Authoritative/Confident Tone)
    3. Treatment B (Confused/Novice Tone)
* **Metric:** Binary outcome (Agree/Disagree with a false premise).
* **Sample Size:** $n=50$ trials per group ($N=150$ total).
* **Statistical Analysis:** We will use a **Chi-Square Test of Independence** to determine if there is a statistically significant association between the user persona and the model's agreement rate. If significant, We will follow up with pairwise Z-tests with Bonferroni correction.


## 2. "Lost in the Middle": Context Retrieval Accuracy

**The Concept:**  
We want to investigate whether an LLM’s ability to retrieve a specific fact from a provided context depends on where that fact appears in the input. In particular, we test whether the model is less accurate when the target fact is placed in the middle of a long context compared to the beginning or the end.

**Experimental Design:**

* **Treatment Groups:**  
  1. Target fact placed at the start of the context  
  2. Target fact placed in the middle of the context  
  3. Target fact placed at the end of the context  

* **Metric:**  
  Binary outcome (Correct / Incorrect）

* **Sample Size:**  
  A fixed number of synthetic documents per position, where each document is evaluated once and the target fact is inserted at exactly one position.

* **Statistical Analysis:**  
  We will compare retrieval accuracy across positions using a Chi-square test (or an equivalent proportion-based test). If there is a significant difference, we will follow up with pairwise comparisons to see which positions differ.


## 3. Impact of Chain-of-Thought (CoT) on Ethical Guardrails

**The Concept:**  
We want to investigate whether asking an LLM to reason step by step before answering makes it more likely to refuse ethically questionable (but not explicitly illegal) requests. In particular, we examine whether Chain-of-Thought prompting increases the model’s caution compared to zero-shot prompting.

**Experimental Design:**

* **Treatment Groups:**  
  1. Zero-shot prompting (directly asking the question)  
  2. Chain-of-Thought prompting (explicitly asking the model to think step by step before answering)

* **Metric:**  
  Binary outcome (Refusal / Non-refusal).

* **Sample Size:**  
  A fixed set of borderline ethical prompts, with each prompt evaluated under both prompting strategies.

* **Statistical Analysis:**  
  We will use logistic regression to model the probability of refusal as a function of the prompting strategy (CoT vs. zero-shot). Because each prompt is tested under both conditions, we will account for the paired structure by comparing responses within the same prompt, ensuring that differences are not driven by some prompts being inherently more sensitive than others.
