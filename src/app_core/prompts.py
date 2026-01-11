# Prompt templates used by the orchestration tools


REFINE_PROMPT = """
Refine the following user input into a clear, specific, and effective
prompt suitable for an AI language model.

User input:
{user_input}

Refined prompt:
"""


BLOG_PROMPT = """
Write a well-structured blog post based on the following refined prompt.

Prompt:
{topic}

The blog post should be clear, engaging, and informative.
"""


SUMMARY_PROMPT = """
Summarize the following text into a concise, readable summary.

Text:
{text}

Summary:
"""
