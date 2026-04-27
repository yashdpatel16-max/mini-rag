from app.retrieval.embedding import get_embedding
from app.retrieval.qdrant_service import client, COLLECTION_NAME

# def retrieve_context(query: str):
    # query_vector = get_embedding(query)

    # results = client.query_points(
    #     collection_name=COLLECTION_NAME,
    #     query=query_vector,
    #     limit=3
    # )

    # # texts = [point.payload["text"] for point in results.points]
    # # Which document is used
    # # Which chunk matched
    # texts = []
    # for point in results.points:
    #     texts.append(point.payload["text"])
    #     print("Source:", point.payload.get("source"))
    # return "\n".join(texts)

def retrieve_context(query: str, source: str = None):
    query_vector = get_embedding(query)

    search_filter = None

    if source:
        search_filter = {
            "must": [
                {
                    "key": "source",
                    "match": {
                        "value": source
                    }
                }
            ]
        }

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        query_filter=search_filter,
        limit=3
    )

    texts = []
    for point in results.points:
        texts.append(point.payload["text"])
        print("Source:", point.payload.get("source"))

    return "\n".join(texts)