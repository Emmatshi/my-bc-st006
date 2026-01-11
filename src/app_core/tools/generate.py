from app_core.llm import get_llm
from app_core.prompts import BLOG_PROMPT


def generate_blog(refined_prompt: str) -> str:
    llm = get_llm()

    query = BLOG_PROMPT.format(
        topic=refined_prompt.strip()
    )

    try:
        response = llm.invoke(query)
        return response.content.strip()
    except Exception as exc:
        return (
            "⚠️ Unable to generate blog content at this time.\n\n"
            f"Details: {exc}"
        )
