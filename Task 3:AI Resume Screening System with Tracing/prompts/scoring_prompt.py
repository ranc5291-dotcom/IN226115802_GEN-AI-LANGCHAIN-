"""
prompts/scoring_prompt.py
--------------------------
Prompt template for Step 3: Candidate Scoring (0-100)
"""

from langchain_core.prompts import PromptTemplate

SCORING_TEMPLATE = """
You are an expert technical recruiter. Based on the match analysis below,
assign a final score from 0 to 100 for this candidate.

SCORING RUBRIC:
- Skills Match (40 points max): How many required skills does the candidate have?
- Experience (25 points max): Does the candidate meet the 3+ year requirement?
- Education (15 points max): Is the degree relevant and from a good institution?
- Bonus Qualifications (20 points max): Extra tools, certifications, cloud, big data, NLP, etc.

MATCH ANALYSIS:
{match_analysis}

RULES:
- Score based ONLY on the information in the match analysis above.
- Do NOT add points for skills not present in the match analysis.
- Apply the rubric strictly.

Return a JSON object:
{{
  "total_score": <0-100 integer>,
  "breakdown": {{
    "skills_score": <0-40>,
    "experience_score": <0-25>,
    "education_score": <0-15>,
    "bonus_score": <0-20>
  }},
  "tier": "<one of: Highly Recommended | Recommended | Average | Below Average | Not Suitable>"
}}

Return ONLY valid JSON. No explanation, no markdown, no extra text.
"""

scoring_prompt = PromptTemplate(
    input_variables=["match_analysis"],
    template=SCORING_TEMPLATE
)
