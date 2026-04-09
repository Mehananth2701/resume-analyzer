SKILL_DATABASE = {
    "programming_languages": [
        "python", "java", "c", "c++", "javascript", "typescript",
        "html", "css", "sql", "php", "kotlin"
    ],
    "frameworks_tools": [
        "react", "spring boot", "django", "flask", "git", "github",
        "docker", "postman", "vs code", "intellij"
    ],
    "databases": [
        "mysql", "postgresql", "mongodb", "sqlite"
    ],
    "concepts": [
        "data structures", "algorithms", "oops", "machine learning",
        "deep learning", "nlp", "computer vision", "dbms",
        "operating system", "computer networks"
    ],
    "soft_skills": [
        "communication", "teamwork", "leadership", "problem solving",
        "time management", "adaptability", "critical thinking"
    ]
}


def get_all_skills():
    all_skills = []

    for category in SKILL_DATABASE.values():
        all_skills.extend(category)

    return sorted(set(all_skills))