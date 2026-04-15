"""
data/job_description.py
-----------------------
Contains the job description for a Data Scientist role.
"""

JOB_DESCRIPTION = """
ROLE: Data Scientist
COMPANY: TechCorp Analytics (Bangalore, India)

JOB SUMMARY:
We are looking for a skilled Data Scientist to join our AI/ML team.
The ideal candidate will build and deploy machine learning models that
drive business decisions and create value for our customers.

REQUIRED SKILLS:
- Python (advanced proficiency)
- Machine Learning: Scikit-learn, XGBoost, or similar
- Deep Learning: TensorFlow or PyTorch
- SQL and database knowledge
- Data manipulation: Pandas, NumPy
- Model deployment and MLOps experience
- Statistical analysis and hypothesis testing
- NLP experience is a strong plus

REQUIRED EXPERIENCE:
- 3+ years of hands-on data science experience
- Experience with cloud platforms (AWS, GCP, or Azure)
- Experience building production-grade ML pipelines
- Familiarity with big data tools (Spark, Hadoop) is a plus

REQUIRED EDUCATION:
- B.Tech / M.S. in Computer Science, Statistics, or related field
- Degree in Data Science or Machine Learning preferred

KEY RESPONSIBILITIES:
- Design, build, and maintain ML models for business use cases
- Collaborate with engineering teams to deploy models into production
- Perform EDA and feature engineering on large datasets
- Communicate insights to non-technical stakeholders
- Mentor junior team members
"""

# Parsed required skills for matching logic
REQUIRED_SKILLS = [
    "Python", "Machine Learning", "Deep Learning",
    "TensorFlow", "PyTorch", "Scikit-learn", "XGBoost",
    "SQL", "Pandas", "NumPy", "MLOps", "NLP",
    "Cloud (AWS/GCP/Azure)", "Spark/Big Data",
    "Statistical Analysis"
]

REQUIRED_EXPERIENCE_YEARS = 3
REQUIRED_EDUCATION = ["B.Tech", "M.S.", "M.Tech", "PhD", "Computer Science", "Statistics", "Data Science"]
