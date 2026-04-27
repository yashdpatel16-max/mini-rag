from fastapi import FastAPI
from app.llm.ollama_client import generate_response
from app.retrieval.retriever import retrieve_context
from app.core.prompt_builder import build_prompt
from app.db.chat_store import save_chat, get_chat_history
from app.ingestion.ingest import ingest_documents
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "RAG system running"}

@app.post("/query")
def query_llm(prompt: str):
    response = generate_response(prompt)
    return {"response": response}

# @app.post("/rag-query")
# def rag_query(query: str):
#     context = retrieve_context(query)
#     print("Context:", context)  # DEBUG

#     prompt = build_prompt(context, query)
#     response = generate_response(prompt)

#     return {
#         "query": query,
#         "context": context,
#         "response": response
#     }


# source as option
# @app.post("/rag-query")
# def rag_query(query: str, source: str = None):
#     context = retrieve_context(query, source)

#     prompt = build_prompt(context, query)
#     response = generate_response(prompt)

#     return {
#         "query": query,
#         "source_filter": source,
#         "context": context,
#         "response": response
#     }

# simple memory operation
# 


# mongo db chat store
@app.post("/rag-query")
def rag_query(query: str, user_id: str = "default", source: str = None):

    # 1. Load history from DB
    history = get_chat_history(user_id)

    # 2. Retrieve context
    context = retrieve_context(query, source)

    # 3. Combine
    full_context = history + "\n" + context

    # 4. Prompt + response
    prompt = build_prompt(full_context, query)
    response = generate_response(prompt)

    # 5. Save to DB
    save_chat(user_id, query, response)

    return {
        "query": query,
        "response": response
    }

@app.post("/ingest")
def ingest():
    ingest_documents()
    return {"status": "ingestion done"}