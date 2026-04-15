"""
prompts/extraction_prompt.py
-----------------------------
Prompt template for Step 1: Skill & Experience Extraction
"""
from langchain_core.prompts import PromptTemplate
EXTRACTION_TEMPLATE = """
You are an expert HR analyst and resume parser.

Your task is to extract structured information from the resume below.

STRICT RULES:
- Extract ONLY information explicitly mentioned in the resume.
- Do NOT infer or assume skills that are not clearly stated.
- Do NOT add skills based on job title alone.
- If a field is not present, return an empty list [] or "Not mentioned".

RESUME:
{resume}

Extract the following in valid JSON format:
{{
  "candidate_name": "<name>",
  "education": {{
    "degrees": ["<list of degrees>"],
    "institutions": ["<list of institutions>"],
    "fields_of_study": ["<list of fields>"]
  }},
  "experience_years": <total years as a number, or 0 if not mentioned>,
  "skills": {{
    "programming_languages": ["<list>"],
    "ml_frameworks": ["<list>"],
    "data_tools": ["<list>"],
    "cloud_platforms": ["<list>"],
    "databases": ["<list>"],
    "other_tools": ["<list>"]
  }},
  "previous_roles": ["<list of job titles held>"],
  "certifications": ["<list>"],
  "notable_projects": ["<list of project names or descriptions>"]
}}

Return ONLY valid JSON. No explanation, no markdown, no extra text.
"""

extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template=EXTRACTION_TEMPLATE
)
