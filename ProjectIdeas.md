## 1. The "Sycophancy" Effect: Do LLMs Bow to Authority?
**The Concept:** I want to investigate if LLMs prioritize being "agreeable" over being factually correct. Does the model's error rate change depending on the user's authoritative tone?
**Experimental Design:**
* **Treatment Groups:** 1. Control (Neutral Tone)
    2. Treatment A (Authoritative/Confident Tone)
    3. Treatment B (Confused/Novice Tone)
* **Metric:** Binary outcome (Agree/Disagree with a false premise).
* **Sample Size:** $n=50$ trials per group ($N=150$ total).
* **Statistical Analysis:** I will use a **Chi-Square Test of Independence** to determine if there is a statistically significant association between the user persona and the model's agreement rate. If significant, I will follow up with pairwise Z-tests with Bonferroni correction.

## 2. "Lost in the Middle": Context Retrieval Accuracy

**The Concept:**  
We want to investigate whether an LLM’s ability to retrieve a specific fact from a provided context depends on the position of that fact within the input. In particular, we examine whether retrieval accuracy decreases when the relevant information appears in the middle of a long context, compared to the beginning or the end.

**Experimental Design:**

* **Treatment Groups:**  
  1. Target fact at the start of the context  
  2. Target fact in the middle of the context  
  3. Target fact at the end of the context  

* **Metric:**  
  Binary outcome (Correct / Incorrect retrieval of the target fact).

* **Sample Size:**  
  $n = 30$ trials per position ($N = 90$ total).

* **Statistical Analysis:**  
  We will use a **Chi-Square Test of Independence** to determine whether retrieval accuracy is associated with the position of the target fact within the context. If the test is statistically significant, we will follow up with pairwise proportion tests using Bonferroni correction.

## 3. Impact of Chain-of-Thought (CoT) on Ethical Guardrails

**The Concept:**  
We want to examine whether prompting an LLM to reason step by step using a Chain-of-Thought (CoT) approach affects its likelihood of refusing ethically questionable but not explicitly illegal requests. The hypothesis is that explicit reasoning may increase the model’s tendency to reject such requests.

**Experimental Design:**

* **Treatment Groups:**  
  1. Zero-shot prompting  
  2. Chain-of-Thought prompting  

* **Metric:**  
  Binary outcome (Refusal / No refusal).

* **Sample Size:**  
  A fixed set of ethically ambiguous prompts, with each prompt evaluated under both prompting strategies.

* **Statistical Analysis:**  
  We will compare refusal rates across prompting strategies using a **Chi-Square Test of Independence** or a two-proportion Z-test, depending on sample size assumptions.
