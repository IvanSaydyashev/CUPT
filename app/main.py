from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from telegram import Bot

from app.core.config import Settings
from app.db.session import get_async_session, engine, Base
app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    settings = Settings()  # type: ignore
    app.state.bot = Bot(token=settings.TG_TOKEN)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/")
async def db_access(db: AsyncSession = Depends(get_async_session)):
    return {"status": "ok"}