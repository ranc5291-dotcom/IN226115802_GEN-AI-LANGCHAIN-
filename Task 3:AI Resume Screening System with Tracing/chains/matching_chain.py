"""
chains/matching_chain.py
-------------------------
Step 2: Job Requirement Matching Chain
Compares extracted resume profile against the job description.
"""

import json
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from prompts.matching_prompt import matching_prompt


def build_matching_chain(llm: ChatOpenAI):
    """
    Builds and returns the LCEL matching chain.

    Chain: matching_prompt | llm | StrOutputParser
    """
    chain = matching_prompt | llm | StrOutputParser()
    return chain


def run_matching(llm: ChatOpenAI, job_description: str, extracted_profile: dict) -> dict:
    """
    Runs the matching chain to compare resume against JD.

    Args:
        llm: The ChatOpenAI model instance
        job_description: The job description text
        extracted_profile: Output from extraction chain

    Returns:
        dict: Match analysis result
    """
    chain = build_matching_chain(llm)

    # Convert extracted profile dict to string for prompt
    profile_str = json.dumps(extracted_profile, indent=2)

    raw_output = chain.invoke({
        "job_description": job_description,
        "extracted_profile": profile_str
    })

    try:
        cleaned = raw_output.strip().strip("```json").strip("```").strip()
        match_result = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"[WARNING] JSON parse error in matching: {e}")
        print(f"[RAW OUTPUT]: {raw_output}")
        match_result = {"raw_output": raw_output, "parse_error": str(e)}

    return match_result
