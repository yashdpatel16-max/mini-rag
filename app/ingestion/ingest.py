import os 
# from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.retrieval.embedding import get_embedding
from app.retrieval.qdrant_service import client, COLLECTION_NAME
from qdrant_client.models import PointStruct
from app.retrieval.embedding import get_embedding
from app.retrieval.qdrant_service import client, COLLECTION_NAME
from qdrant_client.models import VectorParams, Distance
import uuid

# def ingest_documents():

#     # 1. Create collection (if not exists)
#     client.recreate_collection(
#         collection_name=COLLECTION_NAME,
#         vectors_config=VectorParams(size=384, distance=Distance.COSINE)
#     )

#     # 2. Dummy sample data (replace with PDF later)
#     documents = [
#         {"text": "RAG stands for Retrieval Augmented Generation", "source": "rag.pdf"},
#         {"text": "AI is intelligence demonstrated by machines", "source": "ai.pdf"}
#     ]

#     points = []

#     for doc in documents:
#         vector = get_embedding(doc["text"])

#         points.append({
#             "id": str(uuid.uuid4()),
#             "vector": vector,
#             "payload": {
#                 "text": doc["text"],
#                 "source": doc["source"]
#             }
#         })

#     # 3. Insert into Qdrant
#     client.upsert(
#         collection_name=COLLECTION_NAME,
#         points=points
#     )

#     print("Ingestion complete")
    
# # one pdf ingestion
# def ingest_pdf(file_path: str):
#     text = load_pdf(file_path)

#     chunks = chunk_text(text)

#     points = []

#     for i, chunk in enumerate(chunks):
#         embedding = get_embedding(chunk)

#         points.append(
#             PointStruct(
#                 id=i,
#                 vector=embedding,
#                 payload={
#                     "text": chunk,
#                     "source": file_path,
#                     "chunk_id": i
#                 }
#             )
#         )

#     client.upsert(
#         collection_name=COLLECTION_NAME,
#         points=points
#     )

#     print(f"Inserted {len(points)} chunks into Qdrant")



# def ingest_folder(folder_path: str):
#     all_points = []
#     point_id = 0

#     for file_name in os.listdir(folder_path):
#         if not file_name.endswith(".pdf"):
#             continue

#         file_path = os.path.join(folder_path, file_name)
#         print(f"Processing: {file_name}")

#         text = load_pdf(file_path)
#         chunks = chunk_text(text)

#         for i, chunk in enumerate(chunks):
#             embedding = get_embedding(chunk)

#             all_points.append(
#                 PointStruct(
#                     id=point_id,
#                     vector=embedding,
#                     payload={
#                         "text": chunk,
#                         "source": file_name,
#                         "chunk_id": i
#                     }
#                 )
#             )
#             point_id += 1

#     client.upsert(
#         collection_name=COLLECTION_NAME,
#         points=all_points
#     )

#     print(f"Inserted {len(all_points)} chunks from all PDFs")

from app.retrieval.embedding import get_embedding
from app.retrieval.qdrant_service import client, COLLECTION_NAME
from qdrant_client.models import VectorParams, Distance
import uuid

def ingest_documents():

    # 1. Create collection (if not exists)
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )

    # 2. Dummy sample data (replace with PDF later)
    documents = [
        {"text": "RAG stands for Retrieval Augmented Generation", "source": "rag.pdf"},
        {"text": "AI is intelligence demonstrated by machines", "source": "ai.pdf"}
    ]

    points = []

    for doc in documents:
        vector = get_embedding(doc["text"])

        points.append({
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": {
                "text": doc["text"],
                "source": doc["source"]
            }
        })

    # 3. Insert into Qdrant
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print("Ingestion complete")