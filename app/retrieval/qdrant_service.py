from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from app.retrieval.embedding import get_embedding

# Connect to Qdrant
client = QdrantClient(
    host="qdrant", #(normal run vs docker) host="localhost",
    port=6333
)

COLLECTION_NAME = "documents"


# ✅ Step 4: Create Collection
def create_collection():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )


# Step 5: Insert Sample
# def insert_sample():
#     client.upsert(
#         collection_name=COLLECTION_NAME,
#         points=[
#             PointStruct(
#                 id=1,
#                 vector=[0.1]*384,
#                 payload={"text": "sample document"}
#             )
#         ]
#     )

# from qdrant_client.models import PointStruct

def insert_sample():
    text = "RAG stands for Retrieval Augmented Generation. It combines retrieval with LLMs."

    embedding = get_embedding(text)

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=1,
                vector=embedding,
                payload={"text": text}
            )
        ]
    )

# Step 6: Search
def search_test():
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=[0.1]*384,
        limit=1
    )
    return results