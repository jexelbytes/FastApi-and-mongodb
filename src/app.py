from fastapi import FastAPI, Depends
from database import init_db
from contextlib import asynccontextmanager
from config import app_configs, swagger_config, SHOW_SWAGGER
from auth.swagger_auth import get_current_username
from fastapi.openapi.docs import get_swagger_ui_html

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing database...")
    await init_db()
    print("Complete initialization...")
    yield

app = FastAPI(lifespan=lifespan, **app_configs)

if SHOW_SWAGGER:
    @app.get("/docs", include_in_schema=False)
    async def get_swagger_documentation(username: str = Depends(get_current_username)):
        return get_swagger_ui_html(
            title="FastAPI full configured swagger.",
            swagger_ui_parameters=swagger_config,
            openapi_url="/openapi.json"
        )

    @app.get("/openapi.json", include_in_schema=False)
    async def openapi(username: str = Depends(get_current_username)):
        return app.openapi()

# ROUTES
from hello_world.router import router as hello_world_router
from users.router import router as users_router
from auth.routes import router as auth_router

app.include_router(hello_world_router, tags=['Products'])
app.include_router(users_router, tags=['Users'])
app.include_router(auth_router, tags=['Auth'])
