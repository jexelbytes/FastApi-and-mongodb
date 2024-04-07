from fastapi import FastAPI
from database import init_db
from contextlib import asynccontextmanager
from hello_world.router import router as hello_world_router
from users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("initializing...")
    await init_db()
    print("complete...")
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(hello_world_router, tags=['Products'])
app.include_router(users_router, tags=['Users'])

    
@app.get("/", include_in_schema=False)
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}