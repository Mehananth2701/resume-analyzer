from text_utils import load_document, extract_skills, extract_keywords


def calculate_match_score(resume_skills, job_skills):
    if not job_skills:
        return 0.0

    matched = set(resume_skills) & set(job_skills)
    score = (len(matched) / len(job_skills)) * 100
    return round(score, 2)


def generate_suggestions(missing_skills, match_score):
    suggestions = []

    if match_score >= 80:
        suggestions.append("Strong profile for this role. You can improve it by adding measurable project outcomes.")
    elif match_score >= 60:
        suggestions.append("Good match, but the resume can be improved by highlighting more role-specific skills.")
    else:
        suggestions.append("Your resume needs better alignment with the job description.")

    if missing_skills:
        suggestions.append("Missing skills to focus on: " + ", ".join(missing_skills))

    suggestions.append("Use clear project descriptions with action words.")
    suggestions.append("Tailor the resume for each job role.")

    return suggestions


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    print("Resume Analyzer & Job Matcher")
    print("-" * 60)

    resume_path = input("Enter resume file path (.txt or .pdf): ").strip()
    job_path = input("Enter job description file path (.txt or .pdf): ").strip()

    try:
        resume_text = load_document(resume_path)
        job_text = load_document(job_path)
    except Exception as error:
        print("Error:", error)
        return

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched_skills = sorted(list(set(resume_skills) & set(job_skills)))
    missing_skills = sorted(list(set(job_skills) - set(resume_skills)))
    match_score = calculate_match_score(resume_skills, job_skills)

    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    print_section("ANALYSIS RESULT")
    print("Resume Skills Found      :", resume_skills)
    print("Job Skills Required      :", job_skills)
    print("Matched Skills           :", matched_skills)
    print("Missing Skills           :", missing_skills)
    print("Match Score              :", str(match_score) + "%")

    print_section("TOP RESUME KEYWORDS")
    for word, count in resume_keywords:
        print(f"{word} -> {count}")

    print_section("TOP JOB DESCRIPTION KEYWORDS")
    for word, count in job_keywords:
        print(f"{word} -> {count}")

    print_section("SUGGESTIONS")
    suggestions = generate_suggestions(missing_skills, match_score)
    for i, suggestion in enumerate(suggestions, start=1):
        print(f"{i}. {suggestion}")


if __name__ == "__main__":
    main()