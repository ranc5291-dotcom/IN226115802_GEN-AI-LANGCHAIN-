"""
prompts/explanation_prompt.py
------------------------------
Prompt template for Step 4: Human-Readable Explanation
Includes few-shot examples for better output quality.
"""

from langchain_core.prompts import PromptTemplate

EXPLANATION_TEMPLATE = """
You are a senior recruiter writing a concise candidate evaluation report.

Given the analysis below, write a clear, professional explanation of:
1. Why this score was given
2. The candidate's key strengths
3. The candidate's key gaps
4. A final hiring recommendation

FEW-SHOT EXAMPLES:

Example 1 (Score: 88):
---
EVALUATION SUMMARY FOR: Jane Doe | Score: 88/100 | Tier: Highly Recommended

SCORE RATIONALE:
Jane scored 88/100 based on an excellent skill match (38/40), strong experience of 5 years
exceeding the 3-year requirement (25/25), and a relevant M.S. in Computer Science (15/15).
Bonus points were awarded for her AWS certification and Spark experience (10/20).

STRENGTHS:
- Proficient in Python, TensorFlow, PyTorch, and Scikit-learn — all core requirements met.
- 5 years of production ML experience, well above the 3-year minimum.
- M.S. in Computer Science from a top institution.
- Bonus: AWS Certified, experienced with NLP and Big Data tools.

GAPS:
- Limited experience with real-time model serving pipelines.
- No MLflow or Kubernetes mentioned for MLOps.

RECOMMENDATION: STRONGLY RECOMMEND for interview.
---

Example 2 (Score: 42):
---
EVALUATION SUMMARY FOR: John Smith | Score: 42/100 | Tier: Average

SCORE RATIONALE:
John scored 42/100 due to partial skill coverage (18/40), insufficient experience of 2 years
below the 3-year requirement (12/25), and a related but non-preferred degree (10/15).
Limited bonus qualifications (2/20).

STRENGTHS:
- Familiar with Python and Scikit-learn for basic ML tasks.
- SQL proficiency is a positive.

GAPS:
- No deep learning experience (TensorFlow/PyTorch missing).
- Does not meet the 3-year experience requirement.
- No cloud, MLOps, or NLP experience mentioned.

RECOMMENDATION: CONSIDER for junior role, not ready for this position.
---

NOW EVALUATE THE ACTUAL CANDIDATE:

Candidate Name: {candidate_name}
Score: {total_score}/100
Tier: {tier}
Score Breakdown: {score_breakdown}
Match Analysis: {match_analysis}

Write the evaluation in the same professional format as the examples above.
Be specific, factual, and base all statements on the provided data only.
"""

explanation_prompt = PromptTemplate(
    input_variables=[
        "candidate_name",
        "total_score",
        "tier",
        "score_breakdown",
        "match_analysis"
    ],
    template=EXPLANATION_TEMPLATE
)
