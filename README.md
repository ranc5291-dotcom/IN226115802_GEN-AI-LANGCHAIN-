# AI Resume Screening System
### Built with LangChain + LangSmith + OpenAI

---

## Project Structure

```
intern_resume/
├── main.py                  ← Run this to start the pipeline
├── requirements.txt         ← All dependencies
├── .env.example             ← Rename to .env and add your keys
├── results.json             ← Auto-generated after running
│
├── prompts/                 ← All PromptTemplates
│   ├── extraction_prompt.py
│   ├── matching_prompt.py
│   ├── scoring_prompt.py
│   └── explanation_prompt.py
│
├── chains/                  ← LCEL Chains (.invoke())
│   ├── extraction_chain.py
│   ├── matching_chain.py
│   ├── scoring_chain.py
│   └── explanation_chain.py
│
├── data/                    ← Resumes + Job Description
│   ├── resumes.py
│   └── job_description.py
│
└── utils/
    └── tracing.py           ← LangSmith setup helpers
```

## Pipeline Flow

```
Resume Text
    │
    ▼
Step 1: Skill Extraction     ← Extract skills, experience, education
    │
    ▼
Step 2: Matching             ← Compare against job requirements
    │
    ▼
Step 3: Scoring (0–100)      ← Assign score using rubric
    │
    ▼
Step 4: Explanation          ← Human-readable recruiter report
    │
    ▼
LangSmith Trace              ← All steps visible in dashboard
```

## Setup Instructions

### Step 1 — Get your API Keys

| Key | Where to get it |
|-----|----------------|
| `OPENAI_API_KEY` | https://platform.openai.com/api-keys |
| `LANGCHAIN_API_KEY` | https://smith.langchain.com → Settings → API Keys |

---

### Step 2 — Create your .env file

```bash
# In the intern_resume/ folder, rename the example file:
cp .env.example .env
```

Then open `.env` and replace the placeholder values:

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
LANGCHAIN_API_KEY=lsv2_pt_xxxxxxxxxxxxx
```

---

### Step 3 — Create a virtual environment

```bash
python -m venv venv
```

Activate it:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

---

### Step 4 — Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 5 — Run the system

```bash
python main.py
```

---

## Expected Output

```
████████████████████████████████████████████████████████████
   AI RESUME SCREENING SYSTEM
   Powered by LangChain + OpenAI + LangSmith
████████████████████████████████████████████████████████████

[LangSmith] Tracing enabled → Project: 'AI-Resume-Screener'

============================================================
  SCREENING: Alice Sharma (Strong Candidate)
============================================================

  ▶ Step 1: Skill Extraction
  Candidate: Alice Sharma
  Experience: 5 years
  Key Skills: Python, R, SQL, TensorFlow, PyTorch, XGBoost

  ▶ Step 2: Job Requirement Matching
  Matched Skills (12): Python, TensorFlow, PyTorch, ...
  Missing Skills (1): ...
  Overall Match: 92%

  ▶ Step 3: Scoring (0-100)
  Total Score: 91/100
  Tier:        Highly Recommended
  Breakdown:   Skills=38/40 | Experience=25/25 | Education=15/15 | Bonus=13/20

  ▶ Step 4: Explanation Generation
  EVALUATION SUMMARY FOR: Alice Sharma | Score: 91/100 ...
```

---

## Viewing Traces in LangSmith

1. Go to **https://smith.langchain.com**
2. Click on the project **"AI-Resume-Screener"**
3. You will see **4 runs** (Strong, Average, Weak, Debug)
4. Click any run to see:
   - All 4 pipeline steps (Extract → Match → Score → Explain)
   - Input/output for each step
   - Latency and token usage
   - The debug run tagged separately

---

## Scoring Rubric

| Category | Max Points |
|----------|-----------|
| Skills Match | 40 |
| Experience (3+ years) | 25 |
| Education (CS/Stats/DS) | 15 |
| Bonus (Cloud, NLP, MLOps) | 20 |
| **Total** | **100** |

| Score Range | Tier |
|-------------|------|
| 80–100 | Highly Recommended |
| 65–79 | Recommended |
| 45–64 | Average |
| 25–44 | Below Average |
| 0–24 | Not Suitable |
