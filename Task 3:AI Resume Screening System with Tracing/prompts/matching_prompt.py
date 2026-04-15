"""
prompts/matching_prompt.py
---------------------------
Prompt template for Step 2: Job Requirement Matching
"""

from langchain_core.prompts import PromptTemplate

MATCHING_TEMPLATE = """
You are a senior technical recruiter evaluating a candidate for a Data Scientist role.

JOB DESCRIPTION:
{job_description}

CANDIDATE EXTRACTED PROFILE:
{extracted_profile}

Your task is to perform a detailed skill and requirement match.

RULES:
- Only match skills/experience that are EXPLICITLY present in the extracted profile.
- Do NOT assume or give benefit of the doubt for missing skills.
- Be objective and precise.

Return a JSON object with this structure:
{{
  "matched_skills": ["<skills from the job description found in the candidate profile>"],
  "missing_skills": ["<required skills NOT found in the candidate profile>"],
  "experience_match": {{
    "required_years": 3,
    "candidate_years": <number>,
    "meets_requirement": <true/false>
  }},
  "education_match": {{
    "required": "B.Tech/M.S. in CS, Statistics, or related field",
    "candidate_education": "<candidate's actual education>",
    "meets_requirement": <true/false>
  }},
  "bonus_qualifications": ["<extra positive qualifications the candidate has beyond requirements>"],
  "overall_match_percentage": <0-100 integer representing % of job requirements met>
}}

Return ONLY valid JSON. No explanation, no markdown, no extra text.
"""

matching_prompt = PromptTemplate(
    input_variables=["job_description", "extracted_profile"],
    template=MATCHING_TEMPLATE
)
