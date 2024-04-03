from sqlalchemy.ext.asyncio import create_async_engine


class Config:
    # DB_URL = "postgresql+asyncpg://postgres:567234@localhost:5432/abc"
    DB_URL ="postgresql+asyncpg://postgres:1@localhost/asd"
    # engine = create_async_engine("postgresql+asyncpg://postgres:1@localhost/abc", echo=True)

config = Config
