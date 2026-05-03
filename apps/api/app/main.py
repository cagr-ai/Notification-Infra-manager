from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import close_client, get_client
from app.routes import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    _ = get_client()
    yield
    close_client()


app = FastAPI(title="Notification API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["health"])
