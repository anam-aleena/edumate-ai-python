"""
EduMate AI — Personalized Learning Platform & Chatbot Tutor
Capstone Project | SDG 4: Quality Education
Author: Aleena Anam

Run with:
    streamlit run app.py
"""

import streamlit as st
from data import SUBJECTS
from nlp_engine import get_bot_reply
from progress_tracker import load_progress, mark_topic_done

st.set_page_config(page_title="EduMate AI", page_icon="🎓", layout="wide")

# ---------------------------------------------------------------
# Styling
# ---------------------------------------------------------------
st.markdown("""
<style>
    .stApp { background-color: #EFF3F1; color: #1E2A28; }
    .stApp, .stApp p, .stApp li, .stApp span, .stApp label,
    .stMarkdown, .stMarkdown p, .stMarkdown li,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] li {
        color: #1E2A28 !important;
    }
    div[data-testid="stMetricValue"] { color: #123832 !important; }
    div[data-testid="stMetricLabel"] { color: #4B5A57 !important; }
    .stApp h1, .stApp h2, .stApp h3 { color: #123832 !important; }
    section[data-testid="stSidebar"] { background-color: #FFFFFF !important; }
    section[data-testid="stSidebar"] * { color: #1E2A28 !important; }
    .edumate-header {
        background: #123832;
        color: #F3EFE3;
        padding: 18px 28px;
        border-radius: 12px;
        margin-bottom: 18px;
    }
    .edumate-header h1 { margin: 0; font-size: 26px; }
    .edumate-header p { margin: 2px 0 0; opacity: 0.75; font-size: 13px; }
    .sdg-tag {
        background: rgba(243,239,227,0.12);
        border: 1px solid rgba(243,239,227,0.3);
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 12px;
        display: inline-block;
        margin-top: 8px;
    }
    div[data-testid="stChatMessage"] { font-size: 15px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="edumate-header">
    <h1>🎓 EduMate AI</h1>
    <p>Personalized Learning Platform & Chatbot Tutor</p>
    <span class="sdg-tag">🔴 SDG 4 · Quality Education</span>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Sidebar — subject & topic navigation
# ---------------------------------------------------------------
st.sidebar.header("📚 Subjects")
subject_name = st.sidebar.radio(
    "Choose a subject",
    list(SUBJECTS.keys()),
    format_func=lambda s: f"{SUBJECTS[s]['icon']}  {s}",
)

topics = SUBJECTS[subject_name]["topics"]
progress = load_progress()

st.sidebar.markdown("**Topics**")
topic_name = st.sidebar.radio(
    "Choose a topic",
    list(topics.keys()),
    format_func=lambda t: f"✓ {t}" if progress.get(t, {}).get("completed") else t,
    label_visibility="collapsed",
)

topic = topics[topic_name]

# ---------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------
tab_lesson, tab_chat, tab_quiz, tab_progress = st.tabs(
    ["📖 Lesson", "💬 Ask AI Tutor", "📝 Quiz", "📊 My Progress"]
)

# ---------------- Lesson tab ----------------
with tab_lesson:
    st.caption(f"{subject_name} · {topic['grade']}")
    st.subheader(topic_name)
    st.write(topic["summary"])
    for point in topic["lesson"]:
        st.markdown(f"- {point}")

# ---------------- Chat tab ----------------
with tab_chat:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": f"Hi! I'm your AI tutor 👋 Ask me about {subject_name} or any topic in Math, Science, or English."}
        ]

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    suggestions = ["What is a fraction?", "Explain photosynthesis", "What is a noun?"]
    cols = st.columns(len(suggestions))
    clicked_suggestion = None
    for c, s in zip(cols, suggestions):
        if c.button(s, key=f"sugg_{s}"):
            clicked_suggestion = s

    user_input = st.chat_input("Type your question... e.g. 'What is a fraction?'")
    final_input = clicked_suggestion or user_input

    if final_input:
        st.session_state.chat_history.append({"role": "user", "content": final_input})
        reply = get_bot_reply(final_input)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

# ---------------- Quiz tab ----------------
with tab_quiz:
    quiz_key = f"quiz_state_{topic_name}"
    if quiz_key not in st.session_state:
        st.session_state[quiz_key] = {"index": 0, "score": 0, "answered": False, "last_choice": None}

    qs = st.session_state[quiz_key]
    quiz_questions = topic["quiz"]

    if qs["index"] >= len(quiz_questions):
        pct = round((qs["score"] / len(quiz_questions)) * 100)
        mark_topic_done(topic_name, qs["score"], len(quiz_questions))
        st.success(f"Quiz complete! You scored {qs['score']} / {len(quiz_questions)} ({pct}%) on \"{topic_name}\"")
        if st.button("Retake Quiz"):
            st.session_state[quiz_key] = {"index": 0, "score": 0, "answered": False, "last_choice": None}
            st.rerun()
    else:
        q = quiz_questions[qs["index"]]
        st.caption(f"Question {qs['index'] + 1} of {len(quiz_questions)} · Score: {qs['score']}")
        st.markdown(f"**{q['q']}**")

        if not qs["answered"]:
            for i, opt in enumerate(q["options"]):
                if st.button(opt, key=f"{quiz_key}_opt_{qs['index']}_{i}"):
                    qs["answered"] = True
                    qs["last_choice"] = i
                    if i == q["answer"]:
                        qs["score"] += 1
                    st.rerun()
        else:
            for i, opt in enumerate(q["options"]):
                if i == q["answer"]:
                    st.success(f"✅ {opt}")
                elif i == qs["last_choice"]:
                    st.error(f"❌ {opt}")
                else:
                    st.write(opt)
            if st.button("Next Question →"):
                qs["index"] += 1
                qs["answered"] = False
                qs["last_choice"] = None
                st.rerun()

# ---------------- Progress tab ----------------
with tab_progress:
    all_topics = [t for s in SUBJECTS.values() for t in s["topics"].keys()]
    progress = load_progress()
    completed = [t for t in all_topics if progress.get(t, {}).get("completed")]
    total_score = sum(progress[t]["score"] for t in completed)
    total_possible = sum(progress[t]["total"] for t in completed)
    avg_pct = round((total_score / total_possible) * 100) if total_possible else 0

    c1, c2, c3 = st.columns(3)
    c1.metric("Topics completed", f"{len(completed)}/{len(all_topics)}")
    c2.metric("Average quiz score", f"{avg_pct}%")
    c3.metric("Streak", "🔥" if completed else "—")

    st.markdown("#### Topic Progress")
    for t in all_topics:
        p = progress.get(t)
        if p and p.get("completed"):
            st.write(f"✅ **{t}** — {p['score']}/{p['total']}")
        else:
            st.write(f"⬜ {t} — Not started")
