# EduMate AI (Python) — Personalized Learning Platform & Chatbot Tutor

**Capstone Milestone 8 — Concept Note: Individual Submission**
**Author:** Aleena Anam ([anamaleena0@gmail.com](mailto:anamaleena0@gmail.com))
**Program:** Lenovo LEAP × Bharat Cares
**SDG Addressed:** SDG 4 — Quality Education

## 🎯 Problem
Many students lack consistent access to a teacher or tutor who can explain concepts
at their own pace outside class hours, causing learning gaps to widen over time.

## 💡 Solution
EduMate AI is a Python-based (Streamlit) web application that gives every student:
- **Structured lessons** in Math, Science, and English.
- **An AI tutor chatbot** using a lightweight NLP keyword-matching engine to answer
  questions in plain language.
- **Instant-feedback quizzes** with automatic scoring.
- **A progress dashboard** that persists completed topics and scores to a local
  JSON file (`progress.json`).

## 🛠️ Technology Stack
- **Language:** Python 3
- **Framework:** Streamlit (web UI)
- **NLP:** Custom keyword-matching engine (`nlp_engine.py`) — tokenization,
  normalization, and keyword-overlap scoring
- **Persistence:** JSON file storage (`progress_tracker.py`)

## 📂 Project Structure
```
edumate-ai-python/
├── app.py                # Streamlit application (UI + navigation)
├── data.py                # Subjects, lessons, quizzes, chatbot knowledge base
├── nlp_engine.py           # Keyword-matching NLP engine for the chatbot
├── progress_tracker.py     # JSON-based progress persistence
├── requirements.txt
└── assets/                 # Screenshots (proof of work)
```

## ▶️ How to run
```bash
pip install -r requirements.txt
streamlit run app.py
```
Then open the URL Streamlit prints (typically `http://localhost:8501`) in your browser.

## 🚀 Future Scope
- Replace the keyword-matching engine with a real LLM (OpenAI API / Hugging Face
  Transformers) for open-ended question answering.
- Add more subjects, grade levels, and regional-language support.
- Add a teacher/parent dashboard to track multiple students.
- Deploy on Streamlit Community Cloud for public access.
