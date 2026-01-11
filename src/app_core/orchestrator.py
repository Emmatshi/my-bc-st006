from app_core.tools.refine import refine_prompt
from app_core.tools.generate import generate_blog
from app_core.tools.summarize import summarize_text


def run_workflow(user_goal: str):
    """
    Orchestrates a multi-step AI workflow:
    1. Refine the user's goal into a clear prompt
    2. Generate a blog post from the refined prompt
    3. Summarize the generated blog post

    Returns a dictionary containing outputs from each step.
    """
    refined = refine_prompt(user_goal)
    blog = generate_blog(refined)
    summary = summarize_text(blog)

    return {
        "refined_prompt": refined,
        "blog_post": blog,
        "summary": summary,
    }