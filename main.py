from app_core.orchestrator import run_workflow

if st.button("Run AI Workflow"):
    result = run_workflow(user_input)

    st.subheader("Refined Prompt")
    st.code(result["refined_prompt"])

    st.subheader("Generated Blog")
    st.write(result["blog_post"])

    st.subheader("Summary")
    st.info(result["summary"])

    