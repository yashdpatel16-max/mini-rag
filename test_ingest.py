# from app.ingestion.ingest import ingest_pdf
# from app.retrieval.qdrant_service import create_collection

# create_collection()

# ingest_pdf("sample.pdf")


from app.ingestion.ingest import ingest_folder
from app.retrieval.qdrant_service import create_collection

create_collection()

ingest_folder("data")