from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.utils.logger import logger
from app.config.db import get_client, close_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    _ = get_client()
    yield
    close_client()


app = FastAPI(
    title="Template Generator API",
    version="1.0.0",
    description="API for generating templates",
    docs_url="/docs",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(f"HTTP exception: {exc}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": exc.detail, "data": None},
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"success": False,
                 "message": "Internal server error", "data": None},
    )


@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", reload=True)
