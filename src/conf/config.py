from sqlalchemy.ext.asyncio import create_async_engine


class Config:
    # DB_URL = "postgresql+asyncpg://postgres:567234@localhost:5432/abc"
    # DB_URL =
    engine = create_async_engine("postgresql+asyncpg://user:password@localhost/dbname", echo=True)

# config = Config
