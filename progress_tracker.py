"""
EduMate AI — Progress Tracker

Persists each student's completed topics and quiz scores to a local JSON
file, so progress is remembered between sessions.
"""

import json
import os
from datetime import datetime

PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")


def load_progress() -> dict:
    if not os.path.exists(PROGRESS_FILE):
        return {}
    try:
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def save_progress(progress: dict) -> None:
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def mark_topic_done(topic_name: str, score: int, total: int) -> None:
    progress = load_progress()
    progress[topic_name] = {
        "completed": True,
        "score": score,
        "total": total,
        "date": datetime.now().isoformat(timespec="seconds"),
    }
    save_progress(progress)
