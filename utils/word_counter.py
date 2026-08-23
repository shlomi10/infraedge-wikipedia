import re
from collections import Counter


BRACKET_CONTENTS = re.compile(r"\[.*?\]")
WORD_DELIMITERS = re.compile(r"[^a-z0-9]+")


def normalize_text(text: str) -> str:
    cleaned = BRACKET_CONTENTS.sub(" ", text)
    cleaned = cleaned.lower().replace("-", " ")
    cleaned = WORD_DELIMITERS.sub(" ", cleaned)
    return " ".join(cleaned.split())


def count_words(text: str) -> dict[str, int]:
    words = normalize_text(text).split()
    return dict(Counter(words))


def unique_word_count(word_counts: dict[str, int]) -> int:
    return len(word_counts)


def format_word_counts(word_counts: dict[str, int]) -> str:
    return "\n".join(
        f"{word}: {count}"
        for word, count in sorted(word_counts.items())
    )
