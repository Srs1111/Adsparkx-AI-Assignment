import streamlit as st 

from agents.persona_detector import detect_persona

from rag.retriver import retrieve

from agents.response_generator import generate_response
from agents.escalation import should_escalate
from agents.handsoff import generate_summary


st.title(
    "Persona-Aware Support Agents"
)

query = st.text_input(
    "Ask your question"
)

if query:

    persona = detect_persona(query)

    docs = retrieve(query)

    context = "\n".join(
        [d.page_context for d in docs]
    )

    response = generate_response(
        persona,
        query,
        context
    )

    st.write("Persona:", persona)
    st.write(response)

    st.write("Sources:")

    for d in docs:
        st.write(
            d.metadata.get("source")
        )
    if should_escalate(
        query,
        docs
    ):
        st.error(
            "Escalated to human Agents" 
        )

        st.json(
            generate_summary(
                persona,
                query,
                docs
            )
        )