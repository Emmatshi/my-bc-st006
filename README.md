# 🧠 AI Writing Assistant (Orchestrated)

An orchestrated Streamlit AI application that coordinates multiple
specialized LLM-powered tools into a single, multi-step workflow.

This app demonstrates how prompt refinement, content generation, and
summarization can be combined through an explicit orchestration layer.

---

## ✨ What This App Does

Instead of calling a single AI function, this application runs a
**multi-step workflow**:

1. Refines a rough user goal into a clear AI-ready prompt
2. Generates a structured blog post from the refined prompt
3. Produces a concise summary of the generated content

Each step is handled by an independent tool and coordinated by an
orchestrator.

---

## 🧩 Why Orchestration Matters

Most AI demos perform a single LLM call.

This app demonstrates **orchestration**, where application code
controls:

-   Which AI tools run
-   The order they run in
-   How outputs from one step feed into the next

This mirrors how real-world AI systems are designed in production.

---

## 🏗 Architecture

The application is intentionally layered:

-   **`main.py`**  
    Streamlit UI (input, triggering workflow, displaying results)

-   **`orchestrator.py`**  
    Central workflow coordinator that chains multiple AI tools

-   **`tools/`**  
    Independent, reusable AI capabilities:

    -   `refine.py` – prompt refinement
    -   `generate.py` – content generation
    -   `summarize.py` – text summarization

-   **`llm.py`**  
    Centralized LLM client configuration

-   **`prompts.py`**  
    Prompt templates shared across tools

Secrets (API keys) are managed via Streamlit’s `secrets.toml` system.

---

## 🧠 Orchestration Flow (Conceptual)

```text
User Goal
   ↓
Prompt Refiner
   ↓
Blog Generator
   ↓
Summarizer
   ↓
Final Output
```
