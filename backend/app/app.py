from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user_model import User
from app.api.api_v1.router import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STRING}/openapi.json"
)


@app.on_event("startup")
async def app_init():
    """
        initialize crucial applictaion services here
    """
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)

    await init_beanie(
        database=db_client.get_default_database(),
        document_models=[
            User
        ]
    )

app.include_router(router, prefix=settings.API_V1_STRING)
