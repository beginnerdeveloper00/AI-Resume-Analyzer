import re


def analyze_resume(resume_text):
    """
    Analyze a resume for common sections, contact information,
    online profiles, and quantified achievements.
    """

    text = resume_text.lower()

    results = {}

    # -------------------------------------------------
    # Contact Information
    # -------------------------------------------------

    results["Email"] = bool(
        re.search(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
            resume_text
        )
    )

    results["Phone"] = bool(
        re.search(
            r"(?:\+91[\s-]?)?\b[6-9]\d{9}\b",
            resume_text
        )
    )

    # -------------------------------------------------
    # Resume Sections
    # -------------------------------------------------

    results["Skills Section"] = (
        "skills" in text
        or "technical skills" in text
    )

    results["Education Section"] = any(
        keyword in text
        for keyword in [
            "education",
            "b.tech",
            "bachelor",
            "degree",
            "university",
            "college",
            "school"
        ]
    )

    results["Projects Section"] = any(
        keyword in text
        for keyword in [
            "projects",
            "project experience"
        ]
    )

    results["Experience Section"] = any(
        keyword in text
        for keyword in [
            "work experience",
            "professional experience",
            "internship",
            "employment"
        ]
    )

    # -------------------------------------------------
    # Online Profiles
    # -------------------------------------------------

    results["GitHub"] = "github" in text

    results["LinkedIn"] = "linkedin" in text

    # -------------------------------------------------
    # Quantified Achievements
    # -------------------------------------------------

    percentage_numbers = re.findall(
        r"\b\d+(?:\.\d+)?%",
        resume_text
    )

    plus_numbers = re.findall(
        r"\b\d+\+",
        resume_text
    )

    quantified_numbers = percentage_numbers + plus_numbers

    results["Quantified Achievements"] = (
        len(quantified_numbers) >= 2
    )

    return results


def calculate_resume_quality(results):
    """
    Calculate the overall resume quality score
    based on detected resume components.
    """

    if not results:
        return 0

    completed = sum(
        bool(value)
        for value in results.values()
    )

    total = len(results)

    score = (completed / total) * 100

    return round(score, 2)