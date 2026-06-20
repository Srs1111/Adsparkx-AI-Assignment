def generate_response(persona, question, context):

    return f"""
Persona Detected: {persona}

User Question:
{question}

Retrieved Context:
{context}

Response:
Based on the retrieved documents, the above information is relevant to the user's query.
"""