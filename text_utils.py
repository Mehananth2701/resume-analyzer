import re
from PyPDF2 import PdfReader
from skills_db import get_all_skills

KNOWN_SKILLS = get_all_skills()

STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "while", "with", "to", "from",
    "of", "on", "in", "for", "by", "at", "as", "is", "am", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did", "will",
    "would", "shall", "should", "can", "could", "may", "might", "must", "this",
    "that", "these", "those", "it", "its", "he", "she", "they", "them", "his",
    "her", "their", "you", "your", "we", "our", "i", "me", "my", "us"
}


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_pdf_file(file_path):
    reader = PdfReader(file_path)
    content = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            content.append(text)

    return "\n".join(content)


def load_document(file_path):
    lower_path = file_path.lower()

    if lower_path.endswith(".pdf"):
        return read_pdf_file(file_path)
    elif lower_path.endswith(".txt"):
        return read_text_file(file_path)
    else:
        raise ValueError("Unsupported file format. Please use .txt or .pdf")


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_text(text):
    return text.split()


def remove_stopwords(tokens):
    return [token for token in tokens if token not in STOP_WORDS]


def extract_skills(text):
    cleaned = clean_text(text)
    found_skills = set()

    for skill in KNOWN_SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, cleaned):
            found_skills.add(skill)

    return sorted(found_skills)


def extract_keywords(text):
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)
    filtered_tokens = remove_stopwords(tokens)

    keyword_freq = {}
    for token in filtered_tokens:
        if len(token) > 2:
            keyword_freq[token] = keyword_freq.get(token, 0) + 1

    sorted_keywords = sorted(
        keyword_freq.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_keywords[:15]