"""
utils/tracing.py
-----------------
LangSmith tracing setup and helper utilities.
Enables tracing for all LangChain runs.
"""

import os
from datetime import datetime


def setup_langsmith_tracing(project_name: str = "AI-Resume-Screener"):
    """
    Sets up LangSmith tracing environment variables.

    Make sure your .env file has:
        LANGCHAIN_API_KEY=your_key_here
        OPENAI_API_KEY=your_key_here

    Args:
        project_name: Name of the LangSmith project
    """
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = project_name
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"

    api_key = os.getenv("LANGCHAIN_API_KEY")
    if not api_key:
        print("[WARNING] LANGCHAIN_API_KEY not found in environment.")
        print("          LangSmith tracing will be disabled.")
        print("          Add LANGCHAIN_API_KEY to your .env file.")
    else:
        print(f"[LangSmith] Tracing enabled → Project: '{project_name}'")
        print(f"[LangSmith] View traces at: https://smith.langchain.com")


def get_run_metadata(candidate_label: str) -> dict:
    """
    Returns metadata tags for LangSmith run tracking.

    Args:
        candidate_label: e.g. 'Strong Candidate', 'Average Candidate'

    Returns:
        dict with tags and metadata
    """
    return {
        "tags": ["resume-screening", candidate_label.lower().replace(" ", "-")],
        "metadata": {
            "candidate_type": candidate_label,
            "timestamp": datetime.now().isoformat(),
            "pipeline_version": "1.0.0"
        }
    }


def print_section_header(title: str):
    """Prints a formatted section header to the console."""
    width = 60
    print("\n" + "=" * width)
    print(f"  {title}")
    print("=" * width)


def print_step(step_num: int, step_name: str):
    """Prints a step indicator."""
    print(f"\n  ▶ Step {step_num}: {step_name}")
    print("  " + "-" * 40)
