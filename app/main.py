from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.upload import router as upload_router
import logging

app = FastAPI()



logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(name)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)

logger = logging.getLogger(__name__)

app.include_router(chat_router)
app.include_router(upload_router)

@app.get("/")
async def health_check():
    try:

        return {
            "status": "running",
            "service": "AI Backend"
        }
    except Exception as e:
        logger.error(f"health check failed: {e}")
