from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_URI, DATABASE_RETRY_WRITES

# PYDANTIC MODELS TO INITIALIZE
from users.schemas import User
from auth.schemas import ActiveSession

documents_models = [
    User,
    ActiveSession,
]

async def init_db():
    client = AsyncIOMotorClient(f"mongodb+srv://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_URI}/?retryWrites={DATABASE_RETRY_WRITES}")
    await init_beanie(database=client.db_name, document_models=documents_models)