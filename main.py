import streamlit as st
from app_core.orchestrator import run_workflow

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Writing Assistant (Orchestrated)",
    layout="wide",
)

# -----------------------------
# Safety guard for API key
# -----------------------------
try:
    _ = st.secrets["OPENAI_API_KEY"]
except Exception:
    st.error(
        "Missing OpenAI API key.\n\n"
        "- Local: add it to `.streamlit/secrets.toml`\n"
        "- Cloud: add it in App Settings → Secrets"
    )
    st.stop()


# -----------------------------
# Header
# -----------------------------
st.title("🧠 AI Writing Assistant")
st.caption(
    "An orchestrated AI workflow that refines a prompt, "
    "generates a blog post, and summarizes the result."
)

# -----------------------------
# User input
# -----------------------------
user_goal = st.text_area(
    "What do you want to write?",
    height=150,
    placeholder="e.g. Write a blog post about how AI is changing software engineering",
)

# -----------------------------
# Action button
# -----------------------------
run_clicked = st.button(
    "🚀 Run AI Workflow",
    disabled=not user_goal.strip(),
)

# -----------------------------
# Run orchestration
# -----------------------------
if run_clicked:
    with st.spinner("Running orchestrated AI workflow..."):
        result = run_workflow(user_goal)
        st.session_state["result"] = result

# -----------------------------
# Output display
# -----------------------------
if "result" in st.session_state:
    result = st.session_state["result"]

    st.divider()

    with st.expander("🪄 Step 1 — Refined Prompt", expanded=True):
        st.code(result["refined_prompt"])

    with st.expander("📝 Step 2 — Generated Blog Post", expanded=True):
        st.write(result["blog_post"])

    with st.expander("📌 Step 3 — Summary", expanded=True):
        st.info(result["summary"])
else:
    st.info("The orchestrated workflow output will appear here.")
