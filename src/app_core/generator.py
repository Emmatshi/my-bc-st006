from app_core.llm import get_llm
from app_core.prompts import DEFAULT_PROMPT

def generate_response(user_input: str) -> str:
    llm = get_llm()
    prompt = DEFAULT_PROMPT.format(input=user_input)
    response = llm.invoke(prompt)
    return response.content

