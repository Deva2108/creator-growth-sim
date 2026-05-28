from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from app.core.config import get_settings


def build_engine() -> AsyncEngine:
    settings = get_settings()
    return create_async_engine(
        settings.database_url,
        echo=settings.database_echo,
        pool_size=settings.database_pool_size,
        max_overflow=settings.database_max_overflow,
        pool_pre_ping=True,
    )


engine: AsyncEngine = build_engine()


def get_engine() -> AsyncEngine:
    return engine
