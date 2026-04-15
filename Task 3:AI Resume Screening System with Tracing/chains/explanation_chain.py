"""
chains/explanation_chain.py
----------------------------
Step 4: Explanation Chain
Generates a human-readable recruiter-style evaluation report.
"""

import json
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from prompts.explanation_prompt import explanation_prompt


def build_explanation_chain(llm: ChatOpenAI):
    """
    Builds and returns the LCEL explanation chain.

    Chain: explanation_prompt | llm | StrOutputParser
    """
    chain = explanation_prompt | llm | StrOutputParser()
    return chain


def run_explanation(
    llm: ChatOpenAI,
    candidate_name: str,
    score_result: dict,
    match_analysis: dict
) -> str:
    """
    Runs the explanation chain to generate a recruiter evaluation report.

    Args:
        llm: The ChatOpenAI model instance
        candidate_name: Name of the candidate
        score_result: Output from scoring chain
        match_analysis: Output from matching chain

    Returns:
        str: Human-readable evaluation report
    """
    chain = build_explanation_chain(llm)

    explanation = chain.invoke({
        "candidate_name": candidate_name,
        "total_score": score_result.get("total_score", "N/A"),
        "tier": score_result.get("tier", "N/A"),
        "score_breakdown": json.dumps(score_result.get("breakdown", {}), indent=2),
        "match_analysis": json.dumps(match_analysis, indent=2)
    })

    return explanation
