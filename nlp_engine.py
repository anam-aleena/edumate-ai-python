"""
EduMate AI — Simple NLP Engine

A lightweight, dependency-free NLP pipeline for matching a student's free-text
question to the most relevant knowledge-base entry:

1. Normalize text (lowercase, strip punctuation)
2. Tokenize into words
3. Score each knowledge-base entry by keyword overlap
4. Return the best match if it clears a minimum confidence threshold,
   otherwise fall back to a clarifying response.
"""

import re
import random
from data import CHAT_KB, FALLBACK_RESPONSES

_PUNCT_RE = re.compile(r"[^\w\s]")


def normalize(text: str) -> str:
    """Lowercase and strip punctuation from input text."""
    return _PUNCT_RE.sub("", text.lower()).strip()


def tokenize(text: str) -> list:
    """Split normalized text into word tokens."""
    return normalize(text).split()


def score_entry(user_tokens: list, keywords: list) -> int:
    """Count how many keyword phrases appear in the user's message."""
    user_text = " ".join(user_tokens)
    score = 0
    for kw in keywords:
        if kw in user_text:
            score += len(kw.split())  # multi-word keyword matches score higher
    return score


def get_bot_reply(message: str) -> str:
    """Return the chatbot's reply to a free-text student message."""
    tokens = tokenize(message)
    if not tokens:
        return random.choice(FALLBACK_RESPONSES)

    best_score = 0
    best_response = None
    for entry in CHAT_KB:
        score = score_entry(tokens, entry["keywords"])
        if score > best_score:
            best_score = score
            best_response = entry["response"]

    if best_score > 0:
        return best_response
    return random.choice(FALLBACK_RESPONSES)
