from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
from app.services.llm_services import ask_llm
import logging

logger = logging.getLogger(__name__)

class RAGService:

    @classmethod
    async def ask_question(
        cls,
        question: str
    ):
        try:
        
            logger.info(f"Question received: {question}")



            # Step 1
            query_embedding = (
                EmbeddingService.generate_embedding(
                    question
                )
            )

            # Step 2
            results = VectorService.search(
                query_embedding=query_embedding,
                n_results=5
            )

            logger.info(f"Retrieved {len(results['documents'][0])} chunks")
            print(results.keys())
            print(results["metadatas"])

            print("=" * 50)
            print("QUESTION:", question)
            print("=" * 50)

            print(results)

            print("=" * 50)

            # Step 3
            documents = results["documents"][0]
            sources = results["metadatas"][0]
            logger.info(f"Sources: {sources}")
            context = "\n".join(documents)

            # Step 4
            prompt = f"""
            You are an AI assistant.

            Answer ONLY using the context below.

            Context:
            {context}

            Question:
            {question}
            """

            # Step 5
            answer = await ask_llm(prompt)

            return {'answer':answer,
                    'sources':sources
            }
        except Exception as e:
            logger.error(f"ask_question failed: {e}")
            raise