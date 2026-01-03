import streamlit as st
from app_core.generator import generate_response

st.set_page_config(page_title="Streamlit AI Template", layout="wide")

if "OPENAI_API_KEY" not in st.secrets:
    st.error(
        "Missing OpenAI API key.\n\n"
        "- Local: add it to `.streamlit/secrets.toml`\n"
        "- Cloud: add it in App Settings → Secrets"
    )
    st.stop()


st.title("🚀 Streamlit AI Template")
st.caption("Reusable starter for Streamlit + OpenAI apps")
