from langchain_core.prompts import PromptTemplate

DEFAULT_PROMPT = PromptTemplate.from_template(
    """
Respond helpfully to the following input:

{input}
"""
)
