from app_core.llm import get_llm
from app_core.prompts import REFINE_PROMPT


def refine_prompt(user_input: str) -> str:
    llm = get_llm()

    query = REFINE_PROMPT.format(
        user_input=user_input.strip()
    )

    try:
        response = llm.invoke(query)
        return response.content.strip()
    except Exception as exc:
        return (
            "⚠️ Unable to refine the prompt at this time.\n\n"
            f"Details: {exc}"
        )
