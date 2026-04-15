"""
chains/extraction_chain.py
---------------------------
Step 1: Skill Extraction Chain
Uses LCEL (LangChain Expression Language) to build a modular chain.
"""

import json
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from prompts.extraction_prompt import extraction_prompt


def build_extraction_chain(llm: ChatOpenAI):
    """
    Builds and returns the LCEL extraction chain.

    Chain: extraction_prompt | llm | StrOutputParser
    """
    chain = extraction_prompt | llm | StrOutputParser()
    return chain


def run_extraction(llm: ChatOpenAI, resume_text: str) -> dict:
    """
    Runs the extraction chain on a resume.

    Args:
        llm: The ChatOpenAI model instance
        resume_text: Raw resume text

    Returns:
        dict: Parsed extracted profile
    """
    chain = build_extraction_chain(llm)

    # Use .invoke() as required
    raw_output = chain.invoke({"resume": resume_text})

    # Safely parse JSON output
    try:
        # Strip markdown code fences if LLM adds them
        cleaned = raw_output.strip().strip("```json").strip("```").strip()
        extracted = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"[WARNING] JSON parse error in extraction: {e}")
        print(f"[RAW OUTPUT]: {raw_output}")
        # Return raw text wrapped in dict for debugging
        extracted = {"raw_output": raw_output, "parse_error": str(e)}

    return extracted
