import streamlit as st
from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=st.secrets["OPENAI_API_KEY"],
    )
