import logging

logger = logging.getLogger(__name__)

class ChunkService:

    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = 500,
        overlap: int = 100
    ) -> list[str]:

        logger.info(
            f"Chunking text of length {len(text)}"
        )

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start += (chunk_size - overlap)

        logger.info(
            f"Generated {len(chunks)} chunks"
        )

        return chunks