from fastapi import APIRouter, UploadFile, File
import os

from app.services.pdf_services import PDFService
from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService

router = APIRouter()


@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    os.makedirs("data", exist_ok=True)

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:

        content = await file.read()
        buffer.write(content)

    text = PDFService.extract_text(file_path)

    chunks = ChunkService.chunk_text(text)

    for idx, chunk in enumerate(chunks):

        embedding = (
            EmbeddingService.generate_embedding(chunk)
        )

        VectorService.add_document(
            doc_id=f"{file.filename}_{idx}",
            text=chunk,
            embedding=embedding,
            metadata={
                "filename": file.filename,
                "chunk_id": idx
    }
        )

    return {
        "message": "PDF processed successfully",
        "chunks": len(chunks)
    }