# from sentence_transformers import SentenceTransformer

# # Load model once (important)
# model = SentenceTransformer("all-MiniLM-L6-v2")

# def get_embedding(text: str):
#     return model.encode(text).tolist()

# above best when local

from fastembed import TextEmbedding

# Initialize model
embedding_model = TextEmbedding()

def get_embedding(text: str):
    embeddings = list(embedding_model.embed([text]))
    return embeddings[0]