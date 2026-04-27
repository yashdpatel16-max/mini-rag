# def chunk_text(text: str, chunk_size=500, overlap=50): # Smaller chunks → better relevance
def chunk_text(text: str, chunk_size=300, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks