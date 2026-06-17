from sentence_transformers import SentenceTransformer
import logging
logger = logging.getLogger(__name__)

class EmbeddingService:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    @classmethod
    def generate_embedding(
        cls,
        text: str
    ):

        try:

            logger.info(
                f"Generating embedding for text length {len(text)}"
            )

            embedding = cls.model.encode(text)

            logger.info(
                f"Embedding generated successfully. Dimension: {len(embedding)}"
            )

            return embedding.tolist()

        except Exception:

            logger.exception(
                "generate_embedding failed"
            )

            raise