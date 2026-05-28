from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.router import v1_router
from app.core.config import get_settings
from app.db.engine import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
    )
    app.include_router(v1_router, prefix=settings.api_prefix)
    return app


app = create_app()
