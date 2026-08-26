import re


SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "nlp",
    "natural language processing",
    "computer vision",
    "streamlit",
    "flask",
    "fastapi",
    "django",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "google cloud",
    "power bi",
    "tableau",
    "excel",
]


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


def calculate_match(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    if not job_skills:
        return 0, [], []

    matching_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills - resume_skills

    score = (len(matching_skills) / len(job_skills)) * 100

    return round(score, 2), sorted(matching_skills), sorted(missing_skills)