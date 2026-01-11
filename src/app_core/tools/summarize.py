from app_core.llm import get_llm
from app_core.prompts import SUMMARY_PROMPT


def summarize_text(text: str) -> str:
    llm = get_llm()

    query = SUMMARY_PROMPT.format(
        text=text.strip()
    )

    try:
        response = llm.invoke(query)
        return response.content.strip()
    except Exception as exc:
        return (
            "⚠️ Unable to summarize text at this time.\n\n"
            f"Details: {exc}"
        )
