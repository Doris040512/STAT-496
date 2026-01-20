## 1. The "Sycophancy" Effect: Do LLMs Bow to Authority?
**The Concept:** I want to investigate if LLMs prioritize being "agreeable" over being factually correct. Does the model's error rate change depending on the user's authoritative tone?
**Experimental Design:**
* **Treatment Groups:** 1. Control (Neutral Tone)
    2. Treatment A (Authoritative/Confident Tone)
    3. Treatment B (Confused/Novice Tone)
* **Metric:** Binary outcome (Agree/Disagree with a false premise).
* **Sample Size:** $n=50$ trials per group ($N=150$ total).
* **Statistical Analysis:** I will use a **Chi-Square Test of Independence** to determine if there is a statistically significant association between the user persona and the model's agreement rate. If significant, I will follow up with pairwise Z-tests with Bonferroni correction.
