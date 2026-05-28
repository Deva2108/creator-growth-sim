import inspect

from sqlalchemy.ext.asyncio import AsyncEngine

from app.core.config import get_settings
from app.db.engine import build_engine, get_engine
from app.db.session import get_db


def test_database_url_uses_asyncpg_scheme():
    settings = get_settings()
    assert settings.database_url.startswith("postgresql+asyncpg://")


def test_database_pool_defaults_are_valid():
    settings = get_settings()
    assert settings.database_pool_size > 0
    assert settings.database_max_overflow >= 0


def test_get_db_is_async_generator():
    assert inspect.isasyncgenfunction(get_db)


def test_engine_factory_returns_async_engine():
    assert isinstance(build_engine(), AsyncEngine)


def test_get_engine_returns_shared_instance():
    assert get_engine() is get_engine()
