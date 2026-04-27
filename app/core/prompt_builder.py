def build_prompt(context: str, query: str):
    return f"""
You are a helpful assistant.

Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}

Answer:
"""