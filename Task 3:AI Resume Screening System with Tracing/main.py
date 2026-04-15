
"""
main.py
--------
AI Resume Screening System — Main Entry Point
Pipeline: Resume → Extract → Match → Score → Explain → Trace
"""

import os
import json
from dotenv import load_dotenv
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langsmith import traceable

# Load environment variables
load_dotenv()

# Project imports
from data import RESUMES, JOB_DESCRIPTION
from chains import run_extraction, run_matching, run_scoring, run_explanation
from utils import setup_langsmith_tracing, print_section_header, print_step


# ─────────────────────────────────────────────
# Setup LangSmith Tracing
# ─────────────────────────────────────────────
setup_langsmith_tracing(project_name="AI-Resume-Screener")


# ─────────────────────────────────────────────
# Initialize LLM (HuggingFace - FREE)
# ─────────────────────────────────────────────
def get_llm():
    pipe = pipeline(
        "text-generation",   # ✅ FIXED
        model="google/flan-t5-small",  # use small (faster + safer)
        max_new_tokens=512
    )
    llm = HuggingFacePipeline(pipeline=pipe)
    return llm


# ─────────────────────────────────────────────
# Core Pipeline Function
# ─────────────────────────────────────────────
@traceable(name="resume_screening_pipeline", tags=["resume-screening"])
def screen_resume(llm, candidate_key: str) -> dict:

    resume_data = RESUMES[candidate_key]
    resume_text = resume_data["text"]
    candidate_label = resume_data["label"]
    candidate_name = resume_data["name"]

    print_section_header(f"SCREENING: {candidate_name} ({candidate_label})")

    # STEP 1: Extraction
    print_step(1, "Skill Extraction")
    extracted = run_extraction(llm, resume_text)

    print(f"  Candidate: {extracted.get('candidate_name', 'N/A')}")
    print(f"  Experience: {extracted.get('experience_years', 0)} years")

    skills = extracted.get("skills", {})
    all_skills = (
        skills.get("programming_languages", []) +
        skills.get("ml_frameworks", []) +
        skills.get("cloud_platforms", [])
    )
    print(f"  Key Skills: {', '.join(all_skills[:6]) if all_skills else 'None'}")

    # STEP 2: Matching
    print_step(2, "Matching")
    match_result = run_matching(llm, JOB_DESCRIPTION, extracted)

    matched = match_result.get("matched_skills", [])
    missing = match_result.get("missing_skills", [])
    match_pct = match_result.get("overall_match_percentage", 0)

    print(f"  Matched: {', '.join(matched[:5])}")
    print(f"  Missing: {', '.join(missing[:5])}")
    print(f"  Match %: {match_pct}")

    # STEP 3: Scoring
    print_step(3, "Scoring")
    score_result = run_scoring(llm, match_result)

    total_score = score_result.get("total_score", 0)
    tier = score_result.get("tier", "N/A")
    breakdown = score_result.get("breakdown", {})

    print(f"  Score: {total_score}/100")
    print(f"  Tier: {tier}")

    # STEP 4: Explanation
    print_step(4, "Explanation")
    explanation = run_explanation(llm, candidate_name, score_result, match_result)

    print(f"\n{explanation}")

    return {
        "candidate_name": candidate_name,
        "candidate_type": candidate_label,
        "total_score": total_score,
        "tier": tier,
        "score_breakdown": breakdown,
        "matched_skills": matched,
        "missing_skills": missing,
        "match_percentage": match_pct,
        "explanation": explanation
    }


# ─────────────────────────────────────────────
# Debug Demo
# ─────────────────────────────────────────────
def debug_demonstrate_issue(llm):

    print_section_header("DEBUG MODE")

    ambiguous_resume = """
    Name: Unknown
    Skills: Some computer knowledge. Python once.
    Experience: 1 year
    """

    extracted = run_extraction(llm, ambiguous_resume)

    print("\nExtracted Output:")
    print(json.dumps(extracted, indent=2))


# ─────────────────────────────────────────────
# Main Function
# ─────────────────────────────────────────────
def main():

    print("\n" + "█" * 60)
    print("   AI RESUME SCREENING SYSTEM")
    print("   Powered by LangChain + HuggingFace + LangSmith")
    print("█" * 60)

    # ✅ FIXED: Proper LLM initialization
    llm = get_llm()

    print("\n[Model] Using: HuggingFace (flan-t5-base)")

    all_results = {}

    # Run pipeline
    for candidate_key in ["strong", "average", "weak"]:
        try:
            result = screen_resume(llm, candidate_key)
            all_results[candidate_key] = result
        except Exception as e:
            print(f"\n[ERROR] {candidate_key}: {e}")

    # Debug run
    debug_demonstrate_issue(llm)

    # Final Summary
    print_section_header("FINAL RESULTS")

    for key, r in all_results.items():
        print(f"{r['candidate_name']} → {r['total_score']}/100 ({r['tier']})")

    # Save output
    with open("results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print("\nResults saved to results.json")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
