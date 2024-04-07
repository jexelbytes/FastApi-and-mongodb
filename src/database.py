from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from hello_world.schemas import ProductReview
from users.schemas import User

documents_models = [
    ProductReview,
    User
]

async def init_db():
    client = AsyncIOMotorClient("mongodb+srv://jexelg53:mongopruebasdb@cluster0.kftu6mm.mongodb.net")
    await init_beanie(database=client.db_name, document_models=documents_models)