import chromadb


class VectorService:

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="knowledge_base"
    )

    @classmethod
    def add_document(
        cls,
        doc_id,
        text,
        embedding, metadata
    ):

        cls.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[embedding],
            metadatas = [metadata]
        )

    @classmethod
    def search(
        cls,
        query_embedding,
        n_results=3
    ):

        results = cls.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return results