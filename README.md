# Streamlit AI Template

A reusable template for building Streamlit apps powered by OpenAI.

## Features

-   Streamlit + Poetry
-   Clean `src/` layout
-   OpenAI safety guard
-   Ready for Streamlit Cloud

## Usage

1. Click **Use this template** on GitHub
2. Clone your new repo
3. Add `OPENAI_API_KEY`:
    - Local: `.streamlit/secrets.toml`
    - Cloud: App Settings → Secrets
4. Run:

````bash
poetry install
poetry run python -m streamlit run main.py

##  Local smoke test (one last time)
```bash
rm -rf .venv
poetry env use $(pyenv which python)
poetry install
poetry run python -m streamlit run main.py
````
