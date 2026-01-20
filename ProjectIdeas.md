## 1. The "Sycophancy" Effect: Do LLMs Bow to Authority?
**The Concept:** I want to investigate if LLMs prioritize being "agreeable" over being factually correct. My main question is: If I sound like a confident expert, is the model less likely to correct my mistakes than if I sound like a confused beginner?

**Experiment Setup:**
* **What I'm changing (Independent Variable):** The persona in the prompt. I'll test an "Authoritative Expert" tone against a "Confused Novice" tone.
* **What I'm measuring (Dependent Variable):** How often the model agrees with a clearly false statement (e.g., "Given that 12 is a prime number...").
* **The Plan:** I'll write 50 prompts containing false premises. I plan to use a local model like Mistral or Llama 3 to refine the wording first so I don't waste money. For the final results, I'll run the prompts through the GPT-4o API.
* **Budgeting:** Since I only need to see if the model agrees or disagrees, I don't need long paragraphs of text. I will set the `max_tokens` limit to 50, which should keep the API costs to just a few cents.
