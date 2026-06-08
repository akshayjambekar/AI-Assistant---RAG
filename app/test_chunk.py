from services.chunk_service import ChunkService

text = "A" * 1500

chunks = ChunkService.chunk_text(
    text=text,
    chunk_size=500,
    overlap=100
)

print(len(chunks))