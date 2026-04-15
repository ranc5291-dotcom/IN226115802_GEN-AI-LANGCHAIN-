"""
data/resumes.py
---------------
Contains 3 sample resumes: Strong, Average, and Weak candidates
for a Data Scientist role.
"""

RESUMES = {
    "strong": {
        "name": "Alice Sharma",
        "label": "Strong Candidate",
        "text": """
Name: Alice Sharma
Email: alice.sharma@email.com
Phone: +91-9876543210

SUMMARY
Experienced Data Scientist with 5 years of industry experience building
end-to-end ML pipelines. Passionate about solving real-world problems
using data-driven approaches.

EDUCATION
- M.S. in Computer Science (Machine Learning) – IIT Bombay, 2019
- B.Tech in Computer Science – NIT Trichy, 2017

SKILLS
- Languages: Python, R, SQL, Scala
- ML/DL Frameworks: TensorFlow, PyTorch, Scikit-learn, Keras, XGBoost
- Data Tools: Pandas, NumPy, Matplotlib, Seaborn, Plotly
- MLOps: MLflow, Docker, Kubernetes, CI/CD pipelines
- Cloud: AWS SageMaker, GCP Vertex AI, Azure ML
- Big Data: Spark, Hadoop, Hive
- NLP: HuggingFace Transformers, spaCy, NLTK
- Databases: PostgreSQL, MongoDB, Redis

EXPERIENCE

Data Scientist – Google India (2021–Present)
- Built a real-time recommendation engine serving 10M+ users using collaborative filtering and deep learning
- Reduced model inference latency by 40% through model quantization and TensorRT optimization
- Led a team of 4 data scientists on a churn prediction project saving $2M annually
- Implemented A/B testing framework used across 5 product teams

Data Scientist – Flipkart (2019–2021)
- Developed demand forecasting models using LSTM and Prophet, improving accuracy by 25%
- Created NLP pipelines for product review sentiment analysis using BERT
- Automated feature engineering pipelines using Featuretools

PROJECTS
- LLM-based document summarizer using LangChain and OpenAI GPT-4
- Kaggle Competition: Top 2% in IEEE Fraud Detection (XGBoost + stacking)

CERTIFICATIONS
- AWS Certified Machine Learning Specialty
- Google Professional Data Engineer
        """,
    },

    "average": {
        "name": "Ravi Mehta",
        "label": "Average Candidate",
        "text": """
Name: Ravi Mehta
Email: ravi.mehta@email.com
Phone: +91-9123456789

SUMMARY
Data analyst with 2 years of experience in data analysis and basic machine
learning. Familiar with Python and SQL. Looking to transition into a full
Data Scientist role.

EDUCATION
- B.Tech in Information Technology – VIT Vellore, 2022

SKILLS
- Languages: Python, SQL
- Libraries: Pandas, NumPy, Matplotlib, Scikit-learn
- Tools: Jupyter Notebook, Excel, Tableau
- Databases: MySQL

EXPERIENCE

Data Analyst – TCS (2022–Present)
- Performed EDA on customer datasets using Pandas and Matplotlib
- Built basic classification models (Logistic Regression, Decision Tree) in Scikit-learn
- Created dashboards in Tableau for business reporting
- Wrote SQL queries to extract and clean data from MySQL databases

Intern – Infosys (Summer 2021)
- Worked on a data cleaning project using Python
- Assisted senior analysts in generating weekly Excel reports

PROJECTS
- House Price Prediction using Linear Regression (Kaggle dataset)
- Customer Segmentation using K-Means Clustering

CERTIFICATIONS
- Coursera: Machine Learning by Andrew Ng
        """,
    },

    "weak": {
        "name": "Priya Nair",
        "label": "Weak Candidate",
        "text": """
Name: Priya Nair
Email: priya.nair@email.com
Phone: +91-9001234567

SUMMARY
Recent graduate interested in data and technology. Eager to learn and grow
in a challenging environment.

EDUCATION
- B.Com (Bachelor of Commerce) – Mumbai University, 2023

SKILLS
- MS Excel (basic)
- PowerPoint
- Basic internet research
- Communication skills

EXPERIENCE

Intern – Local Retail Store (2023, 3 months)
- Maintained inventory spreadsheets in Excel
- Helped prepare monthly sales reports
- Assisted manager with data entry tasks

PROJECTS
- College project: Survey analysis on consumer buying behavior (Excel-based)

CERTIFICATIONS
- None
        """,
    },
}
