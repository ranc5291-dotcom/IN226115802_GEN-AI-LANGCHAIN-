"""
chains/scoring_chain.py
------------------------
Step 3: Candidate Scoring Chain
Assigns a 0–100 score based on match analysis.
"""

import json
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from prompts.scoring_prompt import scoring_prompt


def build_scoring_chain(llm: ChatOpenAI):
    """
    Builds and returns the LCEL scoring chain.

    Chain: scoring_prompt | llm | StrOutputParser
    """
    chain = scoring_prompt | llm | StrOutputParser()
    return chain


def run_scoring(llm: ChatOpenAI, match_analysis: dict) -> dict:
    """
    Runs the scoring chain to assign a score to the candidate.

    Args:
        llm: The ChatOpenAI model instance
        match_analysis: Output from matching chain

    Returns:
        dict: Scoring result with total_score, breakdown, and tier
    """
    chain = build_scoring_chain(llm)

    match_str = json.dumps(match_analysis, indent=2)

    raw_output = chain.invoke({"match_analysis": match_str})

    try:
        cleaned = raw_output.strip().strip("```json").strip("```").strip()
        score_result = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"[WARNING] JSON parse error in scoring: {e}")
        print(f"[RAW OUTPUT]: {raw_output}")
        score_result = {"raw_output": raw_output, "parse_error": str(e)}

    return score_result
