import re


def analyze_resume(resume_text):
    text = resume_text.lower()

    results = {}

    # Contact information
    results["Email"] = bool(
        re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", resume_text)
    )

    results["Phone"] = bool(
        re.search(r"\b\d{10}\b", resume_text)
    )

    # Common resume sections
    results["Skills Section"] = "skills" in text or "technical skills" in text

    results["Education Section"] = any(
        word in text
        for word in [
            "education",
            "b.tech",
            "bachelor",
            "degree",
            "university",
            "college"
        ]
    )

    results["Projects Section"] = "projects" in text or "project" in text

    results["Experience Section"] = any(
        word in text
        for word in [
            "experience",
            "internship",
            "work experience"
        ]
    )

    results["GitHub"] = "github" in text

    results["LinkedIn"] = "linkedin" in text

    # Count measurable achievements
    numbers = re.findall(r"\b\d+%|\b\d+\+|\b\d+\b", resume_text)

    results["Quantified Achievements"] = len(numbers) > 2

    return results


def calculate_resume_quality(results):
    total = len(results)
    completed = sum(results.values())

    score = (completed / total) * 100

    return round(score, 2)